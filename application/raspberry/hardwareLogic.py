import time
import stepperMotor
import weightSensor
import videoCamera
from application import db

# Funcție pentru rotația motorului până când senzorul de greutate atinge 100 grame
def rotate_until_100_grams():
    while True:
        weight = weightSensor.get_weight()
        if weight >= 100:
            break
        stepperMotor.step_sequence()

def rotate_for_snack():
    while True:
        weight = weightSensor.get_weight()
        if weight >= 100:
            print("Bolul este deja aprope plin!")
            break
        stepperMotor.rotate_360_degrees()

def check_camera():
    videoCamera.video_camera()



# # Testare funcții
# try:
#     print("Rotire 360 de grade")
#     stepperMotor.rotate_360_degrees()
#     time.sleep(2)
#     print("Rotire până la 100 grame")
#     rotate_until_100_grams()
# finally:
#     stepperMotor.cleanup()
