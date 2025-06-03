from setuptools import setup, find_packages

setup(
    name="vertex-client",
    version="0.1.0",
    description="Vertex OpenAPI client for Google Vertex AI endpoints.",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "python-dotenv",
        "google-auth",
        "openai"
    ],
    python_requires=">=3.8",
)
