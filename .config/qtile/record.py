"""
just a prprogram to record my screen.
the ra record command look like:
    ffmpeg -video_size 1920x1080 -framerate 1 -f x11grab -i :0.0+1366,0 \
            -c:v libx264rgb -crf 0 -preset ultrafast -filter:v "setpts=N/TB/30" -r 30 -y records.mkv
"""
from pathlib import Path
from time import sleep
from datetime import datetime
import subprocess

REC_PATH = Path('~/.local/share/qtile/REC').expanduser()


def main():
    print('running main')
    proc = None
    while True:
        if REC_PATH.is_file() and proc is None:
            print('start record...')
            path = Path('~/records').expanduser() / (datetime.now().strftime('%Y-%m-%d_%H:%M:%S') + '.mkv')
            proc = subprocess.Popen([
                'ffmpeg', '-video_size', '1920x1080', '-framerate', '1',
                '-f', 'x11grab', '-i', ':0.0+1366,0',
                '-c:v', 'libx264rgb', '-crf', '0', '-preset', 'ultrafast',
                '-filter:v', 'setpts=N/TB/30', '-r', '30', '-y',
                path
            ], stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        elif not REC_PATH.is_file() and proc:
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
