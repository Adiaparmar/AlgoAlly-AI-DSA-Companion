import { NextRequest, NextResponse } from 'next/server';
import axios from 'axios';
import * as cheerio from 'cheerio';

export async function POST(req: NextRequest) {
  try {
    const { url } = await req.json();

    if (!url || (!url.includes('leetcode.com') && !url.includes('geeksforgeeks.org'))) {
      return NextResponse.json({ error: 'Please provide a valid LeetCode or GFG URL' }, { status: 400 });
    }

    // Try server-side scraping
    const response = await axios.get(url, {
      headers: {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
      }
    });

    const $ = cheerio.load(response.data);
    let title = '';
    let description = '';

    if (url.includes('geeksforgeeks.org')) {
      title = $('.problem-header-name').text().trim() || $('h1').first().text().trim();
      description = $('.problem-statement').text().trim();
    } else if (url.includes('leetcode.com')) {
      // NOTE: LeetCode uses dynamic React rendering. Basic cheerio won't get descriptions deeply.
      // We will extract the slug and encourage users to paste if it fails.
      title = url.split('/problems/')[1]?.split('/')[0] || 'LeetCode Problem';
      description = `LeetCode Problem: ${title}\n\n(Note: LeetCode requires authentication/cookies for deep scraping. Please paste the description here if needed.)`;
    }

    return NextResponse.json({ 
      title, 
      description: `${title}\n\n${description}`.trim() 
    });

  } catch (error: any) {
    console.error('Scraping Error:', error);
    return NextResponse.json({ error: 'Failed to access the link. Many platforms block automatic scraping. Please copy-paste manually.' }, { status: 500 });
  }
}
