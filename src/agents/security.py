from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser

def security_agent(state):
    llm=state["llm"]
    prompt=ChatPromptTemplate.from_template("""
    You are the Security Agent.
    Review the code for:
    - Vulnerabilities
    - Insecure practices
    - Data leaks
    - Injection risks
    Output ONLY findings in bullet points.
    Code:
    {code}
    """)
    chain=prompt|llm|StrOutputParser()
    r={}
    for f,c in state["code_diffs"].items():
        r[f]=chain.invoke({"code":c})
    return {"security":r}
