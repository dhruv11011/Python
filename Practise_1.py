# Assignment: Automated Data Backup and Cleanup
# Consider you are working on a project where you need to periodically backup and clean up data files from a specific directory.
# You want to create a Python application that performs the following tasks:
# Data Backup:
# Copy all files from a source directory to a backup directory at a specific interval (e.g., daily).
# Use the subprocess module to execute the necessary shell commands for copying files.
# Data Cleanup:
# Delete files older than a certain number of days from the source directory to save space.
# Use the subprocess module to execute shell commands for file deletion.
# Logging:
# Log the backup and cleanup operations along with timestamps to a log file.
# Use the logging module to create and manage logs.
# Scheduling:
# Schedule the backup and cleanup tasks to run automatically daily at 2 PM.
# Use the schedule module to set up the desired scheduling intervals.
# Threading:
# Perform the backup and cleanup tasks concurrently using threads.
# Use the threading module to manage multiple tasks simultaneously.

import os
import subprocess
import logging
import schedule
import time
import threading

def copy_files(source_path, destination_path):
    try:
        # Using the 'cp' command to copy files
        subprocess.run(['xcopy', source_path, destination_path])
        print("Files copied successfully!")
    except Exception as e:
        print("Error copying files:", e)

log_file = "text.log"
logging.basicConfig(filename=log_file, level=logging.INFO,
                    format='%(asctime)s - %(message)s')

# Source and backup directories
source_dir = "Source"
backup_dir = "Destination"

max_age = 5

def backup():
    try:
        for filename in os.listdir(source_dir):
            source_path = os.path.join(source_dir, filename)
            if os.path.isfile(source_path):
                backup_path = os.path.join(backup_dir, filename)
                copy_files(source_path,backup_path)
                logging.info(f"Backup: Copied {filename} to {backup_path}")
    except Exception as e:
        logging.error(f"Backup Error: {str(e)}")

def cleanup():
    try:
        for filename in os.listdir(source_dir):
            file_path = os.path.join(source_dir, filename)
            if os.path.isfile(file_path):
                file_age = (time.time() - os.path.getctime(file_path)) / ( 3600)
                if file_age > max_age:
                    os.remove(file_path)
                    logging.info(f"Cleanup: Removed {filename}")
    except Exception as e:
        logging.error(f"Cleanup Error: {str(e)}")

def daily_tasks():
    backup()
    cleanup()

def schedule_tasks():
    schedule.every().day.at("09:30").do(daily_tasks)
    while True:
        schedule.run_pending()
        time.sleep(60)  # Check every minute

def main():
    # Set up threads for backup, cleanup, and scheduling
    backup_thread = threading.Thread(target=backup)
    cleanup_thread = threading.Thread(target=cleanup)
    schedule_thread = threading.Thread(target=schedule_tasks)

    # Start the threads
    backup_thread.start()
    cleanup_thread.start()
    schedule_thread.start()

    # Wait for threads to finish
    backup_thread.join()
    cleanup_thread.join()
    schedule_thread.join()

if __name__ == "__main__":
    main()