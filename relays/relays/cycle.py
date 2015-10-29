#!/usr/bin/env python

from log import Log

class Cycle:
    
    def __init__(self, subCycles, numRelays, name = "", lapsedSeconds = 0):
        self.name = name
        self.subCycles = subCycles
        self.numRelays = numRelays
        self.setLapsedSeconds(lapsedSeconds)
        
    def run(self, startByKey = None):
        nextCycle = {}
        lenSubCycles = len(self.subCycles)
        key = self.__getNextSubCycle(startByKey)
        exeCount = 0
        loopCount = 0
        while True:
            if type(self.subCycles[key]) is Cycle:
                nextCycle = self.subCycles[key]
                break
            # Escribir en el log
            Log.writeLog(key, self.name, self.numRelays, self.subCycles[key])
            exeCount += self.subCycles[key].run(self.numRelays)
            loopCount += 1
            key = (key+1) if key < (lenSubCycles - 1) else 0
            if lenSubCycles == loopCount:
                loopCount = 0
                if exeCount == 0:
                    break
                exeCount = 0
        return nextCycle
    
    def __getNextSubCycle(self, startByKey = None):
        lenSubCycles = len(self.subCycles)
        key = startByKey if (startByKey != None and startByKey < lenSubCycles) else 0
        if self.__lapsedSeconds == 0 :
            return key            
            
        while self.__lapsedSeconds > 0:
            subCycle = self.subCycles[key]
            if type(subCycle) is Cycle:
                subCycle.setLapsedSeconds(self.__lapsedSeconds)
                self.__lapsedSeconds = 0
                break
            if self.__lapsedSeconds > subCycle.seconds:
                self.__lapsedSeconds -= subCycle.seconds
            else:
                tempSeconds = subCycle.seconds
                subCycle.seconds -= self.__lapsedSeconds
                # Escribir en el log
                Log.writeLog(key, self.name, self.numRelays, subCycle.mode, subCycle.seconds)
                subCycle.run(self.numRelays)
                subCycle.seconds = tempSeconds
                self.__lapsedSeconds = 0
                
            key = (key+1) if key < lenSubCycles - 1 else 0
        return key
    
    def addLapsedSeconds(self, lapsedSeconds):
        if lapsedSeconds > 0:
            lapsedSeconds += self.__lapsedSeconds
            self.setLapsedSeconds(lapsedSeconds)
    
    def setLapsedSeconds(self, lapsedSeconds):
        if lapsedSeconds != 0:
            totalSeconds = self.getTotalSeconds()
            while lapsedSeconds > totalSeconds:
                lapsedSeconds -= totalSeconds
        self.__lapsedSeconds = lapsedSeconds
    
    def getLapsedSeconds(self):
        return self.__lapsedSeconds
        
    def getTotalSeconds(self):
        seconds = 0
        for subCycle in self.subCycles:
            seconds += subCycle.seconds
        return seconds
