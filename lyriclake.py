#!/usr/bin/env python
# encoding: utf=8

import sys
import random

import librosa

from amen.audio import Audio
from amen.synthesize import synthesize

audio_file = 'cant_stop.wav'
y, sr = librosa.load(audio_file, sr=44100)

harmonic = librosa.effects.harmonic(y, margin=3.0)
harmonic_audio = Audio(raw_samples=harmonic, sample_rate=44100)

beats = harmonic_audio.timings['beats']
chroma = harmonic_audio.features['chroma'].at(beats)


# Set up the tone row array
notes = ['f', 'e', 'c', 'a', 'g', 'd', 'ab', 'db', 'eb', 'gb', 'bb', 'b']
sorted_chroma = {}
for note in notes:
        sorted_chroma[note] = []

# sort the chroma and beats
for beat, chrom in chroma.with_time():
    note = max(chrom, key=lambda k: chrom[k])
    value = max(chrom.values())
    try:
        sorted_chroma[note].append((beat, value))
    except KeyError:
        pass # Because we have d# and eb
for note in sorted_chroma:
    sorted_chroma[note] = sorted(sorted_chroma[note], key=lambda x: x[1], reverse=True)

# Make the audio
output = []
counter = 0
notes = ['f', 'e', 'c', 'a', 'g', 'd', 'ab', 'db', 'eb', 'gb', 'bb', 'b']
while counter < 20:
    for note in notes:
        if len(sorted_chroma[note]) <= counter:
            continue
        output.append(sorted_chroma[note][counter][0]) # the beat, not the value
    counter = counter + 1

# write out
out = synthesize(output)
out.output('lyriclake.wav')
