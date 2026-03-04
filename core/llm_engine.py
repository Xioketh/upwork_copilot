import os
from google import genai
from pydantic import BaseModel
from dotenv import load_dotenv
from core.prompts import JOB_ANALYZE_DETAILS, PORTFOLIO_CONTEXT, PROPOSAL_STRICT_RULES

load_dotenv()

# Define structured output schema
class JobAnalysis(BaseModel):
    job_explanation: str
    is_aligned: bool
    alignment_reason: str
    matching_projects: list[str]
    skill_gaps: list[str]
    budget_assessment: str
    red_flags: list[str]

class UpworkEngine:
    def __init__(self):
        # The new SDK automatically picks up GEMINI_API_KEY from your .env file
        self.client = genai.Client()
        self.model_id = 'gemini-2.5-flash'

    def analyze_job(self, job_description: str) -> JobAnalysis:
        prompt = f"""
        You are an expert Upwork job analyzer. Review the following job description against my portfolio.
        
        {PORTFOLIO_CONTEXT}
        
        Job Description:
        {job_description}
        
        Analyze the job and provide the following:
        {JOB_ANALYZE_DETAILS}
        """
        
        # New SDK syntax for structured outputs
        response = self.client.models.generate_content(
            model=self.model_id,
            contents=prompt,
            config={
                "response_mime_type": "application/json",
                "response_json_schema": JobAnalysis.model_json_schema(),
                "temperature": 0.1
            }
        )
        return JobAnalysis.model_validate_json(response.text)

    def generate_proposal(self, job_description: str, analysis_data: dict, client_name: str = "") -> str:
        # Dynamically create the greeting
        greeting = f"Hi {client_name.strip()}," if client_name.strip() else "Hi there,"
        
        prompt = f"""
        Write a brief, highly concise Upwork proposal for the job description below in PLAIN TEXT.
        
        USE THIS EXACT GREETING: {greeting}
        
        Job Description: {job_description}
        
        Use this analysis to pick the right projects to highlight:
        {analysis_data}
        
        {PROPOSAL_STRICT_RULES}
        """


        response = self.client.models.generate_content(
            model=self.model_id,
            contents=prompt,
            config={
                "temperature": 0.4
            }
        )
        
        clean_text = response.text.replace("**", "").replace("*", "")
        
        return clean_text.strip()