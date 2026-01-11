# Let's Build LLM-Powered Apps!

Here are the setup instructions:

## ⚙️ Environment Setup

Before running the application, create a `.env` file in the root directory with the following environment variables:

```
OPENAI_API_KEY=
ANTHROPIC_API_KEY=
PINECONE_API_KEY=
LANGFUSE_SECRET_KEY=
LANGFUSE_PUBLIC_KEY=
LANGFUSE_BASE_URL="http://langfuse-web:3000"
```

> ⚠️ Replace each value with your actual API credentials. At a minimum, fill in the `OPENAI_API_KEY`

## 🚀 Running the Scripts

To build and run the Python scripts using Docker:

```
docker compose build
docker compose run app
```

To check if everything is working, run:

```
python chatbot_00.py
```

If you get some juicy info about George Washington, you should be good to go!

## Running Langfuse locally

In a separate terminal tab, run:

```
docker compose up
```

Be patient, as this may take a few minutes to boot up. If you get an error message saying `address already in use`, this might be fixed by changing the line `- 127.0.0.1:5432:5432` to `- 127.0.0.1:5433:5432`.

Once you're booted up, follow these steps:

1. Direct your web browser to `localhost:3000`.
2. Sign up for a new Langfuse account.
3. Create a new "organization".
4. Create a new "project" within that organization.
5. Create API keys.
6. Place the API keys (`LANGFUSE_SECRET_KEY` and `LANGFUSE_PUBLIC_KEY`) inside your `.env` file. **NOTE**: You'll be told by Langfuse to set your `LANGFUSE_BASE_URL` to `localhost...`. *Don't do this!* Leave this set to `http://langfuse-web:3000`.

To test Langfuse out, run `python chatbot_19_langfuse.py` and ask the chatbot a query. Then, head to the Langfuse dashboard to see whether a trace shows up. (On the left-hand side of the screen, you'll see a link called "Tracing".) If you see a trace, it worked!