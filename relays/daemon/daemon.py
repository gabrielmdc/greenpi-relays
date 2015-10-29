#!/usr/bin/env python
import sys
from pyDaemon import pyDaemon
sys.path.append("/usr/lib/greenPi/relays/relays")
from log import Log
from config import Config
from cycle import Cycle

class Daemon(pyDaemon):
    
    def run(self):
        self.__runCycleByLog()

    def stop(self):
        super().stop()
    
    @staticmethod
    def __runCycle(cycle):
        while Cycle == type(cycle):
            cycle = cycle.run()
    
    def runCycle(self, cycleName):
        config = Config()
        cycle = config.getCycle(cycleName)
        daemon.__runCycle(cycle)
    
    def __runCycleByLog(self):
        Log.fileName = "/home/pi/.greenPi/relays/log.json"#os.environ['HOME'] + "/.greenPi/relays/log.json"
        lastLog = Log.readLastLog()
        if len(lastLog) > 0:
            config = Config()
            cycle = config.getCycle(lastLog["cycleName"])
            if cycle != None:
                if "lapsedSeconds" in lastLog:
                    cycle.setLapsedSeconds(lastLog["lapsedSeconds"])
                daemon.__runCycle(cycle.run(lastLog["key"]))

if __name__ == "__main__":
    daemon = Daemon("/tmp/gpirelays.pid")
    if len(sys.argv) > 1:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        elif 'run' == sys.argv[1] and len(sys.argv) == 3:
            daemon.runCycle(sys.argv[2])
        else:
            print("Unknown command")
            sys.exit(2)
        sys.exit(0)
    else:
        print("usage: %s start|stop|restart" % sys.argv[0])
        sys.exit(2)