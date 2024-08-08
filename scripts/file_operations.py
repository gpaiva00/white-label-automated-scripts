import shutil
import os

def replace_file(source, destination):
    shutil.copy2(source, destination)
    print(f" file: {os.path.basename(source)} replaced successfully.")

def ensure_dir_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"directory {directory} created successfully.")

def clear_temp_dir(LOCAL_TEMP_DIR):
    shutil.rmtree(LOCAL_TEMP_DIR)
    print("temporary directory deleted successfully.")
