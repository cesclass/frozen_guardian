#!/usr/bin/python3
#coding: UTF-8
#
#-------------------------------------------------------------------
#
#                         FROZEN GUARDIAN
#
#   Frozen Guardian est un programme gerant l'alimentation USB d'un
#   ventilateur en fonction de la temperature mesuré par un capteur
#
#   FG est conçu pour tourner sur Raspberry PI avec Sense Hat.
#
#   Pour fonctionner correctement, ce programme est dependant d'un
#   autre, 'hub-ctrl', dont les sources sont disponnibles ici :
#   https://github.com/codazoda/hub-ctrl.c
#   Une fois compiler, il faut mettre le programme dans le dossier
#   'frozen' de l'utilisateur qui lancera ce programme '~/frozen'
#
#   Le programme n'a pas de fonction d'arret. 
#   Il doit etre execute de la façon suivante :
#   user@machine:~/frozen $ sudo ./frozen_guardian.py &
#
#   Schema :
#    ________            __________________
#   |        |          |                  |
#   |  USB   |          |   Raspberry PI   |
#   |  FAN   [----------]    Sense Hat     |
#   |________|          |__________________|
#                        ____   ____  ____
#       ___             |*  *| |____||____|
#      |___| < FAN      |____| |_x__||____| < RPI with Sense Hat
#        |                       |
#        |_______________________| < USB
#
#-------------------------------------------------------------------
#   Dev.    : Cyril ESCLASSAN 
#   Contact : @cynex294 sur Twitter
#   Sources : github.com/cesclass/...
#   Update  : 04.11.2016
#   Licence : GPL v3
#-------------------------------------------------------------------

from sense_hat import SenseHat;
from time import sleep;
from os import system;

#-------------------------------------------------------------------

SENSE = SenseHat();
TEMPERATURE = 25; # 25°C / Temperature de declenchement
FROST_TIME = 300; # 300s = 5 min 
CHECK_TIME = 20;

fan_on = lambda: system('/home/pi/frozen/hub-ctrl -h 0 -P 2 -p 1');
fan_off = lambda: system('/home/pi/frozen/hub-ctrl -h 0 -P 2 -p 0');

#-------------------------------------------------------------------

# main(none) : none

def main(): 
    while(True): 
        if(SENSE.get_temperature() > TEMPERATURE):
            fan_on();
            sleep(FROST_TIME);
        elif(SENSE.get_temperature() < TEMPERATURE):
            fan_off();
            sleep(CHECK_TIME);

#-------------------------------------------------------------------

if(__name__ == '__main__'): 
    main();