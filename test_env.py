import os 
from dotenv import load_dotenv

load_dotenv()

GEMIAIKEY = os.getenv("GEMIAIKEY")
GroqKEY = os.getenv("GroqKEY")
print("GEMIAIKEY:", GEMIAIKEY)
print("GroqKEY:", GroqKEY)