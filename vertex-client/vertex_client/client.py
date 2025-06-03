import os
from dotenv import load_dotenv
from google.auth import default
import google.auth.transport.requests
from openai import OpenAI

def get_vertex_openai_client():
    """
    Loads environment variables and returns an OpenAI client configured for Vertex AI OpenAPI endpoints.
    Requires:
      - GCP_PROJECT_ID
      - GCP_LOCATION
    """
    load_dotenv()
    project_id = os.getenv('GCP_PROJECT_ID')
    location = os.getenv('GCP_LOCATION')
    if not project_id or not location:
        raise ValueError("GCP_PROJECT_ID and GCP_LOCATION must be set in the environment or .env file.")

    credentials, _ = default(scopes=["https://www.googleapis.com/auth/cloud-platform"])
    credentials.refresh(google.auth.transport.requests.Request())

    base_url = (
        f"https://{location}-aiplatform.googleapis.com/v1/projects/"
        f"{project_id}/locations/{location}/endpoints/openapi"
    )

    client = OpenAI(
        base_url=base_url,
        api_key=credentials.token,
    )
    return client
