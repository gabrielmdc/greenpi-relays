#!/usr/bin/env python

from relays import Relays

class SubCycle:
    
    def __init__(self, seconds, mode = True):
        self.seconds = seconds
        self.mode = mode
    
    def run(self, numRelays):
        Relays.switch(numRelays, self.mode, self.seconds)
        return 1
