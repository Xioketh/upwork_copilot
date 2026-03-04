# core/prompts.py

PORTFOLIO_CONTEXT = """
My Portfolio Projects (Categorized):

[AI AGENTS & LLM ENGINEERING]
1. OpsVoice: Real-time VoiceOps assistant. Tech: Gemini Multimodal Live API, WebSockets, Python. Value: Sub-500ms latency voice-to-server infrastructure control and JSON UI updates.
2. The Concierge: Autonomous MCP AI Agent. Tech: Next.js 15, Vercel AI SDK, Gemini 1.5 Flash, Node.js, SQLite, Zod. Value: Hallucination-free database operations, strict schema validation, and generative UI for hotel bookings.
3. InsightNode: Agentic GraphRAG Engine. Tech: Next.js 14, Neo4j, LangGraph, Ollama, Docker, Three.js. Value: Converts unstructured text into self-correcting 3D knowledge graphs using multi-agent architect/critic loops.
4. The Echo Directive: VoiceOps 3D Game AI. Tech: Godot 4, LangGraph, Python FastAPI, Pinecone, WebSockets. Value: Replaces NPC logic with autonomous agent reasoning, spatial navigation, and RAG-based lore retrieval.

[FULL-STACK SAAS & WEB]
5. ContentFodge: AI Content SaaS. Tech: Gemini 2.0 Flash, Streamlit, YouTube API. Value: Automated transcription and ghostwriting of YouTube videos into structured viral blogs and social threads.
6. wristTrade: iOS-First Trading PWA. Tech: Next.js, Tailwind, Binance WebSockets, Lightweight Charts. Value: Sub-second live crypto price streaming with a mobile-first, battery-efficient architecture.
7. Mentora-AI: Career Guidance SaaS. Tech: Next.js, Python FastAPI, Random Forest, KNN. Value: End-to-end platform using machine learning to predict optimal career paths for students.

[AUTOMATION & DATA ENGINEERING]
8. GhostCrawler: Stealth Web Scraper. Tech: Python, FastAPI, SeleniumBase. Value: Bypasses Cloudflare Turnstile and secure logins to extract 100% accurate data to Excel.
9. WhatsApp CRM: 2-Way Sheet Automation. Tech: Node.js, n8n, Google Sheets, Meta API, Docker. Value: Cost-free, bidirectional WhatsApp CRM hosted on a Linux VPS via Cloudflare Tunnels.
10. AutoLedger: Financial Automation. Tech: Python, Pandas, Streamlit. Value: Processes raw CSVs to auto-generate Excel reports with dynamic charts and margin calculations.

[COMPUTER VISION & RAG]
11. Real-Time Video Analytics: Object Tracking. Tech: YOLOv9, Deep SORT. Value: Live traffic and vehicle object detection for security and footfall analysis.
12. EquityLense: FinTech RAG Dashboard. Tech: Python, Gemini AI, Streamlit. Value: PDF extraction to automatically calculate complex financial metrics (EPS, NVPS) from interim reports.
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
- No Fluff or Desperation: Get straight to the point. Do NOT use filler phrases like 'I have read your requirements,' 'I fully understand,' 'I promise to,' or 'Please consider my proposal.'
- No Questions: Do NOT ask any questions about the project or job description in this proposal.
- Keep it simple: Do not explain the development process, step-by-step plans, or list out technologies.
- Tone: Confident, direct, and professional. State clearly that I am fully capable of completing this project successfully based on my past work.
- Relevant Projects: Highlight the matching projects. Format this strictly as a bulleted list using "- ". Example: "- [Project Name]: [One very brief sentence explaining alignment]". Do absolutely no large descriptions.
- Call to Action: End by simply telling the client to send me a message so we can discuss the details further.
- Sign-off: End the proposal exactly with:
  Best regards,
  Kethaka Ranasinghe
- P.S. Line: Add a compelling "P.S." line at the very bottom (after the sign-off). Make it highly relevant to the job if possible, or use a strong default like "P.S. I specialize in fast turnarounds without sacrificing quality."
"""