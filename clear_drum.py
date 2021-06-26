import pretty_midi as pm

sound = pm.PrettyMIDI("example.mid")

# check all songs, remove the not in case you want to remove all drums
# instead of including all drums
drum_instruments_index = [i for i, inst in enumerate(sound.instruments) if not inst.is_drum]
# remove all non drums, from the sorted such that no conflicting indexes
for i in sorted(drum_instruments_index, reverse=True):
    del sound.instruments[i]
sound.write('MyDrumOnlyMidi.midi')