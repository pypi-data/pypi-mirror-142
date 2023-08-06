import os
import unittest

from smartparams.utils import str_to_bool

_INTEGRATION = str_to_bool(os.getenv('TEST_INTEGRATION', default='1'))


@unittest.skipUnless(_INTEGRATION, reason="Integration tests are disabled")
class IntegrationCase(unittest.TestCase):
    pass
