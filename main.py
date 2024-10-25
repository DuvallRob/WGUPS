# main.py
# Student ID: 007792396

from hash_table import HashTable
from load_data import load_package_data, load_distance_data, load_address_data
from routing import calculate_route, update_delivery_status

def main():
    # Load data
    print("Loading data...")
    package_data = load_package_data()
    distance_data = load_distance_data()
    address_data = load_address_data()
    
    # Verify data loaded correctly
    print("Package Data Loaded:")
    print(package_data[:5])  # Print the first 5 entries
    print("Distance Data Loaded:")
    print(distance_data.head())  # Print the first 5 rows
    print("Address Data Loaded:")
    print(address_data.head())  # Print the first 5 rows
    
    # Create hash table to store package details
    package_table = HashTable()
    
    # Insert package data into hash table
    for package in package_data:
        package_table.insert(package['Package ID'], package)
    
    # Calculate delivery routes
    print("Calculating routes...")
    truck_routes = calculate_route(package_table, distance_data, address_data)
    
    # Update and display delivery status
    print("Updating delivery status...")
    update_delivery_status(truck_routes, package_table)

if __name__ == "__main__":
    main()
