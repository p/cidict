import unittest
import cidict

class CidictTest(unittest.TestCase):
    def test_empty(self):
        d = cidict.cidict()
        self.assertEqual(0, len(d))
    
    def test_init_maping_no_conflict(self):
        d = cidict.cidict(dict(foo=1, bar=2))
        self.assertEqual(2, len(d))
        self.assertEqual(1, d['foo'])
        self.assertEqual(2, d['bar'])
    
    def test_init_mapping_conflict(self):
        d = cidict.cidict(dict(foo=1, bar=2, BAR=3))
        self.assertEqual(2, len(d))
        self.assertEqual(1, d['foo'])
        assert d.has_key('bar')
        assert d['bar'] in [2, 3]
    
    def test_init_kwargs_no_conflict(self):
        d = cidict.cidict(foo=1, bar=2)
        self.assertEqual(2, len(d))
        self.assertEqual(1, d['foo'])
        self.assertEqual(2, d['bar'])
    
    def test_init_kwargs_conflict(self):
        d = cidict.cidict(foo=1, bar=2, BAR=3)
        self.assertEqual(2, len(d))
        self.assertEqual(1, d['foo'])
        assert d.has_key('bar')
        assert d['bar'] in [2, 3]
    
    def test_init_kwargs_override(self):
        d = cidict.cidict(dict(foo=1, bar=2), foo=4, bar=5)
        self.assertEqual(2, len(d))
        self.assertEqual(4, d['foo'])
        self.assertEqual(5, d['bar'])
    
    def test_init_kwargs_ci_override(self):
        d = cidict.cidict(dict(foo=1, BAR=2), FOO=4, bar=5)
        self.assertEqual(2, len(d))
        self.assertEqual(4, d['foo'])
        self.assertEqual(5, d['bar'])
    
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
