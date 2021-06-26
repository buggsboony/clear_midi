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
            