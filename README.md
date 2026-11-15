# FactoryOS

An agentic manufacturing simulation: a simulated PCB assembly factory — one SMT line (paste printer, 2× pick & place, reflow oven, AOI, functional test, rework) producing a dev board, a sensor module and a power supply — run by a team of AI agents (orders, production planning, maintenance, procurement, supervisor) with a live dashboard for the factory manager.

> Status: Phase 0 — setup. See `docs/devlog.md` for the latest progress.

## Core idea
Code computes, agents decide. The simulation, scheduling algorithms and database are plain, tested code. Agents are invoked only on events, choose between options, and explain their decisions.

## How success is measured
The factory is judged on two numbers:
- **On-time delivery** — % of orders shipped by their promised date.
- **Profit** — revenue from shipped boards minus chips and materials, repairs, scrapped boards and late-delivery penalties.

**Do the agents actually help?** Every scenario runs twice with the same random seed: once with the AI agents, and once in the background with simple rule-based policies (e.g. "reorder from the cheap supplier when stock drops below 100"). The baseline run uses no LLM, so it is fast and free. The dashboard shows only the result: the improvement in each KPI, as a percentage.

## The factory
- **Order flow:** customer order → Orders agent accepts, rejects or proposes a new date → Planning agent schedules it → Procurement agent checks the warehouse and buys missing chips → boards go through the SMT line → Maintenance agent watches machine health → the order ships, on time or late. The Supervisor resolves conflicts between agents.
- **Money:** each product has a material cost and a customer price (starting values in ₪ per board: sensor module 30 / 50, dev board 40 / 70, power supply 55 / 90). Late penalty: 2% of order value per day late, capped at 20%.
- **Warehouse:** stock per chip type, purchases in transit with arrival dates, stock reserved for open orders.
- **Suppliers:** cheap, slow distributor vs. fast broker at ~3× the price. Purchases above 20,000 ₪ need manager approval.
- **Crises:** chip shortage, reflow oven drift → yield drop, huge rush order.

## Dashboard (planned)
| Screen | What it shows |
|---|---|
| Control room | The 7 stations of the SMT line, colored by state (working / waiting / down), with boards moving between them |
| Orders | Every order and its status: on time, at risk, late |
| Warehouse | Stock, purchases in transit, expected arrival |
| Decision feed | Every agent decision in plain language, with its reason |
| Approvals | Purchases above 20,000 ₪ waiting for the manager: approve / reject |
| KPIs | On-time %, profit, scrap rate, improvement vs. baseline |

Special features:
- **Crisis button:** trigger a chip shortage, an oven failure or a rush order and watch the agents react live. Also available in view-only mode, with a click limit to protect the free LLM quota.
- **Ask the factory:** a chat that answers questions like "why is order 17 late?" from what actually happened.

## Architecture
```
simulation/  SimPy digital twin: machines, queues, failures, suppliers, event bus
backend/     FastAPI + PostgreSQL: REST API, WebSocket event stream
scheduler_cpp/ C++17 scheduling engine, exposed to Python via pybind11
agents/      LangGraph agents: orders, planning, maintenance, procurement, supervisor
mcp_server/  MCP server exposing factory actions as tools
frontend/    React + Vite + TypeScript dashboard for the factory manager
config/      factory.yaml — machines, products, BOMs, suppliers, prices
docs/        plan, devlog, ideas, ADRs
```

## Quick start (target)
```bash
cp .env.example .env      # add your free API keys
docker compose up         # db + backend + frontend
```

## Stack
Python 3.12 · C++17 · pybind11 · CMake · GoogleTest · SimPy · FastAPI · SQLAlchemy · PostgreSQL · LangGraph · MCP · Gemini (free tier) / OpenRouter / Ollama · React · Recharts · Langfuse · Docker · GitHub Actions
