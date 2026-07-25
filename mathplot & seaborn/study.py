import matplotlib.pyplot as plt

x = ['kismat', 'bikki', 'siddu', 'yuth', 'prabin', 'sanjok']
y = [1, 5, 10, 33, 2, 5]

plt.plot(x, y, color='red', linestyle='-', marker='o', linewidth=2)

plt.title("Study Hours Per Day")
plt.xlabel("Study By:")
plt.ylabel("No. of Hours Per Day")

plt.grid(color='gray', linestyle='--', linewidth=1)

plt.show()