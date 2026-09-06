"""
Local grader for the Python adaptation of Andrew Ng's Machine Learning course.

This is a drop-in replacement for the original Coursera submission helper. The
public interface used by every exercise is unchanged:

    grader = utils.Grader()
    grader[1] = someFunction
    grader.grade()

The difference is that ``grade()`` no longer contacts Coursera and no longer asks
for a login/token. Instead it runs each graded part against a bundled set of
reference outputs and prints a local pass/fail table, so students can check the
correctness of their own solutions offline.

The reference solutions live (obfuscated) in ``grader_answers.dat``. They are
lightly scrambled so students cannot simply open the file and copy an answer, but
this is deliberately *not* strong encryption -- it only discourages casual
copying. Instructors can regenerate or inspect the bundle with
``build_grader_answers.py``.
"""

import os
import sys
import json
import zlib
import base64
import warnings
import importlib
import itertools
from collections import OrderedDict

import numpy as np

ANSWERS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'grader_answers.dat')

# Obfuscation key. Changing this requires rebuilding grader_answers.dat.
_XOR_KEY = b'ml-coursera-python-assignments::local-grader'

# Default numerical tolerance when comparing a student's output with the
# reference output (absolute, relative).
_DEFAULT_TOL = (1e-3, 3e-3)


def _xor(data, key):
    return bytes(b ^ key[i % len(key)] for i, b in enumerate(data))


def _pack(mapping):
    """Serialize + scramble a {name: source} mapping into an ascii blob."""
    raw = json.dumps(mapping).encode('utf-8')
    return base64.b64encode(_xor(zlib.compress(raw, 9), _XOR_KEY)).decode('ascii')


def _unpack(blob):
    """Inverse of :func:`_pack`."""
    raw = zlib.decompress(_xor(base64.b64decode(blob.encode('ascii')), _XOR_KEY))
    return json.loads(raw.decode('utf-8'))


def sprintf(fmt, arg):
    """ Emulates (part of) the Octave sprintf function. """
    if isinstance(arg, tuple):
        # for multiple return values, only use the first one
        arg = arg[0]

    if isinstance(arg, (np.ndarray, list)):
        # concatenates all elements, column by column
        return ' '.join(fmt % e for e in np.asarray(arg).ravel('F'))
    else:
        return fmt % arg


def _load_reference(assignment_slug, utils_module):
    """Decode the bundled reference solution module for a given exercise."""
    with open(ANSWERS_FILE, 'r') as f:
        bundle = _unpack(f.read().strip())

    if assignment_slug not in bundle:
        raise KeyError('No bundled reference solutions for "%s"' % assignment_slug)

    namespace = {'utils': utils_module, '__name__': 'reference_%s' % assignment_slug}
    exec(compile(bundle[assignment_slug], '<reference:%s>' % assignment_slug, 'exec'), namespace)
    parts = namespace['PARTS']
    tol = namespace.get('TOL', {})
    return parts, tol


def _tokenize(result):
    return sprintf('%0.5f ', result).split()


def _matches(student_result, reference_result, tol):
    atol, rtol = tol
    a = _tokenize(student_result)
    b = _tokenize(reference_result)
    if len(b) == 0 or len(a) != len(b):
        return False
    for x, y in zip(a, b):
        try:
            xf, yf = float(x), float(y)
        except ValueError:
            if x != y:
                return False
            continue
        if not np.isfinite(xf) or abs(xf - yf) > atol + rtol * abs(yf):
            return False
    return True


def _distribute_points(n):
    """Split 100 points across n parts as evenly as possible."""
    base = 100 // n
    points = [base] * n
    for i in range(100 - base * n):
        points[i] += 1
    return points


class SubmissionBase:

    def __init__(self, assignment_slug, assignment_key, part_names, part_names_key):
        self.assignment_slug = assignment_slug
        self.assignment_key = assignment_key
        self.part_names = part_names
        self.part_names_key = part_names_key
        self.login = None
        self.token = None
        self.functions = OrderedDict()
        self.args = dict()

    # ------------------------------------------------------------------
    # public interface (unchanged)
    # ------------------------------------------------------------------
    def __setitem__(self, key, value):
        self.functions[key] = value

    def __iter__(self):
        for part_id in self.functions:
            yield part_id

    def grade(self):
        print('\nGrading Solutions | Programming Exercise %s\n' % self.assignment_slug)

        utils_module = sys.modules.get(type(self).__module__)
        if utils_module is None:
            try:
                utils_module = importlib.import_module('utils')
            except ImportError:
                pass
        try:
            ref_parts, ref_tol = _load_reference(self.assignment_slug, utils_module)
        except Exception as e:  # pragma: no cover - defensive
            print('Could not load the local grader reference data: %s' % e)
            return

        student = self._evaluate(self.functions)

        # Build every combination of acceptable reference implementations and
        # collect the reference output(s) for each part.
        part_ids = sorted(ref_parts)
        choices = [ref_parts[p] if isinstance(ref_parts[p], (list, tuple)) else [ref_parts[p]]
                   for p in part_ids]
        reference = {p: [] for p in part_ids}
        for combo in itertools.product(*choices):
            variant = OrderedDict(zip(part_ids, combo))
            result = self._evaluate(variant)
            for p in part_ids:
                if p in result:
                    reference[p].append(result[p])

        points = _distribute_points(len(self.part_names))

        print('%43s | %9s | %-s' % ('Part Name', 'Score', 'Feedback'))
        print('%43s | %9s | %-s' % ('---------', '-----', '--------'))

        total = 0
        for index, name in enumerate(self.part_names):
            part_id = index + 1
            max_score = points[index]

            if part_id not in self.functions:
                feedback = 'Not submitted'
                score = 0
            elif part_id not in student:
                feedback = student.get('_errors', {}).get(part_id, 'Error while running your function')
                score = 0
            else:
                tol = ref_tol.get(part_id, _DEFAULT_TOL)
                ok = any(_matches(student[part_id], ref, tol) for ref in reference.get(part_id, []))
                if ok:
                    feedback = 'Correct!'
                    score = max_score
                else:
                    feedback = 'Incorrect output'
                    score = 0

            total += score
            print('%43s | %9s | %-s' % (name, '%d / %3d' % (score, max_score), feedback))

        print('                                  --------------------------------')
        print('%43s | %9s | %-s\n' % (' ', '%d / %d' % (total, sum(points)), ' '))

    # ------------------------------------------------------------------
    # internals
    # ------------------------------------------------------------------
    def _evaluate(self, functions):
        """Run the exercise-specific part dispatch (defined in each Grader
        subclass' ``__iter__``) using ``functions`` as the function table."""
        saved = self.functions
        self.functions = functions
        results = {}
        errors = {}
        try:
            gen = iter(self)
            while True:
                try:
                    with warnings.catch_warnings():
                        warnings.simplefilter('ignore')
                        part_id, value = next(gen)
                except StopIteration:
                    break
                except Exception as e:
                    # A submitted function raised. We cannot resume the
                    # subclass generator, so remaining parts are unknown.
                    errors['_generator'] = str(e)
                    break
                results[part_id] = value
        finally:
            self.functions = saved
        if errors:
            missing = [pid for pid in sorted(functions) if pid not in results]
            results['_errors'] = {}
            if missing:
                raiser = missing[0]
                results['_errors'][raiser] = errors['_generator']
                for pid in missing[1:]:
                    results['_errors'][pid] = 'Not evaluated (part %d raised an error)' % raiser
        return results
