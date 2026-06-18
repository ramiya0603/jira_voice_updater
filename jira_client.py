import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

JIRA_URL = os.getenv("JIRA_URL")
JIRA_EMAIL = os.getenv("JIRA_EMAIL")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")

def post_comment(issue_key, comment):
    url = f"{JIRA_URL}/rest/api/3/issue/{issue_key}/comment"

    payload = {
        "body": comment
    }

    requests.post(
        url,
        json=payload,
        auth=HTTPBasicAuth(JIRA_EMAIL, JIRA_API_TOKEN),
        headers={"Accept": "application/json"}
    )
