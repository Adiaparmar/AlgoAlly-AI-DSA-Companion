import { NextRequest, NextResponse } from 'next/server';

export async function POST(req: NextRequest) {
  try {
    const { problem, mode, model, provider, temperature } = await req.json();

    if (!problem) {
      return NextResponse.json({ error: 'Problem content is required' }, { status: 400 });
    }

    if (provider === 'gemini') {
      const apiKey = process.env.GEMINI_API_KEY;
      if (!apiKey) return NextResponse.json({ error: 'Gemini API key not configured in environment' }, { status: 500 });
      
      const endpoint = `https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent?key=${apiKey}`;
      
      // Mode-to-System prompt logic
      const modePrompts: Record<string, string> = {
        "Hint": "Give ONE high-level hint. NO code. END your response with [COMPLEXITY: O(?)] where ? is the expected complexity.",
        "Test Cases": "Generate 5 test cases. END your response with [COMPLEXITY: N/A].",
        "Complexity": "Analyze time/space complexity. AT THE END, add a marker: [COMPLEXITY: O(N)] or [COMPLEXITY: O(N^2)] etc.",
        "Explain": "Explain algorithm step by step. NO code. END with [COMPLEXITY: O(?)].",
        "Code": "Write optimal solution. ALWAYS end with a single line: [COMPLEXITY: O(N)] (replace O(N) with actual complexity)."
      };
      
      const res = await fetch(endpoint, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          contents: [{
            parts: [{ text: `${modePrompts[mode]}\n\nPROBLEM:\n${problem}` }]
          }],
          generationConfig: {
            temperature: temperature || 0.2,
            maxOutputTokens: 2000
          }
        })
      });

      const data = await res.json();
      const content = data?.candidates?.[0]?.content?.parts?.[0]?.text;
      
      if (!content) throw new Error('Failed to get content from Gemini');
      
      return NextResponse.json({ content });

    } else {
      // OpenRouter integration
      const apiKey = process.env.OPENROUTER_API_KEY;
      if (!apiKey) return NextResponse.json({ error: 'OpenRouter API key not configured' }, { status: 500 });

      const modePrompts: Record<string, string> = {
        "Hint": "Give ONE hint. NO code. END with [COMPLEXITY: O(?)].",
        "Test Cases": "Generate 5 test cases. END with [COMPLEXITY: N/A].",
        "Complexity": "Analyze time/space. AT THE END, add [COMPLEXITY: O(N)] or similar.",
        "Explain": "Explain algorithm. NO code. END with [COMPLEXITY: O(?)].",
        "Code": "Write optimal solution. ALWAYS end with a single line: [COMPLEXITY: O(N)] (replace O(N) with actual complexity)."
      };

      const res = await fetch('https://openrouter.ai/api/v1/chat/completions', {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${apiKey}`,
          'Content-Type': 'application/json',
          'HTTP-Referer': 'https://github.com/Adiaparmar/AlgoAlly',
          'X-Title': 'AlgoAlly AI'
        },
        body: JSON.stringify({
          model: model,
          messages: [
            { role: 'system', content: modePrompts[mode] },
            { role: 'user', content: problem }
          ],
          temperature: temperature || 0.2
        })
      });

      const data = await res.json();
      return NextResponse.json({ content: data?.choices?.[0]?.message?.content });
    }
    
  } catch (error: any) {
    console.error('API Error:', error);
    return NextResponse.json({ error: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
