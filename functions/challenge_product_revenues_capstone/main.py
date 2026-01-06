# Task 1: Define a function to calculate the revenue for each product
def calculate_revenue(prices, quantities_sold):
    revenue = []
    for p, q in zip(prices, quantities_sold):
        revenue.append(p * q)
    return revenue

# Task 2: Define a function to format and display the sorted revenues
def formatted_output(revenue_per_product):
    for product, rev in sorted(revenue_per_product):
        print(f"{product} has total revenue of ${rev}")

# Given data
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]
quantities_sold = [150, 200, 100, 50]

# Task 3 & 4: Calculate and combine
revenue = calculate_revenue(prices, quantities_sold)
revenue_per_product = list(zip(products, revenue))

# Task 5: Display
formatted_output(revenue_per_product)