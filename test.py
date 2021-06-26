from mido import MidiFile
from mido import tempo2bpm

mid = MidiFile('2C_2fake_sustain.mid')

for i, track in enumerate(mid.tracks):
    print('Track {}: {}'.format(i, track.name))
    for msg in track:
        print(msg)
        print("type",msg.type)
        if msg.type=="set_tempo":
            print("tempo:",tempo2bpm(msg.tempo))
            print("time:",msg.time)
        if not msg.is_meta:
            print("humm msg:",msg)
            if hasattr(msg,'note'):
                print("note:",msg.note)
            if hasattr(msg,'velocity'):
                print("velocity:",msg.velocity)
        if msg.type=="note_on":
            print(msg.note)
            print(msg.velocity)
        if msg.type=="note_off":
            print(msg.note)
            


from mido import Message, MidiFile, MidiTrack

mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

track.append(Message('program_change', program=12, time=0))
track.append(Message('note_on', note=64, velocity=64, time=32))
track.append(Message('note_off', note=64, velocity=127, time=32))

mid.save('new_song.mid')