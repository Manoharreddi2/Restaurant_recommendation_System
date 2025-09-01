import os
import pandas as pd
import numpy as np

# Set working directory
os.chdir(r"C:\Users\manoh\Data")
print("Current working directory:", os.getcwd())

# Function to check required CSV files
def check_files():
    """
    Check if all required CSV files are present in the current directory.
    """
    required_files = [
        'train_customers.csv',
        'train_locations.csv',
        'train_orders.csv', 
        'vendors.csv',
        'test_customers.csv',
        'test_locations.csv'
    ]
    all_files = os.listdir('.')
    missing_files = [f for f in required_files if f not in all_files]
    
    if missing_files:
        print("Missing files:", missing_files)
        return False
    print("All required files are present.")
    return True

# Function to create sample data for testing
def create_sample_data():
    """
    Create sample CSV files for testing the recommendation pipeline.
    """
    print("\nCreating sample data...")
    
    # Sample train_customers
    n_customers = 1000
    train_customers = pd.DataFrame({
        'customer_id': range(1, n_customers + 1),
        'gender': np.random.choice(['M', 'F'], n_customers),
        'dob': np.random.randint(1970, 2005, n_customers),
        'status': np.random.choice(['active', 'inactive'], n_customers, p=[0.8, 0.2]),
        'verified': np.random.choice([True, False], n_customers, p=[0.9, 0.1]),
        'language': np.random.choice(['english', 'spanish', 'french'], n_customers, p=[0.7, 0.2, 0.1])
    })
    
    # Sample train_locations
    train_locations = []
    for customer_id in range(1, n_customers + 1):
        n_locations = np.random.choice([1, 2, 3], p=[0.6, 0.3, 0.1])
        for loc_num in range(1, n_locations + 1):
            train_locations.append({
                'customer_id': customer_id,
                'location_number': loc_num,
                'location_type': np.random.choice(['Home', 'Work', 'Other'], p=[0.6, 0.3, 0.1]),
                'latitude': np.random.uniform(40.0, 41.0),
                'longitude': np.random.uniform(-74.5, -73.5)
            })
    train_locations = pd.DataFrame(train_locations)
    
    # Sample vendors
    n_vendors = 100
    vendors = pd.DataFrame({
        'id': range(1, n_vendors + 1),
        'latitude': np.random.uniform(40.0, 41.0, n_vendors),
        'longitude': np.random.uniform(-74.5, -73.5, n_vendors),
        'vendor_tag_name': np.random.choice(['Pizza', 'Chinese', 'Indian', 'Mexican', 'Italian'], n_vendors)
    })
    
    # Sample train_orders
    n_orders = 5000
    train_orders = pd.DataFrame({
        'order_id': range(1, n_orders + 1),
        'customer_id': np.random.choice(range(1, n_customers + 1), n_orders),
        'vendor_id': np.random.choice(range(1, n_vendors + 1), n_orders),
        'item_count': np.random.randint(1, 6, n_orders),
        'grand_total': np.random.uniform(10, 100, n_orders)
    })
    
    # Sample test_customers
    n_test_customers = 200
    test_customers = pd.DataFrame({
        'customer_id': range(n_customers + 1, n_customers + n_test_customers + 1),
        'gender': np.random.choice(['M', 'F'], n_test_customers),
        'dob': np.random.randint(1970, 2005, n_test_customers),
        'status': np.random.choice(['active', 'inactive'], n_test_customers, p=[0.8, 0.2]),
        'verified': np.random.choice([True, False], n_test_customers, p=[0.9, 0.1]),
        'language': np.random.choice(['english', 'spanish', 'french'], n_test_customers, p=[0.7, 0.2, 0.1])
    })
    
    # Sample test_locations
    test_locations = []
    for customer_id in range(n_customers + 1, n_customers + n_test_customers + 1):
        n_locations = np.random.choice([1, 2, 3], p=[0.6, 0.3, 0.1])
        for loc_num in range(1, n_locations + 1):
            test_locations.append({
                'customer_id': customer_id,
                'location_number': loc_num,
                'location_type': np.random.choice(['Home', 'Work', 'Other'], p=[0.6, 0.3, 0.1]),
                'latitude': np.random.uniform(40.0, 41.0),
                'longitude': np.random.uniform(-74.5, -73.5)
            })
    test_locations = pd.DataFrame(test_locations)
    
    # Save CSV files
    train_customers.to_csv('train_customers.csv', index=False)
    train_locations.to_csv('train_locations.csv', index=False)
    train_orders.to_csv('train_orders.csv', index=False)
    vendors.to_csv('vendors.csv', index=False)
    test_customers.to_csv('test_customers.csv', index=False)
    test_locations.to_csv('test_locations.csv', index=False)
    
    print("Sample data files created successfully.")

# Main execution
if __name__ == "__main__":
    print("Restaurant Recommendation Data Helper")
    print("=" * 40)
    
    if not check_files():
        print("\nCreating sample data for testing the pipeline...")
        create_sample_data()
        print("\nYou can now run the recommendation engine using sample data.")
    else:
        print("\nAll files found! You can proceed with the recommendation engine.")
