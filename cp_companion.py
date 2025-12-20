import streamlit as st
import time
from coder import CodeAssistant
from openrouter_assistant import OpenRouterAssistant

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================
st.set_page_config(
    page_title="AlgoAlly - AI DSA Companion",
    page_icon="🧩",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# ENHANCED DARK THEME STYLING
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
    
    /* Global Background Fix */
    .main, .block-container, 
    [data-testid="stAppViewContainer"],
    [data-testid="stHeader"],
    [data-testid="stToolbar"],
    .stApp {
        background-color: var(--bg-primary) !important;
        color: var(--text-primary) !important;
    }
    
    /* Hide Header/Toolbar */
    [data-testid="stHeader"],
    [data-testid="stToolbar"] {
        display: none !important;
    }
    
    /* Optimal Padding */
    .main > div {
        padding: 1.5rem 2rem !important;
    }
    
    .block-container {
        padding-top: 1rem !important;
        max-width: 1400px !important;
    }
    
    /* ==================== SIDEBAR ==================== */
    [data-testid="stSidebar"] {
        background-color: var(--bg-secondary) !important;
        padding: 1.5rem 1rem !important;
    }
    
    [data-testid="stSidebar"] > div:first-child {
        background-color: var(--bg-secondary) !important;
    }
    
    /* IMPORTANT: Keep collapse/expand buttons visible! */
    button[kind="header"],
    button[data-testid="baseButton-header"],
    button[aria-label*="collapse"],
    button[aria-label*="expand"] {
        display: block !important;
        visibility: visible !important;
        opacity: 1 !important;
        color: var(--text-primary) !important;
        background-color: transparent !important;
    }
    
    button[kind="header"]:hover,
    button[data-testid="baseButton-header"]:hover {
        background-color: var(--bg-tertiary) !important;
    }
    
    /* Hide sidebar header element */
    [data-testid="stSidebarHeader"] {
        display: none !important;
    }
    
    /* Style the collapsed sidebar reopen button */
    [data-testid="collapsedControl"] {
        display: block !important;
        visibility: visible !important;
        background-color: var(--bg-secondary) !important;
        border: 1px solid var(--border-color) !important;
        border-radius: 0 8px 8px 0 !important;
        color: var(--text-primary) !important;
    }
    
    [data-testid="collapsedControl"]:hover {
        background-color: var(--bg-tertiary) !important;
        border-color: var(--accent-blue) !important;
    }
    
    [data-testid="stSidebar"] * {
        color: var(--text-primary) !important;
    }
    
    /* ==================== TYPOGRAPHY ==================== */
    h1 {
        color: var(--accent-blue) !important;
        font-weight: 700 !important;
        font-size: 2.5rem !important;
        margin-bottom: 0.5rem !important;
        letter-spacing: -0.02em;
    }
    
    h2, h3 {
        color: var(--text-primary) !important;
        font-weight: 600 !important;
    }
    
    p, span, div, label, li {
        color: var(--text-primary) !important;
    }
    
    .subtitle {
        color: var(--text-secondary) !important;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }
    
    /* ==================== INPUTS ==================== */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        background-color: var(--bg-secondary) !important;
        color: var(--text-primary) !important;
        border: 1px solid var(--border-color) !important;
        border-radius: 8px !important;
        font-size: 0.95rem !important;
        transition: all 0.2s ease;
    }
    
    .stTextInput > div > div > input::placeholder,
    .stTextArea > div > div > textarea::placeholder {
        color: var(--text-secondary) !important;
        opacity: 0.6;
    }
    
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {
        border-color: var(--accent-blue) !important;
        box-shadow: 0 0 0 3px rgba(88, 166, 255, 0.15) !important;
        outline: none !important;
    }
    
    /* ==================== SELECTBOX ==================== */
    .stSelectbox > div > div,
    div[data-baseweb="select"] > div {
        background-color: var(--bg-secondary) !important;
        border: 1px solid var(--border-color) !important;
        border-radius: 8px !important;
        color: var(--text-primary) !important;
    }
    
    /* Dropdown Menu */
    div[data-baseweb="popover"],
    ul[role="listbox"] {
        background-color: var(--bg-secondary) !important;
        border: 1px solid var(--border-color) !important;
        border-radius: 8px !important;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4) !important;
    }
    
    ul[role="listbox"] > li {
        background-color: var(--bg-secondary) !important;
        color: var(--text-primary) !important;
        transition: all 0.2s ease;
    }
    
    ul[role="listbox"] > li:hover {
        background-color: var(--bg-tertiary) !important;
        color: var(--accent-blue) !important;
    }
    
    /* ==================== RADIO BUTTONS ==================== */
    .stRadio > div {
        gap: 0.75rem;
    }
    
    .stRadio label {
        padding: 0.5rem 0.75rem;
        border-radius: 6px;
        transition: all 0.2s ease;
        cursor: pointer;
    }
    
    .stRadio label:hover {
        background-color: var(--bg-tertiary);
    }
    
    /* ==================== BUTTONS ==================== */
    .stButton > button {
        background: linear-gradient(135deg, #238636 0%, #2ea043 100%) !important;
        color: white !important;
        border-radius: 8px !important;
        border: none !important;
        padding: 0.75rem 1.5rem !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: 0 4px 12px rgba(35, 134, 54, 0.3) !important;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #2ea043 0%, #3fb950 100%) !important;
        box-shadow: 0 6px 20px rgba(46, 160, 67, 0.5) !important;
        transform: translateY(-2px) !important;
    }
    
    .stButton > button:active {
        transform: translateY(0) !important;
    }
    
    /* ==================== ALERTS ==================== */
    .stSuccess, .stWarning, .stError, .stInfo {
        background-color: var(--bg-secondary) !important;
        border-radius: 8px !important;
        padding: 1rem !important;
        margin: 0.5rem 0 !important;
    }
    
    .stSuccess {
        border-left: 4px solid var(--accent-green) !important;
    }
    
    .stWarning {
        border-left: 4px solid var(--accent-orange) !important;
    }
    
    .stError {
        border-left: 4px solid var(--accent-red) !important;
    }
    
    .stInfo {
        border-left: 4px solid var(--accent-blue) !important;
    }
    
    /* ==================== EXPANDER ==================== */
    .streamlit-expanderHeader {
        background-color: var(--bg-tertiary) !important;
        border-radius: 8px !important;
        color: var(--text-primary) !important;
        padding: 0.75rem 1rem !important;
        transition: all 0.2s ease;
    }
    
    .streamlit-expanderHeader:hover {
        background-color: #2d333b !important;
    }
    
    /* ==================== SLIDER ==================== */
    .stSlider > div > div > div {
        background-color: var(--border-color) !important;
    }
    
    .stSlider [role="slider"] {
        background-color: var(--accent-blue) !important;
    }
    
    /* ==================== MARKDOWN CODE ==================== */
    code {
        background-color: var(--bg-tertiary) !important;
        color: var(--accent-blue) !important;
        padding: 0.2rem 0.4rem !important;
        border-radius: 4px !important;
        font-size: 0.9em !important;
    }
    
    pre {
        background-color: var(--bg-tertiary) !important;
        border: 1px solid var(--border-color) !important;
        border-radius: 8px !important;
        padding: 1rem !important;
    }
    
    /* ==================== MISC ==================== */
    .element-container {
        margin-bottom: 0.5rem;
    }
    
    hr {
        border-color: var(--border-color) !important;
        margin: 1rem 0 !important;
    }
    
    /* Custom Caption Style */
    .caption-text {
        color: var(--text-secondary) !important;
        font-size: 0.85rem;
        margin-top: 0.5rem;
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

@st.cache_resource
def load_local_assistant(_hf_token, _model_name):
    """Load local model assistant with caching."""
    return CodeAssistant(hf_token=_hf_token, model_name=_model_name)

# ============================================================================
# HEADER
# ============================================================================
st.title("🧩 AlgoAlly - AI DSA Companion")
st.markdown('<p class="subtitle">Your intelligent partner for competitive programming — choose between fast cloud inference or private local models</p>', unsafe_allow_html=True)

# ============================================================================
# SIDEBAR CONFIGURATION
# ============================================================================
with st.sidebar:
    st.markdown("## ⚙️ Configuration")
    
    # Backend Selection
    backend = st.radio(
        "**Backend:**",
        ["⚡ OpenRouter (Cloud)", "🔒 Local Model (Private)"],
        help="OpenRouter: 2-5s response time | Local: 60-300s response time"
    )
    
    st.markdown("---")
    
    # Model Selection & Authentication
    with st.expander("🤖 Model & Authentication", expanded=True):
        if backend == "⚡ OpenRouter (Cloud)":
            openrouter_models = OpenRouterAssistant.FREE_MODELS
            selected_model_name = st.selectbox(
                "Select Model:",
                list(openrouter_models.keys()),
                help="Choose from available OpenRouter models"
            )
            selected_model_id = openrouter_models[selected_model_name]
            
            api_key = st.text_input(
                "OpenRouter API Key:",
                type="password",
                placeholder="sk-or-v1-...",
                help="Get your free API key at openrouter.ai/keys"
            )
        else:
            local_models = CodeAssistant.LOCAL_MODELS
            selected_model_name = st.selectbox(
                "Select Model:",
                list(local_models.keys()),
                help="Choose a local model to run"
            )
            selected_model_id = local_models[selected_model_name]
            
            api_key = st.text_input(
                "HuggingFace Token (Optional):",
                type="password",
                placeholder="hf_...",
                help="Optional: Required for gated models"
            )
    
    st.markdown("---")
    
    # Mode Selection
    st.markdown("**💭 Assistant Mode:**")
    mode = st.radio(
        "mode_selector",
        [
            "🔍 Hint Only",
            "🧪 Generate Test Cases",
            "⚠️ Complexity Analysis",
            "💡 Algorithm Idea",
            "💻 Full Solution"
        ],
        label_visibility="collapsed",
        help="Choose what type of help you want"
    )
    
    # Advanced Settings
    with st.expander("🎛️ Advanced Settings"):
        temp = st.slider(
            "Temperature:",
            min_value=0.0,
            max_value=1.0,
            value=0.2,
            step=0.1,
            help="Lower = More focused, Higher = More creative"
        )
    
    st.markdown("---")
    st.caption("💡 **Tip:** Start with hints before viewing solutions!")

# ============================================================================
# LOAD ASSISTANT
# ============================================================================
try:
    if backend == "⚡ OpenRouter (Cloud)":
        if not api_key:
            st.warning("⚠️ Please enter your OpenRouter API key in the sidebar")
            st.stop()
        assistant = load_openrouter_assistant(_api_key=api_key, _model=selected_model_id)
        st.success(f"✅ Connected: **{selected_model_name}**")
    else:
        assistant = load_local_assistant(_hf_token=api_key or None, _model_name=selected_model_id)
        st.success(f"✅ Loaded: **{selected_model_name}**")
except Exception as e:
    st.error(f"❌ Failed to initialize: {str(e)}")
    st.stop()

# ============================================================================
# MAIN INTERFACE
# ============================================================================
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown("### 📝 Problem Input")
    problem_text = st.text_area(
        "problem_input",
        height=350,
        placeholder="""Paste your competitive programming problem here...

Example:
Given an array of integers and a target sum, find two numbers that add up to the target.

Input: nums = [2,7,11,15], target = 9
Output: [0,1] (because nums[0] + nums[1] = 9)""",
        label_visibility="collapsed"
    )
    
    generate_btn = st.button(
        "🚀 Generate Response",
        use_container_width=True,
        type="primary"
    )

with col2:
    st.markdown("### 🤖 AI Response")
    
    if generate_btn and problem_text:
        # Mode to System Prompt Mapping
        MODE_PROMPTS = {
            "🔍 Hint Only": "You are a competitive programming coach. Give only a high-level hint about the approach (like 'Consider using Two Pointers' or 'Think about Dynamic Programming'). DO NOT write code or explain the full algorithm. Keep it under 3 sentences.",
            
            "🧪 Generate Test Cases": "Generate 5 diverse test cases for this problem. Include: 1 basic case, 1 edge case (empty/single element), 1 large input case, 1 case with negative numbers or special values, and 1 tricky corner case. Format each clearly with input and expected output.",
            
            "⚠️ Complexity Analysis": "Analyze the time and space complexity of the optimal solution to this problem. Explain WHY it has that complexity (e.g., 'O(N) because we traverse the array once' or 'O(log N) because we use binary search'). Also mention any trade-offs.",
            
            "💡 Algorithm Idea": "Explain the optimal algorithm approach in plain English, step by step. Focus on the logic and intuition. DO NOT write actual code. Help them understand the 'why' behind each step.",
            
            "💻 Full Solution": "Write a complete, optimal solution in C++ or Python (your choice based on what's better for this problem). Include: 1) Clear comments explaining the approach, 2) Well-named variables, 3) Edge case handling, 4) Time/Space complexity as comments."
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
                
                # Display response
                st.markdown(response)
                
                # Footer with metadata
                st.markdown(f'<p class="caption-text">✨ Generated in {elapsed:.1f}s using {selected_model_name}</p>', unsafe_allow_html=True)
                
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
    
    elif generate_btn:
        st.warning("⚠️ Please enter a problem in the left panel first!")
    
    else:
        st.info("👈 Enter your problem and click **Generate Response** to get started!")

# ============================================================================
# FOOTER
# ============================================================================
st.markdown("---")
st.caption("Made with ❤️ for programmers | Supports both cloud and local inference")