# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function
import hashlib

from django import template

register = template.Library()


@register.filter
def md5(value):
    mdhash = hashlib.md5()
    mdhash.update(str(value))
    return str(mdhash.hexdigest())
