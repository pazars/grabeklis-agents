from pydantic import BaseModel
from google.genai import types
from google.adk.agents import Agent
from .prompts import SUMMARY_SYSTEM_PROMPT


class Article(BaseModel):
    title: str
    url: str
    summary: str


class Summary(BaseModel):
    category: str
    articles: list[Article]


class ResponseSchema(BaseModel):
    category_summary: list[Summary]


config = types.GenerateContentConfig(
    max_output_tokens=8192,
)
root_agent = Agent(
    name="summary_agent",
    model="gemini-2.0-flash",
    description=("News article summary assistant"),
    instruction=(SUMMARY_SYSTEM_PROMPT),
    output_schema=ResponseSchema,
    generate_content_config=config,
)
