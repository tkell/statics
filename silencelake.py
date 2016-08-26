#!/usr/bin/env python
# encoding: utf=8

import sys
import random
import datetime import timedelta

import librosa

from amen.audio import Audio
from amen.synthesize import synthesize

audio_file = 'cant_stop.wav'
audio = Audio(audio_file)
beats = audio.timings['beats']

def g(beats):
    for i, beat in enumerate(beats[0:16]):
        offset = timedelta(seconds = i ** 2)
        yield (beat, beat.time + offset)

out = synthesize(gen)
out.output('silencelake.wav', 'WAV')

