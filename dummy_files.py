import os
import random
from datetime import datetime, timedelta

def generate_dummy_files(folder_path, num_files):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    for i in range(num_files):
        # Generate a random age for the file in days (between 1 and 365 days)
        age_in_days = random.randint(1, 365)
        
        # Calculate the last modified timestamp based on the age
        last_modified = datetime.now() - timedelta(days=age_in_days)

        # Format the timestamp to use in the filename
        timestamp_str = last_modified.strftime("%Y%m%d%H%M%S")

        # Create a dummy file with the formatted timestamp
        file_name = f"dummy_file_{timestamp_str}.txt"
        file_path = os.path.join(folder_path, file_name)

        with open(file_path, 'w') as file:
            file.write(f"This is a dummy file created on {last_modified}")

if __name__ == "__main__":
    folder_path = "dummy_folder"
    num_files = 100  # Change this to the desired number of dummy files

    generate_dummy_files(folder_path, num_files)
    print(f"{num_files} dummy files created in the folder: {folder_path}")
