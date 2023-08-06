import logging
import time
from typing import Union, Optional
import threading

from ftdi_serial import NumberType, Serial

from ika.errors import IKAError
from ika.utilities import _is_float_int


class ChillerProtocol:
    """
    From the manual
    Command syntax and format:
        - commands and parameters are transmitted as capital letters
        - commands and parameters including successive parameters are seperated by at least one space (hex 0x20)
        - each individual command (including parameters and data and each response are terminated with
          Blank CR LF (hex 0x0d hex 0x0A) and have a maximum length of 80 characters
        - the decimal separator in a number is a dt (hex 0x2E)
    About watchdog:
        watchdog functions monitors the serial data flow. if, once this function has been activated there is no
        retransmission of the command from the computer within the set time ("watchog time:), the tempering and
        pump functions are switched off in accordance with the set "watchdog" function or are changed to the set
        target values. data transmission may be interrupted by, for example, a crash in the operating system,
        a power failure in the pc, or an issue with the connection table between the computer and the device
        watchdog mode 1
            - if there is an interruption in data communications (longer than the set watchdog time), the tempering
            and pump functions are switched off and Error 2 is displayed
        watchdog mode 2
            - if there is an interruption in data communications (longer than the set watchdog time), speed target
            value is changed to the WD safety speed limit and the temperature target value is changed to the WD
            safety temperature value. error message Error 2 is displayed
    """
    # chiller NAMUR commands
    READ_INTERNAL_ACTUAL_TEMPERATURE = "IN_PV_2"  # current actual temperature
    READ_INTERNAL_SETTING_TEMPERATURE = "IN_SP_1"  # temperature to go to
    SET_INTERNAL_SETTING_TEMPERATURE = "OUT_SP_1"  # set temperature to go to to xxx: OUT_SP_1 xxx
    # set the WD-safety temperature with echo of the set defined value: OUT_SP_12@n
    SET_WATCHDOG_SAFETY_TEMPERATURE = "OUT_SP_12@"
    # start the watchdog mode 1 and set the watchdog time to n (20 to 1500) second: OUT_WD1@N
    # echos the Watchdog time. during a WD1-event, the tempering and pump functions are switched off. This command
    # needs to be sent within the watchdog time
    WATCHDOG_MODE_1 = "OUT_WD1@"
    # start the watchdog mode 2 and set the watchdog time to n (20 to 1500) second: OUT_WD2@N
    # echos the Watchdog time. during a WD2-event, the set temperature is changed to the WD safety temperature and
    # the pump set speed is set speed is set to the WD safety speed. This command needs to be sent within the watchdog
    # time
    WATCHDOG_MODE_2 = "OUT_WD2@"
    RESET = 'RESET'
    START_TEMPERING = "START_1"
    STOP_TEMPERING = "STOP_1"


class Chiller:
    CONNECTION_SETTINGS = dict(
        baudrate=9600,
        data_bits=Serial.DATA_BITS_7,
        stop_bits=Serial.STOP_BITS_1,
        parity=Serial.PARITY_EVEN,
    )

    # constants useful for the serial communication protocol with an IKA device
    CR_HEX = "\x0d"  # carriage return
    LF_HEX = "\x0a"  # line feed or new line
    LINE_ENDING = CR_HEX + LF_HEX  # each individual command and each response are terminated CR LF
    LINE_ENDING_ENCODED = LINE_ENDING.encode()

    def __init__(self,
                 port: str,
                 ):
        """
        Driver for an IKA chiller
        Supported/tested models:
            - RC 2 lite

        :param str, port: port to connect to the device
        """
        self.logger = logging.getLogger(__name__)

        self._port = port

        self._ser: Serial = None
        # lock for use when making serial requests
        self._lock = threading.Lock()

        # track the last set watchdog safety temperature
        self._watchdog_safety_temperature: int = None

        self.logger.debug('connecting to ika overhead stirrer')
        self.connect()

    @property
    def port(self):
        """Port used to connect to the IKA device"""
        return self._port

    @port.setter
    def port(self, value: str):
        if value is not None:
            self._port = value

    @property
    def temperature(self) -> float:
        """internal actual temperature"""
        temp = self._request(ChillerProtocol.READ_INTERNAL_ACTUAL_TEMPERATURE)
        return temp

    @property
    def setting_temperature(self) -> float:
        """the internal setting temperature to go to"""
        temp = self._request(ChillerProtocol.READ_INTERNAL_SETTING_TEMPERATURE)
        return temp

    @setting_temperature.setter
    def setting_temperature(self, value: NumberType):
        if value is not None:
            if _is_float_int(value):
                self.logger.debug(f'set setting temperature to {value}')
                self._write(f'{ChillerProtocol.SET_INTERNAL_SETTING_TEMPERATURE} {value}')
            else:
                self.logger.error(f'unable to set setting temperature to {value}, value must be an int or float')

    @property
    def watchdog_safety_temperature(self) -> Union[int, None]:
        """the watchdog safety temperature"""
        return self._watchdog_safety_temperature

    @watchdog_safety_temperature.setter
    def watchdog_safety_temperature(self, value: int):
        if value is not None:
            if type(value) == int:
                self.logger.debug(f'set watchdog safety temperature to {value}')
                self._request(f'{ChillerProtocol.SET_WATCHDOG_SAFETY_TEMPERATURE}{value}')
                self._watchdog_safety_temperature = value
            else:
                self.logger.error(f'unable to set the watchdog safety temperature to {value}, value must be an int')
    def start_tempering(self):
        self.logger.debug('start tempering')
        self._write(ChillerProtocol.START_TEMPERING)

    def stop_tempering(self):
        self.logger.debug('stop tempering')
        self._write(ChillerProtocol.STOP_TEMPERING)

    def start_watchdog_mode_1(self, t: int):
        """
        Start watchdog mode 1 and set the time or the watchdog to t seconds (20 - 1500)
        """
        if 20 <= t <= 1500:
            self.logger.debug(f'set watchdog mode 1 with watch time {t} seconds')
            self._request(f'{ChillerProtocol.WATCHDOG_MODE_1}{t}')
        else:
            raise IKAError('watchdog mode time must be between 20 - 1500 seconds')

    def start_watchdog_mode_2(self, t: int):
        """
        Start watchdog mode 2 and set the time or the watchdog to t seconds (20 - 1500)
        """
        if 20 <= t <= 1500:
            self.logger.debug(f'set watchdog mode 2 with watch time {t} seconds')
            self._request(f'{ChillerProtocol.WATCHDOG_MODE_2}{t}')
        else:
            raise IKAError('watchdog mode time must be between 20 - 1500 seconds')

    def connect(self):
        try:
            if self._ser is None:
                ser = Serial(self._port,
                             **self.CONNECTION_SETTINGS,
                             )
                self._ser = ser
            else:
                self._ser.connect()
            # check connected to the stirrer by checking current temperature
            setting_temp = self.setting_temperature
            self.logger.debug(f'connected to ika chiller')
        except IKAError as e:
            self.logger.error('unable to connect to ika chiller. make sure the port is correct and the '
                              'chiller is connected to the computer')
            raise IKAError('unable to connect to ika chiller. make sure the port is correct and the '
                            'chiller is connected to the computer')

    def disconnect(self):
        self._ser.disconnect()

    # # leave commented out if it seems like the unit needs to actually be power cycled after the reset command is sent
    # def reset(self):
    #     # i think this requires the unit to be power cycled, otherwise it makes an alert noise and using the buttons
    #     # for the display do not work
    #     self.logger.debug('reset the PC control and stop the device functions')
    #     self._request(ChillerProtocol.RESET)

    def _request(self,
                 data: str,
                 ) -> Union[str, NumberType]:
        """
        Perform a Serial request. Write data to the device and get a response back. The response is returned
        decoded as either a string or a float value.

        Command - response
        READ_INTERNAL_ACTUAL_TEMPERATURE - #.# 2, where the first number is the actual temperature
        READ_INTERNAL_SETTING_TEMPERATURE - #.# 1, where the first number is the setting temperature
        SET_WATCHDOG_SAFETY_TEMPERATURE - integer, the temperature you set
        WATCHDOG_MODE_1 - integer, the time you set
        WATCHDOG_MODE_2 - integer, the time you set
        RESET -

        :param data: one of OverheadStirrerProtocol
        :return: a string or float, depending on the appropriate response based on the data
        """
        self._write(data=data)
        response: str = self._ser.read_line(line_ending=self.LINE_ENDING_ENCODED).decode()
        try:
            # try to get the 1st index as a float
            response: float = float(response.split()[0])
        except ValueError as e:
            response = str(response)  # leave the response as a string
        return response

    def _write(self,
               data: Union[bytes, str],
               ) -> None:
        """
        Perform a Serial write. Write data to the device, don't wait for a response back

        :param data: one of OverheadStirrerProtocol and any associated parameters formatted correctly as a string
        """
        with self._lock:
            # Flush data from the input and output buffers
            self._ser.flush()
            formatted_data = data + self.LINE_ENDING
            self._ser.write(data=formatted_data.encode())



