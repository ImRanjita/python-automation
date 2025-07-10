import os
import openai
import langchain
from dotenv import load_dotenv
from langchain.llms import OpenAI

# Load the API key from .env file
load_dotenv()
api_key = os.getenv("OPENAI_KEY", None)

# Initialize OpenAI LLM with a temperature of 0.9 for randomness
llm = OpenAI(temperature=0.9, openai_api_key=api_key)

response=llm.predict("Suggest me a skill that is in demand?")
print(response)