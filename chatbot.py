from typing import List,Dict    

class Chatbot:
    def __init__(self) -> None:
        self.history: List[Dict[str, str]] = []
    
    def ask(self, prompt: str) -> str:
        self.history.append({
            "role": "user",
            "content": prompt
        })

        response: str = f"You asked: {prompt}"

        self.history.append({
            "role": "assistant",
            "content": response
        })

        return response

bot = Chatbot()

answer: str = bot.ask("What is Python?")

print(answer)

print("\nConversation History:")
for entry in bot.history:
    print(f"{entry['role'].capitalize()}: {entry['content']}")