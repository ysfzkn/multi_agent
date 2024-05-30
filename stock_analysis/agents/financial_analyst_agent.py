from agentops.agent import track_agent
from crewai import Agent
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os
from tools.browser_tools import BrowserTools
from tools.calculator_tools import CalculatorTools
from tools.search_tools import SearchTools
from tools.sec_tools import SECTools

load_dotenv()

model_name = os.getenv('MODEL_NAME')
llm = ChatOpenAI(model=model_name)


@track_agent(name='FinancialAnalystAgent')
class FinancialAnalystAgent:
    def __init__(self):
        self.agent = Agent(
            role='The Best Financial Analyst',
            goal="""Impress all customers with your financial data 
            and market trends analysis""",
            backstory="""The most seasoned financial analyst with 
            lots of expertise in stock market analysis and investment
            strategies that is working for a super important customer.""",
            verbose=True,
            llm=llm,
            tools=[
                BrowserTools.scrape_and_summarize_website,
                SearchTools.search_internet,
                CalculatorTools.calculate,
                SECTools.search_10q,
                SECTools.search_10k
            ]
        )
