import json
import csv
import argparse
import os

def ensure_list_of_dicts(data):
    if isinstance(data, dict):
        return [data]
    elif not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
        raise ValueError("JSON data must be an array of objects or a single object.")
    else:
        return data

def json_to_csv(json_file_path, csv_file_path):
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

    data = ensure_list_of_dicts(data)

    if not data:
        raise ValueError("JSON data must contain at least one object.")
    headers = data[0].keys()

    with open(csv_file_path, 'w', newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=headers)
        
        csv_writer.writeheader()
        
        for item in data:
            csv_writer.writerow(item)

def main():
    parser = argparse.ArgumentParser(description="Convert JSON to CSV")
    
    parser.add_argument('--json-file', type=str, required=True,
                        help='Path to the input JSON file')
    
    args = parser.parse_args()
    
    json_file_path = args.json_file
    
    base_name = os.path.splitext(os.path.basename(json_file_path))[0]
    
    csv_file_path = f"{base_name}.csv"
    
    try:
        json_to_csv(json_file_path, csv_file_path)
        print(f"JSON data has been successfully converted to {csv_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

