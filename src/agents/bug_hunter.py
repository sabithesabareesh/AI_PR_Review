from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser

def bug_hunter_agent(state):
    llm = state["llm"]
    prompt = ChatPromptTemplate.from_template("""
    You are the Bug Hunter Agent.
    Review the code for:
    - Functional bugs
    - Logic errors
    - Runtime issues
    Output ONLY bug findings in bullet points.
    Code:
    {code}
    """)
    chain = prompt | llm | StrOutputParser()

    bugs = {}
    for file, code in state["code_diffs"].items():
        bugs[file] = chain.invoke({"code": code})

    return {"bugs": bugs}
