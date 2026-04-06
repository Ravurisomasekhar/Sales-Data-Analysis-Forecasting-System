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



    # these function aare used to shoe the
    #  visualization of the data in the form f graph and charts.
    #  it is used to show the top products and monthly sales trend.