# Vertex OpenAPI Client

A simple Python client for authenticating and connecting to Google Vertex AI OpenAPI endpoints using environment variables and Google credentials.

## Installation

From the root of your project, install the client in editable mode:

```bash
pip install -e ./vertex-client
```

Or, add `-e ./vertex-client` to your requirements.txt in any subproject.

> **Note:** Depending on where your requirements.txt is located, you may need to adjust the path to the `vertex-client` module. For example, if your requirements.txt is in a subdirectory, you might need to escape directories, such as `-e ../../vertex-client`, to reference the module at the project root.

## Usage

Set the following environment variables (in your `.env` or shell):
- `GCP_PROJECT_ID`
- `GCP_LOCATION`

Authenticate with Google Cloud (if you haven't already):

```bash
gcloud auth application-default login
```

This will allow the client to automatically use your application default credentials. You do not need to manually print or copy the access token.

Then, in your Python code:

```python
from vertex_client import get_vertex_openai_client

client = get_vertex_openai_client()
```

This will return an `openai.OpenAI` client configured for Vertex AI endpoints.

## Requirements
- `python-dotenv`
- `google-auth`
- `openai`

These are included in `vertex-client/requirements.txt` and will be installed automatically.
