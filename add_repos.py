import requests

# Set your GitHub username and access token
username = "your_username"
access_token = "your_access_token"

# Set the repositories you want to add to the workflow
repos = ["user/repo1", "user/repo2", "user/repo3"]

# Loop through each repository and add it to the workflow
for repo in repos:
    url = f"https://api.github.com/repos/{repo}/actions/secrets/public-key"
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"token {access_token}"
    }
    response = requests.get(url, headers=headers)
    key_id = response.json()["key_id"]
    
    url = f"https://api.github.com/repos/{repo}/actions/secrets/{key_id}"
    payload = {
        "encrypted_value": "your_encrypted_value",
        "key_id": key_id
    }
    response = requests.put(url, json=payload, headers=headers)
    if response.status_code == 201:
        print(f"{repo} has been added to the workflow.")
    else:
        print(f"{repo} could not be added to the workflow. Error: {response.text}.")
