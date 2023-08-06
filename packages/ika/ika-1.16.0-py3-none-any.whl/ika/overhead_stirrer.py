from ftdi_serial import Serial, NumberType

import logging
import threading
from typing import Union

from ika.errors import IKAError
from ika.utilities import _is_float_int


class OverheadStirrerProtocol:
    """
    From the manual
    Command syntax and format:
        - commands and parameters are transmitted as capital letters
        - commands and parameters including successive parameters are seperated by at least one space (hex 0x20)
        - each individual command (including parameters and data and each response are terminated with
          Blank CR LF (hex 0x20 hex 0x0d hex 0x0A) and have a maximum length of 80 characters
        - the decimal separator in a number is a dt (hex 0x2E)
    """
    # overhead stirrer NAMUR commands
    READ_DEVICE_NAME = "IN_NAME"
    READ_PT1000 = "IN_PV_3"  # read PT1000 value - temperature from the temperature sensor
    READ_ACTUAL_SPEED = "IN_PV_4"  # current actual speed
    READ_ACTUAL_TORQUE = "IN_PV_5"  # current actual torque
    READ_SET_SPEED = "IN_SP_4"  # speed to stir at
    READ_TORQUE_LIMIT = "IN_SP_5"
    READ_SPEED_LIMIT = "IN_SP_6"
    READ_SAFETY_SPEED = "IN_SP_8"  # safety speed value
    SET_SPEED = "OUT_SP_4"  # set the speed to stir at
    SET_TORQUE_LIMIT = "OUT_SP_5"  # set the torque limit
    SET_SPEED_LIMIT = "OUT_SP_6"
    SET_SAFETY_SPEED = "OUT_SP_8"
    START_MOTOR = "START_4"  # start stirring
    STOP_MOTOR = "STOP_4"  # stop stirring
    SWITCH_TO_NORMAL_OPERATING_MODE = 'RESET'
    # todo change the direction or rotation with "OUT_MODE_n" (n = 1 or 2). doesnt seem to work with the microstar C
    SET_ROTATION_DIRECTION = "OUT_MODE_"
    READ_ROTATION_DIRECTION = "IN_MODE"  # todo doesnt seem to work with the microstar C


class OverheadStirrer:
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
        Driver for an IKA overhead stirrer
        Supported/tested models:
            - Microstar 30

        :param str, port: port to connect to the device
        """
        self.logger = logging.getLogger(__name__)

        self._port = port

        self._ser: Serial = None
        # lock for use when making serial requests
        self._lock = threading.Lock()

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
    def name(self) -> str:
        n = self._request(OverheadStirrerProtocol.READ_DEVICE_NAME)
        return n

    @property
    def temperature(self) -> float:
        """temperature from the PT1000 temperature sensor"""
        temp = self._request(OverheadStirrerProtocol.READ_PT1000)
        return temp

    @property
    def speed(self) -> int:
        """actual stir speed"""
        s = int(self._request(OverheadStirrerProtocol.READ_ACTUAL_SPEED))
        return s

    @property
    def torque(self) -> float:
        """torque"""
        t = self._request(OverheadStirrerProtocol.READ_ACTUAL_TORQUE)
        return t

    @property
    def set_speed(self) -> int:
        """the set speed to stir at"""
        s = int(self._request(OverheadStirrerProtocol.READ_SET_SPEED))
        return s

    @set_speed.setter
    def set_speed(self, value: int):
        if value is not None:
            if _is_float_int(value):
                if value < 30:
                    self.logger.error('unable to set the stir speed < 30 rpm')
                    raise Exception('unable to set the stir speed < 30 rpm')
                self.logger.debug(f'set speed to stir at to {value} rpm')
                self._write(f'{OverheadStirrerProtocol.SET_SPEED} {value}')
            else:
                self.logger.error(f'unable to set speed to stir at to {value}, value must be an int or float')
        else:
            self.logger.error(f'did not set speed to stir at; did not receive a value')

    # # todo add setting and reading rotation direction - doesnt work with the microstar c
    # @property
    # def rotation_direction(self) -> str:
    #     """
    #
    #     :return: current rotation direction. cw for clockwise, ccw for counterclockwise
    #     """
    #     # todo check what the return is
    #     rd = self._request(OverheadStirrerProtocol.READ_ROTATION_DIRECTION)
    #     if rd == 1:
    #         return 'cw'
    #     elif rd == 2:
    #         return 'ccw'
    #     else:
    #         raise Exception('unable to read the rotation direction')
    #
    # @rotation_direction.setter
    # def rotation_direction(self, value: str):
    #     """
    #     Set the rotation direction to either clockwise or counterclockwise
    #     :param value: cw for clockwise, ccw for counterclockwise
    #     :return:
    #     """
    #     # todo check direction setting is correct
    #     if value:
    #         direction = None
    #         if value == 'cw':
    #             self.logger.debug(f'set rotation direction to clockwise')
    #             direction = 1
    #         elif value == 'ccw':
    #             self.logger.debug(f'set rotation direction to counterclockwise')
    #             direction = 2
    #         if direction:
    #             self._write(f'{OverheadStirrerProtocol.SET_ROTATION_DIRECTION} {direction}')

    def start_stirring(self):
        """
        for some reason whenever starting stirring the set stir speed seems to be reset to 0, so just set it again
        right
        after starting stirring
        :return:
        """
        set_speed = self.set_speed
        self._write(OverheadStirrerProtocol.START_MOTOR)
        self.set_speed = set_speed

    def stop_stirring(self):
        self._write(OverheadStirrerProtocol.STOP_MOTOR)

    def switch_to_normal_operation_mode(self):
        self.logger.debug('switch to normal operation mode')
        self._write(OverheadStirrerProtocol.SWITCH_TO_NORMAL_OPERATING_MODE)

    def connect(self):
        try:
            if self._ser is None:
                ser = Serial(self._port,
                             **self.CONNECTION_SETTINGS,
                             )
                self._ser = ser
            else:
                self._ser.connect()
            # check connected to the stirrer by checking the name
            name = self.name
            self.logger.debug(f'connected to ika overhead stirrer {name}')
        except IKAError as e:
            self.logger.error('unable to connect to ika overhead stirrer. make sure the port is correct and the '
                              'stirrer is connected to the computer')
            raise IKAError('unable to connect to ika overhead stirrer. make sure the port is correct and the '
                            'stirrer is connected to the computer')

    def disconnect(self):
        self._ser.disconnect()

    def _request(self,
                 data: str,
                 ) -> Union[str, NumberType]:
        """
        Perform a Serial request. Write data to the device and get a response back. The response is returned
        decoded as either a string or a float value.

        String response are for the ThermoshakerProtocols:
            - READ_DEVICE_NAME
        Float response are for the ThermoshakerProtocols -
            {command} - {format of the response}
            - READ_PT1000 - #.# 3
            - READ_ACTUAL_SPEED - #.# 4
            - READ_ACTUAL_TORQUE - #.# 5
            - READ_SET_SPEED - #.# 4
            - READ_TORQUE_LIMIT - #.# 5
            - READ_SPEED_LIMIT - #.# 6
            - READ_SAFETY_SPEED - #.# 8

        :param data: one of OverheadStirrerProtocol
        :return: a string or float, depending on the appropriate response based on the data
        """
        self._write(data=data)
        response: str = self._ser.read_line(line_ending=self.LINE_ENDING_ENCODED).decode()
        if response == 'Microstar C':
            # must have asked for the device name to get back this response, so the response should be
            # returned as is (as a string)
            return response
        else:
            # must have asked for a property that is returned as a number, only return the actual value (first
            # index after splitting the string by " ") as a float
            response: float = float(response.split()[0])
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

