from agentops.agent import track_agent
from crewai import Agent
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os
from tools.browser_tools import BrowserTools
from tools.search_tools import SearchTools
from tools.sec_tools import SECTools
from langchain.tools.yahoo_finance_news import YahooFinanceNewsTool

load_dotenv()

model_name = os.getenv('MODEL_NAME')
llm = ChatOpenAI(model=model_name)


@track_agent(name='ResearchAnalystAgent')
class ResearchAnalystAgent:
    def __init__(self):
        self.agent = Agent(
            role='Staff Research Analyst',
            goal="""Being the best at gathering, interpreting data and amazing
            your customer with it""",
            backstory="""Known as the BEST research analyst, you're
            skilled in sifting through news, company announcements, 
            and market sentiments. Now you're working on a super 
            important customer""",
            verbose=True,
            llm=llm,
            tools=[
                BrowserTools.scrape_and_summarize_website,
                SearchTools.search_internet,
                SearchTools.search_news,
                YahooFinanceNewsTool(),
                SECTools.search_10q,
                SECTools.search_10k
            ]
        )
