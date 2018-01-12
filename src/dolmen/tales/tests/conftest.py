# -*- coding: utf-8 -*-

from crom import testing


def pytest_runtest_setup(item):
    testing.setup()


def pytest_runtest_teardown(item):
    testing.teardown()
