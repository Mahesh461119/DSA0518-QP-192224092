import matplotlib.pyplot as plt
import numpy as np

# Generate random data
x = np.random.rand(50)
y = np.random.rand(50)

# Create scatter plot
plt.scatter(x, y, color='green', alpha=0.5)
plt.title("Scatter Graph with Random Distribution")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)

# Display plot
plt.show()
