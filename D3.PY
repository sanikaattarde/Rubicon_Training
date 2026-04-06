#file handling
# f=open("file.text","w")
# f.write("Introduction \n name: Sanika Attarde")
# print(f)
# f.close()

# file append
# with open("file.text","a")as file:
#     file.write("\n Age:21")
#     print(file)

#file read
# with open("file.text","r")as f:
#   d=f.read()
#   d.split()
#   print(d.split)
#   print(d.count()) needs argument
#   print(d)

#line count
#dont know??............

#copy file
# with open("file.text","r")as f:
#      data=f.read()
# with open("data.text","w")as f1:
#      f1.write(data)


# find a word 
# with open("file.text","r")as f:
#     data=f.read()
#     w=input("word to find:")
#     print(data.find())


#HOMEWORK WHAT IS JSON FILE ? , WHAT IS CSV FILE?

#CSV FILE
# import csv
# with open("file.csv","w",newline="")as f:
#     f.write("Name,Age,City\n")
#     f.write("sanika,21,chh.sambhajinagar\n")
#     f.write("akanksha,20,pune\n")
#     f.write("seerat,22,nashik")
#     print(f)

# import csv
# data = [
#     ["Name", "Age", "Course"],
#     ["Akku", 20, "Python"],
#     ["Riya", 21, "Java"]
# ]

# with open("data.csv", "w", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerows(data)



# string1="i am sanika attarde\n"
# string2="age:21"
# # print("letter at index is:",string1[7:14])
# # print("letter at index is:",string1[4:])
# # print("letter at index is:",string1[:5])
# # print("letter at index is:",string1[-3:])
# # print(string1+string2)

# print(4*string2)     #printing string for 4 times

# str="myself sanika"
# print("length:",len(str))
# print(str.upper())
# print(str.lower())
# print(str.capitalize())


# string1="i am sanika attarde\n"
# string2="age:21"
# string2.replace(string1,string2)
