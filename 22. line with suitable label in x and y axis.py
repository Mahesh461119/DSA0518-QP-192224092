import matplotlib.pyplot as plt

# Define data points
x = [0, 10, 20, 30, 40, 50]
y = [0, 20, 40, 60, 80, 100]

# Create the plot
plt.plot(x, y, color='blue')

# Add labels and title
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Draw a line.')

# Display the plot
plt.show()
