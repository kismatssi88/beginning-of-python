import matplotlib.pyplot as plt


plt.scatter([1,2,3,4,5],[40,50,60,70,80],marker='d',color='b', label='section A')
plt.scatter([1,2,3,4,5],[45,55,40,60,45],marker='o',color='g', label='section B')

plt.title('marks according to the hours of study')
plt.xlabel('hours of study')
plt.ylabel('marks scored')

plt.legend()

plt.show()