import matplotlib.pyplot as plt

# Create a figure with multiple subplots
fig = plt.figure()

# Add the first subplot (spanning the top row)
ax1 = plt.subplot2grid((2, 3), (0, 0), colspan=3)
ax1.set_title("Top Plot")

# Add the second subplot (bottom left)
ax2 = plt.subplot2grid((2, 3), (1, 0))
ax2.set_title("Bottom Left")

# Add the third subplot (bottom middle)
ax3 = plt.subplot2grid((2, 3), (1, 1))
ax3.set_title("Bottom Middle")

# Add the fourth subplot (bottom right)
ax4 = plt.subplot2grid((2, 3), (1, 2))
ax4.set_title("Bottom Right")

# Adjust layout
plt.tight_layout()

# Show the plots
plt.show()
