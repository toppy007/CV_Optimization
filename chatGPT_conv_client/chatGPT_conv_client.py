import os
import openai

from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

class ChatGPTConvClient:
    def gpt_ad_keyword_finder(message):

        model='gpt-3.5-turbo'

        response = openai.ChatCompletion.create(
            model=model, 
            messages=message, 
            temperature=0.8, 
            top_p=1, 
            frequency_penalty=0, 
            presence_penalty=0
        )

        return response.choices[0].message['content']
    
    def chatGPT_append_builder(original_text, text_to_append):
        return None
    
    def chatGPT_save_local():
        return None

        
