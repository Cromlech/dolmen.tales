"""Test setup for megrok.chameleon.
"""
import doctest
import unittest
import dolmen.tales

FLAGS = (doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE)


def test_suite():
    """Get a testsuite of all doctests.
    """
    suite = unittest.TestSuite()
    for name in ['slot.txt']:
        test = doctest.DocFileSuite(
            name,
            package=dolmen.tales.tests,
            globs=dict(__name__="dolmen.tales.tests"),
            optionflags=FLAGS,
            )
        suite.addTest(test)
    return suite
