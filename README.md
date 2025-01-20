
# Customer Purchase Analysis Program

This program is designed to provide an interactive and comprehensive solution for customer purchase analysis. It generates synthetic data or allows users to upload their own datasets. The program performs in-depth analysis, including customer segmentation, personalized recommendations using collaborative filtering, and detailed reporting. Outputs include a visually rich PDF report summarizing findings such as top-selling products, revenue trends, and customer-specific recommendations. Full analysis results are saved as CSV files for detailed review.

---

## Features

### Data Generation or Upload their own dataset in the correct format.
- Includes a module for generating synthetic customer purchase data with customizable parameters.
- Automatically creates datasets (`customer_purchase_data.csv`) for analysis, ensuring realistic distributions for testing and evaluation.
- Allows users to upload their own datasets for customized analysis.

### Data Analysis
- Identifies top-selling products, categories, and average spending per customer.
- Displays the top 5 results for better readability in the console, while saving the full analysis results in CSV files for detailed review.
- Tracks monthly revenue trends using purchase history.
- Segments customers into meaningful groups (e.g., "High Spenders," "Occasional Buyers") using KMeans clustering.

### Personalized Recommendations
- Uses collaborative filtering to suggest products based on customer similarity.
- Excludes products already purchased by the customer to ensure relevancy.

### Report Generation
- Outputs a visually rich PDF report summarizing findings such as:
  - Top product categories (Top 5 displayed; full results saved in `data/all_categories.csv`).
  - Monthly revenue trends.
  - Customer segments (saved in `data/customer_segments.csv`).
  - Personalized product recommendations.
  - Recommendation logic.

### Interactive Design
- The program prompts you to input a **Customer ID** (e.g., `CUST0001`), ensuring a personalized and seamless experience.
- Dynamically adapts to user-provided datasets or generated data for flexibility.

---

## Requirements

Before running the program, ensure you have the following installed:
- Python 3.8+
- Required libraries (listed in `requirements.txt`)

---


## How to Run: 
## Step 1: Setting Up the Virtual Environment

It is recommended to use a virtual environment to manage dependencies. Follow these steps based on your operating system:

### For macOS/Linux:
```bash
# Create the virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### For Windows:
```bash
# Create the virtual environment
python -m venv venv

# Activate the virtual environment
venv\Scripts\activate

# Install dependencies 
pip install -r requirements.txt
```

---

## Step 2: Run the Program

1. **Run the Main Script**:
   - Execute the program by running `main.py`:
     ```bash
     python src/main.py
     ```
   - NOTE: FIRST TIME U RUN 'main.py', IT MAY TAKE UPTO 60 SECONDS TO RUN. Please be patient. This WONT happen after running the first time.  
   - Now use it according to the interactive interface. 
   - When you will be prompted to input a **Customer ID** (e.g., `CUST0001`or any other customer from the database) to generate a personalized PDF report, data analysis and other outputs.

2. **First-Time Execution**:
   - The first run after Git Cloning may take up to **60 seconds** .
   - Subsequent runs will be faster.

3. **Outputs**:
   - **PDF Report**:
     - A visually rich PDF report is saved in the current directory, named `Customer_Purchase_Analysis_Report_<CustomerID>.pdf`. This report includes:
       - Top product categories (Top 5 displayed; full results saved in `data/all_categories.csv`).
       - Monthly revenue trends.
       - Customer segmentation.
       - Personalized product recommendations.
   - **CSV Files**:
     - Several CSV files are generated and saved in the `data/` directory:
       - `customer_segments.csv`: Contains customer segmentation data.
       - `all_products.csv`: Full product sales analysis.
       - `all_categories.csv`: Full category sales analysis.
       - `full_avg_spending.csv`: Full average spending per customer.

4. **Custom Data**:
   - If you wish to use your own dataset, replace the `customer_purchase_data.csv` file in the `data/` directory with your custom data, following the same format.
   - The program will adapt and generate new outputs based on the uploaded data.

---

## Folder Structure

```
AI_Customer_Analysis/
│
├── data/                       # Data storage (input/output)
│   ├── customer_purchase_data.csv    # Input customer purchase data
│   ├── customer_segments.csv         # Output customer segments
│   ├── all_products.csv              # Full product sales analysis
│   ├── all_categories.csv            # Full category sales analysis
│   ├── full_avg_spending.csv         # Full average spending per customer
├── visualizations/                   # Output visualizations for the PDF report
│   │   ├── top_categories.png        # Bar chart for top-selling categories
│   │   ├── customer_segments.png     # Pie chart for customer segments
│   │   └── monthly_revenue.png       # Line chart for monthly revenue trends
├── src/                        # Source code
│   ├── data_generation.py      # Generate synthetic data
│   ├── analysis.py             # Perform data analysis
│   ├── clustering.py           # Classify customers
│   ├── recommendations.py      # Generate product recommendations
│   ├── report_generator.py     # Generate the PDF report
│   ├── main.py                 # Main script to run all components
├── README.md                   # Project documentation
├── requirements.txt            # List of dependencies
└── venv/                       # Virtual environment (not included in version control)
```

---

## Key Notes

- **Interactive Design**:
  - The program handles all components internally through `main.py`, so there’s no need to run individual scripts like `data_generation.py` or `report_generator.py`.
  - Users are prompted for input (e.g., **Customer ID**, such as `CUST0001`) to generate personalized insights and recommendations.

- **Data Analysis**:
  - Displays the top 5 results for better readability, with full results saved in CSV files for detailed review.

- **Recommendation System**:
  - Employs **collaborative filtering** to calculate similarity scores between customers based on purchasing behavior.

- **Error Handling**:
  - Provides clear error messages for invalid Customer IDs, missing data, or other runtime issues.

---

## Example

1. Launch the program inside the virtual environment:
   ```bash
   python src/main.py
   ```
2. Enter a **Customer ID** when prompted (e.g., `CUST0001`).
3. Wait for the analysis to complete. The PDF report will include:
   - Top product categories (Top 5 displayed; full results saved in `data/all_categories.csv`).
   - Monthly revenue trends.
   - Customer segments (Uses k-means).
   - Personalized product recommendations for specific customers.
   - Recommendation Logic.
