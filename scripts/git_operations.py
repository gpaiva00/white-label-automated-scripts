import subprocess
import os

def clone_repo(repo_url, local_repo_path):
    subprocess.run(["git", "clone", repo_url, local_repo_path])

def create_branch(branch_name):
    subprocess.run(["git", "checkout", "-b", branch_name])

def commit_changes(message):
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", message])

def push_changes(branch_name):
    subprocess.run(["git", "push", "origin", branch_name])
