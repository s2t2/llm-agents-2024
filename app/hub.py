# https://python.langchain.com/docs/integrations/llms/huggingface_hub
# https://python.langchain.com/docs/integrations/llms/huggingface_pipelines
# https://huggingface.co/models?pipeline_tag=text-generation&sort=downloads
#

import os

from dotenv import load_dotenv
from langchain_community.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

from app.prompts import QUERIES

load_dotenv()

HF_TOKEN = os.getenv("HUGGING_FACE_TOKEN")
REPO_ID = os.getenv("REPO_ID", default="google/flan-t5-xxl")

class HuggingFaceService:
    def __init__(self, repo_id=REPO_ID, temp=0.5, max_length=64, token=HF_TOKEN, system_template=None):
        self.token = token
        self.repo_id = repo_id
        self.temp = temp
        self.max_length = max_length

        # not a format string
        self.system_template = system_template or "You are a helpful and accurate assistant. Please answer the following question: {query}."

    @property
    def llm(self):
        return HuggingFaceHub(
            repo_id=self.repo_id, huggingfacehub_api_token=self.token,
            model_kwargs={"temperature": self.temp, "max_length": self.max_length}
        )

    @property
    def system_prompt(self):
        return PromptTemplate.from_template(self.system_template)

    def generate(self, query):
        llm_chain = LLMChain(prompt=self.system_prompt, llm=self.llm)
        return llm_chain.invoke({"query": query})


if __name__ == "__main__":


    hf = HuggingFaceService(repo_id=REPO_ID, temp=0.5, max_length=64)
    print("REPO:", hf.repo_id)
    print("TEMP:", hf.temp)
    print("MAX LENGTH:", hf.max_length)

    for query in QUERIES:
        print("---------")
        print(hf.generate(query))
