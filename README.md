greenPi
===================

It's a python daemon  to control relays connected to a **Raspberry Pi** and **Raspbian** as OS.
You can program them, to turn on/off automatically.
It uses the [RPI.GPIO library](https://pypi.python.org/pypi/RPi.GPIO)

It runs using a config file and the following concept:
A cycle it's something that is executed without stop, and it has sub cycles, so each sub cycle do an action during a time period. For example a sub cycle could turn on a relay during 3 seconds, and the next sub cycle turn off during 5 seconds.

----------


Installation
-------------

Just download the [ZIP](https://github.com/nearlg/greenPi/archive/master.zip) , and execute relay/install.sh as root.
It will create a folder: *~/.greenRpi* where you can find a JSON config file with some examples.

    sudo sh install.sh

Configuration
-------------

To configure the daemon, It has *2 config files* in *~/.greenPi*:

 - relay.json, has only a simple array with the 
 - config.json

Just see the config file, it's very simple to understand:
The config file is a JSON array with 2 elements:

 - **numRelays**: The GPIO numbers where are connected the relays that you are going to use. It is related with *relay.json* array. For example, *relay.json* has [21, 7], *config.json* should have [1, 2]. It means that in the program, the relay number 1, is the relay that is connected in the port 21, and relay number 2, represent the relay that is connected in the port 7.
 - **cycles**: Here is where you define the cycles, it means, each cycle has:
	 - **subCycles**: Is part of the subCycle
		 - **Mode**: On or Off (true/false)
		 - **seconds**: The number off seconds that take the *subCycle*
		 - **[numRelays]**: (Optional) The affected relays.

Config file, example:


    {
        "cycles" : {
            "test" : {
                "subCycles" : [{"mode" : true, "seconds" : 20}, {"mode" : false, "seconds" : 20}],
                "numRelays" : [1,2]
                },
            "floracion" : {
                "subCycles" : [{"mode" : true, "seconds" : 43200}, {"mode" : false, "seconds" : 43200}]
                },
            "crecimiento" : {
                "subCycles" : [{"mode" : true, "seconds" : 64800}, {"mode" : false, "seconds" : 21600}]
                },
            "cambio" : {
                "subCycles" : [{"mode" : true, "seconds" : 129600}, {"cycleName" : "floracion", "numRelays" : [1]}]
                },
            "powerOn" : {
                "subCycles" : [{"mode" : true, "seconds" : null}]
                },
            "powerOff" : {
                "subCycles" : [{"mode" : true, "seconds" : null}]
                }
        },
        "numRelays" : [1,2,3
    }

Use
----

Once installed, execute as root:
sh /etc/init.d/gpirelays.sh {option}
OPTIONS:
 - **start**: To start the daemon
 - **stop**: To stop the daemon
 - **restart**: To restart the daemon
 - **run** {cycleName}: To run a cycle. The cycle name is in the configuration file *config.json*

Example of use:
    sudo sh /etc/init.d/gpirelays.sh run test