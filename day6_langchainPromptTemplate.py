import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate

load_dotenv()

# Option A: Explicitly pass api_key using your custom env variable name
api_key = os.getenv("GEMIAIKEY")

# Initialize the model correctly using 'api_key' and a valid model identifier
model = ChatGoogleGenerativeAI(
  model="gemini-3.5-flash",
    google_api_key=api_key
)

# 1. PromptTemplate setup (renamed variable to avoid shadowing)
my_prompt_template = PromptTemplate.from_template(
    "Explain the topic of {topic} in tone {tone} within {word_count} words."
) 

def run_prompt_template(topic: str, tone: str, word_count: int) -> int:
    filled_template = my_prompt_template.format(topic=topic, tone=tone, word_count=word_count)
    response = model.invoke(filled_template)
    content = response.content
    if isinstance(content, list):
        text_parts = []

        for item in content:
            if isinstance(item, dict) and "text" in item:
                text_parts.append(item["text"])

        return "".join(text_parts)

    return content

# 2. ChatPromptTemplate setup (renamed variable to avoid shadowing)
my_chat_prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("user", "Explain the topic of {topic} in tone {tone} within {word_count} words.")
])

def run_chat_prompt_template(topic: str, tone: str, word_count: int) -> str:
    filled_chat_prompt = my_chat_prompt_template.format_messages(topic=topic, tone=tone, word_count=word_count)
    response = model.invoke(filled_chat_prompt)
    content = response.content
    if isinstance(content, list):
        text_parts = []

        for item in content:
            if isinstance(item, dict) and "text" in item:
                text_parts.append(item["text"])

        return "".join(text_parts)

    return content
    
if __name__ == "__main__":
    topic = input("Enter the topic: ")
    tone = input("Enter the tone (e.g., formal, casual): ")
    word_count = int(input("Enter the word count: "))

    response1 = run_prompt_template(topic, tone, word_count)
    print("\nResponse using PromptTemplate:")
    print(response1)

    response2 = run_chat_prompt_template(topic, tone, word_count)
    print("\nResponse using ChatPromptTemplate:")
    print(response2)