"""Sherlock Tests

This module contains various tests.
"""
from tests.base import SherlockBaseTest
import unittest


class SherlockDetectTests(SherlockBaseTest):
    def test_detect_true(self):
        """Test Username Existence Detection.

        This test ensures that the mechanism of ensuring that a Username
        exists works properly.

        Keyword Arguments:
        self                   -- This object.

        Return Value:
        N/A.
        Will trigger an assert if Usernames which are known to exist are
        not detected.
        """

        self.username_check(['jack'],  ['Twitter'],   exist_check=True)
        #self.username_check(['dfox'],  ['devRant'],   exist_check=True)
        self.username_check(['blue'],  ['Pinterest'], exist_check=True)
        self.username_check(['kevin'], ['Instagram'], exist_check=True)
        self.username_check(['zuck'],  ['Facebook'],  exist_check=True)

        return

    def test_detect_false_via_message(self):
        """Test Username Does Not Exist (Via Message).

        This test ensures that the "message" detection mechanism of
        ensuring that a Username does *not* exist works properly.

        Keyword Arguments:
        self                   -- This object.

        Return Value:
        N/A.
        Will trigger an assert if detection mechanism did not work as expected.
        """

        self.username_check(['jackkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk'],
                            ['Instagram'],
                            exist_check=False
                           )

        return

    def test_detect_false_via_status_code(self):
        """Test Username Does Not Exist (Via Status Code).

        This test ensures that the "status code" detection mechanism of
        ensuring that a Username does *not* exist works properly.

        Keyword Arguments:
        self                   -- This object.

        Return Value:
        N/A.
        Will trigger an assert if detection mechanism did not work as expected.
        """

        self.username_check(['jackkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk'],
                            ['Facebook'],
                            exist_check=False
                           )

        return

    def test_detect_false_via_response_url(self):
        """Test Username Does Not Exist (Via Response URL).

        This test ensures that the "response URL" detection mechanism of
        ensuring that a Username does *not* exist works properly.

        Keyword Arguments:
        self                   -- This object.

        Return Value:
        N/A.
        Will trigger an assert if detection mechanism did not work as expected.
        """

        self.username_check(['jackkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk'],
                            ['Pinterest'],
                            exist_check=False
                           )

        return
