def extractor_agent(state):
    files=state["github"].get_pull_request_files(state["repo"],state["pr"])
    return {"code_diffs":{f:c for f,c in files if c and f.endswith((".py",".js",".ts",".java",".go"))}}
