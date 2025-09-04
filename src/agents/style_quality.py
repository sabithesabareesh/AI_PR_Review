from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser

def style_quality_agent(state):
    llm=state["llm"]
    prompt=ChatPromptTemplate.from_template("""
    You are the Style & Quality Agent.
    Review the code for:
    - Readability
    - Maintainability
    - Code smells
    - Performance issues
    Output ONLY findings in bullet points.
    Code:
    {code}
    """)
    chain=prompt|llm|StrOutputParser()
    q={}
    for f,c in state["code_diffs"].items():
        q[f]=chain.invoke({"code":c})
    return {"quality":q}
