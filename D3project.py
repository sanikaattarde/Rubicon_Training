#STUDENT FEEDBACK(string operation (lower,count),file handling (open read write append )and basic conditions)
#1.add feedback 2.view all feedback ,3.veiw particular feedback ,4.analyze(like positive and negative)
#use basic python like functions ,sets,lists,loops etc ..not advanced

# Student Feedback System

file_name = "feedback.txt"

#1. add feedback
def add_feedback():
    name = input("Enter student name: ")
    feedback = input("Enter feedback: ")

    with open(file_name, "a") as f:
        f.write(name + ":" + feedback + "\n")

    print("Feedback added successfully!\n")


# 2. View all feedback
def view_all():
    with open(file_name,"r")as f:
        data=f.readlines()
        if (len(data)==0):
            print("file is empty")
        else:
            for line in data:
                print(line.strip())


# 3. View particular feedback
def view_particular():
    name = input("Enter student name to search: ").lower()

    found = False
    try:
        with open(file_name, "r") as f:
            for line in f:
                parts = line.strip().split(":")
                if parts[0].lower() == name:
                    print("Feedback:", parts[1])
                    found = True
        if not found:
            print("No feedback found!\n")
    except:
        print("File not found!\n")


# 4. Analyze feedback (positive / negative)
def analyze_feedback():
    positive_words = ["good", "excellent", "great", "nice", "happy"]
    negative_words = ["bad", "poor", "worst", "sad", "not"]

    pos_count = 0
    neg_count = 0
    
    try:
        with open(file_name, "r") as f:
            for line in f:
                feedback = line.split(":")[1].lower()

                for word in positive_words:
                    pos_count += feedback.count(word)

                for word in negative_words:
                    neg_count += feedback.count(word)

        print("\nAnalysis:")
        print("Positive words count:", pos_count)
        print("Negative words count:", neg_count)

        if pos_count > neg_count:
            print("Overall Feedback: Positive \n")
        elif neg_count > pos_count:
            print("Overall Feedback: Negative \n")
        else:
            print("Overall Feedback: Neutral \n")


while True:
    print("Student Feedback System")
    print("1. Add Feedback")
    print("2. View All Feedback")
    print("3. View Particular Feedback")
    print("4. Analyze Feedback")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_feedback()
    elif choice == "2":
        view_all()
    elif choice == "3":
        view_particular()
    elif choice == "4":
        analyze_feedback()
    