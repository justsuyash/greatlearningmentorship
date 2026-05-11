# ABC Corp. Experimentation Platform

A mock experimentation platform demonstrating agentic workflows.

## Setup
```bash
pip install -r requirements.txt
export GOOGLE_API_KEY="your-key-here"
uvicorn app:app --reload
```

## Observability (LangSmith)
1. Get free API key at https://smith.langchain.com
2. Add to your environment:
   export LANGSMITH_API_KEY="ls__..."
3. Run as normal — all agent traces auto-appear in LangSmith
