import matplotlib.pyplot as plt
import numpy as np

# Generate random data
x = np.random.rand(50)
y = np.random.rand(50)
sizes = np.random.rand(50) * 1000  # Sizes for points

# Create scatter plot
plt.scatter(x, y, s=sizes, alpha=0.5, color='purple')
plt.title("Scatter Plot with Varying Ball Sizes")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)

# Display plot
plt.show()
