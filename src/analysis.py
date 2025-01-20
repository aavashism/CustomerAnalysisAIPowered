import pandas as pd

def analyze_data(file_path):
    """
    Analyzes the dataset to extract key insights:
    - Top-selling products
    - Top-selling categories
    - Average spending per customer
    """
    try:
        # Load the dataset
        df = load_data(file_path)

        # Top-selling products
        product_sales = df.groupby("Product ID")["Purchase Amount"].sum().sort_values(ascending=False)
        top_products = product_sales.head(5)
        print("\nTop-Selling Products (Top 5 displayed for better readability):")
        print(top_products)
        print("Full results saved in 'data/all_products.csv'.\n")

        # Top-selling categories
        category_sales = df.groupby("Product Category")["Purchase Amount"].sum().sort_values(ascending=False)
        top_categories = category_sales.head(5)
        print("\nTop-Selling Categories (Top 5 displayed for better readability):")
        print(top_categories)
        print("Full results saved in 'data/all_categories.csv'.\n")

        # Average spending per customer
        customer_spending = df.groupby("Customer ID")["Purchase Amount"].mean().sort_values(ascending=False)
        top_avg_spending = customer_spending.head(5)
        print("\nAverage Spending per Customer (Top 5 displayed for better readability):")
        print(top_avg_spending)
        print("Full results saved in 'data/full_avg_spending.csv'.\n")

        # Save full results for detailed analysis
        product_sales.to_csv("data/all_products.csv", header=["Total Sales"])
        category_sales.to_csv("data/all_categories.csv", header=["Total Sales"])
        customer_spending.to_csv("data/full_avg_spending.csv", header=["Average Spending"])

        # Save top results for the report
        top_products.to_csv("data/top_products.csv", header=["Total Sales"])
        top_categories.to_csv("data/top_categories.csv", header=["Total Sales"])
        top_avg_spending.to_csv("data/top_avg_spending.csv", header=["Average Spending"])

        print("\nAnalysis results have been successfully saved for reporting and detailed review.")
    except Exception as e:
        print(f"Error during data analysis: {e}")

def load_data(file_path):
    """
    Loads the dataset from a CSV or Excel file.
    """
    if file_path.endswith(".csv"):
        return pd.read_csv(file_path)
    elif file_path.endswith(".xlsx"):
        return pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file format. Please provide a .csv or .xlsx file.")

if __name__ == "__main__":
    dataset_path = "data/customer_purchase_data.csv"
    analyze_data(dataset_path)
