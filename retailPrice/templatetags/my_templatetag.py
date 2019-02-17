import random, os
from django import template



register = template.Library()
@register.simple_tag
def random_int(a, b=None):
    if b is None:
        a, b = 0, a
    return random.randint(a, b)

#Generate random img function
def random_filename(width=128, height=128):
    path = r"C:\Users\Andrea\Desktop\Game\priceisright\assets\img"
    random_filename = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
])
    return random_filename()


# grill = 139.99, Kenmore 4-Burner Gas Grill with Side Burner
# toothpaste = 2.99, Crest Cavity Protection
#coffee maker = 2,730, automatic espresso coffee machine
