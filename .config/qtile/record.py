"""
just a prprogram to record my screen.
the ra record command look like:
    ffmpeg -video_size 1920x1080 -framerate 1 -f x11grab -i :0.0+1366,0 \
            -c:v libx264rgb -crf 0 -preset ultrafast -filter:v "setpts=N/TB/30" -r 30 -y records.mkv
"""
import subprocess
from time import sleep
from datetime import datetime

from config import REC_TRIGGER, REC_STORAGE


def main():
    print('running main')
    proc = None
    while True:
        if REC_TRIGGER.is_file() and proc is None:
            print('start record...')
            path = REC_STORAGE / (datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + '.mkv')
            path.parent.mkdir(parents=True, exist_ok=True)
            proc = subprocess.Popen([
                'ffmpeg', '-video_size', '1920x1080', '-framerate', '1',
                '-f', 'x11grab', '-i', ':0.0+1366,0',
                '-c:v', 'libx264rgb', '-crf', '0', '-preset', 'ultrafast',
                '-filter:v', 'setpts=N/TB/30', '-r', '30', '-y',
                path
            ], stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        elif not REC_TRIGGER.is_file() and proc:
            print('now stop record...')
            proc.stdin.write('q'.encode("GBK"))
            proc.communicate()
            #proc.kill()
            proc.wait()
            proc = None
        sleep(0.5)


while True:
    try:
        main()
    except KeyboardInterrupt:
        break
print('exit...')
