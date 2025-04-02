import numpy as np
import pandas as pd


sales_data_df = pd.read_csv("data/AusApparalSales4thQrt2020.csv", parse_dates=['Date'])


# Total Sales Revenue
total_revenue = sales_data_df['Sales'].sum()
print(f"Total Revenue: {total_revenue:,.2f}")
print("\n============================\n")
#top selling groups
top_cat = sales_data_df.groupby('Group')['Sales'].sum().sort_values(ascending=False)
print(f"Total Sales by Category: {top_cat}")

print("\n============================\n")

#total sales by month
monthly_sales = sales_data_df.groupby(sales_data_df['Date'].dt.to_period('M'))['Sales'].sum()
print(f"Total Sales by Month: {monthly_sales}")

