
from mido import MidiFile
from mido import Message, MidiFile, MidiTrack
#from mido import tempo2bpm
data_path='./'
#filename='2C_2fake_sustain.mid'
filebasename='freeplay'
filename = filebasename+'.mid'

target_path='./'
target_filename=filebasename+'_clean.mid'

mid = MidiFile(data_path + filename)
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

print('Saving file :',target_path + target_filename)
new_mid.save(target_path + target_filename) 
print('job done.')