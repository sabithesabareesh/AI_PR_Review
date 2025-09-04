from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser

def test_agent(state):
    llm = state["llm"]
    prompt = ChatPromptTemplate.from_template("""
    You are the Test Agent.
    Generate concise, high-value unit tests for the code.
    Return ONLY test code.
    Code:
    {code}
    """)
    chain = prompt | llm | StrOutputParser()

    tests = {}
    for file, code in state["code_diffs"].items():
        tests[file] = chain.invoke({"code": code})

    return {"tests": tests}
