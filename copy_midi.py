
from mido import MidiFile
from mido import Message, MidiFile, MidiTrack
#from mido import tempo2bpm
data_path='./'
filename='2C_2fake_sustain.mid'

target_path='./'
target_filename='output.mid'

mid = MidiFile(data_path + filename)
new_mid = MidiFile()
new_mid.ticks_per_beat = mid.ticks_per_beat
for track in mid.tracks:
    new_track = MidiTrack()
    for msg in track:
        new_msg = msg.copy()
        if new_msg.type == 'set_tempo':
            new_msg.tempo = 500000
        new_track.append(new_msg)
    new_mid.tracks.append(new_track)
new_mid.save(target_path + target_filename) 