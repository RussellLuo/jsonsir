#!/usr/bin/env python
# -*- coding: utf-8 -*-

from jsonsir import Serializer
from jsonsir.contrib.intencoder import IntEncoder
from jsonsir.contrib.boolencoder import BoolEncoder
from jsonsir.contrib.regexencoder import RegexEncoder
from jsonsir.contrib.datetimeencoder import DateTimeEncoder


def init():
    # register some encoders
    Serializer.register(IntEncoder())
    Serializer.register(BoolEncoder())
    Serializer.register(RegexEncoder())
    Serializer.register(DateTimeEncoder('%Y-%m-%dT%H:%M:%SZ'))
