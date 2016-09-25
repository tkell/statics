#!/usr/bin/env python
# encoding: utf=8

import sys
import random

import pandas as pd
import librosa

from amen.audio import Audio
from amen.synthesize import synthesize

audio_file = 'cant_stop.wav'
y, sr = librosa.load(audio_file, sr=44100)

percussive = librosa.effects.percussive(y)
percussive_audio = Audio(raw_samples=percussive, sample_rate=44100)
beats = percussive_audio.timings['beats']

output = []
for bar_count in range(133):
    if (bar_count + 1) % 2 == 0:
        if bar_count > 30:
            repeater = 8
        elif bar_count > 60:
            repeater = 16
        elif bar_count > 90:
            repeater = 8
        elif bar_count > 120:
            repeater = 4    

        if bar_count % 16 == 0:
            repeater = repeater * 2
        elif bar_count % 32 == 0:
            repeater = repeater * 4

        beat_index = bar_count * 8
        output.extend(beats[beat_index:beat_index + 2] * repeater)


a = synthesize(output)
a.output('dublake.wav')
