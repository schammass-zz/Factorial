number = int(input("Type a positive integer number: "))
if number > 0:
    factorial = 1
    for item in range(1, number + 1):
        factorial = factorial * item
    print(factorial)
