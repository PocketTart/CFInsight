from langchain.chat_models import ChatOpenAI

from core.config import settings

from prompts.report_prompt import report_prompt


class AIService:

    def __init__(self):

        self.llm = ChatOpenAI(
            openai_api_key=settings.MISTRAL_API_KEY,
            openai_api_base="https://api.mistral.ai/v1",
            model="ministral-8b-latest",
            temperature=0.2
        )

        self.chain = (
            report_prompt
            |
            self.llm
        )

    def generate_insights(
        self,
        profile,
        contest_analysis,
        problem_analysis,
        activity_analysis,
        suspicion_analysis
    ):

        response = self.chain.invoke(
            {
                "profile": profile,
                "contest_analysis":
                    contest_analysis,
                "problem_analysis":
                    problem_analysis,
                "activity_analysis":
                    activity_analysis,
                "suspicion_analysis":
                    suspicion_analysis
            }
        )

        return response.content