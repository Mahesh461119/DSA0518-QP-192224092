import matplotlib.pyplot as plt

# Data
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
colors = ['red', 'black', 'green', 'blue', 'yellow', 'cyan']  # Colors for each bar

# Create bar chart
plt.bar(languages, popularity, color=colors, edgecolor='black')

# Add chart title and labels
plt.title('Popularity of Programming Languages\nWorldwide, Oct 2017 compared to a year ago', fontsize=12)
plt.xlabel('Languages', fontsize=10)
plt.ylabel('Popularity', fontsize=10)

# Add gridlines
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the chart
plt.tight_layout()
plt.show()
