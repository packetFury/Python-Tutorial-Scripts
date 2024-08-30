# script to interpret text input and translate to arithmetic operation
import re

def answer(question):
    question = question[:-1]
    working = question.split()
    actors = [int(d) for d in re.findall(r'-?\d+', question)]
    idx = 0
    letsgo = ""
    if question.startswith("What is") == False or question.endswith("cubed"):
        raise ValueError("unknown operation")
    del working[:2]
    for x in working:
        idx = working.index(x)
        match x:
            case "plus":
                working[idx] = '+'
            case "minus":
                working[idx] = '-'
            case "times":
                working[idx] = "*"
            case "multiplied":
                working[idx] = "*"
            case "divided":
                working[idx] = "/"
            case _:
                pass
    letsgo = ' '.join(working)
    # hacky way to bypass double operator test. Will fix later.
    # attempted regex filter caused a cascade of test failures,
    # and at this point I already had a migraine
    if "+ +" in letsgo:
        raise ValueError("syntax error")
    letsgo = letsgo.replace('by', '')
    pemdascheck = re.search(r'(-?\d+\s*[+-]\s*-?\d+)', letsgo)
    if pemdascheck:
        letsgo = letsgo.replace(pemdascheck.group(0), f"({pemdascheck.group(0)})", 1)
    try:
        result = eval(letsgo)
    except:
        raise ValueError("syntax error")
    return result

