import pandas as pd

# Creating a sample dataset (Simulating an export from Google Ads/Facebook)
data = {
    'Campaign': ['Metaverse_Alpha', 'Metaverse_Beta', 'General_Search'],
    'Ad_Spend': [5000, 3000, 1500],
    'Revenue': [12000, 4000, 6000],
    'COGS': [2000, 1000, 800]  # Cost of Goods Sold (Accounting Logic)
}

df = pd.DataFrame(data)

# 1. Calculate Net Profit (Revenue - Spend - COGS)
df['Net_Profit'] = df['Revenue'] - df['Ad_Spend'] - df['COGS']

# 2. Calculate ROI %
df['ROI_Percentage'] = (df['Net_Profit'] / (df['Ad_Spend'] + df['COGS'])) * 100

print("--- Marketing Performance Report ---")
print(df[['Campaign', 'Net_Profit', 'ROI_Percentage']])
