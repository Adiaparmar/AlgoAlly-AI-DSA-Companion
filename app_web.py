import streamlit as st
import time
from openrouter_assistant import OpenRouterAssistant

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================
st.set_page_config(
    page_title="AlgoAlly - AI DSA Companion",
    page_icon="🧩",
    layout="wide",
    initial_sidebar_state="collapsed"  # Collapsed by default for mobile
)

# ============================================================================
# MOBILE-FRIENDLY DARK THEME
# ============================================================================
st.markdown("""
<style>
    /* Root Variables */
    :root {
        --bg-primary: #0d1117;
        --bg-secondary: #161b22;
        --bg-tertiary: #21262d;
        --border-color: #30363d;
        --text-primary: #e6edf3;
        --text-secondary: #7d8590;
        --accent-blue: #58a6ff;
        --accent-green: #3fb950;
        --accent-orange: #d29922;
        --accent-red: #f85149;
    }
    
    /* Global Background */
    .main, .block-container, 
    [data-testid="stAppViewContainer"],
    .stApp {
        background-color: var(--bg-primary) !important;
        color: var(--text-primary) !important;
    }
    
    /* Hide Header */
    [data-testid="stHeader"],
    [data-testid="stToolbar"] {
        display: none !important;
    }
    
    /* Mobile-optimized padding */
    .main > div {
        padding: 1rem !important;
    }
    
    .block-container {
        padding-top: 1rem !important;
        max-width: 100% !important;
    }
    
    /* Mobile: Reduce padding on small screens */
    @media (max-width: 768px) {
        .main > div {
            padding: 0.5rem !important;
        }
        
        .block-container {
            padding: 0.5rem !important;
        }
    }
    
    /* Typography */
    h1 {
        color: var(--accent-blue) !important;
        font-weight: 700 !important;
        font-size: 2rem !important;
        margin-bottom: 0.5rem !important;
    }
    
    @media (max-width: 768px) {
        h1 {
            font-size: 1.5rem !important;
        }
    }
    
    h2, h3 {
        color: var(--text-primary) !important;
        font-weight: 600 !important;
    }
    
    p, span, div, label, li {
        color: var(--text-primary) !important;
    }
    
    /* Inputs */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        background-color: var(--bg-secondary) !important;
        color: var(--text-primary) !important;
        border: 1px solid var(--border-color) !important;
        border-radius: 8px !important;
    }
    
    .stTextInput > div > div > input::placeholder,
    .stTextArea > div > div > textarea::placeholder {
        color: var(--text-secondary) !important;
    }
    
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {
        border-color: var(--accent-blue) !important;
        box-shadow: 0 0 0 3px rgba(88, 166, 255, 0.15) !important;
    }
    
    /* Selectbox */
    .stSelectbox > div > div,
    div[data-baseweb="select"] > div {
        background-color: var(--bg-secondary) !important;
        border: 1px solid var(--border-color) !important;
        border-radius: 8px !important;
        color: var(--text-primary) !important;
    }
    
    ul[role="listbox"] {
        background-color: var(--bg-secondary) !important;
        border: 1px solid var(--border-color) !important;
    }
    
    ul[role="listbox"] > li {
        background-color: var(--bg-secondary) !important;
        color: var(--text-primary) !important;
    }
    
    ul[role="listbox"] > li:hover {
        background-color: var(--bg-tertiary) !important;
        color: var(--accent-blue) !important;
    }
    
    /* Radio Buttons */
    .stRadio label {
        color: var(--text-primary) !important;
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #238636 0%, #2ea043 100%) !important;
        color: white !important;
        border-radius: 8px !important;
        border: none !important;
        padding: 0.75rem 1.5rem !important;
        font-weight: 600 !important;
        box-shadow: 0 4px 12px rgba(35, 134, 54, 0.3) !important;
        transition: all 0.3s ease !important;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #2ea043 0%, #3fb950 100%) !important;
        transform: translateY(-2px) !important;
    }
    
    /* Alerts */
    .stSuccess, .stWarning, .stError, .stInfo {
        background-color: var(--bg-secondary) !important;
        border-radius: 8px !important;
        padding: 1rem !important;
    }
    
    .stSuccess { border-left: 4px solid var(--accent-green) !important; }
    .stWarning { border-left: 4px solid var(--accent-orange) !important; }
    .stError { border-left: 4px solid var(--accent-red) !important; }
    .stInfo { border-left: 4px solid var(--accent-blue) !important; }
    
    /* Expander */
    .streamlit-expanderHeader {
        background-color: var(--bg-tertiary) !important;
        border-radius: 8px !important;
        color: var(--text-primary) !important;
        padding: 0.75rem 1rem !important;
    }
    
    /* Code blocks */
    code {
        background-color: var(--bg-tertiary) !important;
        color: var(--accent-blue) !important;
        padding: 0.2rem 0.4rem !important;
        border-radius: 4px !important;
    }
    
    pre {
        background-color: var(--bg-tertiary) !important;
        border: 1px solid var(--border-color) !important;
        border-radius: 8px !important;
        padding: 1rem !important;
    }
    
    /* Compact spacing for mobile */
    @media (max-width: 768px) {
        .element-container {
            margin-bottom: 0.5rem !important;
        }
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# CACHED RESOURCE LOADERS
# ============================================================================
@st.cache_resource
def load_openrouter_assistant(_api_key, _model):
    """Load OpenRouter assistant with caching."""
    return OpenRouterAssistant(api_key=_api_key, model=_model)

# ============================================================================
# HEADER
# ============================================================================
st.title("🧩 AlgoAlly")
st.caption("Your AI partner for competitive programming")

# Security notice
st.info("🔒 **Privacy**: Your API key is only used in your session and never stored. [Open source on GitHub](https://github.com/yourusername/AlgoAlly)")

st.markdown("---")

# ============================================================================
# CONFIGURATION (IN MAIN AREA - MOBILE FRIENDLY)
# ============================================================================
with st.expander("⚙️ **Configuration** (Click to expand)", expanded=False):
    config_col1, config_col2 = st.columns([1, 1])
    
    with config_col1:
        st.markdown("#### 🤖 Model")
        openrouter_models = OpenRouterAssistant.FREE_MODELS
        selected_model_name = st.selectbox(
            "Select model:",
            list(openrouter_models.keys()),
            help="All models are free or very cheap!",
            label_visibility="collapsed"
        )
        selected_model_id = openrouter_models[selected_model_name]
        
        st.markdown("#### 💭 Mode")
        mode = st.radio(
            "Assistant mode:",
            [
                "🔍 Hint Only",
                "🧪 Test Cases",
                "⚠️ Complexity",
                "💡 Algorithm Idea",
                "💻 Full Solution"
            ],
            label_visibility="collapsed",
            help="Choose what type of help you want"
        )
    
    with config_col2:
        st.markdown("#### 🔐 API Key")
        api_key = st.text_input(
            "OpenRouter API key:",
            type="password",
            placeholder="sk-or-v1-...",
            help="Get free key at https://openrouter.ai/keys",
            label_visibility="collapsed"
        )
        
        if not api_key:
            st.warning("⚠️ Enter API key above")
        
        st.markdown("#### 🎛️ Temperature")
        temp = st.slider(
            "Creativity:",
            0.0, 1.0, 0.2, 0.1,
            help="Lower = focused, Higher = creative",
            label_visibility="collapsed"
        )
    
    st.markdown("---")
    st.caption("💡 **Tip:** Start with hints! • [Get API Key](https://openrouter.ai/keys) • [Desktop App](https://github.com/yourusername/AlgoAlly/releases)")

# Quick config bar (always visible)
st.markdown("**Quick Settings:**")
quick_col1, quick_col2, quick_col3 = st.columns([2, 2, 1])

with quick_col1:
    # API key input (compact)
    if 'api_key' not in locals() or not api_key:
        api_key = st.text_input(
            "🔐 API Key",
            type="password",
            placeholder="sk-or-v1-...",
            key="quick_api_key"
        )

with quick_col2:
    # Model selector (compact)
    if 'selected_model_name' not in locals():
        openrouter_models = OpenRouterAssistant.FREE_MODELS
        selected_model_name = st.selectbox(
            "🤖 Model",
            list(openrouter_models.keys()),
            key="quick_model"
        )
        selected_model_id = openrouter_models[selected_model_name]

with quick_col3:
    # Mode selector (compact)
    if 'mode' not in locals():
        mode_short = st.selectbox(
            "� Mode",
            ["Hint", "Tests", "Complexity", "Idea", "Code"],
            key="quick_mode"
        )
        mode_map = {
            "Hint": "� Hint Only",
            "Tests": "🧪 Test Cases",
            "Complexity": "⚠️ Complexity",
            "Idea": "💡 Algorithm Idea",
            "Code": "💻 Full Solution"
        }
        mode = mode_map[mode_short]

# Set defaults if not set
if 'temp' not in locals():
    temp = 0.2

st.markdown("---")

# ============================================================================
# LOAD ASSISTANT
# ============================================================================
if api_key:
    try:
        assistant = load_openrouter_assistant(_api_key=api_key, _model=selected_model_id)
        st.success(f"✅ Connected: **{selected_model_name}**")
    except Exception as e:
        st.error(f"❌ Failed: {str(e)}")
        st.stop()
else:
    st.warning("⚠️ Please enter your OpenRouter API key above to continue")
    st.stop()

# ============================================================================
# MAIN INTERFACE (SINGLE COLUMN FOR MOBILE)
# ============================================================================
st.markdown("### 📝 Your Problem")
problem_text = st.text_area(
    "problem_input",
    height=250,
    placeholder="""Paste your competitive programming problem here...

Example:
Given an array of integers and a target sum, find two numbers that add up to the target.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]""",
    label_visibility="collapsed"
)

generate_btn = st.button(
    "🚀 Generate Response",
    use_container_width=True,
    type="primary"
)

st.markdown("---")

st.markdown("### 🤖 AI Response")

if generate_btn and problem_text:
    # Mode to System Prompt Mapping
    MODE_PROMPTS = {
        "🔍 Hint Only": "Give ONE high-level hint (e.g., 'Use Two Pointers'). NO code. Keep under 2 sentences.",
        "🧪 Test Cases": "Generate 5 test cases: basic, edge, large, negative, corner case. Show input/output.",
        "⚠️ Complexity": "Analyze time/space complexity. Explain WHY (e.g., 'O(N) because single pass').",
        "💡 Algorithm Idea": "Explain algorithm in plain English, step by step. NO code.",
        "💻 Full Solution": "Write optimal C++/Python solution with comments and complexity notes."
    }
    
    system_prompt = MODE_PROMPTS[mode]
    
    with st.spinner("🤔 Thinking..."):
        start_time = time.time()
        try:
            response = assistant.generate_response(
                system_prompt,
                problem_text,
                temp=temp
            )
            elapsed = time.time() - start_time
            
            # Display response in a nice container
            response_container = st.container()
            with response_container:
                st.markdown(response)
                st.caption(f"✨ Generated in {elapsed:.1f}s using {selected_model_name}")
            
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

elif generate_btn:
    st.warning("⚠️ Please enter a problem above!")

else:
    st.info("� Enter your problem and click **Generate Response** to get started!")

# ============================================================================
# FOOTER
# ============================================================================
st.markdown("---")
st.caption("Made with ❤️ for programmers | [GitHub](https://github.com/yourusername/AlgoAlly) | [Desktop App](https://github.com/yourusername/AlgoAlly/releases)")
