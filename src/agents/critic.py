from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser

def critic_agent(state):
    llm=state["llm"]
    prompt=ChatPromptTemplate.from_template("""
    You are the Critic Agent.
    Evaluate the other agents' findings:
    - Consistency
    - Coverage
    - Missing considerations
    Output a short critique.
    Findings:
    {findings}
    """)
    chain=prompt|llm|StrOutputParser()
    findings=str({"bugs":state.get("bugs",{}),"quality":state.get("quality",{}),"security":state.get("security",{})})
    return {"critic":chain.invoke({"findings":findings})}
