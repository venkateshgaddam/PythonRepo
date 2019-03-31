class Test():
    def __init__(self):
        self.pub=("I am public ")
        self._pro=("I am Protected ")
        self.__pri=("I am the Private Variable")
    def pubfunction(self):
        print ("I am the public Method")
    def __priFunction(self):
        print("Private Function")

ob=Test()
print(ob.pub)
print(ob._pro)
print(ob._Test__pri)

ob._Test__priFunction()

import pandas

listx=[{'a':1,'b':2},{'a':5,'b':223},{'a':7,'c':2},{'a':10,'b':22}]

series1=pandas.Series([40,50,60],index=['maths','chemistry','physics'])

series2=pandas.Series([70,80,60],index=['maths','chemistry','physics'])

table=pandas.DataFrame(dict(jim=series1, jam=series2)
                       )

print(table)

table.to_csv('Test.csv')

