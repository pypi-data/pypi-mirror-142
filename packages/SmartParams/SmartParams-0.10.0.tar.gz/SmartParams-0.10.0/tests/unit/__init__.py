import os
import unittest

from smartparams.utils import str_to_bool

_UNIT = str_to_bool(os.getenv('TEST_UNIT', default='1'))


@unittest.skipUnless(_UNIT, reason="Unit tests are disabled")
class UnitCase(unittest.TestCase):
    pass
