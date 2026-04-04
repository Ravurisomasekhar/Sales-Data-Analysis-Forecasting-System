def total_sales(df):
    return df['Sales'].sum()

def top_products(df):
    return df.groupby('Product')['Sales'].sum().sort_values(ascending=False)

def monthly_sales(df):
    df['Month'] = df['Date'].dt.to_period('M')
    return df.groupby('Month')['Sales'].sum()



# home 