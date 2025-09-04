import sys, os
from dotenv import load_dotenv
from gemini_client import get_llm
from github_utils import GitHubUtils
from graph import build_graph

load_dotenv()

if __name__=="__main__":
    repo=sys.argv[1]
    pr=int(sys.argv[2])
    state={
        "repo": repo,
        "pr": pr,
        "github": GitHubUtils(),
        "llm": get_llm()
    }
    final=build_graph().invoke(state)
    print("Final:",final.get("status"))
