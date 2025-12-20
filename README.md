# 🧩 AlgoAlly - AI DSA Companion

AlgoAlly is an AI-powered assistant that helps you solve competitive programming problems **your way**. Instead of just giving you the answer, it offers **5 intelligent modes** to match your learning style:

- 🔍 **Hint Mode** - Get a subtle nudge in the right direction without spoilers
- 🧪 **Test Case Generator** - Create comprehensive test cases including edge cases
- ⚠️ **Complexity Analyzer** - Understand time/space complexity with clear explanations
- 💡 **Algorithm Explainer** - Learn the approach step-by-step in plain English
- 💻 **Solution Generator** - Get optimized, well-commented code implementations

Choose between **high-speed cloud inference** (2-5s responses via OpenRouter) or **privacy-focused local models** (runs entirely on your machine). Available as a **web app**, **desktop application**, or **run from source** for maximum flexibility.

---

## 🚀 Quick Start - Choose Your Platform

AlgoAlly is available in **4 different ways** - pick what works best for you:

### 1️⃣ **Web App (Easiest - OpenRouter Only)** ⚡

**👉 [Launch AlgoAlly Web App](https://algoally.streamlit.app)** *(Replace with your actual URL)*

- ✅ **No installation** - Works instantly in your browser
- ✅ **Cross-platform** - Windows, Mac, Linux, Mobile
- ✅ **Always updated** - Latest features automatically
- ⚠️ **OpenRouter only** - Requires API key (free tier available)
- ⚠️ **No local models** - Cloud-based only

**Perfect for:** Quick access, mobile users, trying it out

---

### 2️⃣ **Desktop App - Windows Executable (OpenRouter Only)** 💻

**👉 [Download AlgoAlly.exe](https://github.com/yourusername/AlgoAlly/releases)** *(Replace with your repo)*

- ✅ **No Python needed** - Standalone executable
- ✅ **Native Windows app** - Fast and responsive
- ✅ **Offline-capable** - Once downloaded, runs without internet (except API calls)
- ⚠️ **OpenRouter only** - Requires API key
- ⚠️ **Windows only** - For Mac/Linux, run from source

**Perfect for:** Windows users who want a native app experience

---

### 3️⃣ **Run Locally - Full Features (Recommended for Developers)** 🔧

**Clone and run from source** - Supports both OpenRouter AND local models

```bash
# Clone the repository
git clone https://github.com/yourusername/AlgoAlly.git
cd AlgoAlly

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run Streamlit web app
streamlit run cp_companion.py
# OR run native desktop app
python cp_companion_desktop.py
```

**Features:**
- ✅ **Full functionality** - Both OpenRouter AND local models
- ✅ **Privacy** - Local models run entirely on your machine
- ✅ **Customizable** - Modify code as needed
- ✅ **Cross-platform** - Works on Windows, Mac, Linux

**Perfect for:** Developers, privacy-conscious users, those wanting local models

---

### 4️⃣ **Mobile-Optimized Web App** 📱

Same as option 1, but optimized for mobile screens:

**👉 [Launch on Mobile](https://algoally.streamlit.app)**

- ✅ **Touch-friendly** - Optimized UI for small screens
- ✅ **Responsive** - Works on phones and tablets
- ✅ **Same features** - Full OpenRouter support

**Perfect for:** Solving problems on the go

---

## 📊 Platform Comparison

| Feature | Web App | Desktop .exe | Run from Source |
|---------|---------|--------------|-----------------|
| **Installation** | None | Download only | Python + packages |
| **OpenRouter Support** | ✅ Yes | ✅ Yes | ✅ Yes |
| **Local Models** | ❌ No | ❌ No | ✅ Yes |
| **Platforms** | All (browser) | Windows only | All |
| **Updates** | Automatic | Manual download | `git pull` |
| **Privacy** | Good | Good | Excellent |
| **Speed** | Fast | Fast | Fast |
| **Mobile Support** | ✅ Yes | ❌ No | ❌ No |

---

## ✨ Features

- 🚀 **Dual Interface**: Web app (Streamlit) + Native desktop app (CustomTkinter)
- ⚡ **Fast Cloud Inference**: OpenRouter API with free/cheap models (2-5s responses)
- 🔒 **Private Local Models**: Run HuggingFace models offline (60-300s on CPU)
- 🎯 **Smart Assistance Modes**:
  - 🔍 **Hint Only** - Get subtle hints without spoilers
  - 🧪 **Test Cases** - Generate comprehensive test cases
  - ⚠️ **Complexity Analysis** - Understand time/space complexity
  - 💡 **Algorithm Idea** - Learn the approach without code
  - 💻 **Full Solution** - Get complete implementations
- 🎨 **Modern Dark UI**: GitHub-inspired dark theme
- 🤖 **Multiple AI Models**: Choose from various coding-optimized models
- 📱 **Mobile-Friendly**: Responsive design for all screen sizes

---

## ⚙️ Configuration

### For OpenRouter (Fast, Recommended) ⚡

1. **Get a free API key** from [OpenRouter](https://openrouter.ai/keys)
2. Enter it in the app's API Key field
3. Select a model (KwaiPilot KAT Coder Pro is free!)
4. Start solving problems!

**Cost**: Most models are **FREE** or ~$0.001 per request

**Available Models:**
- **KwaiPilot KAT Coder Pro** (FREE) - Optimized for competitive programming
- **Qwen3 Coder** (FREE) - General coding tasks
- **Olympic Coder 32B** (~$0.001/req) - Complex algorithms
- **DeepSeek Chat** (~$0.0001/req) - Fast and cheap

---

### For Local Models (Private, Slow) 🔒

**⚠️ Only available when running from source**

1. (Optional) Get HuggingFace token from [HF Settings](https://huggingface.co/settings/tokens)
2. Select a local model
3. Click "Load Model"
4. First run will download ~2-3GB model

**Available Models:**
- **DeepSeek Coder 1.3B** - Balanced performance
- **VibeThinker 1.5B** - Experimental
- **Qwen2.5 Coder 1.5B** - Latest technology

**Note**: Local models are SLOW on CPU (60-300s per response) but completely private.

---

## 🔒 Privacy & Security

### Web App & Desktop .exe:
- 🔐 Your API keys are **only used in your session** and **never stored**
- 🔐 All code is **open source** - verify yourself on GitHub
- 🔐 API calls go directly from your device to OpenRouter

### Running from Source (Local Models):
- 🔒 **100% private** - Models run entirely on your machine
- 🔒 **No internet needed** - After downloading models
- 🔒 **Your code never leaves your computer**

---

## 📁 Project Structure

```
AlgoAlly/
├── cp_companion.py              # Streamlit app (full features)
├── app_web.py                   # Streamlit app (web-optimized, OpenRouter only)
├── cp_companion_desktop.py      # Desktop app (full features)
├── coder.py                     # Local model handler
├── openrouter_assistant.py      # OpenRouter API handler
├── requirements.txt             # Python dependencies
├── .env.example                 # Environment variables template
├── AlgoAlly.spec               # PyInstaller build config (gitignored)
├── MODEL_GUIDE.md              # Detailed model comparison
├── RELEASE_GUIDE.md            # How to build and release
└── README.md                   # This file
```

---

## 🛠️ Tech Stack

- **UI Frameworks**: Streamlit, CustomTkinter
- **AI/ML**: Transformers, PyTorch
- **APIs**: OpenRouter, HuggingFace
- **Utilities**: python-dotenv, requests

---

## 📝 Environment Variables (Optional)

Create a `.env` file for convenience (copy from `.env.example`):

```env
# OpenRouter API Key (for cloud inference)
OPENROUTER_API_KEY=sk-or-v1-your-key-here

# HuggingFace Token (optional, for local models)
HF_TOKEN=hf_your-token-here
```

**Note**: You can also enter these directly in the app UI.

---

## 💡 Usage Tips

1. **Start with Hints**: Don't jump straight to solutions - learn the approach first!
2. **Use Test Cases**: Validate your solution before submitting
3. **Understand Complexity**: Know why your solution is O(N) or O(log N)
4. **Choose the Right Platform**:
   - **Web App**: Quick access, mobile, trying it out
   - **Desktop .exe**: Native Windows experience
   - **From Source**: Full features, local models, customization

---

## 🚀 Deployment (For Developers)

### Deploy Web App to Streamlit Cloud

1. Fork this repository
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repo
4. Deploy `app_web.py` (mobile-optimized, OpenRouter only)
5. Share your URL!

### Build Desktop Executable

See [RELEASE_GUIDE.md](RELEASE_GUIDE.md) for detailed instructions.

```bash
# Install PyInstaller
pip install pyinstaller

# Build (creates dist/AlgoAlly.exe)
pyinstaller AlgoAlly.spec
```

**Note**: The .exe will be OpenRouter-only to keep size manageable (~100-200MB).

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- [OpenRouter](https://openrouter.ai/) - For providing access to multiple AI models
- [HuggingFace](https://huggingface.co/) - For hosting open-source models
- [Streamlit](https://streamlit.io/) - For the amazing web framework
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) - For modern Tkinter widgets

---

## 📧 Support & Links

- 🐛 **Bug Reports**: [GitHub Issues](https://github.com/yourusername/AlgoAlly/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/yourusername/AlgoAlly/discussions)
- 📖 **Documentation**: [MODEL_GUIDE.md](MODEL_GUIDE.md)
- 🌐 **Web App**: [algoally.streamlit.app](https://algoally.streamlit.app)
- 💻 **Desktop App**: [Releases](https://github.com/yourusername/AlgoAlly/releases)

---

## ⭐ Star History

If you find AlgoAlly helpful, please consider giving it a star! ⭐

---

**Made with ❤️ for competitive programmers**

*Choose your platform and start solving problems smarter, not harder!*
