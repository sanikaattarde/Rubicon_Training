#student course managment sysytem
#student name, course details,unique skills,student info
#student add,student display, skill add and display

student=[]

while True:
    print("1.Add Student")
    print("2.Display Students")
    print("3.Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name=input("Enter name:")
        course=input("Enter course:")
        skills=input("Enter skills:")
        info=input("Enter info:")

        stud= { "name":name,"course":course,"skills":skills,"info":info}
        student.append(stud)
        print("Student added successfully!")

    elif choice=='2':
        if len(stud)==0:
            print("No students found!")
        else:
            print("Student List")
            for s in student:
                print("Name:",s["name"])
                print("Course:",s["course"])
                print("Skills:",s["skills"])
                print("Info:",s["info"])

    elif choice == '3':
        print("Exit.")
        


