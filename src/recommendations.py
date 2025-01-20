import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import csr_matrix

def recommend_products(customer_id, file_path, top_n=5):
    """
    Recommends products for a given customer based on collaborative filtering.
    Uses customer similarity scores to suggest products purchased by similar customers.

    Parameters:
    - customer_id: The ID of the customer for whom recommendations are generated.
    - file_path: Path to the dataset file (CSV or Excel).
    - top_n: Number of recommendations to generate.

    Returns:
    - List of recommended products with their categories.
    """
    try:
        # Load dataset
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
        elif file_path.endswith('.xlsx'):
            df = pd.read_excel(file_path)
        else:
            raise ValueError("Unsupported file format. Please provide a .csv or .xlsx file.")

        # Check if customer exists in the dataset
        if customer_id not in df["Customer ID"].unique():
            print(f"Error: Customer ID '{customer_id}' not found in the dataset.")
            return []

        # Create a customer-product matrix
        customer_product_matrix = df.pivot_table(index='Customer ID', columns='Product ID', values='Purchase Amount', fill_value=0)

        # Convert to a sparse matrix for efficiency
        sparse_matrix = csr_matrix(customer_product_matrix.values)

        # Calculate cosine similarity between customers
        customer_similarity = cosine_similarity(sparse_matrix)

        # Get index for the target customer
        customer_index = customer_product_matrix.index.tolist().index(customer_id)

        # Get similarity scores for the target customer
        similarity_scores = customer_similarity[customer_index]

        # Weight product scores by similarity scores
        weighted_product_scores = customer_product_matrix.T.dot(similarity_scores)

        # Create a DataFrame for recommended products
        product_scores_df = pd.DataFrame({
            "Product ID": customer_product_matrix.columns,
            "Score": weighted_product_scores
        })

        # Exclude products already purchased by the customer
        purchased_products = set(customer_product_matrix.loc[customer_id][customer_product_matrix.loc[customer_id] > 0].index)
        recommendations = product_scores_df[~product_scores_df["Product ID"].isin(purchased_products)]

        # Sort by score and return top N recommendations
        recommendations = recommendations.sort_values(by="Score", ascending=False).head(top_n)

        # Fetch product categories
        product_data = df[["Product ID", "Product Category"]].drop_duplicates().set_index("Product ID")
        recommendations = [
            {"Product ID": row["Product ID"], "Product Category": product_data.loc[row["Product ID"], "Product Category"]}
            for _, row in recommendations.iterrows()
        ]

        return recommendations

    except Exception as e:
        print(f"Error generating recommendations: {e}")
        return []

if __name__ == "__main__":
    # Example usage
    dataset_path = "data/customer_purchase_data.csv"
    customer_id = input("Enter Customer ID for recommendations: ").strip()
    recommendations = recommend_products(customer_id, dataset_path)
    if recommendations:
        print(f"\nRecommendations for Customer {customer_id}:")
        for rec in recommendations:
            print(f"Product ID: {rec['Product ID']} | Category: {rec['Product Category']}")
    else:
        print(f"No recommendations available for Customer {customer_id}.")
