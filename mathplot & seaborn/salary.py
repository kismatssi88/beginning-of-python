import matplotlib.pyplot as plt
x=[1,1.5,2,2.5,3,4]
y=[10000,20000,30000,200025,2250,50025]
plt.plot(x,y,color='red',linestyle='--',linewidth='2',marker='o') 
plt.legend(loc='upper left',fontsize=12)
plt.grid(color='grey',linestyle=':',linewidth=1)
plt.xlim(1,5)

plt.show()
