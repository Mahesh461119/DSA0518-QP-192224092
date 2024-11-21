import matplotlib.pyplot as plt

# File path
file_path = r"C:\Users\malat\Downloads\test.txt.txt"

# Read data from the file
x = []
y = []

with open(file_path, 'r') as file:
    for line in file:
        values = line.split()
        x.append(float(values[0]))
        y.append(float(values[1]))

# Plot the data
plt.plot(x, y, color='blue')

# Add labels and title
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Sample graph!')

# Display the plot
plt.show()
