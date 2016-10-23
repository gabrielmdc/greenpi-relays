#!/usr/bin/env python

#import os
import json
from subCycle import SubCycle
from cycle import Cycle


class Config:
    #def __init__
    #(self, fileName = os.environ['HOME'] + "/.greenPi/relays/config.json"):
    def __init__(self, fileName="/home/pi/.greenPi/relays/config.json"):
        self.cycles = []
        self.numRelays = []
        self.load(fileName)

    def load(self, fileName):
        config = {}
        self.fileName = fileName
        try:
            with open(self.fileName, "r") as data_file:
                config = json.load(data_file)
        except Exception as e:
            print("Error: " + str(e.args[0]))
            return False
        if(len(config) < 1):
            return False
        self.__loadConfig(config)
        return True

    def __loadConfig(self, config):
        if "numRelays" in config:
            self.numRelays = config["numRelays"]
        numRelays = self.numRelays

        if "cycles" in config:
            for key, cycleList in config["cycles"].items():
                subCycles = []
                if "numRelays" in cycleList:
                    numRelays = cycleList["numRelays"]
                for sub in cycleList["subCycles"]:
                    if "seconds" in sub and "mode" in sub:
                        subCycles.append(SubCycle(sub["seconds"], sub["mode"]))
                    elif "cycleName" in sub:
                        subCycles.append(sub)
                        break
                self.cycles.append(Cycle(subCycles, numRelays, key))
            for cycle in self.cycles:
                subCycles = []
                for subCycle in cycle.subCycles:
                    if type(subCycle) is SubCycle:
                        subCycles.append(subCycle)
                    elif type(subCycle) is dict and "cycleName" in subCycle:
                        newSubCycle = self.getCycle(subCycle["cycleName"])
                        if type(newSubCycle) is Cycle:
                            subCycles.append(newSubCycle)
                            break
                cycle.subCycles = subCycles

    def getCycle(self, cycleName):
        for cycle in self.cycles:
            if cycle.name == cycleName:
                return cycle
        return None