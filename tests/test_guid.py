from guid import Guid
import unittest
import sys, os
import mock


class TestGuid(unittest.TestCase):
    def setUp(self):
        pass

    @mock.patch("guid.utils.time.time")
    def test_guid_time_is_0(self, time):
        time.return_value = 0
        epoch = 0
        g = Guid(0, 0, epoch)
        value = g.next()
        self.assertEqual(0, value)

    @mock.patch("guid.utils.time.time")
    def test_guid_time_is_0_twice(self, time):
        time.return_value = 0
        epoch = 0
        g = Guid(0, 0, epoch)
        self.assertEqual(0, g.next())
        self.assertEqual(1, g.next())
