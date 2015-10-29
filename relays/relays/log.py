#!/usr/bin/env python

import time
import json
from datetime import datetime

class Log:
    fileName = "/home/pi/.greenPi/relays/log.json"
    #fileName = os.environ['HOME'] + "/.greenPi/relays/log.json"
    
    @staticmethod
    def writeLog(key, cycleName, numRelays, mode, seconds = None):
        log = Log.getLog()
        strNumRelays = '%s' % ' '.join(map(str, numRelays))
        mode = "on" if mode else "off"
        dicc = {"date" : time.strftime('%b %d %Y %H:%M:%S'), "key" : key,  "cycleName" : cycleName, "numRelays" : strNumRelays, "mode" : mode}
        if seconds != None and seconds > 0:
            dicc["lapsedSeconds"] = seconds
        log.append(dicc)
        with open(Log.fileName, 'w') as outfile:
            json.dump(log, outfile)
    
    @staticmethod
    def getLog():
        try:
            with open(Log.fileName, "r") as data_file:    
                return json.load(data_file)
        except:
            f = open(Log.fileName, 'w')
            f.write("[]")
            f.close()
            return []
            
    @staticmethod
    def getLastLog():
        log = Log.getLog()
        lenLog = len(log)
        if lenLog > 0:
            return log[lenLog - 1]
        return []
    
    @staticmethod
    def readLastLog():
        lastLog = Log.getLastLog()
        if len(lastLog) > 3:
            date = datetime.strptime(lastLog["date"], '%b %d %Y %H:%M:%S')
            seconds = (datetime.now() - date).total_seconds()
            seconds = int(round(seconds))
            finalLog = {"lapsedSeconds" : seconds}
            for item in lastLog:
                if item == "date":
                    continue
                elif item == "lapsedSeconds":
                    finalLog[item] += lastLog[item]
                elif item == "mode":
                    finalLog[item] = True if lastLog[item] == "on" else False
                else:
                    finalLog[item] = lastLog[item]
            return finalLog
        return {}
