from data_generation import generate_data
from analysis import analyze_data
from clustering import cluster_customers
from recommendations import recommend_products
from report_generator import generate_report

def main():
    print("Welcome to the AI-Powered Customer Purchase Analysis Tool!")
    print("Let's get started!")

    # Ask the user to upload or generate data
    while True:
        print("\nDo you want to:")
        print("1. Generate a new dataset")
        print("2. Upload an existing dataset (CSV or Excel)")
        data_choice = input("Enter your choice (1 or 2): ")

        if data_choice == "1":
            print("\nGenerating a new dataset...")
            generate_data()
            file_path = "data/customer_purchase_data.csv"
            break
        elif data_choice == "2":
            file_path = input("\nEnter the path to your dataset (.csv or .xlsx): ").strip()
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

    # Main program options
    while True:
        print("\nOptions:")
        print("1. Analyze data")
        print("2. Run customer segmentation")
        print("3. Generate product recommendations")
        print("4. Generate a PDF report")
        print("5. Exit")
        action = input("Enter your choice (1-5): ")

        if action == "1":
            print("\nPerforming data analysis...")
            analyze_data(file_path)
        elif action == "2":
            print("\nRunning customer segmentation...")
            cluster_customers(file_path)
        elif action == "3":
            print("\nGenerating product recommendations...")
            customer_id = input("Enter a Customer ID for recommendations: ").strip()
            recommendations = recommend_products(customer_id, file_path)
            if recommendations:
                print(f"\nRecommendations for Customer {customer_id}:")
                for rec in recommendations:
                    print(f"Product ID: {rec['Product ID']}, Category: {rec['Product Category']}")
            else:
                print(f"No recommendations available for Customer ID: {customer_id}.")
        elif action == "4":
            print("\nGenerating PDF report...")
            customer_id = input("Enter a Customer ID for recommendations in the report: ").strip()
            generate_report(file_path, customer_id)
        elif action == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
