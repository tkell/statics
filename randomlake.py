#!/usr/bin/env python
# encoding: utf=8

import sys
import random

import librosa

from amen.audio import Audio
from amen.synthesize import synthesize

audio_file = 'cant_stop.wav'
y, sr = librosa.load(audio_file, sr=44100)

harmonic = librosa.effects.harmonic(y)
harmonic_audio = Audio(raw_samples=harmonic, sample_rate=44100)
harmonic_beats = harmonic_audio.timings['beats']

percussive = librosa.effects.percussive(y)
percussive_audio = Audio(raw_samples=percussive, sample_rate=44100)
percussive_beats = percussive_audio.timings['beats']

random.shuffle(harmonic_beats)

slices = []
times = []
for p_beat, h_beat in zip(percussive_beats, harmonic_beats):
    slices.append(h_beat)
    times.append(p_beat.time)
    slices.append(p_beat)
    times.append(p_beat.time)

out = synthesize((slices, times))
out.output('randomlake.wav', 'WAV')
