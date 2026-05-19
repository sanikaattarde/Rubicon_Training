# This code demonstrates basic file operations in Python.

#writeing to a file
f = open("demo.txt", "w")
f.write("This is a new line added to the file.\n")
f.close()

#reading from a file
f = open("demo.txt", "r")
content = f.read()
print(content)
f.close()

#appending to a file
f = open("demo.txt", "a")
f.write("This line is appended to the file.\n") 
f.close()

#reading the updated file
f = open("demo.txt", "r")
content = f.read()
print(content)
f.close()


#spliting the content into lines (use append)
f = open("demo.txt", "r")
lines = f.readlines()
f.close()


# Read lines from the file and print them
for line in lines:
    print(line.strip()) 
    
# copy the file content to a new file
with open("demo.txt", "r") as source_file:
    content = source_file.read()    
    
with open("copy_demo.txt", "w") as dest_file:
    dest_file.write(content)

# Search a word in the file (do not use f-strings)
search_word = input("Enter a word to search in the file: ")
with open("demo.txt", "r") as file:
    content = file.read()
    if search_word in content:
        print("The word '" + search_word + "' is found in the file.")
    else:
        print("The word '" + search_word + "' is not found in the file.")  

# count its occurrences
occurrences = content.count(search_word)
print("The word '" + search_word + "' occurs " + str(occurrences) + " times in the file.")

# Find what is JSON file


# Open a .csv file and read its content
import csv
with open("data.csv", "w", newline='') as csvfile:
    csvv = csv.writer(csvfile)
    csvv.writerows([["Name", "Age"], ["Yuvraj", 20], ["sachin", 50], ["virat", 35]])
    csvv.writerows([["hobbies", "sports"], ["cricket", "football"], ["music", "tennis"], ["reading", "swimming"]])
with open("data.csv", "r") as csvfile:
    csvv = csv.reader(csvfile)
    for row in csvv:
        print(row)


# Print hello four times in csv file
with open("hello.csv", "w", newline='') as csvfile:
    csvv = csv.writer(csvfile)
    csvv.writerow(["Hello"] * 4)
    
# Find length of the csv file
with open("data.csv", "r") as csvfile:
    csvv = csv.reader(csvfile)
    rows = list(csvv)
    print("Number of rows in the CSV file: " + str(len(rows)))
    
#count occurances of a word in csv file
search_word = input("Enter a word to search in the CSV file: ")
with open("data.csv", "r") as csvfile:
    csvv = csv.reader(csvfile)
    content = ""
    for row in csvv:
        content += " ".join(row) + " "
    occurrences = content.count(search_word)
    print("The word '" + search_word + "' occurs " + str(occurrences) + " times in the CSV file.")


    






    
    
    






    

    







