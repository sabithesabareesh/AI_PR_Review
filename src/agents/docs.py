from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser

def docs_agent(state):
    llm = state["llm"]
    prompt = ChatPromptTemplate.from_template("""
    You are the Docs Agent.
    Improve documentation for the code.
    Add missing docstrings and inline comments where needed.
    Output ONLY doc improvements.
    Code:
    {code}
    """)
    chain = prompt | llm | StrOutputParser()

    docs = {}
    for file, code in state["code_diffs"].items():
        docs[file] = chain.invoke({"code": code})

    return {"docs": docs}
