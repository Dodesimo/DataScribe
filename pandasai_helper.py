import pandas as pd
from pandasai import SmartDataframe
from pandasai.llm import OpenAI
import os
import glob
import os.path
import pyimgur


def generateGraph(link, query):
    llm = OpenAI(api_token=os.environ.get("OPENAI_API_KEY"))
    df = pd.read_csv(link, skip_blank_lines=True)
    df = SmartDataframe(df, config={"llm": llm})
    df.chat(query)


def getImagePath():
    files = glob.glob('exports/charts/*')
    latest_file = max(files, key=os.path.getctime)
    return latest_file
