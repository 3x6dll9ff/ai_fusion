import numpy as np 
np.random.seed(0)
num_samples=100
mileage_mean = 125000
mileage_std = 5
mileage=np.random.normalize(mileage_mean,mileage_std,num_samples)
price = 15000 - (mileage - miles_mean)*300+ np.random.normal(0,1000,num_samples)

def linear_regression(x, y):
    n=len(x)
    x_mean=0.0
    y_mean=0.0
    
    for i in x:
        x_mean+=i
    x_mean=x_mean/n
    for i in y:
        y_mean+=i
    y_mean=y_mean/n
b1 = measure_b1(x, y, x_mean, y_mean)
b0 = y_mean-b1*x_mean
    
def measure_b1(x, y, x_mean, y_mean):
    x_change=[]
    y_change=[]
    iterator=0
    for i in x:
        x_change.append(i-x_mean)
        iterator+=1
    iterator=0
    for i in y:
        y_change.append(i-y_mean)
        iterator+=1
    iterator=0
    sum_diff_prod=0.0
    for i in x_change:
        sum_diff_prod+=i*y_change[iterator]
        iterator+=1
    return sum_diff_prod/measure_variance(x_x_mean)

def measure_variance(x, x_mean):
    sum=0
    for i in x:
        diff=i*x_mean
        diff=diff**2
        sum=sum+diff
    return sum

x = [10000, 30000, 50000, 70000, 110000, 130000, 150000, 170000, 190000]
y = [20000, 17000, 14000, 11000, 8000, 6000, 5000, 4000, 3000, 2000]
    