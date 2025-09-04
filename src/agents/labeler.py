def labeler_agent(state):
    labels=[]
    if any(state.get("bugs",{}).values()): labels.append("bug")
    if any(state.get("security",{}).values()): labels.append("security")
    if any(state.get("quality",{}).values()): labels.append("refactor")
    if not labels: labels.append("ai-approved")
    return {"labels":labels}
