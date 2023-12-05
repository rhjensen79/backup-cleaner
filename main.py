import os
import datetime

def find_old_backup_files(path, days_threshold=7):
    # Get the current date and time
    current_time = datetime.datetime.now()

    # Calculate the time threshold for old files
    threshold_time = current_time - datetime.timedelta(days=days_threshold)

    # Walk through all folders and subfolders
    for foldername, subfolders, filenames in os.walk(path):
        for filename in filenames:
            # Get the full path of the file
            file_path = os.path.join(foldername, filename)

            # Check if the file name starts with "backup" and ends with ".tar.gz"
            if filename.startswith("backup") and filename.endswith(".tar.gz"):
                # Get the last modification time of the file
                last_modification_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))

                # Check if the file is older than the specified threshold
                if last_modification_time < threshold_time:
                    print(f"Old Backup File: {file_path}, Last Modified: {last_modification_time}")

# Example usage: Replace 'your_path_here' with the actual path you want to search
find_old_backup_files('.', days_threshold=0)
