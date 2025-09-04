from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser

def security_agent(state):
    llm = state["llm"]
    prompt = ChatPromptTemplate.from_template("""
    You are the Security Agent.
    Review the code for:
    - Vulnerabilities
    - Insecure coding patterns
    - Dependency risks
    Output ONLY security issues in bullet points.
    Code:
    {code}
    """)
    chain = prompt | llm | StrOutputParser()

    security = {}
    for file, code in state["code_diffs"].items():
        security[file] = chain.invoke({"code": code})

    return {"security": security}
