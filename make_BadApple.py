import ffmpeg
import cv2
import os
import sys
import time
import shutil
from tqdm import tqdm
import subprocess
from concurrent.futures import ProcessPoolExecutor

import numpy as np

video_path = "./【東方】Bad Apple!! ＰＶ【影絵】 [FtutLA63Cp8].webm"

#動画を配列に

video_info = ffmpeg.probe(video_path)
width = video_info["streams"][0]['width']
height = video_info["streams"][0]['height']
duration = float(video_info["format"]['duration'])

out, _ = (
    ffmpeg
    .input(video_path, ss=0, t=duration)
    .output('pipe:', format='rawvideo', pix_fmt='rgb24')
    .run(capture_stdout=True)
)

arr = (
    np
    .frombuffer(out, np.uint8)
    .reshape([-1, height, width, 3])
)


#配列を文字に
#heightとwidth次第で縦横比を変更できます

fix_height = 19
fix_width = 19

frame = arr.shape[0]
text_array = np.full((frame, fix_height, fix_width), None)
for i in tqdm(range(frame)):
    resize_im = cv2.resize(arr[i], dsize=(fix_width, fix_height))
    gray_sca = resize_im[:, :, 0] * 0.299 + \
        resize_im[:, :, 1] * 0.587 + resize_im[:, :, 2] * 0.114
    for j in range(fix_height):
        for k in range(fix_width):
            if 0 <= gray_sca[j, k] < 30:
                text_array[i, j, k] = "□"
            elif 30 <= gray_sca[j, k] < 80:
                text_array[i, j, k] = "□"
            elif 80 <= gray_sca[j, k] < 160:
                text_array[i, j, k] = "■"
            else:
                text_array[i, j, k] = "■"

#ファイル保存フェーズ
with open("badapple.txt","w") as o:
    print(duration, sep="", file=o)
    print(frame, sep="", file=o)
    print(fix_height, sep="", file=o)
    print(fix_width, sep="", file=o)
    for row in text_array:
        for row2 in row:
            print(*row2, sep="", file=o) 
