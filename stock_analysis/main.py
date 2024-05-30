import os
from crewai import Crew
import agentops
from agents.financial_analyst_agent import FinancialAnalystAgent
from agents.research_analyst_agent import ResearchAnalystAgent
from agents.investment_advisor_agent import InvestmentAdvisorAgent
from stock_analysis_tasks import StockAnalysisTasks
import logging
from dotenv import load_dotenv
from util import pdf_exporter

load_dotenv()
logging.basicConfig(level=logging.DEBUG)
agentops.init(api_key=os.getenv('AGENTOPS_API_KEY'), auto_start_session=True)


class FinancialCrew:
    def __init__(self, company):
        self.company = company

    def run(self):
        tasks = StockAnalysisTasks()

        research_analyst_agent = ResearchAnalystAgent().agent
        financial_analyst_agent = FinancialAnalystAgent().agent
        investment_advisor_agent = InvestmentAdvisorAgent().agent

        research_task = tasks.research(research_analyst_agent, self.company)
        financial_task = tasks.financial_analysis(financial_analyst_agent)
        filings_task = tasks.filings_analysis(financial_analyst_agent)
        recommend_task = tasks.recommend(investment_advisor_agent)

        crew = Crew(
            agents=[
                research_analyst_agent,
                financial_analyst_agent,
                investment_advisor_agent
            ],
            tasks=[
                research_task,
                financial_task,
                filings_task,
                recommend_task
            ],
            verbose=True
        )

        result = crew.kickoff()
        return result


if __name__ == "__main__":
    print("## Welcome to Financial Analysis Crew")
    print('-------------------------------')
    """
    company = input(
        dedent("What is the company you want to analyze?"))
    """
    company = "Turkish Airlines"

    financial_crew = FinancialCrew(company)
    result = financial_crew.run()
    print("\n\n########################")
    print("## Here is the Report")
    print("########################\n")
    print(result)

    # Save the result as a PDF
    pdf_exporter.save_report_as_pdf(company_name=company, report_content=result)
    agentops.end_session("Success")
