#!/usr/bin/env python
# encoding: utf=8

import sys
import random

import librosa

from amen.audio import Audio
from amen.synthesize import synthesize


audio_file = 'cant_stop.wav'
y, sr = librosa.load(audio_file)
harmonic = librosa.effects.harmonic(y)
percussive = librosa.effects.percussive(y)

harmonic_audio = Audio(raw_samples=harmonic, sample_rate=22050)
percussive_audio = Audio(raw_samples=percussive, sample_rate=22050)

harmonic_beats = harmonic_audio.timings['beats']
percussive_beats = percussive_audio.timings['beats']
random.shuffle(harmonic_beats)


print len(harmonic_beats), len(percussive_beats)

