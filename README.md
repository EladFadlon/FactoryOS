# FactoryOS

An agentic manufacturing simulation: a simulated wooden-furniture factory (desk, chair, shelf) run by a team of AI agents — orders, production planning, maintenance, procurement and a supervisor — with a live dashboard for the factory manager.

> Status: Phase 0 — setup. See `docs/devlog.md` for the latest progress.

## Core idea
Code computes, agents decide. The simulation, scheduling algorithms and database are plain, tested code. Agents are invoked only on events, choose between options, and explain their decisions.

## Architecture
```
simulation/  SimPy digital twin: machines, queues, failures, suppliers, event bus
backend/     FastAPI + PostgreSQL: REST API, WebSocket event stream
agents/      LangGraph agents: orders, planning, maintenance, procurement, supervisor
mcp_server/  MCP server exposing factory actions as tools
frontend/    React + Vite + TypeScript dashboard for the factory manager
config/      factory.yaml — machines, products, BOMs, suppliers
docs/        plan, devlog, ideas, ADRs
```

## Quick start (target)
```bash
cp .env.example .env      # add your free API keys
docker compose up         # db + backend + frontend
```

## Stack
Python 3.12 · SimPy · FastAPI · SQLAlchemy · PostgreSQL · LangGraph · MCP · Gemini (free tier) / OpenRouter / Ollama · React · Recharts · Langfuse · Docker · GitHub Actions
