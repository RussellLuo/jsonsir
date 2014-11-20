#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import re
import unittest

from jsonsir import Serializer

from encoders import init
init()


class JsonSirTest(unittest.TestCase):

    def setUp(self):
        self.serializer = Serializer()

    def test_intencoder_serialize(self):
        data = {'age': 10}
        self.serializer.serialize(data)
        self.assertEqual(data, {'age': 10})

        data = {'age': 10}
        self.serializer.serialize(data, with_type_name=True)
        self.assertEqual(data, {'age': 10})

    def test_intencoder_deserialize(self):
        data = {'age': 'int(10)'}
        self.serializer.deserialize(data)
        self.assertEqual(data, {'age': 10})

    def test_boolencoder_serialize(self):
        data = {'male': True}
        self.serializer.serialize(data)
        self.assertEqual(data, {'male': True})

        data = {'male': True}
        self.serializer.serialize(data, with_type_name=True)
        self.assertEqual(data, {'male': True})

    def test_boolencoder_deserialize(self):
        data = {'male': 'bool(true)'}
        self.serializer.deserialize(data)
        self.assertEqual(data, {'male': True})

    def test_regexencoder_serialize(self):
        data = {'name': re.compile(r'^russell')}
        self.serializer.serialize(data)
        self.assertEqual(data, {'name': '/^russell/'})

        data = {'name': re.compile(r'^russell')}
        self.serializer.serialize(data, with_type_name=True)
        self.assertEqual(data, {'name': 'regex(/^russell/)'})

    def test_regexencoder_deserialize(self):
        data = {'name': 'regex(/^russell/)'}
        self.serializer.deserialize(data)

        origin, current = data['name'], re.compile(r'^russell')
        # suppose type-equality and pattern-equality mean regex-equality
        self.assertEqual(type(origin), type(current))
        self.assertEqual(origin.pattern, current.pattern)

    def test_datetimeencoder_serialize(self):
        data = {'birthday': datetime.datetime(2014, 10, 10)}
        self.serializer.serialize(data)
        self.assertEqual(data, {'birthday': '2014-10-10T00:00:00Z'})

        data = {'birthday': datetime.datetime(2014, 10, 10)}
        self.serializer.serialize(data, with_type_name=True)
        self.assertEqual(data, {'birthday': 'datetime(2014-10-10T00:00:00Z)'})

    def test_datetimeencoder_deserialize(self):
        data = {'birthday': 'datetime(2014-10-10T00:00:00Z)'}
        self.serializer.deserialize(data)
        self.assertEqual(data, {'birthday': datetime.datetime(2014, 10, 10)})


if __name__ == '__main__':
    unittest.main()
