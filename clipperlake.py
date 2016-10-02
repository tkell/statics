import sys
import random

import pandas as pd
import librosa

from amen.audio import Audio
from amen.synthesize import synthesize

audio_file = 'cant_stop.wav'
audio = Audio(audio_file)
beats = audio.timings['beats']
beat_length = 0.487619

counts = [7, 6, 5, 4, 3, 2, 1]
while len(counts) < 256:
    for i in range(1, 8):
        reps = random.randint(1, 4)
        if i == 1:
            reps = random.randint(1, 3)
        elif i == 2:
            reps = random.randint(1, 4)
        else:
            reps = random.randint(1, 5)
            
        counts.extend([i] * reps)

counts.extend([7, 6, 5, 4, 3, 2, 1, 4, 3, 2, 1, 4, 3, 2, 1, 0, 0])

slices = []
times = []
time = pd.to_timedelta(0, 's')
for count, beat in zip(counts, beats[0:len(counts)]):
    t = beat_length / (2 ** count)
    time = time + pd.to_timedelta(t, 's')
    slices.append(beat)
    times.append(time)

a = synthesize((slices, times))
a.output('clipperlake.wav')
