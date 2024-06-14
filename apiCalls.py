import json
import os
import sqlite3
from openai import OpenAI
from dotenv import load_dotenv
from db import init_db, insert_into_db

# Load environment variables
load_dotenv()

# API key from environment variables
api_key = os.getenv('OPENAI_API_KEY')

# System and user prompts
sysPrompt = """You are a history guide designed to output JSON. of format {
"Place": "String",
"history": "String... 5 lines",
"Ecological Relevance": "String",
"timeline": [
  {
    "Year": "String",
    "Details": "String"
  }... 10 events(major)
]
}"""
userPrompt = f"Tell me about the history of: ."

# Function to call GPT-3 and retrieve historical data
def callGPT3(systemPrompt=sysPrompt, userPrompt=userPrompt, loc="", dataSave = False):
    client = OpenAI(api_key=api_key)
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": systemPrompt},
            {"role": "user", "content": userPrompt + loc},
        ]
    )

    content_str = response.choices[0].message.content
    content_dict = json.loads(content_str)

    # Print content
    print(content_str)

    # Save response as text
    with open('response.txt', 'w') as f:
        f.write(content_str)

    if dataSave == True:
        os.makedirs('./data', exist_ok=True)
        place_name = content_dict.get("Place", "unknown").replace(" ", "_").lower()
        json_path = os.path.join('./data', f'{place_name}.json')
    else:
        place_name = content_dict.get("Place", "unknown").replace(" ", "_").lower()
        json_path = os.path.join('response.json') 
    
    with open(json_path, 'w') as f:
        json.dump(content_dict, f, indent=4)
    
    print(f"Data saved to {json_path}")
    return content_str

# Main execution
if __name__ == "__main__":
    # Initialize the database
    init_db()
    
    # Example location to query
    
    popular_places = [
    "The Great Wall of China",
    "Machu Picchu",
    "The Colosseum",
    "The Pyramids of Giza",
    "The Taj Mahal",
    "Stonehenge",
    "The Acropolis",
    "Petra",
    "Chichen Itza",
    "Angkor Wat"
]
    
    # Call the function to retrieve data from GPT-3
    for location in popular_places:
        data = callGPT3(loc=location, dataSave=True)
    
    