import statistics

data = [10,20,30,40,50,60]

Mean= statistics.mean(data)
print("data is",data)
print("mean of the above data",Mean)
Sum = statistics._sum(data)

print("Summation of dataset is :",Sum)

Median = statistics.median(data)

print("Median od the dataset is :",Median)


#Variance 

data = [ 20,40,50,60]
Mode = statistics.mode(data)
print("mode of te data is:",Mode)

#Variance 


data = [1,2,3,5,6,7,8]
Variance = statistics.variance(data)
print("variance of te data is:",Variance)

#Measures how spread out  data is
# Low variance->consistent data
# high vaariance->unstable/risky data 
#Standard deviation

data = [50,100,150,200,250,300]

SD = statistics.stdev(data)
print("Standard deviation of te above data is:",SD)

#Square root of variance is SD
#How much te data values are spread out from the mean 
# Large SD -> values are far from the mean 
# samll SD -> vaues are close to the mean 


data = [10,20,30,40,50]
range_value = max(data) -min(data)

print(range_value)






 




