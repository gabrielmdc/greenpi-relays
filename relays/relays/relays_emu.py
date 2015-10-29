#!/usr/bin/env python

from time import sleep

class Relays:
    configGpioNums = [17, 22, 23, 24]
    gpioNumsStates = {17 : False, 22 : False, 23 : False, 24 : False}
    
    @staticmethod
    def switch(numRelays, mode, seconds = None):
        gpioNums = Relays.getRealGpioNums(numRelays)
        Relays.switchByGpioNums(gpioNums, mode, seconds)
    
    @staticmethod
    def switchByGpioNums(gpioNums, mode, seconds = None):
        for index in gpioNums:
            Relays.gpioNumsStates[index] = bool(mode)
        if not seconds == None:
            sleep(seconds)
            for index in gpioNums:
                Relays.gpioNumsStates[index] = not bool(mode) 
        
    @staticmethod
    def state(numRelay):
        res = ""
        numRelays = Relays.getRealGpioNums([numRelay])
        if len(relaysNum) > 0:
            res = Relays.stateByGpioNum(numRelays[0])
        return res

    @staticmethod
    def stateByGpioNum(gpioNum):
        if not gpioNum in Relays.gpioNumsStates:
            raise ValueError("GPIO port " + gpioNum + " does not exist")
        return Relays.gpioNumsStates[gpioNum]
        
    @staticmethod
    def getRealGpioNums(numRelays):
        realGpioNums = []
        for key, value in enumerate(Relays.configGpioNums):
            if key+1 in numRelays:
                realGpioNums.insert(0, value)
        return realGpioNums
