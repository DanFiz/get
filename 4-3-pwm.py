import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)
gpio.setup(21, gpio.OUT)
pwm=gpio.PWM(21, 1000)
pwm.start(0)

try:
        while True:
                DutyCicle=int(input())
                pwm.start(DutyCicle)
                print(DutyCicle*3.3/100)
finally:
    gpio.output(21, 0)
    gpio.cleanup()
