import pandas as pd
from fpdf import FPDF
import matplotlib.pyplot as plt
from recommendations import recommend_products


def generate_report(file_path, customer_id):
    try:
        # Load purchase data
        df = pd.read_csv(file_path)

        # Top-Selling Products
        top_products = df.groupby("Product ID")["Purchase Amount"].sum().sort_values(ascending=False).head(5)
        full_product_sales = df.groupby("Product ID")["Purchase Amount"].sum()
        full_product_sales.to_csv("data/full_products_sales.csv", header=["Total Sales"])

        # Top-Selling Product Categories
        top_categories = df.groupby("Product Category")["Purchase Amount"].sum().sort_values(ascending=False).head(5)
        full_category_sales = df.groupby("Product Category")["Purchase Amount"].sum()
        full_category_sales.to_csv("data/full_categories_sales.csv", header=["Total Sales"])

        # Average Spending per Customer
        avg_spending = df.groupby("Customer ID")["Purchase Amount"].mean().sort_values(ascending=False).head(5)
        full_avg_spending = df.groupby("Customer ID")["Purchase Amount"].mean()
        full_avg_spending.to_csv("data/full_avg_spending.csv", header=["Average Spending"])

        # Monthly Revenue Trends
        df["Purchase Date"] = pd.to_datetime(df["Purchase Date"])
        monthly_revenue = df.groupby(df["Purchase Date"].dt.to_period("M"))["Purchase Amount"].sum()

        # Load customer segments
        customer_segments = pd.read_csv("data/customer_segments.csv")
        segment_summary = customer_segments["Segment"].value_counts()

        # Create Visualizations
        create_visualizations(top_categories, segment_summary, monthly_revenue)

        # Initialize PDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", "B", 14)
        pdf.cell(0, 10, "Customer Purchase Analysis Report", 0, 1, "C")
        pdf.ln(10)

        # Add Top Products Section
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 10, "Top-Selling Products (Total Sales):", 0, 1)
        pdf.set_font("Arial", "", 10)
        for product, amount in top_products.items():
            pdf.cell(0, 10, f"Product ID {product}: ${amount:.2f}", 0, 1)
        pdf.cell(0, 10, "Full results saved in 'data/full_products_sales.csv'.", 0, 1)
        pdf.ln(10)

        # Add Top Categories Section
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 10, "Top-Selling Categories (Total Sales):", 0, 1)
        pdf.set_font("Arial", "", 10)
        for category, amount in top_categories.items():
            pdf.cell(0, 10, f"{category}: ${amount:.2f}", 0, 1)
        pdf.cell(0, 10, "Full results saved in 'data/full_categories_sales.csv'.", 0, 1)
        pdf.ln(10)

        # Add Average Spending Section
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 10, "Average Spending per Customer (Top 5):", 0, 1)
        pdf.set_font("Arial", "", 10)
        for customer, amount in avg_spending.items():
            pdf.cell(0, 10, f"Customer ID {customer}: ${amount:.2f}", 0, 1)
        pdf.cell(0, 10, "Full results saved in 'data/full_avg_spending.csv'.", 0, 1)
        pdf.ln(10)

        # Add Monthly Revenue Trends Chart
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 10, "Monthly Revenue Trends:", 0, 1)
        pdf.ln(5)
        pdf.image("visualizations/monthly_revenue.png", x=15, w=180)
        pdf.ln(10)

        # Add Customer Segments Summary
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 10, "Customer Segments Summary:", 0, 1)
        pdf.set_font("Arial", "", 10)
        for segment, count in segment_summary.items():
            pdf.cell(0, 10, f"{segment}: {count} customers", 0, 1)
        pdf.ln(10)

        # Embed Customer Segments Pie Chart
        pdf.cell(0, 10, "Customer Segments Distribution:", 0, 1)
        pdf.ln(5)
        pdf.image("visualizations/customer_segments.png", x=15, w=180)
        pdf.ln(10)

        # Add Customer-Specific Recommendations
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 10, f"Recommendations for Customer {customer_id}:", 0, 1)
        pdf.set_font("Arial", "", 10)
        recommendations = recommend_products(customer_id, file_path)
        if recommendations:
            for rec in recommendations:
                pdf.cell(0, 10, f"Product ID: {rec['Product ID']} | Category: {rec['Product Category']}", 0, 1)
        else:
            pdf.cell(0, 10, f"No recommendations available for Customer {customer_id}.", 0, 1)
        pdf.ln(10)

        # Add Recommendation Logic Explanation
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 10, "Recommendation Logic:", 0, 1)
        pdf.set_font("Arial", "", 10)
        pdf.multi_cell(0, 10,
            "The recommendation system uses collaborative filtering, which leverages customer-product interaction data. "
            "It begins by constructing a customer-product matrix, where each row represents a customer and each column represents a product. "
            "The values in this matrix indicate the purchase amounts for each product by the respective customer.\n\n"
            "Using this matrix, the system calculates similarity scores between customers based on their purchasing behaviors. "
            "These scores are derived using cosine similarity, a measure that identifies how closely related two customers are in terms of their product preferences.\n\n"
            "Once customer similarity scores are determined, the system identifies the most similar customers to the target customer. "
            "Products purchased by these similar customers are weighted by their similarity scores and prioritized in the recommendation list. "
            "To ensure relevancy, products already purchased by the target customer are excluded from the final recommendations.\n\n"
            "This collaborative filtering approach ensures that the recommendations are personalized and reflective of trends and patterns observed among similar customers, "
            "rather than relying solely on product attributes. It adapts to dynamic changes in customer behavior, offering relevant suggestions based on collective purchasing patterns."
        )
        pdf.ln(10)

        # Save PDF
        output_path = f"Customer_Purchase_Analysis_Report_{customer_id}.pdf"
        pdf.output(output_path)
        print(f"Report saved as '{output_path}'.")

    except Exception as e:
        print(f"Error generating report: {e}")


def create_visualizations(top_categories, segment_summary, monthly_revenue):
    """
    Creates visualizations for top categories, customer segments, and monthly revenue trends.
    Saves the plots as images for embedding into the PDF.
    """
    import os
    os.makedirs("visualizations", exist_ok=True)

    # Top Categories Bar Chart
    plt.figure(figsize=(8, 5))
    top_categories.plot(kind="bar", title="Top-Selling Categories", ylabel="Total Sales", xlabel="Category")
    plt.tight_layout()
    plt.savefig("visualizations/top_categories.png")
    plt.close()

    # Customer Segments Pie Chart
    plt.figure(figsize=(8, 5))
    segment_summary.plot(kind="pie", autopct="%1.1f%%", title="Customer Segments Distribution")
    plt.ylabel("")  # Remove default ylabel from pie chart
    plt.tight_layout()
    plt.savefig("visualizations/customer_segments.png")
    plt.close()

    # Monthly Revenue Line Chart
    plt.figure(figsize=(8, 5))
    monthly_revenue.plot(kind="line", title="Monthly Revenue Trends", ylabel="Revenue", xlabel="Month", marker="o")
    plt.tight_layout()
    plt.savefig("visualizations/monthly_revenue.png")
    plt.close()


if __name__ == "__main__":
    dataset_path = "data/customer_purchase_data.csv"
    customer_id_input = input("Enter the Customer ID for recommendations in the report: ").strip()
    generate_report(dataset_path, customer_id_input)
