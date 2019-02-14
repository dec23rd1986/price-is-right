from django import template
import random

register = template.Library()

def random_int(a, b=None):
    if b is None:
        a, b = 0, a
    return random.randint(a, b)
