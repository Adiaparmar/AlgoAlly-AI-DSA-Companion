'use client';

import React, { useState, useEffect } from 'react';
import { 
  Sparkles, 
  Settings, 
  Terminal, 
  Code2, 
  Zap, 
  Menu, 
  ChevronRight,
  Loader2,
  Copy,
  LayoutGrid,
  TrendingDown,
  BarChart3,
  Link as LinkIcon,
  AlertCircle,
  Plus,
  X,
  Search
} from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';
import Editor from '@monaco-editor/react';
import { ResponsiveContainer, AreaChart, Area, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';

export default function Home() {
  const [problem, setProblem] = useState('');
  const [url, setUrl] = useState('');
  const [mode, setMode] = useState('Hint');
  const [provider, setProvider] = useState('gemini');
  const [model, setModel] = useState('gemini-3.1-flash-lite-preview');
  const [response, setResponse] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [isScraping, setIsScraping] = useState(false);
  const [sidebarOpen, setSidebarOpen] = useState(true);
  const [showMobileSearch, setShowMobileSearch] = useState(false);
  const [detectedComplexity, setDetectedComplexity] = useState<string | null>(null);

  // Auto-close sidebar on small screens initially
  useEffect(() => {
    if (window.innerWidth < 1024) setSidebarOpen(false);
  }, []);

  const generateChartData = () => {
    const data = [];
    for (let n = 1; n <= 100; n += 5) {
      data.push({
        n,
        'O(1)': 15,
        'O(log N)': Math.log2(n) * 12 + 15,
        'O(N)': n + 15,
        'O(N²)': (n * n / 10) + 15,
      });
    }
    return data;
  };
  const [chartData] = useState(generateChartData());

  const scrapeLink = async () => {
    if (!url.trim()) return;
    setIsScraping(true);
    try {
      const res = await fetch('/api/scrape', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ url })
      });
      const data = await res.json();
      if (data.error) throw new Error(data.error);
      setProblem(data.description);
      setDetectedComplexity(null);
      setShowMobileSearch(false);
    } catch (err: any) {
      alert(`⚠️ ${err.message}`);
    } finally {
      setIsScraping(false);
    }
  };

  const generate = async () => {
    if (!problem.trim()) return;
    setIsLoading(true);
    setResponse('');
    
    try {
      const res = await fetch('/api/generate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ problem, mode, model, provider, temperature: 0.2 })
      });
      const data = await res.json();
      if (data.error) throw new Error(data.error);
      
      const fullContent = data.content;
      const match = fullContent.match(/\[COMPLEXITY:\s*(.*?)\]/);
      if (match && match[1]) {
        const found = match[1].trim().toUpperCase();
        if (found.includes('N^2')) setDetectedComplexity('O(N²)');
        else if (found.includes('LOG')) setDetectedComplexity('O(log N)');
        else if (found.includes('1')) setDetectedComplexity('O(1)');
        else if (found.includes('N')) setDetectedComplexity('O(N)');
      }
      setResponse(fullContent.replace(/\[COMPLEXITY:.*?\]/, '').trim());
    } catch (err: any) {
      setResponse(`❌ Error: ${err.message}`);
    } finally {
      setIsLoading(false);
    }
  };

  const modes = ['Hint', 'Test Cases', 'Complexity', 'Explain', 'Code'];
  const providers = {
    gemini: { 
      name: 'Gemini', 
      models: [
        { id: 'gemini-3.1-flash-lite-preview', label: 'Gemini 3.1 Flash Lite' },
        { id: 'gemini-2.5-flash', label: 'Gemini 2.5 Flash' }
      ] 
    },
    openrouter: { 
      name: 'OpenRouter', 
      models: [
        { id: 'qwen/qwen3-coder:free', label: 'Qwen 3 Coder (Free)' },
        { id: 'stepfun/step-3.5-flash:free', label: 'StepFun 3.5 Flash (Free)' }
      ] 
    }
  };

  return (
    <div className="min-h-screen flex text-zinc-200 bg-[#020202] overflow-hidden selection:bg-blue-500/30">
      
      {/* Mobile Sidebar Backdrop */}
      <AnimatePresence>
        {sidebarOpen && (
          <motion.div 
            initial={{ opacity: 0 }} 
            animate={{ opacity: 1 }} 
            exit={{ opacity: 0 }}
            onClick={() => setSidebarOpen(false)}
            className="fixed inset-0 bg-black/80 backdrop-blur-sm z-[50] lg:hidden"
          />
        )}
      </AnimatePresence>

      {/* Responsive Sidebar */}
      <AnimatePresence>
        {sidebarOpen && (
          <motion.aside 
            initial={{ x: -320 }} 
            animate={{ x: 0 }} 
            exit={{ x: -320 }}
            transition={{ type: 'spring', damping: 25, stiffness: 200 }}
            className="fixed lg:relative top-0 bottom-0 left-0 w-[300px] bg-[#050505] border-r border-white/5 z-[60] flex flex-col"
          >
            <div className="p-8 border-b border-white/5 flex items-center justify-between">
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 rounded-xl bg-blue-600 flex items-center justify-center shadow-lg shadow-blue-500/20"><Sparkles className="text-white w-5 h-5" /></div>
                <div><h1 className="text-lg font-bold text-white tracking-tight">AlgoAlly</h1><p className="text-[10px] text-zinc-600 font-bold uppercase tracking-widest">Dash Pro</p></div>
              </div>
              <button onClick={() => setSidebarOpen(false)} className="lg:hidden p-2 hover:bg-zinc-900 rounded-lg text-zinc-500"><X className="w-5 h-5" /></button>
            </div>

            <div className="p-6 flex-1 overflow-y-auto space-y-10 scrollbar-hide">
              {/* Context Selector */}
              <div className="space-y-4">
                <label className="text-[11px] font-bold uppercase tracking-widest text-zinc-600 px-2 flex items-center gap-2"><Settings className="w-3 h-3"/> Context Settings</label>
                <div className="space-y-3 px-2">
                   <div className="flex bg-zinc-900 border border-white/5 rounded-xl p-1">
                      <button onClick={() => setProvider('gemini')} className={`flex-1 py-2 text-[10px] font-bold uppercase rounded-lg transition-all ${provider === 'gemini' ? 'bg-zinc-800 text-blue-400' : 'text-zinc-600'}`}>Gemini</button>
                      <button onClick={() => setProvider('openrouter')} className={`flex-1 py-2 text-[10px] font-bold uppercase rounded-lg transition-all ${provider === 'openrouter' ? 'bg-zinc-800 text-purple-400' : 'text-zinc-600'}`}>OpenRouter</button>
                   </div>
                   <select className="w-full bg-zinc-900/50 border border-zinc-800 p-3 rounded-xl text-xs outline-none focus:border-blue-500/50 transition-all font-medium" value={model} onChange={e => setModel(e.target.value)}>
                      {providers[provider as keyof typeof providers].models.map(m => (<option key={m.id} value={m.id}>{m.label}</option>))}
                   </select>
                </div>
              </div>

              {/* Modes */}
              <div className="space-y-4">
                <label className="text-[11px] font-bold uppercase tracking-widest text-zinc-600 px-2 flex items-center gap-2"><LayoutGrid className="w-3 h-3"/> Focus Mode</label>
                <div className="space-y-1 px-2">
                  {modes.map(m => (
                    <button key={m} onClick={() => { setMode(m); if (window.innerWidth < 1024) setSidebarOpen(false); }} className={`w-full text-left px-4 py-3 rounded-xl text-sm transition-all flex items-center justify-between font-medium ${mode === m ? 'bg-blue-600/10 text-blue-400 border border-blue-500/20' : 'text-zinc-500 hover:bg-zinc-900 hover:text-zinc-300'}`}>
                      {m} {mode === m && <div className="w-1.5 h-1.5 rounded-full bg-blue-500" />}
                    </button>
                  ))}
                </div>
              </div>

              {/* Chart */}
              <div className="space-y-4">
                <label className="text-[11px] font-bold uppercase tracking-widest text-zinc-600 px-2 flex items-center gap-2"><TrendingDown className="w-3 h-3"/> Complexity Trends</label>
                <div className="bg-[#000] rounded-3xl p-6 border border-white/5 relative group">
                  <div className="absolute top-4 right-4">{detectedComplexity && <span className="text-[9px] font-black text-blue-500 tracking-widest bg-blue-500/10 px-2 py-0.5 rounded-full border border-blue-500/20">{detectedComplexity}</span>}</div>
                  <div className="h-32 w-full mt-2">
                    <ResponsiveContainer width="100%" height="100%">
                      <AreaChart data={chartData}>
                        <defs><linearGradient id="activeG" x1="0" y1="0" x2="0" y2="1"><stop offset="5%" stopColor="#3b82f6" stopOpacity={0.6}/><stop offset="95%" stopColor="#3b82f6" stopOpacity={0}/></linearGradient></defs>
                        {['O(1)', 'O(log N)', 'O(N)', 'O(N²)'].map(key => (
                          <Area key={key} type="monotone" dataKey={key} stroke={detectedComplexity === key ? '#3b82f6' : '#27272a'} strokeWidth={detectedComplexity === key ? 3 : 1} fill={detectedComplexity === key ? 'url(#activeG)' : 'transparent'} isAnimationActive={true} />
                        ))}
                      </AreaChart>
                    </ResponsiveContainer>
                  </div>
                </div>
              </div>
            </div>
          </motion.aside>
        )}
      </AnimatePresence>

      <main className="flex-1 flex flex-col relative h-[100dvh] overflow-hidden">
        {/* Responsive Header */}
        <header className="h-20 lg:h-24 border-b border-white/5 flex items-center justify-between px-6 lg:px-10 bg-black/50 backdrop-blur-2xl sticky top-0 z-40">
          <div className="flex items-center gap-4 lg:gap-8">
            <button onClick={() => setSidebarOpen(!sidebarOpen)} className="p-3 hover:bg-zinc-900 border border-transparent hover:border-white/5 rounded-2xl transition-all active:scale-95"><Menu className="w-6 h-6 text-zinc-400" /></button>
            <div className="h-4 w-px bg-zinc-800 hidden sm:block" />
            
            {/* Desktop Link Importer */}
            <div className="hidden lg:flex items-center bg-[#0d0d0d]/80 border border-white/5 rounded-[22px] px-2 py-2 focus-within:ring-2 focus-within:ring-blue-500/20 w-[420px] transition-all">
               <div className="w-10 h-10 rounded-xl bg-zinc-900 flex items-center justify-center border border-white/5 ml-1"><LinkIcon className="w-4 h-4 text-blue-500" /></div>
               <input className="flex-1 bg-transparent border-none outline-none text-xs px-4 text-zinc-300 placeholder:text-zinc-700 font-semibold" placeholder="Paste Link (LeetCode/GFG)" value={url} onChange={e => setUrl(e.target.value)} onKeyDown={e => e.key === 'Enter' && scrapeLink()}/>
               <button onClick={scrapeLink} disabled={isScraping || !url} className="px-6 py-3 bg-blue-600 hover:bg-blue-500 disabled:opacity-50 text-[10px] uppercase font-bold text-white rounded-xl transition-all"> {isScraping ? <Loader2 className="w-3 h-3 animate-spin"/> : 'Scrape'} </button>
            </div>

            {/* Mobile Link Importer Toggle */}
            <button onClick={() => setShowMobileSearch(!showMobileSearch)} className="lg:hidden p-3 hover:bg-zinc-900 rounded-2xl text-zinc-500"><Search className="w-6 h-6" /></button>
          </div>

          <div className="flex items-center gap-4">
             <div className="w-10 h-10 lg:w-12 lg:h-12 rounded-2xl bg-zinc-900/50 border border-white/5 flex items-center justify-center group cursor-pointer hover:border-blue-500/30 transition-all"><Plus className="w-5 h-5 text-zinc-600 group-hover:text-blue-500" /></div>
          </div>
        </header>

        {/* Mobile Search Overlay */}
        <AnimatePresence>
          {showMobileSearch && (
            <motion.div initial={{ y: -100 }} animate={{ y: 0 }} exit={{ y: -100 }} className="absolute top-24 left-0 right-0 bg-black/90 p-4 border-b border-white/10 z-30 lg:hidden backdrop-blur-xl">
               <div className="flex gap-2">
                 <input className="flex-1 bg-zinc-900 border border-white/10 rounded-xl px-4 py-3 text-sm" placeholder="Paste problem URL..." value={url} onChange={e => setUrl(e.target.value)} autoFocus onKeyDown={e => e.key === 'Enter' && scrapeLink()}/>
                 <button onClick={scrapeLink} disabled={isScraping} className="bg-blue-600 px-6 rounded-xl font-bold text-xs uppercase">{isScraping ? <Loader2 className="animate-spin w-4 h-4"/> : 'Go'}</button>
               </div>
            </motion.div>
          )}
        </AnimatePresence>

        <div className="flex-1 overflow-y-auto overflow-x-hidden custom-scrollbar flex flex-col p-6 lg:p-14 pb-32">
          <div className="max-w-6xl mx-auto w-full space-y-8 lg:space-y-12">
            
            {/* Main Area */}
            <motion.div initial={{ y: 20, opacity: 0 }} animate={{ y: 0, opacity: 1 }} className="space-y-6">
               <div className="flex flex-col sm:flex-row sm:items-center justify-between px-3 gap-2">
                 <div className="flex items-center gap-4">
                   <div className="w-10 h-10 lg:w-12 lg:h-12 rounded-2xl bg-zinc-900 border border-white/5 flex items-center justify-center"><Code2 className="w-5 h-5 text-zinc-400" /></div>
                   <div><h2 className="text-zinc-200 text-base lg:text-lg font-bold italic tracking-tight uppercase">Problem Editor</h2><p className="text-[10px] font-bold text-zinc-600 uppercase tracking-widest hidden sm:block">Real-time Analysis Ready</p></div>
                 </div>
                 <div className="flex gap-2 items-center bg-zinc-900/50 p-1.5 rounded-lg border border-white/5 w-fit">
                   <div className="px-3 py-1 bg-zinc-800 rounded-md text-[10px] font-bold text-zinc-400 uppercase">Active</div>
                   <span className="text-[10px] text-blue-500 font-bold uppercase tracking-wider px-2">{mode.split(' ')[1] || mode}</span>
                 </div>
               </div>

               <div className="rounded-[30px] lg:rounded-[40px] border border-white/5 bg-[#050505] overflow-hidden shadow-2xl h-[40vh] min-h-[350px] lg:h-[480px] relative group">
                  <Editor
                    height="100%"
                    defaultLanguage="python"
                    value={problem}
                    theme="vs-dark"
                    options={{ minimap: { enabled: false }, fontSize: 16, automaticLayout: true, padding: { top: 20, bottom: 20 }, fontFamily: 'JetBrains Mono, Menlo, monospace', wordWrap: 'on' }}
                    onChange={(val) => setProblem(val || '')}
                  />
                  <div className="absolute bottom-6 right-6 lg:bottom-10 lg:right-10 z-10">
                     <button onClick={generate} disabled={isLoading || !problem} className="h-14 lg:h-16 px-10 lg:px-12 bg-white text-black hover:bg-zinc-200 rounded-[20px] lg:rounded-[22px] text-xs lg:text-sm font-black transition-all flex items-center gap-3 shadow-2xl active:scale-95 disabled:bg-zinc-900 disabled:text-zinc-700">
                       {isLoading ? <Loader2 className="w-4 h-4 animate-spin"/> : <Sparkles className="w-4 h-4" />}
                       <span className="hidden xs:inline uppercase">Analyze Now</span>
                     </button>
                  </div>
               </div>
            </motion.div>

            {/* AI Output */}
            <AnimatePresence mode="wait">
              {response && (
                <motion.div initial={{ y: 60, opacity: 0 }} animate={{ y: 0, opacity: 1 }} className="space-y-8 pt-6">
                  <div className="flex items-center justify-between px-4">
                    <div className="flex items-center gap-4">
                      <div className="w-10 h-10 lg:w-12 lg:h-12 rounded-2xl bg-blue-500/10 border border-blue-500/20 flex items-center justify-center"><Sparkles className="w-5 h-5 text-blue-500" /></div>
                      <div><h2 className="text-white text-lg lg:text-xl font-black italic tracking-tighter uppercase">AI Feedback</h2><p className="text-[10px] font-bold text-blue-500/60 uppercase tracking-widest">{provider} Engine</p></div>
                    </div>
                    <button className="p-3 bg-zinc-900 border border-zinc-800 rounded-xl text-zinc-500 hover:text-white transition-all"><Copy className="w-4 h-4"/></button>
                  </div>

                  <div className="p-8 lg:p-14 rounded-[30px] lg:rounded-[50px] bg-zinc-900/30 border border-white/5 shadow-inner backdrop-blur-3xl overflow-x-auto">
                     <div className="whitespace-pre-wrap font-mono text-sm lg:text-[16px] text-zinc-300 antialiased leading-[1.8] prose prose-invert max-w-none">
                         {response}
                     </div>
                  </div>
                </motion.div>
              )}
            </AnimatePresence>

          </div>
        </div>

        {/* Global Footer (Adaptive Mobile/Desktop) */}
        <div className="fixed bottom-6 left-1/2 -translate-x-1/2 flex items-center gap-4 lg:gap-10 p-3 lg:px-10 lg:py-4 bg-black/90 backdrop-blur-2xl border border-white/10 rounded-full z-50 shadow-2xl max-w-[90vw] overflow-hidden">
          <div className="flex items-center gap-2">
             <div className="w-2 h-2 rounded-full bg-blue-500 shadow-[0_0_12px_rgba(59,130,246,0.8)]" />
             <span className="text-[9px] lg:text-[10px] text-white font-black tracking-widest uppercase truncate">Active</span>
          </div>
          <div className="w-px h-4 bg-zinc-800" />
          <div className="flex items-center gap-6 lg:gap-10 overflow-hidden">
            <div className="hidden sm:flex flex-col items-start">
               <span className="text-[8px] font-bold text-zinc-600 uppercase mb-0.5">Model</span>
               <span className="text-[10px] text-zinc-400 font-bold uppercase truncate max-w-[80px]">{provider}</span>
            </div>
            <div className="flex flex-col items-start">
               <span className="text-[8px] font-bold text-zinc-600 uppercase mb-0.5 whitespace-nowrap">Complexity</span>
               <span className="text-[10px] text-blue-500 font-bold uppercase">{detectedComplexity || '---'}</span>
            </div>
            <div className="hidden xs:flex gap-4 text-zinc-700 border-l border-zinc-800 pl-6">
              <Terminal className="w-3 h-3 hover:text-blue-500 transition-colors" />
              <Code2 className="w-3 h-3 hover:text-blue-500 transition-colors" />
            </div>
          </div>
        </div>
      </main>

      <style jsx global>{`
        .custom-scrollbar::-webkit-scrollbar { width: 0px; }
        .custom-scrollbar { scrollbar-width: none; }
        .scrollbar-hide::-webkit-scrollbar { display: none; }
        .scrollbar-hide { -ms-overflow-style: none; scrollbar-width: none; }
        @media (max-width: 640px) { h1 { font-size: 1.1rem !important; } }
      `}</style>
    </div>
  );
}
