# sum_calculator
def calculate_sum(a, b):
    return a + b

#Substraction function
def Substraction(a, b):
    return a - b

#Division function
def Division(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero is not allowed."
    
#Multiplication function
def Multiplication(a, b):
    return a * b

# Main program
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
while True:
    operation = input("Choose an operation (sum, substraction, division, multiplication): ")
    if operation == "sum":
        result = calculate_sum(num1, num2)
        break
    elif operation == "substraction":
        result = Substraction(num1, num2)
        break
    elif operation == "division":
        result = Division(num1, num2)
        break
    elif operation == "multiplication":
        result = Multiplication(num1, num2)
        break
    else:
        print("Invalid operation. Please choose again.")
print("The result is:", result)



    
    