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

harmonic = librosa.effects.harmonic(y)
harmonic_audio = Audio(raw_samples=harmonic, sample_rate=44100)
harmonic_beats = harmonic_audio.timings['beats']

percussive = librosa.effects.percussive(y)
percussive_audio = Audio(raw_samples=percussive, sample_rate=44100)
percussive_beats = percussive_audio.timings['beats']

fib_numbers = [1, 1, 2, 3, 5, 8, 5, 3, 2, 1, 1]
pi_numbers =  [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
e_numbers =   [2, 7, 1, 8, 2, 8, 1, 8, 2, 8, 4]


def process(loops, target, audio):
    output = []
    old_index = 0
    for index, loop in enumerate(loops):
        new_index = old_index + target[index]
        slices = audio[old_index:new_index]
        old_index = new_index
        complete = slices * loop
        output.extend(complete)
    return output

pi_output = process(fib_numbers, pi_numbers, percussive_beats)
e_output = process(fib_numbers, e_numbers, harmonic_beats)

def gen(harm, perc):
    h_now = pd.to_timedelta(0.0, 's')
    p_now = pd.to_timedelta(0.0, 's')
    
    for h in harm:
        yield h, h_now
        h_now = h_now + h.duration
    
    for p in perc:
        yield p, p_now
        p_now = p_now + p.duration

g = gen(pi_output, e_output)
final = synthesize(g)
final.output('epilake.wav')
