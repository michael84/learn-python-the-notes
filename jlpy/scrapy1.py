#!/usr/bin/env python
# *-*coding:utf-8*-*
# Author: Wei Tong

import requests
import xml.etree.ElementTree as ET
from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
    def __init__(self, provinces):
        self.provinces = provinces

    def start_element(self, name, attrs):
        if name

