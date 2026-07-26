import matplotlib.pyplot as plt

marks = [45, 50, 55, 60, 65, 70, 72, 75, 80, 82, 85, 90, 92, 95, 98]

plt.hist(marks, bins=5,color='m')

plt.title("Histogram")
plt.xlabel("Marks")
plt.ylabel("Frequency")

plt.show()