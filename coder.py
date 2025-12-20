from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class CodeAssistant:
    """Local model assistant using HuggingFace transformers"""
    
    # Available local models
    LOCAL_MODELS = {
        "DeepSeek Coder 1.3B": "deepseek-ai/deepseek-coder-1.3b-instruct",
        "VibeThinker 1.5B": "WeiboAI/VibeThinker-1.5B",
        "Qwen2.5 Coder 1.5B": "Qwen/Qwen2.5-Coder-1.5B-Instruct"
    }
    
    def __init__(self, hf_token=None, model_name="deepseek-ai/deepseek-coder-1.3b-instruct"):
        """
        Initialize the Code Assistant with a local model.
        
        Args:
            hf_token (str, optional): HuggingFace API token. If not provided, 
                                     will try to load from HF_TOKEN environment variable.
            model_name (str): Model identifier from HuggingFace. Default is DeepSeek Coder.
        """
        self.MODEL_NAME = model_name
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        
        # Get token from parameter, environment variable, or None
        self.hf_token = hf_token or os.getenv("HF_TOKEN")
        
        if not self.hf_token:
            print("⚠️  No HuggingFace token provided. Using public access (may have limitations).")
        
        print(f"Loading {self.MODEL_NAME} on {self.device}...")
        
        self.tokenizer = AutoTokenizer.from_pretrained(
            self.MODEL_NAME, 
            trust_remote_code=True, 
            token=self.hf_token
        )
        self.tokenizer.pad_token = self.tokenizer.eos_token
        self.tokenizer.padding_side = "right"

        self.model = AutoModelForCausalLM.from_pretrained(
            self.MODEL_NAME, 
            device_map="auto", 
            trust_remote_code=True, 
            token=self.hf_token
        )
    
    def generate_response(self, system_prompt, user_prompt, temp=0.0):
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
        
        full_prompt = self.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        inputs = self.tokenizer(full_prompt, return_tensors="pt").to(self.model.device)

        with torch.no_grad():
            outputs = self.model.generate(
                **inputs, 
                max_new_tokens=1024, 
                do_sample=(temp > 0), 
                temperature=temp if temp > 0 else None,
                top_k=50, 
                eos_token_id=self.tokenizer.eos_token_id
            )
            
        return self.tokenizer.decode(outputs[0][len(inputs["input_ids"][0]):], skip_special_tokens=True)

if __name__ == "__main__":
    # Test run
    assistant = CodeAssistant()
    print(assistant.generate_response("You are a helpful coder.", "Print hello world in python"))