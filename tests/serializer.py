#!/usr/bin/env python
# -*- coding: utf-8 -*-

from jsonsir import Serializer
from jsonsir.contrib.intencoder import IntEncoder
from jsonsir.contrib.boolencoder import BoolEncoder
from jsonsir.contrib.regexencoder import RegexEncoder
from jsonsir.contrib.datetimeencoder import DateTimeEncoder


# instantiate `Serializer` (bound with specified encoders)
serializer = Serializer([
    IntEncoder(),
    BoolEncoder(),
    RegexEncoder(),
    DateTimeEncoder('%Y-%m-%dT%H:%M:%SZ'),
])
