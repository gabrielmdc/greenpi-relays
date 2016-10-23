#!/bin/sh
# Script template para demonios
# Sacado de: https://liberatucodigo.wordpress.com/2012/05/19/crear-demonio-en-linux-servicios/
# Para dar de alta al script como demonio:
# 1- sudo cp miScript /etc/init.d/
# 2- sudo chmod ug+x /etc/init.d/miScript
# 3- sudo update-rc.d miScript defaults

start(){
 echo -n $"Starting service: "
 python3 /usr/lib/greenPi/relays/daemon/daemon.py start
}
 
stop(){
 echo -n $"Stopping service: "
 python3 /usr/lib/greenPi/relays/daemon/daemon.py stop
}
 
restart(){
 stop
 python3 /usr/lib/greenPi/relays/daemon/daemon.py restart
 start
}
run(){
echo -n $"Runing cycle... "
python3 /usr/lib/greenPi/relays/daemon/daemon.py run "$1"
}

# Dependiento del parametro que se le pase
#start - stop - restart ejecuta la función correspondiente.
case "$1" in
start)
 start
 ;;
stop)
 stop
 ;;
restart)
 restart
 ;;
run)
 run "$2"
 ;;
info)
 info "$2"
 ;;
*)
 echo $"Usar: $0 {start|stop|restart| [run|state] (cycle name)}"
 exit 1
esac
 
exit 0
