#!/usr/bin/env python
# encoding: utf=8

import sys
from amen.audio import Audio
from amen.synthesize import synthesize


audio_file = 'cant_stop.wav'
audio = Audio(audio_file)

beats = audio.timings['beats']
new_beats = []
for i, beat in enumerate(beats):
    if i % 4 == 0:
        new_beats.append(beat)

        out = synthesize(new_beats)
        out.output('one_stop.wav')
