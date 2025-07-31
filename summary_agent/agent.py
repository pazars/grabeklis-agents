from pydantic import BaseModel
from google.genai import types
from google.adk.agents import LlmAgent
from .prompts import SUMMARY_SYSTEM_PROMPT

class Article(BaseModel):
    uuid: str
    summary: str


class Summary(BaseModel):
    category: str
    articles: list[Article]


class ResponseSchema(BaseModel):
    summaries: list[Summary]


config = types.GenerateContentConfig(
    max_output_tokens=20000,
)


root_agent = LlmAgent(
    name="summary_agent",
    model="gemini-2.5-flash",
    description=("Ziņu rakstu kopsavilkumu aģents."),
    instruction=(SUMMARY_SYSTEM_PROMPT),
    output_schema=ResponseSchema,
    generate_content_config=config,
)