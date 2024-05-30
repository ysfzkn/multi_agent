from agentops.agent import track_agent
from crewai import Agent
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os
from tools.browser_tools import BrowserTools
from tools.calculator_tools import CalculatorTools
from tools.search_tools import SearchTools
from langchain.tools.yahoo_finance_news import YahooFinanceNewsTool

load_dotenv()

model_name = os.getenv('MODEL_NAME')
llm = ChatOpenAI(model=model_name)


@track_agent(name='InvestmentAdvisorAgent')
class InvestmentAdvisorAgent:
    def __init__(self):
        self.agent = Agent(
            role='Private Investment Advisor',
            goal="""Impress your customers with full analyses over stocks
            and complete investment recommendations""",
            backstory="""You're the most experienced investment advisor
            and you combine various analytical insights to formulate
            strategic investment advice. You are now working for
            a super important customer you need to impress.""",
            verbose=True,
            llm=llm,
            tools=[
                BrowserTools.scrape_and_summarize_website,
                SearchTools.search_internet,
                SearchTools.search_news,
                CalculatorTools.calculate,
                YahooFinanceNewsTool()
            ]
        )
