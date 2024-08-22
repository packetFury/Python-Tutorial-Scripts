def wrap(n, min_value, max_value):
    range = max_value - min_value + 1
    return ((n - min_value) % range) + min_value

def rotate(text, key):
    processing = list(text)
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for i in range(len(processing)):
        stopshouting = False
        if str(processing[i]).isupper():
            stopshouting = True
            processing[i] = str(processing[i]).lower()
        
        if not processing[i].isalpha() or processing[i] == ' ':
            pass
        else:
            origidx = alpha.index(processing[i])
            idx = wrap(key+origidx, 0, 25)
            if stopshouting == True:
                okbeginshouting = ''.join(alpha[wrap(idx, 0, 25)]).upper()
                processing[i] = str(okbeginshouting)
            else:
                processing[i] = alpha[wrap(idx, 0, 25)]
        
        i += 1

    result = ''.join(processing)
    return result

