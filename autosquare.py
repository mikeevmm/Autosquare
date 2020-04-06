#!/usr/bin/env python3
"""Quickly fit an image to a square crop.

Usage:
    autosquare <input> <output>
    autosquare -h | --help
    autosquare --version

Options:
    -h --help            Display this text.
    --version            Display the version.
"""

from internals.docopt import docopt
import subprocess as sp

if __name__ == '__main__':
    arguments = docopt(__doc__, version="autosquare.py 1.0")

    try:
        sp.run(['which', 'convert'], check=True)
    except sp.CalledProcessError:
        print("This utility requires ImageMagick's 'convert' \
 to be in the PATH.")
        exit(1)

    sp.run(['convert', arguments["<input>"], '-set', 'option:size',
            '%[fx:min(w,h)]x%[fx:min(w,h)]', 'xc:none', '+swap',
            '-gravity', 'center', '-composite', arguments["<output>"]])
