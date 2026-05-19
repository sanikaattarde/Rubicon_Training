# Student Course Management System (name[List], course[Tuple], skills[set], info[Dictionary])(User should able to insert data) 

# List
student_name = input("Enter student name: ")
my_list = [student_name]
print("List:", my_list)

# Remove duplicates from the list
my_list = list(set(my_list))
print("List after removing duplicates:", my_list)       


# Tuple
course_name = input("Enter course name: ")
my_tuple = (course_name)
print("Tuple:", my_tuple)

# Set
skill_name = input("Enter skill name: ")
my_set = {skill_name}
print("Set:", my_set)

# Dictionary
student_info = {}
student_info['name'] = student_name
student_info['course'] = course_name
student_info['skills'] = skill_name
print("Student Information Dictionary:", student_info)







