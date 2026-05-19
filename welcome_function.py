# Create a Greeting Function and print it 4 times
def welcome_message():
    print("Welcome to the program!")

for i in range(4):
    welcome_message()

# Create a function to greet user by name(use f-strings)
def greet_user(name):
    print(f"Hello, {name}! Welcome to the program.")
user_name = input("What is your name? ")
greet_user(user_name)

# Create a function to greet user by name(use concatenation)
def greet(name):
    print("Hello, " + name)
name = input("What is your name? ")
greet(name)