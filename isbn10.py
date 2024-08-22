def is_valid(isbn):
    if isbn == "":
        return False
    check = list(isbn)
    sum = 0
    i = 10

    if check[len(check)-1] == 'X':
        check[len(check)-1] = '10'

    for char in check:
        if char.isalpha():
            return "Invalid"

    check = [char for char in check if char.isdigit()]
    check = [int(x) for x in check]

    if len(check) != 10:
        return "Invalid"

    while i > 0:
        sum += check[10-i] * i
        i -= 1
    
    if sum % 11 == 0:
        return "Valid"
    else:
        return "Invalid"

innumber = input("Enter your ISBN-10 number for validation: ")
print(is_valid(innumber))
