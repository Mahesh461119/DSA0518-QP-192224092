import matplotlib.pyplot as plt

# Data
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

# Create horizontal bar chart
plt.barh(languages, popularity, color='green', edgecolor='black')

# Add chart title and labels
plt.title('Popularity of Programming Languages\nWorldwide, Oct 2017 compared to a year ago', fontsize=12)
plt.xlabel('Popularity', fontsize=10)
plt.ylabel('Languages', fontsize=10)

# Add gridlines
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Show the chart
plt.tight_layout()
plt.show()
