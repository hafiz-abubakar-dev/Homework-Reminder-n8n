import json
import sys

# Step 1: Verify if the user provided the subject name as an argument
if len(sys.argv) < 2:
    print("❌ Error: Aapne subject ka naam nahi likha!")
    print("💡 Sahi tareeqa: python update_task.py english")
    sys.exit(1)

# Step 2: Capture the argument from the terminal and convert it to lowercase
subject_name = sys.argv[1].lower()
file_path = "C:/n8n-python/scripts/homework.json"

# Step 3: Read the JSON file
with open(file_path, "r") as f:
    data = json.load(f)

# Step 4: Search the list and update the status to 'done'
task_mil_gaya = False
for task in data:
    if task["subject"] == subject_name:
        task["status"] = "done"
        task_mil_gaya = True
        break

# Step 5: Save the new changes back to the JSON file
if task_mil_gaya:
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)
    print(f"✅ Zabardast! {subject_name} ka status DONE ho gaya hai.")
else:
    print(f"❌ Sorry, {subject_name} list mein nahi mila.")