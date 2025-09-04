def judge_agent(state):
    g=state["github"];repo=state["repo"];pr=state["pr"]
    bugs,sec,ql=state.get("bugs",{}),state.get("security",{}),state.get("quality",{})
    status="SAFE"
    if any(bugs.values()) or any(sec.values()): status="CRITICAL"
    elif any(ql.values()): status="MINOR"
    md="## AI Review\nStatus:"+status+"\n"
    for f in state.get("code_diffs",{}):
        md+=f"\n### {f}\n"
        if bugs.get(f): md+="Bugs:"+bugs[f]+"\n"
        if sec.get(f): md+="Security:"+sec[f]+"\n"
        if ql.get(f): md+="Quality:"+ql[f]+"\n"
        if state.get("fixes",{}).get(f): md+="Fix:"+state["fixes"][f]+"\n"
        if state.get("tests",{}).get(f): md+="Tests:"+state["tests"][f]+"\n"
        if state.get("docs",{}).get(f): md+="Docs:"+state["docs"][f]+"\n"
    if state.get("critic"): md+="Critic:"+state["critic"]+"\n"
    if state.get("labels"): md+="Labels:"+",".join(state["labels"])+"\n"
    g.comment_on_pr(repo,pr,md)
    if state.get("labels"): g.add_labels(repo,pr,state["labels"])
    if status=="SAFE": g.merge_pr(repo,pr)
    return {"status":status}
