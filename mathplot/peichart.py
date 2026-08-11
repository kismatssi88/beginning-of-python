import matplotlib.pyplot as plt

product = ['A', 'B', 'C', 'D']
price = [500, 1000, 1500, 200]

plt.title("Price of Products")

plt.pie(
    price,
    labels=product,
    colors=['red', 'blue', 'yellow', 'green'], 
    autopct='%1.1f%%'
)
plt.legend()
plt.show()