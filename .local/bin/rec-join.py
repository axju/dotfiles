#!/usr/bin/env python
from pathlib import Path
from datetime import datetime
import subprocess


REC_STORAGE = Path('~/records').expanduser()
DATE = datetime.now()

videos = {}
for path in REC_STORAGE.iterdir():
    try:
        dt = datetime.strptime(path.stem, '%Y-%m-%d_%H:%M:%S')
    except ValueError:
        continue
    videos[dt] = path

indexs = sorted(videos.keys())

for dt, path in videos.items():
    print(dt, path.name)

print('sorted:')
for index in indexs:
    print(index, videos[index].name)

output = Path('~/records/days/').expanduser() / DATE.strftime('%Y-%m-%d.mkv')
subprocess.run(['ffmpeg', '-i', 'concat:' + '|'.join([str(videos[i]) for i in indexs]), '-c', 'copy', '-y', output])
