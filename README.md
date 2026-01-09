# LLM-Powered Application

This project uses multiple APIs to power a local AI application using Docker. Make sure to follow the setup instructions below before running the app.

## ⚙️ Environment Setup

Before running the application, create a `.env` file in the root directory with the following environment variables:

```
OPENAI_API_KEY=
ANTHROPIC_API_KEY=
PINECONE_API_KEY=
LANGFUSE_SECRET_KEY=
LANGFUSE_PUBLIC_KEY=
LANGFUSE_BASE_URL=
```

> ⚠️ Replace each value with your actual API credentials.

## 🚀 Running the App

To build and run the app using Docker Compose:

```
docker compose build
docker compose run app
```

