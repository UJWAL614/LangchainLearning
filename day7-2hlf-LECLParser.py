"""
Day 4 - Output Parsers
 
Part 1: StrOutputParser  -> prompt | model | parser gives you a plain
        string directly, instead of an AIMessage object with .content.
 
Part 2: Structured output -> force the model's reply into a Pydantic
        object (a Recipe with name + ingredients), instead of free text.
 
Requires: pip install langchain langchain-google-genai python-dotenv pydantic
.env must contain: GOOGLE_API_KEY=your-key-here
"""


import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI   
from langchain_core.prompts import ChatPromptTemplate
from typing import List, Dict, Any
from pydantic import BaseModel,Field
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
api_key = os.getenv("GEMIAIKEY")

model = ChatGoogleGenerativeAI(model="gemini-3.5-flash", google_api_key=api_key)

chat_prompt = ChatPromptTemplate.from_messages(
    [ ("system", "You are a concise assistant."), 
      ("human", "Tell me one interesting fact about {topic}.") ])
string_output_parser = chat_prompt | model | StrOutputParser()

def get_interesting_fact(topic: str) -> str:
    raw_output = string_output_parser.invoke({"topic": topic})      
    return raw_output

class Recipe(BaseModel):
    name: str = Field(..., description="Name of the recipe")
    ingredients: List[str] = Field(..., description="List of ingredients")

recipe_prompt = ChatPromptTemplate.from_messages(
    [ ("system", "You are a helpful assistant that provides recipes."), 
      ("human", "Provide a recipe for {dish} in JSON format with 'name' and 'ingredients'.") ])
structuredModel = model.with_structured_output(Recipe)
recipe_chain = recipe_prompt | structuredModel

def get_recipe(dish: str) -> Recipe:
    # Returns an actual Recipe OBJECT, not a string — you can access
    # result.name and result.ingredients directly, like a normal Python object
    return recipe_chain.invoke({"dish": dish})
 
if __name__ == "__main__":
    topic = input("Topic: ").strip() or "black holes"
    fact = get_interesting_fact(topic)
    print(f"Interesting fact about {topic}: {fact}")

    dish = input("Dish: ").strip() or "pasta"
    recipe = get_recipe(dish)
    print(f"Recipe for {dish}:")
    print(f"  Name: {recipe.name}")
    print(f"  Ingredients: {', '.join(recipe.ingredients)}")