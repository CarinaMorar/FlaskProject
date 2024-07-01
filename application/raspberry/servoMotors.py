import RPi.GPIO as GPIO
import time

# Configurațiile pentru pinul servo
servo_x_pin = 12  # Pin pentru servo pe axa X
servo_y_pin = 13  # Pin pentru servo pe axa Y
frequency = 50  # Frecvența PWM

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_x_pin, GPIO.OUT)
GPIO.setup(servo_y_pin, GPIO.OUT)

pwm_x = GPIO.PWM(servo_x_pin, frequency)
pwm_y = GPIO.PWM(servo_y_pin, frequency)

# Funcție helper pentru a mapa unghiul la ciclu de lucru (duty cycle)
def map_angle_to_duty_cycle(angle):
    min_duty = 2.5
    max_duty = 12.5
    return ((angle / 180) * (max_duty - min_duty)) + min_duty

# Pornire PWM pentru ambele servo motoare
pwm_x.start(0)
pwm_y.start(0)

# Funcția pentru a seta poziția pe axa X
def set_servo_position_x(angle):
    duty_cycle = map_angle_to_duty_cycle(angle)
    pwm_x.ChangeDutyCycle(duty_cycle)
    time.sleep(0.5)  # Așteaptă puțin pentru ca servo să ajungă în poziție

# Funcția pentru a seta poziția pe axa Y
def set_servo_position_y(angle):
    duty_cycle = map_angle_to_duty_cycle(angle)
    pwm_y.ChangeDutyCycle(duty_cycle)
    time.sleep(0.5)  # Așteaptă puțin pentru ca servo să ajungă în poziție

# Funcția pentru a muta ambele servo motoare simultan
def set_servo_position_xy(angle_x, angle_y):
    duty_cycle_x = map_angle_to_duty_cycle(angle_x)
    duty_cycle_y = map_angle_to_duty_cycle(angle_y)
    pwm_x.ChangeDutyCycle(duty_cycle_x)
    pwm_y.ChangeDutyCycle(duty_cycle_y)
    time.sleep(0.5)  # Așteaptă puțin pentru ca servo să ajungă în poziție
#
# try:
#     while True:
#         # Exemplu de mutare a servo motoarelor la diferite unghiuri
#         set_servo_position_xy(45, 45)
#         time.sleep(1)
#         set_servo_position_xy(90, 90)
#         time.sleep(1)
#         set_servo_position_xy(135, 135)
#         time.sleep(1)
#         set_servo_position_xy(180, 180)
#         time.sleep(1)
#
# except KeyboardInterrupt:
#     print("Program terminat de utilizator.")
# finally:
#     pwm_x.stop()
#     pwm_y.stop()
#     GPIO.cleanup()
