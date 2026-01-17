import matplotlib.pyplot as plt 
data1= [5,10,15,20,25,30,35,40]
data2 =[7,12,18,22,27,32,38,42]
plt.hist(data1,bins = 3,alpha=0.6,label="Dataset1")
plt.hist(data2,bins=3,alpha=0.6,label="Dataset2")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Histogram Example")
plt.legend()
plt.show()
 