import matplotlib.pyplot as plt
hours_0f_study=[1,2,3,4,5,6]
marks=[40,50,55,45,35,60]

plt.scatter(hours_0f_study,marks,marker='^',color='b',label='marks of students')

plt.title('marks according to the hours of study')
plt.xlabel('hours of study')
plt.ylabel('marks scored')



plt.show()