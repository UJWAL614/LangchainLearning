import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

gemini_key = os.getenv("GEMIAIKEY")  # Make sure .env key name matches exactly

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    google_api_key=gemini_key
)

history = []


def ask_gemini(conversation):
    response = llm.invoke(conversation)
    content = response.content

    if isinstance(content, list):
        text_parts = []

        for item in content:
            if isinstance(item, dict) and "text" in item:
                text_parts.append(item["text"])

        return "".join(text_parts)

    return content


def main():
    print("Chat started. Type 'quit' to exit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Exiting the chatbot. Goodbye!")
            break

        # Add user's message to conversation history
        history.append(HumanMessage(content=user_input))

        try:
            response_text = ask_gemini(history)

        except Exception as e:
            print(f"Error occurred: {e}")

            # Remove user's message if API call fails
            history.pop()
            continue

        # Add Gemini's response to conversation history
        history.append(AIMessage(content=response_text))

        print(f"Gemini: {response_text}\n")


if __name__ == "__main__":
    main()