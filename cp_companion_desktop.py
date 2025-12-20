import customtkinter as ctk
from tkinter import messagebox
import threading
from coder import CodeAssistant
from openrouter_assistant import OpenRouterAssistant
import os

# ============================================================================
# APPEARANCE CONFIGURATION
# ============================================================================
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Custom Colors (matching Streamlit theme)
COLORS = {
    'bg_primary': '#0d1117',
    'bg_secondary': '#161b22',
    'bg_tertiary': '#21262d',
    'border': '#30363d',
    'text_primary': '#e6edf3',
    'text_secondary': '#7d8590',
    'accent_blue': '#58a6ff',
    'accent_green': '#3fb950',
    'accent_green_hover': '#2ea043',
    'accent_red': '#f85149',
    'accent_orange': '#d29922'
}

class AlgoAllyApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Window configuration
        self.title("🧩 AlgoAlly - AI DSA Companion")
        self.geometry("1400x850")
        self.minsize(1000, 650)
        self.configure(fg_color=COLORS['bg_primary'])
        
        # State
        self.assistant = None
        self.is_generating = False
        
        # Create UI
        self.create_widgets()
        
    def create_widgets(self):
        # Main container
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        # ===== SIDEBAR =====
        self.create_sidebar()
        
        # ===== MAIN CONTENT =====
        self.create_main_content()
        
    def create_sidebar(self):
        """Create the left sidebar with all controls"""
        self.sidebar = ctk.CTkFrame(
            self, 
            width=330, 
            corner_radius=0,
            fg_color=COLORS['bg_secondary']
        )
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.grid_propagate(False)
        
        # Scrollable frame for sidebar content
        self.sidebar_scroll = ctk.CTkScrollableFrame(
            self.sidebar,
            fg_color="transparent"
        )
        self.sidebar_scroll.pack(fill="both", expand=True, padx=0, pady=0)
        
        # Header
        header_frame = ctk.CTkFrame(self.sidebar_scroll, fg_color="transparent")
        header_frame.pack(fill="x", padx=20, pady=(20, 10))
        
        ctk.CTkLabel(
            header_frame,
            text="🧩 AlgoAlly",
            font=ctk.CTkFont(size=32, weight="bold"),
            text_color=COLORS['accent_blue']
        ).pack()
        
        ctk.CTkLabel(
            header_frame,
            text="AI DSA Companion",
            font=ctk.CTkFont(size=13),
            text_color=COLORS['text_secondary']
        ).pack(pady=(2, 0))
        
        # Divider
        ctk.CTkFrame(
            self.sidebar_scroll,
            height=2,
            fg_color=COLORS['border']
        ).pack(fill="x", padx=20, pady=15)
        
        # Backend Selection
        backend_frame = ctk.CTkFrame(self.sidebar_scroll, fg_color="transparent")
        backend_frame.pack(fill="x", padx=20, pady=(0, 15))
        
        ctk.CTkLabel(
            backend_frame,
            text="⚙️ Backend",
            font=ctk.CTkFont(size=14, weight="bold"),
            anchor="w"
        ).pack(fill="x", pady=(0, 8))
        
        self.backend_var = ctk.StringVar(value="openrouter")
        
        ctk.CTkRadioButton(
            backend_frame,
            text="⚡ OpenRouter (Cloud)",
            variable=self.backend_var,
            value="openrouter",
            command=self.on_backend_change,
            font=ctk.CTkFont(size=12)
        ).pack(anchor="w", pady=3)
        
        ctk.CTkRadioButton(
            backend_frame,
            text="🔒 Local Model (Private)",
            variable=self.backend_var,
            value="local",
            command=self.on_backend_change,
            font=ctk.CTkFont(size=12)
        ).pack(anchor="w", pady=3)
        
        # Model Selection
        model_frame = ctk.CTkFrame(self.sidebar_scroll, fg_color="transparent")
        model_frame.pack(fill="x", padx=20, pady=(0, 15))
        
        ctk.CTkLabel(
            model_frame,
            text="🤖 Model",
            font=ctk.CTkFont(size=14, weight="bold"),
            anchor="w"
        ).pack(fill="x", pady=(0, 8))
        
        # OpenRouter models dropdown
        self.openrouter_models = list(OpenRouterAssistant.FREE_MODELS.keys())
        self.openrouter_model_dropdown = ctk.CTkComboBox(
            model_frame,
            values=self.openrouter_models,
            width=280,
            font=ctk.CTkFont(size=12),
            state="readonly",
            fg_color=COLORS['bg_tertiary'],
            border_color=COLORS['border']
        )
        self.openrouter_model_dropdown.set(self.openrouter_models[0])
        self.openrouter_model_dropdown.pack(fill="x")
        
        # Local models dropdown (initially hidden)
        self.local_models = list(CodeAssistant.LOCAL_MODELS.keys())
        self.local_model_dropdown = ctk.CTkComboBox(
            model_frame,
            values=self.local_models,
            width=280,
            font=ctk.CTkFont(size=12),
            state="readonly",
            fg_color=COLORS['bg_tertiary'],
            border_color=COLORS['border']
        )
        self.local_model_dropdown.set(self.local_models[0])
        
        # API Key Input
        api_frame = ctk.CTkFrame(self.sidebar_scroll, fg_color="transparent")
        api_frame.pack(fill="x", padx=20, pady=(0, 15))
        
        self.token_label = ctk.CTkLabel(
            api_frame,
            text="🔐 API Key",
            font=ctk.CTkFont(size=14, weight="bold"),
            anchor="w"
        )
        self.token_label.pack(fill="x", pady=(0, 8))
        
        self.token_entry = ctk.CTkEntry(
            api_frame,
            placeholder_text="sk-or-v1-...",
            show="*",
            width=280,
            height=36,
            font=ctk.CTkFont(size=12),
            fg_color=COLORS['bg_tertiary'],
            border_color=COLORS['border']
        )
        self.token_entry.pack(fill="x")
        
        # Load Model Button
        self.load_btn = ctk.CTkButton(
            self.sidebar_scroll,
            text="⚡ Connect",
            command=self.load_model_thread,
            fg_color=COLORS['accent_green'],
            hover_color=COLORS['accent_green_hover'],
            height=42,
            font=ctk.CTkFont(size=14, weight="bold"),
            corner_radius=8
        )
        self.load_btn.pack(fill="x", padx=20, pady=(0, 10))
        
        # Status
        self.status_label = ctk.CTkLabel(
            self.sidebar_scroll,
            text="⚪ Not Connected",
            font=ctk.CTkFont(size=11),
            text_color=COLORS['text_secondary']
        )
        self.status_label.pack(pady=(0, 15))
        
        # Divider
        ctk.CTkFrame(
            self.sidebar_scroll,
            height=2,
            fg_color=COLORS['border']
        ).pack(fill="x", padx=20, pady=15)
        
        # Mode Selection
        mode_frame = ctk.CTkFrame(self.sidebar_scroll, fg_color="transparent")
        mode_frame.pack(fill="x", padx=20, pady=(0, 15))
        
        ctk.CTkLabel(
            mode_frame,
            text="💭 Assistant Mode",
            font=ctk.CTkFont(size=14, weight="bold"),
            anchor="w"
        ).pack(fill="x", pady=(0, 8))
        
        self.mode_var = ctk.StringVar(value="hint")
        
        modes = [
            ("🔍 Hint Only", "hint"),
            ("🧪 Test Cases", "test"),
            ("⚠️Complexity", "complexity"),
            ("💡 Algorithm Idea", "idea"),
            ("💻 Full Solution", "code")
        ]
        
        for text, value in modes:
            ctk.CTkRadioButton(
                mode_frame,
                text=text,
                variable=self.mode_var,
                value=value,
                font=ctk.CTkFont(size=12)
            ).pack(anchor="w", pady=3)
        
        # Temperature Slider
        temp_frame = ctk.CTkFrame(self.sidebar_scroll, fg_color="transparent")
        temp_frame.pack(fill="x", padx=20, pady=(15, 15))
        
        self.temp_label = ctk.CTkLabel(
            temp_frame,
            text="🎛️ Temperature: 0.2",
            font=ctk.CTkFont(size=12),
            anchor="w"
        )
        self.temp_label.pack(fill="x", pady=(0, 8))
        
        self.temp_slider = ctk.CTkSlider(
            temp_frame,
            from_=0.0,
            to=1.0,
            number_of_steps=10,
            command=self.update_temp_label,
            fg_color=COLORS['border'],
            progress_color=COLORS['accent_blue']
        )
        self.temp_slider.set(0.2)
        self.temp_slider.pack(fill="x")
        
        # Footer
        ctk.CTkLabel(
            self.sidebar_scroll,
            text="💡 Tip: Start with hints!",
            font=ctk.CTkFont(size=11),
            text_color=COLORS['text_secondary'],
            wraplength=260
        ).pack(pady=20)
        
    def create_main_content(self):
        """Create the main content area"""
        self.main_frame = ctk.CTkFrame(
            self,
            corner_radius=0,
            fg_color=COLORS['bg_primary']
        )
        self.main_frame.grid(row=0, column=1, sticky="nsew", padx=0, pady=0)
        self.main_frame.grid_rowconfigure(1, weight=1)
        self.main_frame.grid_rowconfigure(3, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)
        
        # Header
        header = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        header.grid(row=0, column=0, sticky="ew", padx=30, pady=(25, 15))
        
        ctk.CTkLabel(
            header,
            text="📝 Problem Input",
            font=ctk.CTkFont(size=20, weight="bold"),
            text_color=COLORS['text_primary']
        ).pack(anchor="w")
        
        # Input Text Area
        self.input_text = ctk.CTkTextbox(
            self.main_frame,
            font=ctk.CTkFont(size=12),
            wrap="word",
            fg_color=COLORS['bg_secondary'],
            border_color=COLORS['border'],
            border_width=1
        )
        self.input_text.grid(row=1, column=0, sticky="nsew", padx=30, pady=(0, 15))
        self.input_text.insert("1.0", "Paste your competitive programming problem here...\n\nExample:\nGiven an array of integers and a target sum, find two numbers that add up to the target.\n\nInput: nums = [2,7,11,15], target = 9\nOutput: [0,1]")
        
        # Generate Button
        self.generate_btn = ctk.CTkButton(
            self.main_frame,
            text="🚀 Generate Response",
            command=self.generate_response_thread,
            height=50,
            font=ctk.CTkFont(size=16, weight="bold"),
            fg_color=COLORS['accent_green'],
            hover_color=COLORS['accent_green_hover'],
            corner_radius=8
        )
        self.generate_btn.grid(row=2, column=0, padx=30, pady=(0, 15), sticky="ew")
        
        # Output Header
        output_header = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        output_header.grid(row=3, column=0, sticky="ew", padx=30, pady=(0, 10))
        
        ctk.CTkLabel(
            output_header,
            text="🤖 AI Response",
            font=ctk.CTkFont(size=20, weight="bold"),
            text_color=COLORS['text_primary']
        ).pack(anchor="w")
        
        # Output Text Area
        self.output_text = ctk.CTkTextbox(
            self.main_frame,
            font=ctk.CTkFont(size=13),
            wrap="word",
            fg_color=COLORS['bg_secondary'],
            border_color=COLORS['border'],
            border_width=1
        )
        self.output_text.grid(row=4, column=0, sticky="nsew", padx=30, pady=(0, 25))
        self.output_text.insert("1.0", "Your AI response will appear here...")
        self.output_text.configure(state="disabled")
        
    def update_temp_label(self, value):
        """Update temperature label"""
        self.temp_label.configure(text=f"🎛️ Temperature: {float(value):.1f}")
    
    def on_backend_change(self):
        """Handle backend selection change"""
        backend = self.backend_var.get()
        
        if backend == "openrouter":
            # Show OpenRouter dropdown, hide Local
            self.openrouter_model_dropdown.pack(fill="x")
            self.local_model_dropdown.pack_forget()
            
            self.token_label.configure(text="🔐 OpenRouter API Key")
            self.token_entry.configure(placeholder_text="sk-or-v1-...")
            self.load_btn.configure(text="⚡ Connect to OpenRouter")
            self.status_label.configure(text="⚪ Not Connected")
        else:
            # Show Local dropdown, hide OpenRouter
            self.local_model_dropdown.pack(fill="x")
            self.openrouter_model_dropdown.pack_forget()
            
            self.token_label.configure(text="🔐 HF Token (Optional)")
            self.token_entry.configure(placeholder_text="hf_...")
            self.load_btn.configure(text="⚡ Load Local Model")
            self.status_label.configure(text="⚪ Model Not Loaded")
        
        # Reset assistant
        if self.assistant is not None:
            self.assistant = None
            self.load_btn.configure(state="normal")
    
    def load_model_thread(self):
        """Load model in background thread"""
        if self.assistant is not None:
            messagebox.showinfo("Info", "Already connected!")
            return
        
        thread = threading.Thread(target=self.load_model, daemon=True)
        thread.start()
    
    def load_model(self):
        """Load the model/connect to API"""
        backend = self.backend_var.get()
        self.load_btn.configure(state="disabled", text="Connecting...")
        self.status_label.configure(text="🟡 Connecting...", text_color=COLORS['accent_orange'])
        
        try:
            token = self.token_entry.get().strip() or None
            
            if backend == "openrouter":
                selected_model_name = self.openrouter_model_dropdown.get()
                model_id = OpenRouterAssistant.FREE_MODELS[selected_model_name]
                
                self.assistant = OpenRouterAssistant(api_key=token, model=model_id)
                self.status_label.configure(
                    text=f"🟢 {selected_model_name}",
                    text_color=COLORS['accent_green']
                )
                self.load_btn.configure(text="✓ Connected")
                messagebox.showinfo(
                    "Success",
                    f"Connected to {selected_model_name}! ⚡\n\nResponses will be fast (2-5s)"
                )
            else:
                selected_model_name = self.local_model_dropdown.get()
                model_id = CodeAssistant.LOCAL_MODELS[selected_model_name]
                
                self.assistant = CodeAssistant(hf_token=token, model_name=model_id)
                self.status_label.configure(
                    text=f"🟢 {selected_model_name}",
                    text_color=COLORS['accent_green']
                )
                self.load_btn.configure(text="✓ Model Loaded")
                messagebox.showinfo(
                    "Success",
                    f"{selected_model_name} loaded! 🔒\n\nNote: Generation may take 60-300s on CPU."
                )
            
        except Exception as e:
            self.status_label.configure(
                text="🔴 Connection Failed",
                text_color=COLORS['accent_red']
            )
            self.load_btn.configure(state="normal", text="⚡ Retry Connection")
            messagebox.showerror("Error", f"Failed to connect:\n{str(e)}")
    
    def generate_response_thread(self):
        """Generate response in background thread"""
        if self.assistant is None:
            messagebox.showwarning("Warning", "Please connect to a model first!")
            return
        
        if self.is_generating:
            messagebox.showinfo("Info", "Already generating...")
            return
        
        thread = threading.Thread(target=self.generate_response, daemon=True)
        thread.start()
    
    def generate_response(self):
        """Generate AI response"""
        self.is_generating = True
        self.generate_btn.configure(state="disabled", text="🤔 Thinking...")
        
        try:
            problem = self.input_text.get("1.0", "end-1c").strip()
            
            if not problem:
                messagebox.showwarning("Warning", "Please enter a problem!")
                return
            
            # Mode prompts
            MODE_PROMPTS = {
                "hint": "Give ONE high-level hint (e.g., 'Use Two Pointers'). NO code. Keep under 2 sentences.",
                "test": "Generate 5 test cases: basic, edge, large, negative, corner case. Show input/output.",
                "complexity": "Analyze time/space complexity. Explain WHY (e.g., 'O(N) because single pass').",
                "idea": "Explain algorithm in plain English, step by step. NO code.",
                "code": "Write optimal C++/Python solution with comments and complexity notes."
            }
            
            mode = self.mode_var.get()
            system_prompt = MODE_PROMPTS[mode]
            temp = self.temp_slider.get()
            
            # Generate
            import time
            start = time.time()
            response = self.assistant.generate_response(system_prompt, problem, temp=temp)
            elapsed = time.time() - start
            
            # Display
            self.output_text.configure(state="normal")
            self.output_text.delete("1.0", "end")
            self.output_text.insert("1.0", response)
            self.output_text.insert("end", f"\n\n✨ Generated in {elapsed:.1f}s")
            self.output_text.configure(state="disabled")
            
        except Exception as e:
            messagebox.showerror("Error", f"Generation failed:\n{str(e)}")
        
        finally:
            self.is_generating = False
            self.generate_btn.configure(state="normal", text="🚀 Generate Response")

if __name__ == "__main__":
    app = AlgoAllyApp()
    app.mainloop()
