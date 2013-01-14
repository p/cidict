import unittest
import cidict

class CidictTest(unittest.TestCase):
    def test_empty(self):
        d = cidict.cidict()
        self.assertEqual(0, len(d))
    
    def test_init_no_conflict(self):
        d = cidict.cidict(foo=1, bar=2)
        self.assertEqual(2, len(d))
        self.assertEqual(1, d['foo'])
        self.assertEqual(2, d['bar'])
    
    def test_init_conflict(self):
        d = cidict.cidict(foo=1, bar=2, BAR=3)
        self.assertEqual(2, len(d))
        self.assertEqual(1, d['foo'])
        assert d.has_key('bar')
        assert d['bar'] in [2, 3]
    
    def test_case_insensitive_access(self):
        d = cidict.cidict(foo=1, bar=2)
        self.assertEqual(2, len(d))
        self.assertEqual(1, d['foo'])
        self.assertEqual(1, d['FOO'])
        self.assertEqual(2, d['bar'])
        self.assertEqual(2, d['BAR'])
    
    def test_case_insensitive_membership(self):
        d = cidict.cidict(foo=1, bar=2)
        self.assertEqual(2, len(d))
        assert 'foo' in d
        assert 'FOO' in d
        assert 'bar' in d
        assert 'BAR' in d
