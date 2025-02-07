import time
import sys
import os

import numpy as np

text_array = []
duration = 0
frame = 0
fix_height = 0
fix_width = 0

with open('./badapple.txt') as f:
    lines = f.read()
    fs = lines.split("\n")
    for i in range(len(fs)):
      if i == 0:
        duration = float(fs[i])
      elif i == 1:
        frame = float(fs[i])
      elif i == 2:
        fix_height = int(fs[i])
      elif i == 3:
        fix_width = int(fs[i])
      else:
        for t in fs[i]:
          text_array.append(t)

def video(text_array, frame_per_time):
  base_time = time.time()
  next_time = 0
  i = 0
  while i < len(text_array):
    prtText = "" + str(i) + "\n"
    for j in range(fix_height):
      for k in range(fix_width):
        prtText += "" + ("⬛" if text_array[i] == "□" else "⬜")
        i += 1
      prtText += "\n"
    #os.system('cls')
    sys.stdout.write("\r" + prtText)
    sys.stdout.flush()
    next_time = ((base_time - time.time()) % frame_per_time)
    time.sleep(next_time)

frame_per_time = (duration / frame)
video(text_array, frame_per_time)

print(text_array)