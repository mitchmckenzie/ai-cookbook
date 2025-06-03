from vertex_client import get_vertex_openai_client
from dotenv import load_dotenv
import os

load_dotenv()
client = get_vertex_openai_client()


completion = client.chat.completions.create(
    model=os.getenv("GCP_MODEL_NAME"),
    messages=[
        {"role": "system", "content": "You're a helpful assistant."},
        {
            "role": "user",
            "content": "Write a limerick about the Python programming language.",
        },
    ],
)

response = completion.choices[0].message.content
print(response)
