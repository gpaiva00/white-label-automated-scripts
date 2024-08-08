import shutil
import os

def replace_file(source, destination):
    shutil.copy2(source, destination)
    print(f" file: {os.path.basename(source)} replaced successfully.")

def ensure_dir_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"directory {directory} created successfully.")

def clear_dir(directory):
    shutil.rmtree(directory)
    print(f"directory {directory} deleted successfully.")
