import json

filePath = 'troops.json'

try:
    with open(filePath, 'r') as file:
        # upload is reference to json file
        upload = json.load(file)


except FileNotFoundError:
    print(f"Error: The file {filePath} was not found.")
    exit()


if upload is not None:
    print("✅ Import successful!")
    print(f"Data Type: {type(data)}")
    print(f"First 50 characters of data: {str(data)[:50]}...")
else:
    print("❌ Import failed or file was not found.")