# core/prompts.py

PORTFOLIO_CONTEXT = """
My Portfolio Projects (Categorized):

[AI AGENTS & LLM ENGINEERING]
1. OpsVoice: Real-time VoiceOps assistant. Tech: Gemini Multimodal Live API, WebSockets, Python. Value: Sub-500ms latency voice-to-server infrastructure control and JSON UI updates. Loom Video: https://www.loom.com/share/8d4c33d6254740b4b7a5ea8ffa48958d
2. The Concierge: Autonomous MCP AI Agent. Tech: Next.js 15, Vercel AI SDK, Node.js, SQLite, Zod. Value: Hallucination-free database operations, strict schema validation, and generative UI for bookings. Loom Video: https://www.loom.com/share/1e3c08b904664aa8aee59527c7be1095
3. InsightNode: Agentic GraphRAG Engine. Tech: Next.js 14, Neo4j, LangGraph, Ollama. Value: Converts text into 3D knowledge graphs. Loom Video: [INSERT_LOOM_LINK_HERE]
4. The Echo Directive: VoiceOps 3D Game AI. Tech: Godot 4, LangGraph, Python FastAPI, WebSockets. Value: Replaces NPC logic with autonomous agent reasoning. Loom Video: [INSERT_LOOM_LINK_HERE]

[FULL-STACK SAAS & WEB]
5. ContentFodge: AI Content SaaS. Tech: Gemini 2.0 Flash, Streamlit, YouTube API. Value: Automated transcription and ghostwriting of YouTube videos into viral blogs.
6. wristTrade: iOS-First Trading PWA. Tech: Next.js, Tailwind, Binance WebSockets. Value: Sub-second live crypto price streaming.
7. Mentora-AI: Career Guidance SaaS. Tech: Next.js, Python FastAPI, Machine Learning. Value: End-to-end platform predicting optimal career paths.

[AUTOMATION & DATA ENGINEERING]
8. GhostCrawler: Stealth Web Scraper. Tech: Python, FastAPI, SeleniumBase. Value: Bypasses Cloudflare Turnstile and secure logins to extract 100% accurate data to Excel. Loom Video: https://www.loom.com/share/a8225a67759a4afa920bdc9e5ea13e89
9. WhatsApp CRM: 2-Way Sheet Automation. Tech: Python, Node.js, n8n, Google Sheets, Meta API. Value: Cost-free, bidirectional WhatsApp CRM. Loom Video: https://www.loom.com/share/6a04dde30f9c46afa9fd0a518643baf8
10. AutoLedger: Financial Automation. Tech: Python, Pandas, Streamlit. Value: Processes raw CSVs to auto-generate Excel reports with dynamic charts. Loom Video: https://www.loom.com/share/21a9f2d155cf4f0a8a5aac00517b162b
11. Bet365 Scraper: High-Security Data Extraction. Tech: Python, SeleniumBase UC Mode, WebGL Spoofing. Value: Bypasses infinite loading spinners using hardware-level clicks and positional parsing.

[COMPUTER VISION & RAG]
12. Real-Time Video Analytics: Object Tracking. Tech: YOLOv9, Deep SORT. Value: Live traffic and vehicle object detection.
13. EquityLense: FinTech RAG Dashboard. Tech: Python, Streamlit. Value: PDF extraction to automatically calculate complex financial metrics (EPS, NVPS). Loom Video: https://www.loom.com/share/72c106516ac0411692358ae7b4fd083e
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
- No Fluff or Desperation: Get straight to the point. Do NOT use filler phrases like 'I have read your requirements,' 'I fully understand,' or 'Please consider my proposal.'
- No Questions: Do NOT ask any questions about the project or job description in this proposal.
- Answer Client Questions: If the job description asks specific questions, answer them directly and concisely. Format these answers clearly before the Call to Action.
- Keep it simple: Do not explain the development process, step-by-step plans, or list out technologies randomly.
- Tone: Confident, direct, and professional. State clearly that I am fully capable of completing this project successfully based on my past work.
- THE "SHOW, DON'T TELL" HOOK (CRITICAL): Do not just list matching projects. Instead, identify the SINGLE best matching project from my portfolio. Write a sentence explaining that I recently built a similar solution. Then, you MUST include the Loom Video link for that specific project. Format it exactly like this: "To give you a clear idea of how I build this, I recorded a quick walkthrough of a similar system I recently deployed: [Insert Exact Loom Video URL]"
- Secondary Matches: If there are 1 or 2 other relevant projects, list them briefly below the video link using a simple bullet point format "- [Project Name]: [One very brief sentence explaining alignment]". Do absolutely no large descriptions.
- Call to Action: End by simply telling the client to send me a message so we can discuss the details further.
- Sign-off: End the proposal exactly with:
  Best regards,
  Kethaka Ranasinghe
- P.S. Line: Add a compelling "P.S." line at the very bottom (after the sign-off). Make it highly relevant to the job if possible.
"""