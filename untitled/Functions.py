def add(a,b):
    sum=a+b
    return (sum)

num1=1#input("Enter first number")
num2=1#input("Enter second number")
n1=int(num1)
n2=int(num2)
ans=add(n1,n2)
print("The Result is ",ans)



'''
Below code is an example of Lambda Functions in Python
'''
items=[1,45,5,4]
squared=list(map(lambda x: x ** 2, items))
print(squared)

number_list=range(-10,10)
lessthan=list(filter(lambda x:x>=0,number_list))
print(lessthan)


#reduce KeyWord
from functools import reduce
product=reduce((lambda x,y:x*y),[1,2,3,4])
print(product)



#Passing Variable Parameters
def print_users(user,*users):
    print("First Argument in: ",user)

    for user in users:
        print('variable argument :',user)

print_users('testuser1','testuser2','testuser3')