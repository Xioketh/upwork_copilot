upwork_copilot/
│
├── core/                   # The Brain: Contains all business logic
│   ├── __init__.py
│   ├── llm_engine.py       # Handles Gemini API connections & structured outputs
│   └── prompts.py          # Stores your strict rules and portfolio context
│
├── ui/                     # The Face: Streamlit interface
│   ├── __init__.py
│   └── app.py              # Handles button clicks and displaying data
│
├── .env                    # Environment variables (API Key)
├── requirements.txt        # Python dependencies
└── run.py                  # Entry point to start the app