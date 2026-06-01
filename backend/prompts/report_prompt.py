from langchain_core.prompts import PromptTemplate

report_prompt = PromptTemplate(
    input_variables=[
        "profile",
        "contest_analysis",
        "problem_analysis",
        "activity_analysis",
        "suspicion_analysis"
    ],
    template="""
You are a Codeforces analytics assistant.

TASK:
- Write a short user overview
- Explain suspicion score reasoning

RULES:
- Do NOT add extra fields
- Do NOT hallucinate
- Be concise

INPUT:

Profile:
{profile}

Contest Analysis:
{contest_analysis}

Problem Analysis:
{problem_analysis}

Activity Analysis:
{activity_analysis}

Suspicion Analysis:
{suspicion_analysis}

OUTPUT FORMAT (STRICT JSON ONLY):

{{
  "overview": "short human readable summary",
  "suspicion_reasoning": [
    "reason 1",
    "reason 2",
    "reason 3"
  ]
}}
"""
)