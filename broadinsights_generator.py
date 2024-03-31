import os
import pandas as pd
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain.chat_models import ChatOpenAI
from langchain.llms.openai import OpenAI
from langchain_experimental.agents.agent_toolkits import create_python_agent
from langchain_experimental.tools import PythonREPLTool, PythonAstREPLTool
from langchain.agents import load_tools, initialize_agent, AgentType
from getpass import getpass
from langchain.agents.openai_functions_agent.base import (

    OpenAIFunctionsAgent

)
from langchain.memory import ConversationBufferMemory
from langchain.schema import SystemMessage
from langchain.agents import AgentExecutor

def insight(dset):
    llm = ChatOpenAI(model="gpt-3.5-turbo-0613", openai_api_key=os.environ.get("OPENAI_API_KEY"))
    memory = ConversationBufferMemory(memory_key="chat_history")
    dataset = {'df': pd.read_csv(dset, on_bad_lines='skip')}
    tools = [PythonAstREPLTool(locals=dataset)]
    tool_names = [tool.name for tool in tools]
    prompt = OpenAIFunctionsAgent.create_prompt(system_message=SystemMessage(
        content= f'You are an intelligent chatbot capable of running Python code to do dataset exploration and machine learning. You must provide broad insights for datasets, using tools to show statistical information and summarization of large-scale datasets. The dataset is {dset}'))
    agent = AgentExecutor.from_agent_and_tools(

        agent=OpenAIFunctionsAgent(llm=llm, prompt=prompt, tools=tools, verbose=True),
        tools=tools,
        verbose=True,
        memory=memory,
        handle_parsing_errors=True
    )

    query = "Please provide broad insights and trends for this dataset, including key statistical information as well as important information about the features. Be thorough."
    return agent.run(query)

