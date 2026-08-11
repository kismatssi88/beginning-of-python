import matplotlib.pyplot as plt

fig,ax=plt.subplots(1,2,figsize=(10,15))

x=[1,2,3,4,5]
y=[10,15,20,30,25]

ax[0].plot(x,y)
ax[0].set_title('line graph')

ax[1].bar(x,y)
ax[1].set_title('bar graph')

plt.tight_layout()
plt.show()
