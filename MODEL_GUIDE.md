# 🎯 Model Selection Guide

## Available Models

### ⚡ OpenRouter Models (Fast - Recommended)

All these models are **FREE** or very cheap to use:

| Model Name | Speed | Quality | Best For | Cost |
|------------|-------|---------|----------|------|
| **KwaiPilot KAT Coder Pro** | ⚡⚡⚡ | ⭐⭐⭐⭐ | Competitive Programming | FREE |
| **Qwen3 Coder** | ⚡⚡⚡ | ⭐⭐⭐⭐ | General Coding | FREE |
| **Olympic Coder 32B** | ⚡⚡ | ⭐⭐⭐⭐⭐ | Complex Algorithms | ~$0.001/req |
| **DeepSeek Chat** | ⚡⚡⚡ | ⭐⭐⭐⭐ | Fast & Cheap | ~$0.0001/req |

**Recommendation**: Start with **KwaiPilot KAT Coder Pro** - it's free and optimized for coding!

### 🔒 Local Models (Private but Slow)

These run on your machine (no internet needed after download):

| Model Name | Size | Speed (CPU) | Quality | Best For |
|------------|------|-------------|---------|----------|
| **DeepSeek Coder 1.3B** | 2.6GB | 🐌 60-180s | ⭐⭐⭐⭐ | Balanced |
| **VibeThinker 1.5B** | 3GB | 🐌 80-200s | ⭐⭐⭐ | Experimental |
| **Qwen2.5 Coder 1.5B** | 3GB | 🐌 70-190s | ⭐⭐⭐⭐ | Latest Tech |

**Recommendation**: Use **DeepSeek Coder 1.3B** if you need privacy - it's the most tested.

---

## How to Use

### For OpenRouter (Fast):

1. **Get API Key**: Visit [openrouter.ai/keys](https://openrouter.ai/keys)
2. **Select Backend**: Choose "⚡ OpenRouter (Fast, Recommended)"
3. **Select Model**: Pick from the dropdown (try KwaiPilot first!)
4. **Enter API Key**: Paste your key
5. **Click Connect**: Wait 1-2 seconds
6. **Start Coding**: Get responses in 2-5 seconds!

### For Local Model (Private):

1. **Select Backend**: Choose "🔒 Local Model (Slow, Private)"
2. **Select Model**: Pick from the dropdown (DeepSeek recommended)
3. **Optional Token**: Add HuggingFace token if you have one
4. **Click Load**: Wait 30-60 seconds for download
5. **Be Patient**: Each response takes 60-300 seconds on CPU

---

## Model Comparison Examples

### Speed Test (Same Question):

**Question**: "Write a binary search algorithm in C++"

| Model | Time | Quality |
|-------|------|---------|
| KwaiPilot KAT Coder Pro | 3s | ⭐⭐⭐⭐ |
| Olympic Coder 32B | 5s | ⭐⭐⭐⭐⭐ |
| DeepSeek Chat | 2s | ⭐⭐⭐⭐ |
| DeepSeek Coder (Local) | 120s | ⭐⭐⭐⭐ |

---

## Cost Breakdown (OpenRouter)

### Free Models:
- **KwaiPilot KAT Coder Pro**: Completely FREE ✅
- **Qwen3 Coder**: Completely FREE ✅

### Paid Models (Very Cheap):
- **Olympic Coder 32B**: ~$0.001 per request
  - 100 questions = $0.10
  - Full day of practice = ~$0.30
- **DeepSeek Chat**: ~$0.0001 per request
  - 1000 questions = $0.10
  - Practically free!

---

## Tips for Choosing

### Use OpenRouter If:
- ✅ You want fast responses (2-5s)
- ✅ You're okay with ~$0.30/month cost
- ✅ You have internet connection
- ✅ You're practicing daily

### Use Local Model If:
- ✅ You need 100% privacy
- ✅ You have no internet
- ✅ You have a powerful GPU (makes it faster)
- ✅ You're okay waiting 1-5 minutes per response

---

## Troubleshooting

### OpenRouter Issues:

**"Invalid API Key"**
- Make sure you copied the full key (starts with `sk-or-v1-`)
- Check if you have credits at openrouter.ai

**"Rate Limited"**
- Free models have rate limits
- Wait 1 minute or switch to DeepSeek Chat (cheaper)

### Local Model Issues:

**"Out of Memory"**
- Close other applications
- Try a smaller model
- Use CPU offloading (automatic)

**"Very Slow"**
- Normal on CPU! 60-300s is expected
- Consider using OpenRouter instead
- Or get a GPU for 10x speedup

---

## Recommended Setup

**For Daily CP Practice**:
```
Backend: OpenRouter
Model: KwaiPilot KAT Coder Pro (Free)
Temperature: 0.2
```

**For Privacy-Critical Work**:
```
Backend: Local Model
Model: DeepSeek Coder 1.3B
Temperature: 0.2
```

**For Best Quality**:
```
Backend: OpenRouter
Model: Olympic Coder 32B
Temperature: 0.3
```

---

**Pro Tip**: You can switch models anytime! Just disconnect and reconnect with a different selection.
