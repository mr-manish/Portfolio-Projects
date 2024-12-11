import os,sys
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain.prompts.prompt import PromptTemplate
from agents.scrape_linkedin import linkedin_json
from agents.linkedin_lookup_agent import lookup

import warnings
warnings.filterwarnings("ignore")
 
load_dotenv()


summary_template = """
    Given the Linkedin information about a person which is in json format {information}:
    
    I want you to create 
    
    1. A short summary 
    2. Two interesting facts about them
    """


def main_func(name="Kosuru Sai Maneesh"):
    url = lookup(name=name)
    info = linkedin_json(url)
    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )
    llm = ChatOllama(model="llama3.2", temperature=0.1, num_predict=256)
    chain = summary_prompt_template | llm
    res = chain.invoke(input={"information": info})
    return res


if __name__ == "__main__":
    print(main_func())
