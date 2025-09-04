from langgraph.graph import StateGraph, END
from agents.extractor import extractor_agent
from agents.bug_hunter import bug_hunter_agent
from agents.style_quality import style_quality_agent
from agents.security import security_agent
from agents.critic import critic_agent
from agents.fix import fix_agent
from agents.test import test_agent
from agents.docs import docs_agent
from agents.labeler import labeler_agent
from agents.judge import judge_agent

def build_graph():
    g=StateGraph(dict)
    g.add_node("extractor",extractor_agent)
    g.add_node("bug_hunter",bug_hunter_agent)
    g.add_node("style_quality",style_quality_agent)
    g.add_node("security",security_agent)
    g.add_node("critic",critic_agent)
    g.add_node("fix",fix_agent)
    g.add_node("test",test_agent)
    g.add_node("docs",docs_agent)
    g.add_node("labeler",labeler_agent)
    g.add_node("judge",judge_agent)
    g.set_entry_point("extractor")
    g.add_edge("extractor","bug_hunter")
    g.add_edge("extractor","style_quality")
    g.add_edge("extractor","security")
    g.add_edge("bug_hunter","critic")
    g.add_edge("style_quality","critic")
    g.add_edge("security","critic")
    g.add_edge("critic","fix")
    g.add_edge("critic","test")
    g.add_edge("critic","docs")
    g.add_edge("critic","labeler")
    g.add_edge("fix","judge")
    g.add_edge("test","judge")
    g.add_edge("docs","judge")
    g.add_edge("labeler","judge")
    g.add_edge("judge",END)
    return g.compile()
