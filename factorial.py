# Find factorial of a num

num = int(input("Enter a number: "))
factorial = 1
if num < 0:
    print("Factorial is not defined for -ve numbers.")
elif num == 0 or num == 1:
    print("The factorial of", num, "is 1.")
else:
    for i in range(2, num + 1):
        factorial *= i
    print("The factorial of", num, "is", factorial)
    