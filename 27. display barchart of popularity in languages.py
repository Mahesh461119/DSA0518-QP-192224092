import matplotlib.pyplot as plt

# Sample data
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8.0, 7.7, 6.7]

# Create a bar chart
plt.bar(languages, popularity, color='blue')

# Add titles and labels
plt.title('Popularity of Programming Language\nWorldwide, Oct 2017 compared to a year ago')
plt.xlabel('Languages')
plt.ylabel('Popularity (%)')

# Add gridlines
plt.grid(axis='y', linestyle='--', linewidth=0.5, color='red')

# Show the plot
plt.show()
