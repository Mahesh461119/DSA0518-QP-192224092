import matplotlib.pyplot as plt
import numpy as np

# Sample data
means_men = [22, 30, 35, 35, 26]
means_women = [25, 32, 30, 35, 29]
std_men = [4, 3, 4, 1, 5]
std_women = [3, 5, 2, 3, 3]

# X positions for bars
x_pos = np.arange(len(means_men))

# Create the bar plots
plt.bar(x_pos, means_men, yerr=std_men, label='Men', color='blue', alpha=0.7)
plt.bar(x_pos, means_women, yerr=std_women, label='Women', color='orange', alpha=0.7, bottom=means_men)

# Add labels and title
plt.xlabel('Categories')
plt.ylabel('Scores')
plt.title('Stacked Bar Plot with Error Bars')
plt.xticks(x_pos, ['A', 'B', 'C', 'D', 'E'])  # Custom x-axis labels
plt.legend()

# Show the plot
plt.tight_layout()
plt.show()
