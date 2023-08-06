import time
from ika.overhead_stirrer import OverheadStirrer

if __name__ == '__main__':
    port = 'COM9'  # todo set this
    stirrer = OverheadStirrer(port=port)
    print(f'stirrer name: {stirrer.name}')
    print('set speed to 30')
    stirrer.set_speed = 30
    print(f'stirrer set speed: {stirrer.set_speed}')
    print('start stirring')
    stirrer.start_stirring()
    time.sleep(5)
    print(f'stirrer current speed: {stirrer.speed}')
    print('set speed to 40')
    stirrer.set_speed = 40
    time.sleep(3)
    print(f'stirrer set speed: {stirrer.set_speed}')
    print(f'stirrer current speed: {stirrer.speed}')
    print(f'stirrer torque: {stirrer.torque}')
    print('stop stirring')
    stirrer.stop_stirring()
    print(f'stirrer set speed: {stirrer.set_speed}')
    print(f'stirrer temperature: {stirrer.temperature}')
