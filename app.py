# app.py

import requests
from datetime import datetime

def get_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def call_api():
    response = requests.get("https://api.github.com")
    if response.status_code == 200:
        return "GitHub API is reachable!"
    else:
        return "Failed to reach GitHub API"

if __name__ == "__main__":
    print("Application Started")
    print("Current Time:", get_time())
    print(call_api())
    print("Application Finished Successfully")
