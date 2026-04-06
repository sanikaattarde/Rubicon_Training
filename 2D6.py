# def demo(*arg):
#     print(arg[0]+arg[1])
# demo(10,20,30)

# def demo(*arg):
#     c=0
#     for i in arg:
#         c=c+i
#     print(c)
# demo(10,20,15,13)

# def demo(a,*args,**kwargs):
#         print("normal variable:",a)
#         print("Args:",args)
#         print("Kwargs:",kwargs)
# demo(10,20,30,name="sanu",age="21")

"""
import copy
list_data=[11,22,[33,44]]
print(list_data)
shallo_copy=copy.copy(list_data)

#change values from shallo copy 
shallo_copy[2][0]=55
print("original list:",list_data)
print("copied_data:",shallo_copy)

#deep copy
deep_data=[11,22,[33,44]]
deep_copy=copy.deepcopy(deep_data)
deep_copy[2][0]=99
print("original list:",deep_data)
print("deep copy list:",deep_copy)
"""



# def fibo():
#     num=int(input("enter a number:"))
#     f=0
#     h=1
#     print(f)
#     print(h)
#     for i in range(0,num):
#         c=f+h
#         f=h
#         h=c
#         print(c)
# fibo()

import pandas as pd
df=pd.read_csv('infodata.csv')
# print(df.head())

#retrives all the cars built in year 72:
# print(df.loc[df['model_year']==72].head())

#retrive details of all the cars built in japan having 6 cylinders
# print(df.loc[(df["origin"]=="japan")&(df["cylinders"]==6)])


"""fuel efficient
# MPG>29,horsepower<93.5,
# weight<2500"""
# print(df.loc[(df['mpg']>29)&(df['horsepower']<93.5)&(df['weight']<2500)])

""" Muscle cars
displacement>262,horsepower>126,weightin range[2800,3600]"""
# print(df.loc[(df['displacement']>262)&(df['horsepower']>126)&(df['weight']>=2800)&(df['weight']<=3600)])  

"""SUV
horsepower>140,weight>4500"""
# print(df.loc[(df['horsepower']>140)&(df['weight']>4500)])

"""Racecar
weight<2223,acceleration>17"""
# print(df.loc[(df['acceleration']>17)&(df['weight']<2223)])

"""problem statement
xyz custom cars want the data sorted according to the number of cylinders"""
# print(df.sort_values(by='cylinders'))

"""there is a requirement in which the cars that have lowest acceleration must be assumed 
that which cars have higher horsepower despite having lower acceleration """
# print(df.sort_values(['acceleration','horsepower'],ascending =(1,0)))
# print(df.sort_values(['acceleration','horsepower'],decending =(0,1)))

#how many cars belong to each year?
# print(df.groupby(['model_year']).count()[['name']])

"""ps:some senior engineers in XYZ custom cars want to understand about
 the eefect of model year and number of cylinders on horsepower
 
 sol: checking the mean ,min and max horsepower based on number of cylinders and model year.for such requirements ,
 the'agg' function can be combined with the groupby function as shown """

#creating a dataframe grouped on cylinders and model_year and finding mean ,min and max of horsepower.
grouped_multiple=df.groupby(["cylinders","model_year"]).agg({"horsepower":["mean","min","max"]})

# naming col in grouped dataframe
grouped_multiple.columns=["hp_mean","hp_min","hp_max"]

# reseting index
grouped_multiple=grouped_multiple.reset_index()

# viewing head of resulting dataframe
print(grouped_multiple.head())