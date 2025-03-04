import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Configure OpenAI with API key
client = openai.Client(api_key=os.getenv('OPENAI_API_KEY'))

def get_llm_response(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error getting response: {str(e)}"
