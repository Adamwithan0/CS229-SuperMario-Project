import pandas as pd
import matplotlib.pyplot as plt

MONITOR='logs/PPO/PPO3.monitor.csv'

# Read the monitor.csv file into a pandas DataFrame
df = pd.read_csv(MONITOR)


print(df.keys())

# Convert the relevant columns to the appropriate data types
df['r'] = df['r'].astype(float)
df['l'] = df['l'].astype(int)
df['t'] = pd.to_datetime(df['t'], unit='s')

# Plot the graph using matplotlib
plt.plot(df['t'], df['r'])
plt.xlabel('Time')
plt.ylabel('Reward')
plt.title('Reward over Time')
plt.show()
