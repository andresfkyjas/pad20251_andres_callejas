import openai
import json
import os
from dotenv import load_dotenv


load_dotenv()

class ChatGPTClient:
    def __init__(self, config_path='config.json'):
        
        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
        self.model = config.get("model", "gpt-3.5-turbo")
        self.base_prompt = config.get("base_prompt", "")
        
        
        openai.api_key = os.getenv("MI_TOKEN")
    
    def send_request(self, message, additional_messages=None):
        """
        Envía una solicitud a la API de ChatGPT y retorna la respuesta.
        Se construye la conversación iniciando con el prompt base.
        """
        messages = []
        if self.base_prompt:
            messages.append({"role": "system", "content": self.base_prompt})
        messages.append({"role": "user", "content": message})
        
        
        if additional_messages:
            messages.extend(additional_messages)
            
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=messages
            )
            return response.choices[0].message.content.strip()
        except openai.OpenAIError as e:
            print("Error al llamar a la API:", e)
            return None