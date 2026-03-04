# ui/app.py
import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import streamlit as st
from core.llm_engine import UpworkEngine

# Initialize the engine once
@st.cache_resource
def get_engine():
    return UpworkEngine()

engine = get_engine()

def render_ui():
    st.set_page_config(page_title="Upwork Copilot", layout="wide")
    st.title("Copilot")

    # Session State Management
    if "analysis_data" not in st.session_state:
        st.session_state.analysis_data = None
    if "proposal_text" not in st.session_state:
        st.session_state.proposal_text = None

    # Step 1: Input
    job_desc = st.text_area("Paste Description:", height=200)

    if st.button("1. Analyze"):
        if job_desc:
            with st.spinner("Analyzing job..."):
                try:
                    # Returns a Pydantic object
                    analysis = engine.analyze_job(job_desc) 
                    # Convert to dict for easy storage/passing
                    st.session_state.analysis_data = analysis.model_dump() 
                    st.session_state.proposal_text = None # Reset previous proposal
                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            st.warning("Please paste a job description.")

    # Step 2: Review Analysis
    if st.session_state.analysis_data:
        data = st.session_state.analysis_data
        st.markdown("---")
        st.subheader("Analysis")
        
        # 1. Job Explanation
        st.markdown(f"**What is this about?**\n\n{data['job_explanation']}")
        
        # 2. Layout for Alignment and Projects
        col1, col2 = st.columns(2)
        with col1:
            if data['is_aligned']:
                st.markdown(f"**Skill Alignment: MATCH**\n\n{data['alignment_reason']}")
            else:
                st.markdown(f"**Skill Alignment: MISMATCH**\n\n{data['alignment_reason']}")
            
            st.markdown(f"**Budget Assessment:**\n{data['budget_assessment']}")
            
        with col2:
            st.markdown("**Matching Projects:**")
            if data['matching_projects']:
                for proj in data['matching_projects']:
                    st.write(f"- {proj}")
            else:
                st.write("No direct matching projects found.")
                
        st.markdown("---")
        
        # 3. Layout for Gaps and Red Flags
        col3, col4 = st.columns(2)
        with col3:
            if data['skill_gaps']:
                st.markdown("**Skill Gaps Detected:**")
                for gap in data['skill_gaps']:
                    st.write(f"- {gap}")
            else:
                st.markdown("**No major skill gaps detected.**")
                
        with col4:
            if data['red_flags']:
                st.markdown("**RED ALERTS:**")
                for flag in data['red_flags']:
                    st.write(f"- {flag}")
            else:
                st.markdown("**No red flags detected.**")
                
        st.markdown("---")
        
        # Step 3: Generate Proposal Button
        st.subheader("Draft Proposal")
        
        # Add the text input for the client's name
        client_name = st.text_input("Client Name (Optional - leave blank for 'Hi there'):", placeholder="e.g., John")
        
        if st.button("2. Generate Proposal", type="primary"):
            with st.spinner("Drafting your no-fluff proposal..."):
                try:
                    # Pass the client_name to the engine
                    proposal = engine.generate_proposal(job_desc, st.session_state.analysis_data, client_name)
                    st.session_state.proposal_text = proposal
                except Exception as e:
                    st.error(f"Error: {e}")

    # Step 4: Output
    if st.session_state.proposal_text:
        st.markdown("---")
        st.subheader("Final Proposal (Ready to Copy)")
        # Increased height so you can easily read the P.S. line without scrolling too much
        st.text_area("Copy and paste this directly into Upwork:", value=st.session_state.proposal_text, height=300)

render_ui()