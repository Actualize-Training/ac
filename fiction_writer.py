from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
llm = OpenAI()

assistant_message = "I'd love to write your next great novel for you! Tell me what you have in mind for the book."
user_input = input(f"\nAssistant: {assistant_message}\n\nUser: ")

history = [
    {"role": "developer", "content": "You are a best-selling fiction author, and write new stories for users."},
    {"role": "assistant", "content": assistant_message},
    {"role": "user", "content": user_input}
]

while user_input != "exit":
    response = llm.responses.create(
        model="gpt-4.1-mini",
        temperature=0,
        input=history,
    )

    llm_response_text = f"\nAssistant: {response.output_text}"
    print(llm_response_text)

    user_input = input("\nUser: ")
    history += [
        {"role": "assistant", "content": response.output_text},
        {"role": "user", "content": user_input}
    ]
