from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser

def docs_agent(state):
    llm=state["llm"]
    prompt=ChatPromptTemplate.from_template("""
    You are the Docs Agent.
    Suggest documentation improvements for the given code.
    Focus on clarity, API usage, and maintainability.
    Code:
    {code}
    """)
    chain=prompt|llm|StrOutputParser()
    docs={}
    for f,c in state["code_diffs"].items():
        docs[f]=chain.invoke({"code":c})
    return {"docs":docs}
