import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate


load_dotenv()
api_key = os.getenv("GEMIAIKEY")
if not os.getenv("GEMIAIKEY"):
    raise SystemExit("GEMIAIKEY not found. Check your .env file.")
 
model = ChatGoogleGenerativeAI(model="gemini-3.5-flash", google_api_key=api_key)
 
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a concise assistant."),
        ("human", "Tell me one interesting fact about {topic}."),
    ]
)
 
# THIS is LCEL: chaining two components with |
# prompt runs first -> its output feeds straight into model
chain = prompt | model
 
if __name__ == "__main__":
    topic = input("Topic: ").strip() or "black holes"
 
    # .invoke() runs the WHOLE chain end to end
    raw_output = chain.invoke({"topic": topic})
 
    '''print("\n--- RAW output object ---")
    print(raw_output)
    print("Type:", type(raw_output))'''
 
    print("\n--- Just the text (.content) ---")
    if isinstance(raw_output.content,list):
        text_parts = []
        for item in raw_output.content:
            if isinstance(item, dict) and "text" in item:
                text_parts.append(item["text"])
        print("".join(text_parts))
    print(text_parts)