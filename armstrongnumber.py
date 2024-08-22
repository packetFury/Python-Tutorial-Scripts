def is_armstrong_number(number):
    intake = str(number)
    sum = 0

    for digit in intake:
        sum += int(digit)**len(intake)
    return sum == number

innumber = int(input("Enter your number to test: "))
print(is_armstrong_number(innumber))
