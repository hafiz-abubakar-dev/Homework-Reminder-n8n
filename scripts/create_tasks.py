import json

# Step 1: Initial data payload (Example with 2 subjects)
json_data = [
    {
        "date": "2026-09-22",
        "subject": "english",
        "status": "pending"
    },
    {
        "date": "2026-09-22",
        "subject": "urdu",
        "status": "pending"
    }
]

# Step 2: Create the JSON file (Windows file path)
file_path = "C:/n8n-python/scripts/homework.json"

with open(file_path, "w") as f:
    json.dump(json_data, f, indent=4)

print("✅ Success: homework.json file ban gayi hai!")