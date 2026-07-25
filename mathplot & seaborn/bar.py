import matplotlib.pyplot as plt

x = ['A', 'B', 'C', 'D']
y = [500, 1000, 1500, 200]

plt.title("Price of Products")
plt.xlabel("Product")
plt.ylabel("Price")

plt.bar(x, y, color='red')

plt.show()