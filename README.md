# ⚡ AlgoAlly - Premium AI DSA Companion

AlgoAlly is a professional-grade, high-performance AI platform designed specifically for solving Data Structures and Algorithms (DSA) problems. Built with a modern, glassmorphic aesthetic, it helps engineers find the most efficient path from problem to solution.

![AlgoAlly Dashboard Mockup](https://raw.githubusercontent.com/Adiaparmar/AlgoAlly-AI-DSA-Companion/main/public/demo_preview.png)

## ✨ Key Features

*   🏙️ **Monaco Editor Core**: A full IDE-grade editing experience powered by the same engine as VS Code. Includes syntax highlighting, line numbers, and auto-indentation.
*   📊 **Complexity Visualizer**: Dynamic Sidebar Chart (powered by Recharts) that live-tracks the time complexity ($O(1)$, $O(\log N)$, $O(N)$, $O(N^2)$) of your current AI-generated solution.
*   🔗 **Smart Link Importer**: Instantly import problem statements directly from platforms like **GeeksForGeeks** and **LeetCode** (via Proxy Scraper).
*   🤖 **Dual Engine Support**: Seamlessly switch between **Google Gemini (3.1 Flash/Lite)** and **OpenRouter (DeepSeek, Qwen)** for the most accurate DSA analysis.
*   📱 **Ultra Responsive**: A fully adaptive interface optimized for mobile, tablet, and ultra-wide desktops.

## 🚀 Getting Started

### 1. Prerequisites
*   [Node.js](https://nodejs.org/) (v18.0 or higher)
*   [npm](https://www.npmjs.com/)

### 2. Local Setup
```powershell
# Clone the repository
git clone https://github.com/Adiaparmar/AlgoAlly-AI-DSA-Companion.git

# Install Dependencies
npm install

# Set up Environment Variables
# Copy .env.example to .env.local and fill in your keys
cp .env.example .env.local
```

### 3. Run Development
```powershell
npm run dev
```

The dashboard will be active at [http://localhost:3000](http://localhost:3000).

## 🌍 Deployment (Vercel)

AlgoAlly is fully optimized for **Vercel**. 

1.  Connect your GitHub repository to Vercel.
2.  Add the following **Environment Variables** in the Vercel Dashboard:
    *   `GEMINI_API_KEY` (from [Google AI Studio](https://aistudio.google.com/))
    *   `OPENROUTER_API_KEY` (from [OpenRouter.ai](https://openrouter.ai/))
3.  Click **Deploy**.

## 🏗️ Technology Stack
*   **Frontend**: Next.js 14, Tailwind CSS, Framer Motion
*   **Editor**: Monaco Editor (`@monaco-editor/react`)
*   **Charts**: Recharts
*   **Icons**: Lucide-React
*   **Backend API**: Next.js Server Actions (Edge-Compatible)

---

Developed with ❤️ by [Adiaparmar](https://github.com/Adiaparmar).
