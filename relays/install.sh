#!/bin/bash

sudo cp daemon/gpirelays.sh /etc/init.d/gpirelays.sh
sudo chmod ug+x /etc/init.d/gpirelays.sh
sudo update-rc.d gpirelays.sh defaults
sudo mkdir -p /usr/lib/greenPi/relays
sudo cp -r daemon /usr/lib/greenPi/relays/
sudo cp -r relays /usr/lib/greenPi/relays/
mkdir -p ~/.greenPi/relays
cp examples/* ~/.greenPi/relays/