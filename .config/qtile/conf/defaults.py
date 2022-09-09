from pathlib import Path
from libqtile.utils import guess_terminal

REC_TRIGGER = Path('~/.local/share/qtile/REC').expanduser()
terminal = guess_terminal()
mod = "mod4"