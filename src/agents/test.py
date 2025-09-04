from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser

def test_agent(state):
    llm=state["llm"]
    prompt=ChatPromptTemplate.from_template("""
    You are the Test Agent.
    Propose unit tests for the given code.
    Focus on edge cases and correctness.
    Code:
    {code}
    """)
    chain=prompt|llm|StrOutputParser()
    tests={}
    for f,c in state["code_diffs"].items():
        tests[f]=chain.invoke({"code":c})
    return {"tests":tests}
