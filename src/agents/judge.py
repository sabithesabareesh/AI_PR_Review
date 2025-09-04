def judge_agent(state):
    github = state["github"]
    repo = state["repo"]
    pr = state["pr"]

    bugs = state.get("bugs", {})
    sec = state.get("security", {})
    ql = state.get("quality", {})

    status = "SAFE"
    if any(bugs.values()) or any(sec.values()):
        status = "CRITICAL"
    elif any(ql.values()):
        status = "MINOR"

    md = f"## AI Review\nStatus: {status}\n"
    for f in state.get("code_diffs", {}):
        md += f"\n### {f}\n"
        if bugs.get(f): md += f"- Bugs: {bugs[f]}\n"
        if sec.get(f): md += f"- Security: {sec[f]}\n"
        if ql.get(f): md += f"- Quality: {ql[f]}\n"
        if state.get("fixes", {}).get(f): md += f"- Fix: {state['fixes'][f]}\n"
        if state.get("tests", {}).get(f): md += f"- Tests: {state['tests'][f]}\n"
        if state.get("docs", {}).get(f): md += f"- Docs: {state['docs'][f]}\n"

    if state.get("critic"): md += f"- Critic: {state['critic']}\n"
    if state.get("labels"): md += f"- Labels: {','.join(state['labels'])}\n"

    github.comment_on_pr(repo, pr, md)
    if state.get("labels"): github.add_labels(repo, pr, state["labels"])
    if status == "SAFE": github.merge_pr(repo, pr)

    return {"status": status}
