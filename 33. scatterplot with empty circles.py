import matplotlib.pyplot as plt
import numpy as np

# Generate random data
x = np.random.rand(50)
y = np.random.rand(50)

# Create scatter plot with empty circles
plt.scatter(x, y, edgecolors='blue', facecolors='none', alpha=0.7)
plt.title("Scatter Plot with Empty Circles")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)

# Display plot
plt.show()
