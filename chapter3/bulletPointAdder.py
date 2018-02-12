#! python 3
""" bulletPointAdder.py - Adds Wikipedia style bullets
    to the start of every line."""

import pyperclip

text = pyperclip.paste()

# Separates lines and addes stars
lines = text.split('\n')
for i in range(len(lines)): # Loops all indexes in line list
    lines[i] = '* ' + lines[i] # adds star to each line

text = '\n'.join(lines)

pyperclip.copy(text)
