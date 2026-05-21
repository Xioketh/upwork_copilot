# core/prompts.py

PORTFOLIO_CONTEXT = """
My Portfolio Projects (Categorized):

[AI AGENTS & LLM ENGINEERING]
1. OpsVoice: Real-time VoiceOps assistant. Tech: Gemini Multimodal Live API, WebSockets, Python. Value: Sub-500ms latency voice-to-server infrastructure control and JSON UI updates. Loom Video: https://www.loom.com/share/8d4c33d6254740b4b7a5ea8ffa48958d
2. The Concierge: Autonomous MCP AI Agent. Tech: Next.js 15, Vercel AI SDK, Node.js, SQLite, Zod. Value: Hallucination-free database operations, strict schema validation, and generative UI for bookings. Loom Video: https://www.loom.com/share/1e3c08b904664aa8aee59527c7be1095
3. InsightNode: Agentic GraphRAG Engine. Tech: Next.js 14, Neo4j, LangGraph, Ollama. Value: Converts text into 3D knowledge graphs.
4. The Echo Directive: VoiceOps 3D Game AI. Tech: Godot 4, LangGraph, Python FastAPI, WebSockets. Value: Replaces NPC logic with autonomous agent reasoning.
5. OmniReel: Autonomous AI Video Pipeline. Tech: Node.js, n8n, FFmpeg, Docker, BullMQ, Gemini, ElevenLabs. Value: Headless orchestration converting a Telegram prompt into a fully generated, programmatically animated (Ken Burns) cinematic vertical video. Loom Video: https://www.loom.com/share/167b205f6e454627a201181f1bda3527
6. ClawRouter: AI Frontline Triage System. Tech: OpenClaw, Gemini, Next.js, Node.js, Docker, Telegram API. Value: Autonomous Telegram agent that categorizes queries and extracts high-value B2B lead data (Email, Size, Use Case) directly into a Dockerized Next.js database via strict JSON tool execution. Loom Video: https://www.loom.com/share/ed60012a57214f8e8cb10b71ea27a52f
7. Autonomous Market Intelligence Agent: Multi-Agent Competitor Tracker. Tech: OpenManus, OpenClaw, Docker, Playwright stealth, Gemini API. Value: Deploys isolated sandboxes bypassing anti-bot protections to dynamically parse messy DOM text into strict JSON schemas, delivering synthesized intelligence reports via Telegram. Loom Video: https://www.loom.com/share/a5111a6583b64adeae3e2688630783b8

[FULL-STACK SAAS & WEB]
8. ContentFodge: AI Content SaaS. Tech: Gemini 2.0 Flash, Streamlit, YouTube API. Value: Automated transcription and ghostwriting of YouTube videos into viral blogs.
9. wristTrade: iOS-First Trading PWA. Tech: Next.js, Tailwind, Binance WebSockets. Value: Sub-second live crypto price streaming.
10. Mentora-AI: Career Guidance SaaS. Tech: Next.js, Python FastAPI, Machine Learning. Value: End-to-end platform predicting optimal career paths.

[AUTOMATION & DATA ENGINEERING]
11. GhostCrawler: Stealth Web Scraper. Tech: Python, FastAPI, SeleniumBase. Value: Bypasses Cloudflare Turnstile and secure logins to extract 100% accurate data to Excel. Loom Video: https://www.loom.com/share/a8225a67759a4afa920bdc9e5ea13e89
12. WhatsApp CRM: 2-Way Sheet Automation. Tech: Python, Node.js, n8n, Google Sheets, Meta API. Value: Cost-free, bidirectional WhatsApp CRM. Loom Video: https://www.loom.com/share/6a04dde30f9c46afa9fd0a518643baf8
13. AutoLedger: Financial Automation. Tech: Python, Pandas, Streamlit. Value: Processes raw CSVs to auto-generate Excel reports with dynamic charts. Loom Video: https://www.loom.com/share/21a9f2d155cf4f0a8a5aac00517b162b
14. Bet365 Scraper: High-Security Data Extraction. Tech: Python, SeleniumBase UC Mode, WebGL Spoofing. Value: Bypasses infinite loading spinners using hardware-level clicks and positional parsing.
15. lead-scraper-pro: Automated B2B Lead Pipeline. Tech: Python, Playwright stealth, Regex, n8n. Value: Deduplicates multi-source leads, performs deep-site stealth enrichment for emails, and automatically pipes data to Google Sheets via n8n webhook. Loom Video: https://www.loom.com/share/dc042442dd5f495bb4c84d296e2cdb38
16. MailForge: AI-Powered Workspace Copilot. Tech: Google Apps Script (GAS), Gemini API, Tailwind, Gmail/Sheets API. Value: Serverless extension with a custom UI that batch-processes scraped leads to auto-generate highly personalized cold email drafts natively in Gmail. Loom Video: https://www.loom.com/share/ebaf364939c642da8507f8e18eab9ee6

[COMPUTER VISION & RAG]
17. Real-Time Video Analytics: Object Tracking. Tech: YOLOv9, Deep SORT. Value: Live traffic and vehicle object detection.
18. EquityLense: FinTech RAG Dashboard. Tech: Python, Streamlit. Value: PDF extraction to automatically calculate complex financial metrics (EPS, NVPS). Loom Video: https://www.loom.com/share/72c106516ac0411692358ae7b4fd083e
"""

JOB_ANALYZE_DETAILS = """
Exact Details to fill:
1. job_explanation: A clear, concise explanation of what the client wants to build or achieve.
2. is_aligned: Boolean (True/False) indicating if I have the core skills for this.
3. alignment_reason: A brief sentence explaining why it aligns or doesn't align with my skills.
4. matching_projects: A list of best matching projects from my portfolio limit to best four. Format strictly as "Project Name: Simple note of why it matches".
5. skill_gaps: A list of any required skills or technologies mentioned in the job post that are missing from my portfolio, along with a "Hard" or "Easy" label indicating the difficulty of filling each skill gap.Format strictly as: "Gap simple description: Hard or Easy"
6. budget_assessment: An assessment of the client's budget (if mentioned) vs the complexity of the task.
7. red_flags: A list of any red alerts (e.g., toxic language, highly unrealistic expectations, extremely low budget for the tech stack). Leave the list empty if there are no red flags.
"""

PROPOSAL_STRICT_RULES = """
Strict Rules to follow:
- NO MARKDOWN: Do NOT use markdown formatting like **bold** or *italics*. The output must be pure plain text ready to copy and paste directly into Upwork.
- Greeting: Use the EXACT greeting provided in the prompt instructions.
- Exact Structure Order: 
  1. Greeting
  2. The Loom Hook
  3. Relevant Project Details (separated by blank lines)
  4. Capability Statement
  5. Call to Action
  6. Sign-off
  7. P.S. Line
- THE LOOM HOOK (CRITICAL): Start the very first line of the body immediately with the text: "Similar system I recently deployed: [Insert Exact Loom Video URL]" using the single best matching video from my portfolio. Do not add any conversational filler before it.
- Relevant Project Details: Below the hook, detail 1 to 2 matching projects from my portfolio. Do NOT use bullet points (- or *). Write them as standalone paragraphs separated by a single blank line. Format exactly as: "[Project Name]: [One very brief sentence explaining alignment]."
- Capability Statement: Below the project details, state clearly and confidently that I am fully capable of completing this specific project successfully based on my past work.
- Call to Action: Follow immediately with a direct request telling the client to send me a message so we can discuss the details further.
- No Fluff or Desperation: Get straight to the point. Do NOT use filler phrases like 'I have read your requirements,' 'I fully understand,' or 'Please consider my proposal.'
- No Questions: Do NOT ask any questions about the project or job description in this proposal.
- Answer Client Questions: If the job description asks specific questions, answer them directly and concisely right before the capability statement.
- Sign-off: End the proposal exactly with:
  Best regards,
  Kethaka Ranasinghe
- P.S. Line: Add a compelling "P.S." line at the very bottom (after the sign-off). Make it highly relevant to the job's technical hurdles or edge cases.
"""
