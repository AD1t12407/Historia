import json
from openai import OpenAI
import os
import sqlite3
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
sysPrompt = """You are a history  guide designed to output JSON. of format {
  "history": "String",
  "impEvents": [
    {
      "Year": "String",
      "Details": "String"
    }
  ]
}
 }"""
userPrompt = f"Tell me about the history of: ."

def callGPT3( systemPrompt=sysPrompt, userPrompt=userPrompt , loc=""):
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
    # whether the call failed ?
    print(content_str)
    with open('response.txt', 'w') as f:
        f.write(content_str)

    with open('response.json', 'w') as f:
        json.dump(content_dict, f, indent=4)

    return content_dict

if __name__ == "__main__":
    
    userPrompt = ""
    res = callGPT3( userPrompt=userPrompt, loc="Charminar")
    print(res)
