import unittest
import main as m

class Behavior(unittest.TestCase):
    def test_behavior(self):
        self.assertEqual(m.reorder(114,12,7,30),{'threshold':114,'reorder':True})
        with self.assertRaises(ValueError): m.reorder(-1,1,1,1)
