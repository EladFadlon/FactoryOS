"""Session 5: first LangGraph graph — decide whether to accept an order.

No LLM yet: plain functions as nodes, a conditional edge for the decision.
check_capacity -> (boards <= capacity ? accept : escalate) -> END

Run:  uv run --with langgraph python simulation/playground/03_first_graph.py
"""
from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class OrderState(TypedDict):
    boards: int
    capacity: int
    decision: str

def check_capacity(state):
    return {"capacity" : 54}

def accept(state):
    return {"decision" : "accept"}

def escalate(state):
    return {"decision" : "escalate to manager"}

def route(state):
    if(state["boards"] <= state["capacity"]):
        return "accept"
    else: return "escalate"

def main():
   graph = StateGraph(OrderState)
   graph.add_node("check_capacity", check_capacity)
   graph.add_node("accept", accept)
   graph.add_node("escalate", escalate)
   graph.add_edge(START , "check_capacity")
   graph.add_conditional_edges("check_capacity", route , ["accept" , "escalate"])
   graph.add_edge("accept" , END)
   graph.add_edge("escalate" , END)
   app = graph.compile()
   print(app.invoke({"boards":30}))
   print(app.invoke({"boards":80}))

   
if __name__ == "__main__":
    main()
