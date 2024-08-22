import string

def wrap(n, min_value, max_value):
    range = max_value - min_value + 1
    return ((n - min_value) % range) + min_value

def rotate(text, key):
    alpha = string.ascii_lowercase
    key = wrap(key, 0, 26)

    newtext = alpha[key:] + alpha[:key]
    trans = str.maketrans(alpha + alpha.upper(), newtext + newtext.upper())
    return text.translate(trans)

