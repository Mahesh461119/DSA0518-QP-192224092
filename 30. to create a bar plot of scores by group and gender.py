import numpy as np
import matplotlib.pyplot as plt

# Data
groups = ['Group 1', 'Group 2', 'Group 3', 'Group 4', 'Group 5']
means_men = [22, 30, 35, 35, 26]
means_women = [25, 32, 30, 35, 29]

# X positions for bars
x = np.arange(len(groups))  # the label locations
width = 0.35  # the width of the bars

# Create the bar plot
fig, ax = plt.subplots(figsize=(8, 6))
bars1 = ax.bar(x - width/2, means_men, width, label='Men', color='blue', edgecolor='black')
bars2 = ax.bar(x + width/2, means_women, width, label='Women', color='pink', edgecolor='black')

# Add labels, title, and legend
ax.set_xlabel('Groups', fontsize=12)
ax.set_ylabel('Scores', fontsize=12)
ax.set_title('Scores by Group and Gender', fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(groups)
ax.legend()

# Add gridlines
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Show the chart
plt.tight_layout()
plt.show()
