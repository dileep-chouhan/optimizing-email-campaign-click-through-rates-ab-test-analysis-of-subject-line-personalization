import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
# --- 1. Synthetic Data Generation ---
np.random.seed(42) # for reproducibility
# Number of emails sent in each group
n_emails = 1000
# Create data for A/B test
data = {
    'Group': ['Personalized'] * n_emails + ['Generic'] * n_emails,
    'Clicks': np.concatenate([np.random.binomial(1, 0.12, n_emails), 
                              np.random.binomial(1, 0.08, n_emails)])
}
df = pd.DataFrame(data)
# --- 2. Data Cleaning and Preparation ---
# No cleaning needed for this synthetic data
# --- 3. Analysis ---
# Calculate click-through rates (CTR)
personalized_ctr = df[df['Group'] == 'Personalized']['Clicks'].mean()
generic_ctr = df[df['Group'] == 'Generic']['Clicks'].mean()
# Perform a two-proportion z-test
z_stat, p_value = stats.proportions_ztest(
    [df[df['Group'] == 'Personalized']['Clicks'].sum(), 
     df[df['Group'] == 'Generic']['Clicks'].sum()],
    [n_emails, n_emails]
)
print("Click-Through Rates:")
print(f"Personalized: {personalized_ctr:.4f}")
print(f"Generic: {generic_ctr:.4f}")
print(f"\nTwo-proportion z-test:")
print(f"Z-statistic: {z_stat:.2f}")
print(f"P-value: {p_value:.3f}")
#Interpret Results
alpha = 0.05
if p_value < alpha:
    print("\nThe difference in CTRs is statistically significant.")
else:
    print("\nThe difference in CTRs is not statistically significant.")
# --- 4. Visualization ---
plt.figure(figsize=(8, 6))
sns.countplot(x='Group', hue='Clicks', data=df)
plt.title('Clicks by Email Group')
plt.xlabel('Email Group')
plt.ylabel('Count')
plt.xticks([0,1], ['Personalized', 'Generic'])
plt.legend(title='Click', labels=['No Click', 'Click'])
# Save the plot to a file
output_filename = 'ab_test_results.png'
plt.savefig(output_filename)
print(f"\nPlot saved to {output_filename}")