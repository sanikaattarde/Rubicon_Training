# Find even num between 1 to 20
for num in range(1, 21):
    if num % 2 == 0:
        print(num, "is an even number.")
        
# Find even num (user input)
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num, "is an even number.")
else:
    print(num, "is not an even number.")    