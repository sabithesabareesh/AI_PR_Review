from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser

def critic_agent(state):
    llm = state["llm"]
    prompt = ChatPromptTemplate.from_template("""
    You are the Critic Agent.
    Review findings from Bug Hunter, Security, and Style Agents.
    Identify:
    - Gaps
    - False positives
    - Areas needing more clarity
    Output a concise critique in bullet points.
    Findings:
    {findings}
    """)
    chain = prompt | llm | StrOutputParser()

    findings = str({
        "bugs": state.get("bugs", {}),
        "security": state.get("security", {}),
        "quality": state.get("quality", {})
    })

    return {"critic": chain.invoke({"findings": findings})}
