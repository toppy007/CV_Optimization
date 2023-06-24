import os
import openai

from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

class ChatGPTClient:
    def gpt_req_res(messages):

        model='gpt-3.5-turbo'

        response = openai.ChatCompletion.create(
            model=model, 
            messages=messages, 
            temperature=0.1, 
            top_p=1, 
            frequency_penalty=0, 
            presence_penalty=0
        )
        
        return response.choices[0].message['content']
    
    def chatGPT_append_builder(original_text, text_to_append):
        return chatGPT_script
        
