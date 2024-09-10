#!/usr/bin/env python3
"""
PWM Tone Generator

based on https://www.coderdojotc.org/micropython/sound/04-play-scale/
"""

import machine
import utime

# GP16 is the speaker pin
SPEAKER_PIN = 16

# create a Pulse Width Modulation Object on this pin
speaker = machine.PWM(machine.Pin(SPEAKER_PIN))

# Define musical note frequencies
notes = {
    'C4': 262,
    'D4': 294,
    'E4': 330,
    'F4': 349,
    'G4': 392,
    'A4': 440,
    'B4': 494,
    'C5': 523,
    'D5': 587,
    'E5': 659,
    'F5': 698,
    'F#5': 740,
    'G5': 784,
    'A5': 880,
    'C6': 1047,
    'D6': 1175
}

# Simple melody (notes and durations in seconds)
melody = [
    ('G4', 0.4), ('B4', 0.4), ('D5', 0.4), ('F#5', 0.4),  # Example phrase
    ('G5', 0.4), ('F#5', 0.4), ('D5', 0.4), ('B4', 0.4),
    ('G4', 0.4), ('C5', 0.4), ('D5', 0.4), ('G5', 0.4), ('A5', 1.2),              # Continue with your notes
    # Add more notes and phrases to build the melody
]

def playtone(frequency: float, duration: float) -> None:
    speaker.duty_u16(1000)
    speaker.freq(frequency)
    utime.sleep(duration)


def quiet():
    speaker.duty_u16(0)

# Play the melody
for note, duration in melody:
    if note in notes:
        print(f"Playing: {note} ({notes[note]} Hz)")
        playtone(notes[note], duration)
    else:
        quiet()  # rest or unknown note
    utime.sleep(0.05)  # small pause between notes
    
'''
freq: float = 30
duration: float = 0.1  # seconds

print("Playing frequency (Hz):")

for i in range(64):
    print(freq)
    playtone(freq, duration)
    freq = int(freq * 1.1)
'''
# Turn off the PWM
quiet()
