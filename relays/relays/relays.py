#!/usr/bin/env python

from time import sleep

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need " +
    "superuser privileges.  You can achieve this by using 'sudo' " +
    "to run your script")


class Relays:
    configGpioNums = [17, 22, 23, 24]

    @staticmethod
    def switch(relayNums, mode, seconds=None):
        gpioNums = Relays.getRealGpioNums(relayNums)
        Relays.switchByGpioNums(gpioNums, mode, seconds)

    @staticmethod
    def switchByGpioNums(gpioNums, mode, seconds=None):
        Relays.__prepare()
        GPIO.setup(gpioNums, GPIO.OUT)
        GPIO.output(gpioNums, mode)
        if not seconds is None:
            sleep(seconds)
            GPIO.output(gpioNums, not mode)
            GPIO.cleanup()

    @staticmethod
    def state(relayNum):
        res = ""
        relaysNum = Relays.getRealGpioNums([relayNum])
        if len(relaysNum) > 0:
            res = Relays.stateByGpioNum(relaysNum[0])
        return res

    @staticmethod
    def stateByGpioNum(gpioNum):
        Relays.__prepare()
        GPIO.setup(gpioNum, GPIO.OUT)
        return GPIO.input(gpioNum)

    @staticmethod
    def __prepare():
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

    @staticmethod
    def getRealGpioNums(relayNums):
        realGpioNums = []
        for key, value in enumerate(Relays.configGpioNums):
            if key + 1 in relayNums:
                realGpioNums.insert(0, value)
        return realGpioNums
