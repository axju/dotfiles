#!/usr/bin/env python

from pathlib import Path
from shutil import rmtree
from logging import getLogger, StreamHandler, Formatter, WARNING, INFO, DEBUG
from argparse import ArgumentParser

logger = getLogger()


def setup_logger(level=0, root='', format_str='%(asctime)s - %(levelname)-7s - %(message)s'):
    """setup the root logger"""
    levels = [WARNING, INFO, DEBUG]
    level = levels[min(len(levels) - 1, level or 0)]
    local_logger = getLogger(root)
    local_logger.setLevel(level)
    ch = StreamHandler()
    ch.setFormatter(Formatter(format_str))
    ch.setLevel(level)
    local_logger.addHandler(ch)
    return local_logger


def link_path(path, target):
    path = Path(path)
    
    logger.debug('file:   "%s"', path)
    logger.debug('target: "%s"', target)
    
    if path.is_file() and target.is_file():
        logger.warning('delete existing target')
        target.unlink()
    elif path.is_dir() and target.is_dir():
        logger.warning('delete existing target')
        if target.is_symlink():
            target.unlink()
        else:
            rmtree(target, ignore_errors=False)

    target.parent.mkdir(parents=True, exist_ok=True)
    target.symlink_to(path)


def main():
    home_dir = Path.home()
    src_dir = Path(__file__).parent.parent / 'src'
    config_dir = src_dir / '.config'
    logger.debug('src:    "%s"', src_dir)

    # ~/.bashrc
    # ~/.xinitrc
    for path in src_dir.iterdir():
        if path.is_file():
            target = Path.home() / path.name
            link_path(path, target)

    # ~/.ssh/config
    link_path(src_dir / '.ssh' / 'config', home_dir / '.ssh' / 'config')

    # ~/.config/alacritty
    # ~/.config/conky
    # ~/.config/pip
    # ~/.config/qtile
    # ~/.config/ranger
    for path in config_dir.iterdir():
        if path.is_dir():
            target = Path.home() / '.config' / path.name
            link_path(path, target)
            
    # ln -s ~/.dotfiles/src/.config/qtile ~/.config/qtile
    # ln -s ~/.dotfiles/src/.config/alacritty ~/.config/alacritty
    # ln -s ~/.dotfiles/src/.config/rofi ~/.config/rofi
    # ln -s ~/.dotfiles/src/.config/pip ~/.config/pip
    # ln -s ~/.dotfiles/src/.config/conky/ ~/.config/conky
    # ln -s ~/.dotfiles/src/.config/ranger/ ~/.config/ranger
    # ln -s ~/.dotfiles/src/.ssh/config ~/.ssh/config
    # ln -s ~/.dotfiles/src/.bashrc ~/.bashrc
    # ln -s ~/.dotfiles/src/.xinitrc ~/.xinitrc



def cli():
    parser = ArgumentParser()
    parser.add_argument(
        '-v', '--verbose', action='count', 
        help="verbose level... repeat up to three times"
    )
    args = parser.parse_args()
    setup_logger(args.verbose)
    main()


if __name__ == '__main__':
    cli()
