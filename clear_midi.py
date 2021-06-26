#!/usr/bin/env python
#This script should help to remove bad sustains msg (E4) notes in a midi file

from mido import MidiFile
from mido import Message, MidiFile, MidiTrack
import sys
import os
 



class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    _GREEN = '\033[0;32m'
    _ORANG='\033[0;33m'
    _RED ='\033[0;31m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    CRED = '\033[91m'
    ENDC = '\033[0m'
    _DEF ='\e[39m'
    DEF ='\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    #récent
    GREEN='\033[0;32m' 
    LGREEN='\033[1;32m' 
    WHITE='\033[1;37m'
    YELL='\033[1;33m'
    RED='\033[0;31m'
    LRED='\033[1;31m'
    MAG='\033[0;35m'
    LMAG='\033[1;35m'
    CYAN='\033[0;36m'
    LCYAN='\033[1;36m'
    NC='\033[0m' # No Color
    
#print(bcolors.WARNING + "Warning: No active frommets remain. Continue?" + bcolors.ENDC)

#Check argument presence + exit if arg missing
if len(sys.argv)<2 :
    print(bcolors.RED + "input file needed."+ bcolors.ENDC)
    exit()
fullfilename= sys.argv[1]
#check file existence + exit if not
if( not os.path.exists(fullfilename)):
    print(bcolors.RED + "File '"+fullfilename+"' not found."+ bcolors.ENDC)
    exit()
#Split filename to file basename + file extension :    
filebasename, ext = os.path.splitext(fullfilename)


# #from mido import tempo2bpm
# data_path='./'
# #filename='2C_2fake_sustain.mid'
# filebasename='freeplay'
filename = filebasename+ext
fullfilename = filename

# target_path='./'
target_filename=filebasename+'_clean'+ext
fulltargetfilename = target_filename

print(bcolors.YELL + "Trying to clear midi file '"+fullfilename+"'"+ bcolors.ENDC)

mid = MidiFile(fullfilename)
new_mid = MidiFile()
new_mid.ticks_per_beat = mid.ticks_per_beat
for track in mid.tracks:
    new_track = MidiTrack()
    for msg in track:
        new_msg = msg.copy()
        canAppend = True
        if( hasattr(new_msg,'note') and hasattr(new_msg,'velocity') ):  #Identify failed sustain pump msg => Message('note_on', channel=0, note=64, velocity=127, time=9600),
            if( (new_msg.velocity==127) and (new_msg.note==64) ):                
                print("Found bad sustain pump msg: ", new_msg)
                canAppend = False        
        if (canAppend):                 
            new_track.append(new_msg) #append msg
    new_mid.tracks.append(new_track) #append track

print(bcolors.OKBLUE + "Saving file: " + fulltargetfilename + bcolors.ENDC)
new_mid.save(fulltargetfilename) 
print(bcolors.WHITE + "job done." + bcolors.ENDC)