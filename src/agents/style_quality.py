from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser

def style_quality_agent(state):
    llm = state["llm"]
    prompt = ChatPromptTemplate.from_template("""
    You are the Style & Quality Agent.
    Review the code for:
    - Code style issues
    - Readability
    - Maintainability
    Output ONLY issues in bullet points.
    Code:
    {code}
    """)
    chain = prompt | llm | StrOutputParser()

    quality = {}
    for file, code in state["code_diffs"].items():
        quality[file] = chain.invoke({"code": code})

    return {"quality": quality}
