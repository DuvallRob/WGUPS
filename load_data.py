# load_data.py
import pandas as pd

def load_package_data():
    package_data = pd.read_csv('WGUPS_Package_File.csv', header=None, skiprows=1)
    package_data.columns = ['Package ID', 'Address', 'City', 'State', 'Zip', 'Deadline', 'Weight', 'Special Notes']
    print(f"Total packages loaded: {len(package_data)}")
    return package_data.to_dict('records')

def load_distance_data():
    distance_data = pd.read_csv('WGUPS_Distance_Table.csv', header=0)
    return distance_data

def load_address_data():
    address_data = pd.read_csv('WGUPS_Address_File.csv', header=None)
    address_data.columns = ['ID', 'Location', 'Address']
    return address_data
