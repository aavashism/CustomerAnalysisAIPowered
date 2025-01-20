import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def cluster_customers(file_path):
    """
    Clusters customers into segments based on their purchase behavior:
    - Total spending
    - Purchase frequency

    Parameters:
    - file_path: Path to the dataset file (CSV or Excel).

    Saves:
    - Customer segments to 'data/customer_segments.csv'
    """
    try:
        # Load data
        df = pd.read_csv(file_path)

        # Aggregate data to calculate total spending and purchase frequency
        customer_data = df.groupby('Customer ID').agg({
            'Purchase Amount': 'sum',
            'Product ID': 'count'
        }).reset_index()
        customer_data.columns = ['Customer ID', 'Total Spending', 'Purchase Frequency']

        # Standardize the data for clustering
        scaler = StandardScaler()
        scaled_data = scaler.fit_transform(customer_data[['Total Spending', 'Purchase Frequency']])

        # Perform K-Means clustering
        kmeans = KMeans(n_clusters=4, random_state=42)
        customer_data['Cluster'] = kmeans.fit_predict(scaled_data)

        # Assign intuitive labels to clusters
        cluster_labels = assign_cluster_labels(kmeans, customer_data)
        customer_data['Segment'] = customer_data['Cluster'].map(cluster_labels)

        # Save segmented data
        customer_data.to_csv("data/customer_segments.csv", index=False)
        print("Customer segmentation completed. Results saved to 'data/customer_segments.csv'.")
        print(customer_data[['Segment', 'Customer ID']].groupby('Segment').count())

    except Exception as e:
        print(f"Error during customer segmentation: {e}")


def assign_cluster_labels(kmeans, customer_data):
    """
    Assigns human-readable labels to K-Means clusters based on cluster characteristics.

    Parameters:
    - kmeans: Fitted K-Means model.
    - customer_data: DataFrame with customer data and clusters.

    Returns:
    - A dictionary mapping cluster indices to labels.
    """
    cluster_centers = kmeans.cluster_centers_
    # Sort clusters by total spending and frequency
    sorted_clusters = sorted(enumerate(cluster_centers), key=lambda x: (x[1][0], x[1][1]), reverse=True)
    labels = ["High Spenders", "Frequent Buyers", "Occasional Buyers", "Low Spenders"]
    return {cluster_idx: labels[i] for i, (cluster_idx, _) in enumerate(sorted_clusters)}


if __name__ == "__main__":
    dataset_path = "data/customer_purchase_data.csv"
    cluster_customers(dataset_path)
