import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
llm = OpenAI(
    api_key=os.getenv("ANTHROPIC_API_KEY"),  # Your Claude API key
    base_url="https://api.anthropic.com/v1/"  # the Claude API endpoint
)

assistant_message = "How can I help?"
user_input = input(f"\nAssistant: {assistant_message}\n\nUser: ")

history = [
    {"role": "developer", "content": "You are a chatbot that talks like a pirate."},
    {"role": "assistant", "content": assistant_message},
    {"role": "user", "content": user_input}
]

while user_input != "exit":
    response = llm.chat.completions.create(
        model="claude-haiku-4-5-20251001",
        temperature=0,
        messages=history,
    )

    llm_response_text = f"\nAssistant: {response.choices[0].message.content}"
    print(llm_response_text)

    user_input = input("\nUser: ")
    history += [
        {"role": "assistant", "content": response.choices[0].message.content},
        {"role": "user", "content": user_input}
    ]
