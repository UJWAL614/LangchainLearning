import os
import requests
from dotenv import load_dotenv

load_dotenv()
gemini_key = os.getenv("GEMIAIKEY")  # make sure your .env key name matches exactly

api_url = api_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent?key={gemini_key}"

if not gemini_key:
    raise SystemExit("GEMIAIKEY environment variable is not set. Please set it in your .env file.")

history = []


def ask_gemini(conversation) -> str:
    payload = {"contents": conversation}
    response = requests.post(api_url, json=payload, timeout=600)
    if response.status_code != 200:
        print("Server said:", response.text)  # shows the REAL reason for a 400
    response.raise_for_status()
    data = response.json()
    return data["candidates"][0]["content"]["parts"][0]["text"]


def main():
    print("Chat started. Type 'quit' to exit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting the chatbot. Goodbye!")
            break

        # Gemini needs "parts": [{"text": ...}], not "content"
        history.append({"role": "user", "parts": [{"text": user_input}]})

        try:
            response_text = ask_gemini(history)
        except requests.RequestException as e:
            print(f"Error occurred: {e}")
            history.pop()
            continue

        # Gemini's own role is "model", not "assistant"
        history.append({"role": "model", "parts": [{"text": response_text}]})

        print(f"Gemini: {response_text}\n")  # now INSIDE the loop


if __name__ == "__main__":
    main()