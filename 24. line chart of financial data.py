import pandas as pd
import matplotlib.pyplot as plt

# Sample financial data
data = {
    "Date": ["10-03-16", "10-04-16", "10-05-16", "10-06-16", "10-07-16"],
    "Open": [774.25, 776.03, 779.31, 779.79, 779.66],
    "High": [776.065002, 778.710022, 782.070007, 780.47998, 779.659973],
    "Low": [769.5, 772.890015, 775.650024, 775.539978, 770.75],
    "Close": [772.559998, 776.429993, 776.469971, 776.859985, 775.080017],
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Plot the financial data
plt.plot(df['Date'], df['Open'], label='Open', color='blue')
plt.plot(df['Date'], df['High'], label='High', color='orange')
plt.plot(df['Date'], df['Low'], label='Low', color='green')
plt.plot(df['Date'], df['Close'], label='Close', color='red')

# Add labels, title, and legend
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.title('Alphabet Inc. Financial Data (Oct 3 - Oct 7, 2016)')
plt.legend()

# Display the plot
plt.show()
