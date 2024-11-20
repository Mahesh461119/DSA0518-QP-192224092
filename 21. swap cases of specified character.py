import pandas as pd

# Sample DataFrame
data = {'Name': ['Alice', 'BOB', 'ChArLiE', 'daVid'], 'Age': [25, 30, 22, 35]}
df = pd.DataFrame(data)

# Swapping the cases in the 'Name' column
df['Name'] = df['Name'].str.swapcase()

print(df)
