#!/usr/bin/python3

from signal import signal, SIGTERM, SIGHUP, pause
from threading import Thread
from gpiozero import DistanceSensor, RGBLED, Buzzer, Device, Button
from time import sleep
from gpiozero.pins.pigpio import PiGPIOFactory

Device.pin_factory = PiGPIOFactory()

reading = True
sensor = DistanceSensor(echo=20, trigger=21)
rgb_led = RGBLED(red=13, green=6, blue=5)
buzzer = Buzzer(23)
button = Button(16)
buzzer_sound = True


def safe_exit(signum, frame):
    exit(1)


def read_distance():
    while reading:
        distance_cm = sensor.distance * 100
        message = f"Distance: {distance_cm:.2f} cm"
        print(message)

        if distance_cm > 20:
            rgb_led.color = (1, 0, 1)
            if buzzer_sound:
                buzzer.off()

        elif 10 <= distance_cm <= 20:
            rgb_led.color = (1, 1, 0)
            if buzzer_sound:
                buzzer.beep(0.05, 0.05)

        else:
            rgb_led.color = (0, 1, 1)
            if buzzer_sound:
                buzzer.on()
        sleep(0.5)


def toggle_buzzer():
    global buzzer_sound
    buzzer_sound = not buzzer_sound
    if not buzzer_sound:
        buzzer.off()


def read_sensor():
    try:
        signal(SIGTERM, safe_exit)
        signal(SIGHUP, safe_exit)

        button.when_pressed = toggle_buzzer

        reader = Thread(target=read_distance)
        reader.start()

        pause()

    except KeyboardInterrupt:
        pass

    finally:
        global reading
        reading = False
        reader.join()
        sensor.close()
        rgb_led.close()
        buzzer.close()
        button.close()


read_sensor()
