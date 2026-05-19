# Introduction to NumPy library
# NumPy is a powerful library in Python used for numerical computing. It provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays efficiently.

import numpy as np  

# Create two NumPy arrays
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array(['a', 'b', 'c', 'd', 'e'])
print(array1)
print(array2)

# Multiply the array1 by 4
result = array1 * 4
print(result)

# Perform sum and mean of the array1
sum_array1 = np.sum(array1)
mean_array1 = np.mean(array1)
print("Sum of array1:", sum_array1)
print("Mean of array1:", mean_array1)

# Calculate monthly expense using array
expenses = np.array([1000, 1500, 1200, 1300, 1100])
total_expense = np.sum(expenses)
average_expense = np.mean(expenses)
print("Total monthly expense:", total_expense)
print("Average monthly expense:", average_expense)

# Analyze sales data using array (3 days random data) print day wise sum and column sum (use axis)
sales_data = np.array([[200, 300, 400],
                        [150, 250, 350],
                        [100, 200, 300]])

day_wise_sum = np.sum(sales_data, axis=1)
column_sum = np.sum(sales_data, axis=0)

print("Day-wise sum:", day_wise_sum)
print("Column sum:", column_sum)


# Indtroduction to Pandas library
# Pandas is a powerful library in Python used for data manipulation and analysis. It provides data structures like Series and DataFrame, which allow for efficient handling of structured data. Pandas offers a
# wide range of functions for data cleaning, transformation, and analysis, making it a popular choice for data scientists and analysts.

import pandas as pd

# Use Series and create a column and row (declare a variable and assign a list of 5 values to it) and print the series

data = [10, 20, 30, 40, 50]
data2 = ["a","b","c","d","e"]
series = pd.Series(data)
print(series)

# Create 2D series using pd (Name, Marks)
data = {'Name': ['Yuvraj', 'Sahil', 'Pranav', 'Pratik', 'Aditya'],
        'Marks': [99, 90, 10, 92, 88]}
df = pd.DataFrame(data)
print(df)

# Calculate the average marks of the students
average_marks = df['Marks'].mean()
print("Average Marks:", average_marks)


# use series on main data structures 
# use series when you deal with a single column
# use dataframe when you deal with multiple columns










