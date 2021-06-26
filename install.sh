#!/bin/bash

#install stuff
what=${PWD##*/}
extension=.py

#Le necessaire pour que python fonctionne
pip install mido
#pip install termcolor
#peut être extension vide

echo "Set executable.."
chmod +x $what$extension
echo "lien symbolique vers usr bin"
sudo ln -s "$PWD/$what$extension" /usr/bin/$what