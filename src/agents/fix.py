from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser

def fix_agent(state):
    llm=state["llm"]
    prompt=ChatPromptTemplate.from_template("""
    You are the Fix Agent.
    Suggest safe fixes for the reported issues.
    Only output improved code snippets or precise changes.
    Issues:
    {issues}
    Code:
    {code}
    """)
    chain=prompt|llm|StrOutputParser()
    fixes={}
    for f,c in state["code_diffs"].items():
        issues="\n".join([state.get("bugs",{}).get(f,""),state.get("security",{}).get(f,""),state.get("quality",{}).get(f,"")])
        fixes[f]=chain.invoke({"issues":issues,"code":c})
    return {"fixes":fixes}
