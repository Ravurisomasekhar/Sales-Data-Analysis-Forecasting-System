from src.data_cleaning import load_and_clean_data
from src.analysis import total_sales, top_products, monthly_sales
from src.visualization import plot_top_products, plot_monthly_sales
from src.forecasting import simple_forecast

# Load data
df = load_and_clean_data('data/sales_data.csv')

# Analysis
print("Total Sales:", total_sales(df))

print("\nTop Products:")
print(top_products(df))

monthly = monthly_sales(df)

# Visualization
plot_top_products(top_products(df))
plot_monthly_sales(monthly)

# Forecast
print("\nPredicted Future Sales:", simple_forecast(df))