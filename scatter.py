import matplotlib.pyplot as plt


x = [1,2,3,4,5,6]
y = [10,15,20,25,30,35]
c = [5,10,15,20,25,30]
colores = ['red','blue','green','yellow','pink','black']
sizes = [50,100,200,300,400,500]

plt.scatter(x,c,color=colores,marker='+',s=100,alpha=0.7)

plt.scatter(x,y,color='orange',marker='*',s=sizes,alpha=0.5)

plt.title("Scatter plot")
plt.xlabel("X-axies")
plt.ylabel("Y-axies")

plt.show()

y1 =["java","python","C++","ruby","javascript"]

y2 = [8,14,18,33,38]


plt.bar(y1,y2,c='cyan',width=0.5,alpha=0.7,edgecolor='black')

plt.title("Bar Chart")
plt.xlabel("Programming Languages")
plt.ylabel("Number of Users")

plt.show()