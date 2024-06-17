import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the data from the CSV file
df = pd.read_csv('inputdata.csv', delim_whitespace=True, header=None, names=['x', 'N'])

# Calculate the PDF P(x) from N(x)
total_count = df['N'].sum()
df['P'] = df['N'] / total_count

# Calculate the mean value (μ) and standard deviation (σ)
mean_value = (df['x'] * df['P']).sum()
std_dev = np.sqrt(((df['x'] - mean_value)**2 * df['P']).sum())

# Calculate the 25th percentile (P value)
cdf = df['P'].cumsum()
P_25 = df.loc[cdf >= 0.25, 'x'].iloc[0]


R = P_25

# Plotting the PDF
plt.figure(figsize=(10, 6))
plt.plot(df['x'], df['P'], marker='o', linestyle='-', color='b', label='P(x)')
plt.title(f'Data Sequence Plot \nμ = {mean_value:.2f}, σ = {std_dev:.2f}, R = {R:.2f}')
plt.xlabel('x')
plt.ylabel('P(x)')
plt.grid(True)
plt.legend()
plt.savefig(f'{22103577}.png')
plt.show()

# Print the values of μ, σ, and R
print(f"Mean value (μ): {mean_value}")
print(f"Standard Deviation (σ): {std_dev}")
print(f"R value: {R}")
print(f"Student ID: 22103577")
