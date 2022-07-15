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


def link_path(path, src_dir):
    path = Path(path)
    target = Path.home() / path.relative_to(src_dir)
    
    logger.debug('file:   "%s"', path)
    logger.debug('target: "%s"', target)
    logger.debug('='*42)
    
    if target.is_file():
        logger.warning('delete existing file')
        target.unlink()
    elif target.is_symlink():
        logger.warning('unlink existing link')
        target.unlink()

    target.parent.mkdir(parents=True, exist_ok=True)
    target.symlink_to(path)


def main(src_dir=Path(__file__).parent.parent / 'src'):
    src_dir = Path(src_dir)
    logger.debug('src:    "%s"', src_dir)

    for path in src_dir.glob('**/*'):
        if not path.is_file():
            continue
        if path.suffix in ['.pyc']:
            continue
        link_path(path, src_dir)


def cli():
    default_dir = Path(__file__).parent.parent / 'src'
    parser = ArgumentParser()
    parser.add_argument(
        '-v', '--verbose', action='count', 
        help="verbose level... repeat up to three times"
    )
    parser.add_argument(
        'path', nargs='?',const=default_dir, default=default_dir, 
        help="path to dotfiles"
    )
    args = parser.parse_args()
    setup_logger(args.verbose)
    main(args.path)


if __name__ == '__main__':
    cli()
