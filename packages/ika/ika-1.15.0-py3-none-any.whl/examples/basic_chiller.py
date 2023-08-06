import time
import logging

from ika.chiller import Chiller

logger = logging.getLogger(__name__)
format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(format=format, level=logging.DEBUG)


if __name__ == '__main__':
    port = 'COM14'  # todo set to the correct port

    c = Chiller(port=port)

    c.watchdog_safety_temperature = 10
    # c.start_watchdog_mode_1(20)
    # c.start_watchdog_mode_2(30)

    actual_temperature = c.temperature
    setting_temperature = c.setting_temperature
    logger.info(f'actual temperature: {actual_temperature}, '
                f'setting temperature: {setting_temperature}')

    logger.info('change the setting temperature to 8.5')
    c.setting_temperature = 8.5
    setting_temperature = c.setting_temperature
    logger.info(f'setting temperature: {setting_temperature}')

    logger.info('start tempering')
    c.start_tempering()

    time.sleep(5)

    actual_temperature = c.temperature
    logger.info(f'actual temperature: {actual_temperature}')

    logger.info('change the set temperature to 8')
    c.setting_temperature = 8.0
    setting_temperature = c.setting_temperature
    logger.info(f'setting temperature: {setting_temperature}')
    actual_temperature = c.temperature
    logger.info(f'actual temperature: {actual_temperature}')

    logger.info('stop tempering')
    c.stop_tempering()

    print('done')
