import numpy as np
# your file pATH
# r is for row string 
file_path=(r"C:\Users\AKANKSHA\OneDrive\Desktop\HTML TUT\training\winequality-red.csv")
print(file_path)
# get form

# -------------------using genfromtxt---------------------
# changed the file datatype
data_str=np.genfromtxt(file_path , delimiter=";" , skip_header=1 , dtype="str")
print("data with change dtype : ",data_str)

# ----way 10----
# now we have to copy the data from file_data into another file with changing dtype
np.savetext(r"E:\python projects 2024")