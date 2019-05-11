# FROZEN GUARDIAN

Frozen Guardian est un programme gerant l'alimentation USB d'un
ventilateur en fonction de la temperature mesuré par un capteur

FG est conçu pour tourner sur Raspberry PI avec Sense Hat.

Pour fonctionner correctement, ce programme est dependant d'un
autre, 'hub-ctrl', dont les sources sont disponnibles ici :

https://github.com/codazoda/hub-ctrl.c

Une fois compilé, il faut mettre le programme dans le dossier
'frozen' de l'utilisateur qui lancera ce programme '~/frozen'

Le programme n'a pas de fonction d'arret. 
Il doit etre execute de la façon suivante :

`user@host:~/frozen $ sudo ./frozen_guardian.py &`
