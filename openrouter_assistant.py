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
        # Validate API key format
        if not self.api_key or not self.api_key.strip():
            raise ValueError("API key is empty. Please enter your OpenRouter API key.")
        
        # Remove any whitespace
        api_key = self.api_key.strip()
        
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://github.com/Adiaparmar/AlgoAlly",
            "X-Title": "AlgoAlly - AI DSA Companion"
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
            
            # Handle specific error codes
            if response.status_code == 401:
                raise Exception(
                    "❌ Invalid API Key\n\n"
                    "Your OpenRouter API key is invalid or has expired.\n\n"
                    "Please:\n"
                    "1. Get a new key at https://openrouter.ai/keys\n"
                    "2. Make sure you copied the ENTIRE key (starts with 'sk-or-v1-')\n"
                    "3. Check for extra spaces before/after the key"
                )
            elif response.status_code == 402:
                raise Exception(
                    "❌ Insufficient Credits\n\n"
                    "Your OpenRouter account has no credits.\n\n"
                    "Please add credits at https://openrouter.ai/credits"
                )
            elif response.status_code == 429:
                raise Exception(
                    "❌ Rate Limit Exceeded\n\n"
                    "Too many requests. Please wait a moment and try again."
                )
            
            response.raise_for_status()
            
            result = response.json()
            return result["choices"][0]["message"]["content"]
            
        except requests.exceptions.Timeout:
            raise Exception("⏱️ Request timed out. Please try again.")
        except requests.exceptions.ConnectionError:
            raise Exception("🌐 Connection error. Please check your internet connection.")
        except requests.exceptions.RequestException as e:
            if "401" in str(e):
                raise Exception(
                    "❌ Invalid API Key\n\n"
                    "Please check your OpenRouter API key and try again.\n"
                    "Get a key at: https://openrouter.ai/keys"
                )
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
