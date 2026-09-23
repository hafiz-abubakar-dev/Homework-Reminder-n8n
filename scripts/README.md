# Python Scripts (Homework Reminder)

This folder contains the Python scripts required to manage and process local data for the n8n Homework Reminder automation workflow.

## 📂 Files Overview
* **`create_tasks.py`**: A setup utility script that generates the initial `homework.json` database file with sample tasks.
* **`check_pending.py`**: The core script executed automatically by the n8n `Execute Command` node. It reads the JSON database, filters for tasks with a "pending" status, and outputs a formatted alert string.
* **`update_task.py`**: A command-line interface (CLI) tool used to manually mark a task as completed. 
  * *Usage:* `python update_task.py [subject_name]` (e.g., `python update_task.py english`)

## ⚙️ Environment Note
Ensure the absolute file path inside `check_pending.py` strictly matches the volume mount directory of your n8n Docker container (e.g., `/scripts/homework.json`).
