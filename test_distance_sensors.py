import time
from gpiozero import DistanceSensor

print("Prepare GPIO pins")
sensor_1 = DistanceSensor(echo=17, trigger=27, queue_len=2)
sensor_2 = DistanceSensor(echo=5, trigger=6, queue_len=2)

while True:
    print(f"Sensor 1: {sensor_1.distance * 100:.2f} cm")
    print(f"Sensor 2: {sensor_2.distance * 100:.2f} cm")
    time.sleep(1)