import time
import logging

from ika.vacuum_pump import VacuumPump, EvacuatingMode

logger = logging.getLogger(__name__)
format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(format=format, level=logging.DEBUG)


if __name__ == '__main__':
    port = 'COM9'  # todo set to the correct port

    vp = VacuumPump(port=port)

    logger.info(f'device name: {vp.name}')
    logger.info(f'device type: {vp.type}')
    logger.info(f'device firmware version: {vp.firmware_version}')
    logger.info(f'device firmware version date: {vp.firmware_version_date}')
    logger.info(f'device mac address: {vp.mac_address}')
    logger.info(f'device paired mac address: {vp.paired_mac_address}')

    vp.watchdog_safety_pump_rate = 10  # %
    vp.start_watchdog_mode_1(30)
    logger.info(f'watchdog communication time: {vp.watchdog_communication_time}')

    logger.info('switch to normal mode')
    vp.switch_to_normal_operation_mode()

    logger.info('set to program evacuating mode')
    vp.evacuating_mode = EvacuatingMode.PROGRAM
    logger.info(f'evacuating mode is: {vp.evacuating_mode}')
    logger.info('set to percent evacuating mode')
    vp.evacuating_mode = EvacuatingMode.PERCENT
    logger.info(f'evacuating mode is: {vp.evacuating_mode}')
    logger.info('set to automatic evacuating mode')
    vp.evacuating_mode = EvacuatingMode.AUTOMATIC
    logger.info(f'evacuating mode is: {vp.evacuating_mode}')
    logger.info('set to manual evacuating mode')
    vp.evacuating_mode = EvacuatingMode.MANUAL
    logger.info(f'evacuating mode is: {vp.evacuating_mode}')

    logger.info(f'current set pressure point to go to: {vp.set_pressure}')
    logger.info('set the set pressure point to go to to 1010 mbar')
    vp.set_pressure = 1010
    logger.info('set the set pressure point to go to to 1024 mbar')
    vp.set_pressure = 1024

    logger.info('start')
    vp.start()
    time.sleep(1)
    logger.info(f'current pressure measurement: {vp.pressure} mbar')
    logger.info('stop')
    vp.stop()

    print('done')
