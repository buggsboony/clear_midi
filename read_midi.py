import pretty_midi
# Load MIDI file into PrettyMIDI object
#midi_data = pretty_midi.PrettyMIDI('simple_sustain.midi')
#midi_data = pretty_midi.PrettyMIDI('example.mid')
midi_data = pretty_midi.PrettyMIDI('2C_2fake_sustain.mid')
# Print an empirical estimate of its global tempo
#print midi_data.estimate_tempo()
# Compute the relative amount of each semitone across the entire song,
# a proxy for key

print("instruments:",midi_data.instruments)

# Shift all notes up by 5 semitones
for instrument in midi_data.instruments:
    # Don't want to shift drum notes
        for note in instrument.notes:
            print("note:",note)
            #note.remove()
            #note.pitch += 5
# Synthesize the resulting MIDI data using sine waves
#audio_data = midi_data.synthesize()
