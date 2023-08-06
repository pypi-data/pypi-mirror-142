import unittest

from stringtoolsfpat import StringToolsFpat

class Test(unittest.TestCase):
    def test_lower_method(self):
        self.assertEqual(StringToolsFpat.lower("TEST"), "test")
        self.assertNotEqual(StringToolsFpat.lower("test"), "TEST")