import json

# ⚠️ Note: It is mandatory to provide the Docker (Linux) path here!
file_path = "/scripts/homework.json"

try:
    # Step 1: Read the JSON file
    with open(file_path, "r") as f:
        data = json.load(f)

    # Step 2: Find the pending tasks
    pending_subjects = []
    for task in data:
        if task["status"] == "pending":
            pending_subjects.append(task["subject"])

    # Step 3: Print the message for the n8n execution node
    if len(pending_subjects) > 0:
        names = ", ".join(pending_subjects)
        print(f"Alert! Aaj ke pending tasks yeh hain: {names}")
    else:
        print("Koi task pending nahi hai. Good job!")

except FileNotFoundError:
    print("❌ Error: homework.json file Docker mein nahi mili. Path check karein!")