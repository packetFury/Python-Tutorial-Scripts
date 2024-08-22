def classify(number):
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    sum = 0
    i = 1
    while i < number:
        if number % i == 0:
           sum += i
        i += 1

    if number == sum:
        return "perfect"
    if number < sum:
        return "abundant"
    if number > sum:
        return "deficient"
        
innumber = int(input("Enter your number: "))
print(classify(innumber))
