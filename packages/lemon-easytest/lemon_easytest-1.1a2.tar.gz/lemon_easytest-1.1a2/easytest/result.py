#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/1/20 17:53
# @Author : 心蓝
import time
import unittest
from unittest import TestResult as ts


class TestResult(ts):
    """
    测试结果
    """

    def __init__(self, stream=None, descriptions=None, verbosity=None):
        super().__init__(stream=stream, descriptions=None, verbosity=None)
        self.result = []
        self.passed = 0

    def startTest(self, test: unittest.case.TestCase) -> None:
        super().startTest(test)
        self.start_time = time.perf_counter()

    def stopTest(self, test: unittest.case.TestCase) -> None:
        self.end_time = time.perf_counter()

        super().stopTest(test)
        if test.status != 'skipped':
            self.result.append(
                {'name': test._testMethodDoc,
                 'status': test.status,
                 'duration': self.end_time-self.start_time,
                 'case': test.case,
                 'logs': test.logs,
                 }
            )
        self.name = test.name

    def addSuccess(self, test: unittest.case.TestCase) -> None:
        super(TestResult, self).addSuccess(test)
        test.status = 'passed'
        self.passed += 1

    def addFailure(self, test: unittest.case.TestCase, err) -> None:
        super(TestResult, self).addFailure(test, err)
        test.status = 'failed'

    def addError(self, test, err) -> None:
        super(TestResult, self).addError(test, err)
        test.status = 'broken'

    def addSkip(self, test: unittest.case.TestCase, reason: str) -> None:
        super(TestResult, self).addSkip(test, reason)
        test.status = 'skipped'

