# 1.numpy library
# import numpy as np
# a=np.array([1,2,3])
# b=np.array([1,2,3])
# print(a+b)

#2D array
# a=np.array([[1,3,4],[2,5,3],[4,7,2]])
# print(a)
# print(a.shape)

# a=np.array([[1,3,4],[2,5,3],[4,7,2]])
# row_sum=a.sum(axis=1)
# col_sum=a.sum(axis=0)
# print("\n 3D array")
# print("row wise:\n",row_sum)
# print("col wise:\n",col_sum)
 

# 2. pandas library
# import pandas as pd
# a=pd.Series([10,30,40],index=["a","b","c"])
# print(a)

# data={"NAME":["sanika","akanksha"],
#       "MARKS":[30,50]}
# df=pd.DataFrame(data)
# print(df)



# data={"SUB":["CC","DSBDA","WT","AI"],
#        "MARKS":[30,50,40,35]}
# df=pd.DataFrame(data)
# print("max marks:",df["MARKS"].max())
# print("min marks:",df["MARKS"].min())
# print("average marks:",df["MARKS"].mean())

# data={"NAME":["sanika","akanksha","seerat"],
#        "MARKS":[30,50,25]}
# df=pd.DataFrame(data)
# df.to_csv("xyz.csv",index=False)----used to erite in csv file
# df2=pd.read_csv("xyz.csv")----------used to read in csv file
# print(df2)

# import matplotlib.pyplot as plt
# x=[3,4,2,5]
# y=[10,20,30,40]
# plt.plot(x,y)
# plt.title("line graph")
# plt.xlabel("x.AXIS")
# plt.ylabel("y.AXIS")
# plt.show()

# x=["XS","SE","BH"]
# y=[20,30,52]
# plt.bar(x,y)
# plt.title("Bar raph")
# plt.xlabel("products")
# plt.ylabel("sales")
# plt.show()

# x=["XS","SE","BH"]
# y1=[20,30,52]
# y2=[50,25,65]

# plt.plot(x,y1,marker='o')
# plt.plot(x,y2,marker='o')
# plt.title("line graph")
# plt.xlabel("x.AXIS")
# plt.legend([y1,y2])
# plt.ylabel("y.AXIS")
# plt.grid()
# plt.show()