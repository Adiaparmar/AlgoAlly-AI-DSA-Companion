import os
from dotenv import load_dotenv
import requests

load_dotenv()

class OpenRouterAssistant:
    """Fast cloud-based assistant using OpenRouter API"""
    
    # Available free models for coding
    FREE_MODELS = {
        "KwaiPilot KAT Coder Pro (Free)": "kwaipilot/kat-coder-pro:free",
        "Qwen3 Coder (Free)": "qwen/qwen3-coder:free",
        "Olympic Coder 32B": "open-r1/olympiccoder-32b",
        "DeepSeek Chat (Cheap)": "deepseek/deepseek-chat"
    }
    
    def __init__(self, api_key=None, model="deepseek/deepseek-chat"):
        """
        Initialize OpenRouter assistant.
        
        Args:
            api_key (str, optional): OpenRouter API key
            model (str): Model to use. Default is DeepSeek Chat.
        """
        self.api_key = api_key or os.getenv("OPENROUTER_API_KEY")
        self.model = model
        self.base_url = "https://openrouter.ai/api/v1/chat/completions"
        
        if not self.api_key:
            raise ValueError("OpenRouter API key required. Get one at https://openrouter.ai/keys")
    
    def generate_response(self, system_prompt, user_prompt, temp=0.2):
        """
        Generate a response using OpenRouter API.
        
        Args:
            system_prompt (str): System instruction
            user_prompt (str): User's problem/question
            temp (float): Temperature (0.0-1.0)
        
        Returns:
            str: Generated response
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://github.com/yourusername/cp-companion",  # Optional
            "X-Title": "CP Companion"  # Optional
        }
        
        data = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            "temperature": temp,
            "max_tokens": 2000
        }
        
        try:
            response = requests.post(self.base_url, headers=headers, json=data, timeout=30)
            response.raise_for_status()
            
            result = response.json()
            return result["choices"][0]["message"]["content"]
            
        except requests.exceptions.RequestException as e:
            raise Exception(f"OpenRouter API error: {str(e)}")
        except KeyError:
            raise Exception(f"Unexpected API response format: {response.text}")

if __name__ == "__main__":
    # Test
    assistant = OpenRouterAssistant()
    print(assistant.generate_response(
        "You are a helpful coding assistant.",
        "Write a Python function to reverse a string"
    ))
