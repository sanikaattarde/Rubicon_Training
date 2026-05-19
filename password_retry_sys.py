# Password retry system (Password = PYTHON123)

password = "PYTHON123"
attempts = 3    
while attempts > 0:
    user_input = input("Enter the password: ")
    if user_input == password:
        print("Access granted.")
        break
    else:
        attempts -= 1
        print("Incorrect password. Attempts left:", attempts)
else:
    print("Access denied.")

