import  requests
import os
from dotenv import load_dotenv
load_dotenv()
gemiai_key = os.getenv("GEMIAIKEY")

url =  f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent?key={gemiai_key}"

payload = {
    "contents": [
        {
            "parts": [
                {
                    "text": "Explain Python functions in simple words."
                }
            ]
        }
    ]
}

response = requests.post(url, json=payload)

data = response.json()

if response.status_code == 200:
    text = data["candidates"][0]["content"]["parts"][0]["text"]
    print("\nGemini:")
    print(text)
else:
    print("API Error:")
    print(data)

