import matplotlib.pyplot as plt

x=range(10)

plt.plot(x,[i*i for i in x],label='linear')
plt.plot(x,[i*i*i for i in x],label='square')
plt.plot(x,[i*4 for i in x],label='raised to the power 4')
plt.title('This is the Plot in python')
plt.legend()
plt.grid(True)
plt.show()