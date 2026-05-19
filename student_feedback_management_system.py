# Student feedback management system
# (use string operations,lower count,file handling(open,read,write,append),functions,lists)(do not use classes,error handling,modules,packages,decorators,lambda functions,comprehensions,iterators,generators,context managers,regular expressions,JSON,CSV)

def add():
    print("This function will add feedback.")
    name = input("Enter your name: ")
    feedback = input("Enter your feedback: ")
    
    with open("feedback.txt", "a") as file:
        file.write(name + ": " + feedback)
    print("Feedback added successfully!")

def view():
    print("This function will view the feedbacks.")
    with open("feedback.txt", "r") as file:
        feedbacks = file.readlines()
    
    print("Feedbacks:")
    for feedback in feedbacks:
        print(feedback.strip())

# search_feedback function (search users name and display the feedback)
def search():
    print("This function will search the feedbacks.")
    search_name = input("Enter the name to search for feedback: ").lower()
    
    with open("feedback.txt", "r") as file:
        feedbacks = file.readlines()
    
    found = False
    for feedback in feedbacks:
        if search_name in feedback.lower():
            print("Feedback found: " + feedback.strip())
            found = True
    
    if not found:
        print("No feedback found for the name: " + search_name)
    

def count():
    print("This function will count the feedbacks.")
    with open("feedback.txt", "r") as file:
        content = file.read()
    
    feedback_count = content.count("\n") + 1
    print("Total feedback count: " + str(feedback_count)) 
    
def main():
    while True:
        print("\nStudent Feedback Management System")
        print("1. Add Feedback")
        print("2. View Feedback")
        print("3. Search Feedback")
        print("4. Count Feedback")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add()
        elif choice == '2':
            view()
        elif choice == '3':
            search()
        elif choice == '4':
            count()
        elif choice == '5':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
    
if __name__ == "__main__":
    main()
    
    
    


