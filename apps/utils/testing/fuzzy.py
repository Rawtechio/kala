# -*- coding: utf-8 -*-
# Created on 9 Feb 2016 at 13:41
from __future__ import unicode_literals, absolute_import
import random


# 50/50 chance
def coinflip(): return random.randint(1, 2) == 1


# Is within a certain percentage chance
def in_percentage(x): return random.randint(1, 100) <= x
