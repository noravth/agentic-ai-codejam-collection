# https://community.sap.com/t5/artificial-intelligence-blogs-posts/sap-rpt-1-a-step-by-step-guide-on-getting-started/ba-p/14290171
# https://help.sap.com/docs/sap-ai-core/generative-ai-hub/consume-large-language-models-using-sap-ai-core

from dotenv import load_dotenv
import os
from pathlib import Path
import base64
import requests

env_path = "/Users/D070387/agentic-ai-codejam-collection/crewai/.env"
load_dotenv(env_path)

# read environment variables
AICORE_CLIENT_ID = os.getenv("AICORE_CLIENT_ID")
if not AICORE_CLIENT_ID:
    raise RuntimeError("AICORE_CLIENT_ID not set in .env")
AICORE_CLIENT_SECRET = os.getenv("AICORE_CLIENT_SECRET")
if not AICORE_CLIENT_SECRET:
    raise RuntimeError("AICORE_CLIENT_SECRET not set in .env")
AICORE_AUTH_URL = os.getenv("AICORE_AUTH_URL")
if not AICORE_AUTH_URL:
    raise RuntimeError("AICORE_AUTH_URL not set in .env")

# Function to fetch OAuth token
def fetch_token(auth_url: str | None = None, client_id: str | None = None, client_secret: str | None = None, timeout: int = 30) -> dict:
    auth_url = AICORE_AUTH_URL
    if not auth_url:
        raise ValueError("AICORE_AUTH_URL must be provided (env or arg).")
    data = {
        "grant_type": "client_credentials",
        "client_id": AICORE_CLIENT_ID,
        "client_secret": AICORE_CLIENT_SECRET
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    resp = requests.post(auth_url, data=data, headers=headers, timeout=timeout)
    resp.raise_for_status()
    return resp.json()

# Fetch the token
token = fetch_token()

# Define the deployment URL
deployment_url = (
    "https://api.ai.prod.eu-central-1.aws.ml.hana.ondemand.com/v2/inference/deployments/de31f88d3d9719ab"
    + "/predict"
)
print("Deployment URL:", deployment_url)

# Define the JSON payload for prediction
json_payload = {
    "prediction_config": {
        "target_columns": [
            {
                "name": "COSTCENTER",
                "prediction_placeholder": "[PREDICT]",
                "task_type": "classification",
            },
            {
                "name": "PRICE",
                "prediction_placeholder": "[PREDICT]",
                "task_type": "regression",
            }
        ]
    },
    "index_column": "ID",
    "rows": [
        {
            "PRODUCT": "Couch",
            "PRICE": "[PREDICT]",
            "ORDERDATE": "28-11-2025",
            "ID": "35",
            "COSTCENTER": "[PREDICT]",
        },
        {
            "PRODUCT": "Office Chair",
            "PRICE": 150.8,
            "ORDERDATE": "02-11-2025",
            "ID": "44",
            "COSTCENTER": "Office Furniture",
        },
        {
            "PRODUCT": "Server Rack",
            "PRICE": 210.0,
            "ORDERDATE": "01-11-2025",
            "ID": "108",
            "COSTCENTER": "Data Infrastructure",
        },
        {
            "PRODUCT": "Server Rack",
            "PRICE": "[PREDICT]",
            "ORDERDATE": "01-11-2025",
            "ID": "104",
            "COSTCENTER": "[PREDICT]",
        }
    ],
    "data_schema": {
        "PRODUCT": {"dtype": "string"},
        "PRICE": {"dtype": "numeric"},
        "ORDERDATE": {"dtype": "date"},
        "ID": {"dtype": "string"},
        "COSTCENTER": {"dtype": "string"},
    }
}

# Make the prediction request
access_token = token["access_token"]
resource_group = "default"

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json",
    "AI-Resource-Group": resource_group
}

# Send the POST request to the deployment URL
response = requests.post(
    deployment_url, json=json_payload, headers=headers
)
print("Response status code:", response.status_code)
print("Response JSON:", response.json())
