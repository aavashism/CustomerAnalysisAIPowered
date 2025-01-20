import pandas as pd
import random
from faker import Faker

def generate_data():
    """
    Generates a synthetic dataset of customer purchase history.
    - 500 customers
    - 50 products (each with a fixed category)
    - 5,000 purchase records
    """
    fake = Faker()
    num_customers = 500
    num_products = 50
    num_records = 5000

    # Generate customers
    customer_ids = [f"CUST{str(i).zfill(4)}" for i in range(1, num_customers + 1)]

    # Generate products and assign each product to one category
    categories = [f"Category {i}" for i in range(1, 11)]
    product_ids = [f"PROD{str(i).zfill(4)}" for i in range(1, num_products + 1)]
    product_categories = {product: random.choice(categories) for product in product_ids}

    # Generate purchase records
    records = []
    for _ in range(num_records):
        customer_id = random.choice(customer_ids)
        product_id = random.choice(product_ids)
        category = product_categories[product_id]  # Ensure category matches the product
        purchase_amount = round(random.uniform(10, 200), 2)  # Purchase amount between $10 and $200
        purchase_date = fake.date_this_decade()
        records.append([customer_id, product_id, category, purchase_amount, purchase_date])

    # Create a DataFrame and save as CSV
    df = pd.DataFrame(records, columns=["Customer ID", "Product ID", "Product Category", "Purchase Amount", "Purchase Date"])
    df.to_csv("data/customer_purchase_data.csv", index=False)
    print("Dataset saved to 'data/customer_purchase_data.csv'.")

if __name__ == "__main__":
    generate_data()
