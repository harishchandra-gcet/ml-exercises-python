"""
Build (or inspect) the obfuscated reference-solution bundle used by the local
grader.

Usage
-----
    python build_grader_answers.py            # bundle grader_solutions/*.py -> grader_answers.dat
    python build_grader_answers.py --extract  # grader_answers.dat -> grader_solutions/*.py

The plaintext reference solutions live in ``grader_solutions/`` (git-ignored so
students who clone the repo only ever get the scrambled ``grader_answers.dat``).
Each file is named after the assignment slug, e.g. ``linear-regression.py`` and
must define a module-level ``PARTS`` dict (part id -> callable, or a list of
acceptable callables) and may define a ``TOL`` dict (part id -> (atol, rtol)).
"""

import os
import sys
import glob

from submission import _pack, _unpack

HERE = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(HERE, 'grader_solutions')
OUT_FILE = os.path.join(HERE, 'grader_answers.dat')


def build():
    sources = {}
    for path in sorted(glob.glob(os.path.join(SRC_DIR, '*.py'))):
        slug = os.path.splitext(os.path.basename(path))[0]
        with open(path, 'r', encoding='utf-8') as f:
            sources[slug] = f.read()
    if not sources:
        sys.exit('No reference solutions found in %s' % SRC_DIR)
    with open(OUT_FILE, 'w') as f:
        f.write(_pack(sources))
    print('Wrote %s (%d exercises: %s)' % (OUT_FILE, len(sources), ', '.join(sorted(sources))))


def extract():
    with open(OUT_FILE, 'r') as f:
        sources = _unpack(f.read().strip())
    os.makedirs(SRC_DIR, exist_ok=True)
    for slug, source in sources.items():
        path = os.path.join(SRC_DIR, slug + '.py')
        with open(path, 'w', encoding='utf-8') as f:
            f.write(source)
        print('Wrote %s' % path)


if __name__ == '__main__':
    if '--extract' in sys.argv:
        extract()
    else:
        build()
