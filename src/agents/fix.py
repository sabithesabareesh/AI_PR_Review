from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser

def fix_agent(state):
    llm = state["llm"]
    prompt = ChatPromptTemplate.from_template("""
    You are the Fix Agent.
    Based on identified issues, propose safe fixes.
    Return ONLY fixed code suggestions.
    Issues:
    {issues}
    Code:
    {code}
    """)
    chain = prompt | llm | StrOutputParser()

    fixes = {}
    for file, code in state["code_diffs"].items():
        issues = "\n".join([
            state.get("bugs", {}).get(file, ""),
            state.get("security", {}).get(file, ""),
            state.get("quality", {}).get(file, "")
        ])
        fixes[file] = chain.invoke({"issues": issues, "code": code})

    return {"fixes": fixes}
