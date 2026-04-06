import matplotlib.pyplot as plt

def plot_top_products(top_products):
    top_products.plot(kind='bar')
    plt.title("Top Products")
    plt.xlabel("Product")
    plt.ylabel("Sales")
    plt.show()

def plot_monthly_sales(monthly_sales):
    monthly_sales.plot()
    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.show()