import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[10,15,20,30,25]

plt.subplot(1,2,1)
plt.plot(x,y)
plt.title('LIne graph')


plt.subplot(1,2,2)
plt.bar(x,y)
plt.title('Bar graph')

plt.tight_layout()
plt.show()