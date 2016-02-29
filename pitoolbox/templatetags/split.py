# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

from django import template
register = template.Library()


@register.filter
def split(string, splitter):
    return string.split(splitter)
