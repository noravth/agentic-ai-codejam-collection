# https://community.sap.com/t5/artificial-intelligence-blogs-posts/sap-rpt-1-a-step-by-step-guide-on-getting-started/ba-p/14290171
# https://help.sap.com/docs/sap-ai-core/generative-ai-hub/consume-large-language-models-using-sap-ai-core

import os
import requests

class RPT1Client:
    def __init__(self):
        # Read env vars (assume dotenv already loaded in main)
        self.client_id = os.getenv("AICORE_CLIENT_ID")
        self.client_secret = os.getenv("AICORE_CLIENT_SECRET")
        self.auth_url = os.getenv("AICORE_AUTH_URL")
        self.deployment_url = os.getenv("RPT1_DEPLOYMENT_URL")
        self.token = self._fetch_token()
        self.resource_group = os.getenv("AICORE_RESOURCE_GROUP", "default")

    # Function to fetch OAuth token
    def _fetch_token(auth_url: str | None = None, client_id: str | None = None, client_secret: str | None = None, timeout: int = 30) -> dict:
        auth_url = os.getenv("AICORE_AUTH_URL")
        if not auth_url:
            raise ValueError("AICORE_AUTH_URL must be provided (env or arg).")
        client_id = os.getenv("AICORE_CLIENT_ID")
        if not client_id:
            raise ValueError("AICORE_CLIENT_ID must be provided (env or arg).")
        client_secret = os.getenv("AICORE_CLIENT_SECRET")
        if not client_secret:
            raise ValueError("AICORE_CLIENT_SECRET must be provided (env or arg).")
        data = {
            "grant_type": "client_credentials",
            "client_id": client_id,
            "client_secret": client_secret
        }
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        resp = requests.post(auth_url, data=data, headers=headers, timeout=timeout)
        resp.raise_for_status()
        token = resp.json()
        access_token = token["access_token"]
        return access_token

    def post_request(self, json_payload: dict, timeout: int = 60):
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
            "AI-Resource-Group": self.resource_group
        }

        # Send the POST request to the deployment URL
        response = requests.post(
            self.deployment_url, json=json_payload, headers=headers
        )
        return response
