def primalrage(numb):
    for x in range(numb + 1, 2 * numb):
        if all(x % i != 0 for i in range(2, int(x**0.5) + 1)):
            return x
    return numb + 1

def factors(value):
    result = []
    j = 2
    while j <= value:
        if value % j == 0:
            value = value / j
            result.append(j)
        else:
            k = primalrage(j)
            if k <= j:
                j += 1
            else:
                j = k
    return result
