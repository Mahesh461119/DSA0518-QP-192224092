import matplotlib.pyplot as plt

# Define data for two lines
x = [10, 15, 20, 25, 30]
y1 = [10, 20, 30, 20, 10]
y2 = [40, 30, 20, 30, 40]

# Plot the lines with different styles
plt.plot(x, y1, color='red', linewidth=3, label='line1-width-3')
plt.plot(x, y2, color='blue', linewidth=5, label='line2-width-5')

# Add labels and title
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Two or more lines with different widths and colors with suitable legends')

# Add legend
plt.legend()

# Show the plot
plt.show()
