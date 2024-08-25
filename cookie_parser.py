import json

json_file_name = 'cookies_ig_original.json'

# Load the JSON file
with open(json_file_name, 'r') as file:
    data = json.load(file)

# Filter the data to include only 'name' and 'value'
filtered_data = [{"name": item["name"], "value": item["value"]} for item in data]

# Write the filtered data to a new JSON file
with open('cookies_ig.json', 'w') as file:
    json.dump(filtered_data, file, indent=4)

print("Filtered data saved to 'cookies_ig.json'")