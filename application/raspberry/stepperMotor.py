import RPi.GPIO as GPIO
import time

# Setările GPIO pentru motorul pas cu pas
IN1 = 17
IN2 = 18
IN3 = 27
IN4 = 22

# Inițializarea pinilor GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

# Funcție pentru un pas al motorului pas cu pas
def set_step(w1, w2, w3, w4):
    GPIO.output(IN1, w1)
    GPIO.output(IN2, w2)
    GPIO.output(IN3, w3)
    GPIO.output(IN4, w4)

# Secvență pentru rotația motorului pas cu pas
def step_sequence():
    set_step(1, 0, 0, 0)
    time.sleep(0.001)
    set_step(1, 1, 0, 0)
    time.sleep(0.001)
    set_step(0, 1, 0, 0)
    time.sleep(0.001)
    set_step(0, 1, 1, 0)
    time.sleep(0.001)
    set_step(0, 0, 1, 0)
    time.sleep(0.001)
    set_step(0, 0, 1, 1)
    time.sleep(0.001)
    set_step(0, 0, 0, 1)
    time.sleep(0.001)
    set_step(1, 0, 0, 1)
    time.sleep(0.001)

# Funcție pentru rotația motorului cu 360 de grade
def rotate_360_degrees():  #Pentru Feed Now
    steps = 512  # Numărul de pași pentru 360 de grade
    for _ in range(steps):
        step_sequence()

# Cleanup GPIO
def cleanup():
    GPIO.cleanup()
