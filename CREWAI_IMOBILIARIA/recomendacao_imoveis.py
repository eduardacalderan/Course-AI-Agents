from crewai_tools import CSVSearchTool 
from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI

load_dotenv(find_dotenv())

llm = ChatOpenAI(
  model="gpt-3.5-turbo-0125"
)

csv_imoveis = CSVSearchTool(
  csv="files/imoveis.csv",
)