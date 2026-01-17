
"""Correlation:
measures the strength and direction of relationship between two variables
- correlation does not mean causation
-Ice cream sales imcreases
-Crime increases
-Ice cream does not cause crime
Example:
- study hours <-> marks
- teperature <-> ice-cream sales
-Special cases:
1: +1 Perfect positive relation
2: 0 no relation
3: -1 perfect negative relation"""



import numpy as np

x =[1,2,3,4,5]
y =[2,4,6,8,10]

corr = np.corrcoef(x,y)
print(corr)

"""perfect positive correlation mean temperature increases
ice cream sales also increases iwth the same amount 
"""
#Negative correlation

"""When one variable increases,te other decreases

they move in oposite direction

Ex:
1:Speed increases -> time to finish decreases
2:price increases -> Demand decreases
3:Temperature increases -> jacket usage decreases
4:study hours increases -> free time decreases"""



x = [1,2,3,4]
y = [8,6,4,2]

corr = np.corrcoef(x,y)

print(corr)



