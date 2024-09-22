from Raspi_MotorHAT import Raspi_MotorHAT
from typing import Tuple
from gpiozero import DistanceSensor
import atexit

class Robot:
    def __init__(self, motorhat_addr=0x6f):
        # Setup the motorhat with the passed in address
        self._mh = Raspi_MotorHAT(addr=motorhat_addr)

        # get local variable for each motor
        self.left_motor = self._mh.getMotor(1)
        self.right_motor = self._mh.getMotor(2)

        # Setup the distance sensors
        self.left_distance_sensor = DistanceSensor(echo=17, trigger=27, queue_len=2)
        self.right_distance_sensor = DistanceSensor(echo=5, trigger=6, queue_len=2)

        # ensure the motors get stopped when the code exits
        atexit.register(self.stop_motors)

    def convert_speed(self, speed: int) -> Tuple[int, int]:
        # convert 0-100 to 0-255 and choose running direction
        if speed > 0:
            mode = Raspi_MotorHAT.FORWARD
        elif speed < 0:
            mode = Raspi_MotorHAT.BACKWARD
        else:
            mode = Raspi_MotorHAT.RELEASE

        assert -100 <= speed <= 100, f"Speed {speed} out of range (0-100)"
        return mode, int(abs(speed) * 255 / 100)

    def set_left(self, speed: int):
        mode, speed = self.convert_speed(speed)
        self.left_motor.setSpeed(speed)
        self.left_motor.run(mode)

    def set_right(self, speed: int):
        mode, speed = self.convert_speed(speed)
        self.right_motor.setSpeed(speed)
        self.right_motor.run(mode)

    def stop_motors(self):
        self.left_motor.run(Raspi_MotorHAT.RELEASE)
        self.right_motor.run(Raspi_MotorHAT.RELEASE)

