#!flask/bin/python
# -*- coding: utf-8 -*-
import unittest
import filecmp
import os

from trains import TWC

__test_inputs__ = {
    'tests/test1.txt': 'tests/result1.txt'
}


class TestCaseBase(unittest.TestCase):
    def test(self):
        for ti, tr in __test_inputs__.items():
            tmpfile = 'tests/tmpfile.txt'
            twc = TWC(ti, tmpfile)
            twc.main()
            self.assertTrue(filecmp.cmp(tr, tmpfile))
            os.unlink(tmpfile)

    def setUp(self):
        pass

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
