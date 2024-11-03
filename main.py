import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# GitHub Personal Access Token from .env
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
OWNER_NAME = os.getenv("OWNER_NAME")
REPO_NAME = os.getenv("REPO_NAME")
PULL_NUMBER= os.getenv("PULL_NUMBER")

def get_changed_files(owner, repo, pull_number):
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pull_number}/files"
    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }

    response = requests.get(url, headers=headers)

    # Check for successful response
    if response.status_code == 200:
        files = response.json()
        changed_files = [file["filename"] for file in files]
        return changed_files
    else:
        print(f"Error: {response.status_code}")
        print(response.json())
        return []

if __name__ == "__main__":
    # Replace with your specific values
    owner = OWNER_NAME
    print("owner", owner)
    repo = REPO_NAME
    pull_number = PULL_NUMBER

    changed_files = get_changed_files(owner, repo, pull_number)

    if changed_files:
        print("Files changed in PR:")
        for filename in changed_files:
            print(f"- {filename}")
    else:
        print("No files found or an error occurred.")
