# routing.py
import datetime

def calculate_route(package_table, distance_data, address_data):
    # Flatten the hash table to get all packages in a single list
    all_packages = []
    for bucket in package_table.table:
        if bucket:
            all_packages.extend(bucket)

    # Sort all packages by their deadlines
    sorted_packages = sorted(all_packages, key=lambda x: x['Deadline'] if x else 'EOD')

    truck_routes = {
        1: [],
        2: [],
        3: []
    }

    # Simple logic to distribute sorted packages across trucks
    for i, package in enumerate(sorted_packages):
        truck_number = (i % 3) + 1
        truck_routes[truck_number].append(package['Package ID'])
    
    return truck_routes

def simulate_time(start_time_str, time_increment_minutes):
    time_format = "%I:%M %p"
    current_time = datetime.datetime.strptime(start_time_str, time_format)
    return (current_time + datetime.timedelta(minutes=time_increment_minutes)).strftime(time_format)

def update_delivery_status(truck_routes, package_table):
    # Initial time
    start_time = "08:00 AM"
    
    # Time intervals for D1, D2, D3
    d1_time_start = "08:35 AM"
    d1_time_end = "09:25 AM"
    d2_time_start = "09:35 AM"
    d2_time_end = "10:25 AM"
    d3_time_start = "12:03 PM"
    d3_time_end = "01:12 PM"
    
    print("\n--- D1 Status Check (8:35 AM - 9:25 AM) ---")
    for truck, route in truck_routes.items():
        for i, package_id in enumerate(route):
            # Simulate time passing for each delivery
            delivery_time = simulate_time(start_time, i * 15)  # Increment time by 15 minutes per package
            package = package_table.lookup(package_id)
            if package:
                package['Delivery Status'] = 'Delivered'
                package['Delivery Time'] = delivery_time
                
                # Display the deliveries during D1
                if d1_time_start <= delivery_time <= d1_time_end:
                    print(f"Truck {truck} delivered package {package_id} to {package['Address']} at {delivery_time}")
                
                # Display the deliveries during D2
                if d2_time_start <= delivery_time <= d2_time_end:
                    print(f"--- D2 Status Check (9:35 AM - 10:25 AM) ---")
                    print(f"Truck {truck} delivered package {package_id} to {package['Address']} at {delivery_time}")
                
                # Display the deliveries during D3
                if d3_time_start <= delivery_time <= d3_time_end:
                    print(f"--- D3 Status Check (12:03 PM - 1:12 PM) ---")
                    print(f"Truck {truck} delivered package {package_id} to {package['Address']} at {delivery_time}")
            else:
                print(f"Package {package_id} not found in table.")