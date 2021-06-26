#!/bin/bash

#uninstall stuff
what=${PWD##*/}
extension=py


pip uninstall mido

#peut être extension vide 
 
echo "Supprimer lien symbolique dans usr bin"
sudo rm /usr/bin/$what