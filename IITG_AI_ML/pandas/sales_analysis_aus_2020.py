import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

sales_df = pd.read_csv("data/AusApparalSales4thQrt2020.csv")

# Ensure 'Date' is in datetime format
sales_df['Date'] = pd.to_datetime(sales_df['Date'])

# ====== 📈 1. Interactive Sales Trend Over Time ======
fig1 = px.line(sales_df, x='Date', y='Sales', title="📊 Sales Trend Over Time",
               labels={'Sales': 'Total Sales'}, markers=True)
fig1.update_xaxes(title_text="Date")
fig1.update_yaxes(title_text="Sales Amount")
fig1.show()

# ====== 🌍 2. Total Sales by State ======
fig2 = px.bar(sales_df, x='State', y='Sales', title="🌍 Total Sales by State",
              labels={'Sales': 'Total Sales'}, color='State', text_auto=True)
fig2.update_xaxes(title_text="State")
fig2.update_yaxes(title_text="Total Sales")
fig2.show()

# ====== 🏷️ 3. Sales Distribution by Product Group ======
fig3 = px.pie(sales_df, names='Group', values='Sales', title="🏷️ Sales Distribution by Product Group")
fig3.show()

# ====== 📌 4. Sales Heatmap (Time vs. State) ======
#sales_df['Hour'] = pd.to_datetime(sales_df['Time'], format='%H:%M:%S').dt.hour  # Extract Hour from Time

fig4 = px.density_heatmap(sales_df, x="Time", y="State", z="Sales",
                          title="🔥 Sales Heatmap: Time vs. State", color_continuous_scale="Viridis")
fig4.show()
