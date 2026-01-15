import matplotlib.pyplot as plt
import numpy as np

y1 =["java","python","C++","ruby","javascript","scala"]

y2 = [8,14,18,33,38,40]

y3 =[5,10,12,14,25,30]

x =np.arange(len(y1))
width =0.35

plt.bar(x - width/2,y2,width=width,label='Users',color='cyan',alpha=0.7,edgecolor='black')

plt.bar(x + width/2,y3,width=width,label='New Uers',color='magenta',alpha=0.7,edgecolor='black')


plt.xticks(x,y1)
plt.title("Bar Chart")
plt.xlabel("Programming Languages")
plt.ylabel("Number of Users")

plt.show()