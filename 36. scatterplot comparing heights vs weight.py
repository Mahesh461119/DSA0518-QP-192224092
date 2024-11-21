import matplotlib.pyplot as plt

# Sample data
group1 = {'height': [150, 160, 165], 'weight': [50, 55, 60]}
group2 = {'height': [170, 175, 180], 'weight': [70, 75, 80]}
group3 = {'height': [190, 195, 200], 'weight': [90, 95, 100]}

# Plot scatter for each group
plt.scatter(group1['height'], group1['weight'], color='blue', label='Group 1')
plt.scatter(group2['height'], group2['weight'], color='green', label='Group 2')
plt.scatter(group3['height'], group3['weight'], color='red', label='Group 3')

plt.title("Height vs Weight Comparison")
plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")
plt.legend()
plt.grid(True)

# Display plot
plt.show()
