# -*- coding: utf-8 -*-
from django.test import TestCase


class SpotifyCallerTestCase(TestCase):

    def setUp(self):
        super(SpotifyCallerTestCase, self).setUp()

    def dummy_test(self):
        self.assertEqual(1 + 1, 2)
