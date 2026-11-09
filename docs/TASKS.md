# Tasks — quick checklist (full plan lives in the FactoryOS plan doc)

Pick ONE unchecked item per 60–90 min session.

## Phase 0 — Setup (Nov 9–22, 2026)
- [x] Project folder skeleton
- [ ] Public GitHub repo + first push
- [ ] Install Docker, Python 3.12, Node 22, uv
- [ ] SimPy tutorial (2h)
- [ ] LangGraph quickstart (3h)
- [ ] Gemini key (AI Studio) + OpenRouter key
- [ ] Apply for GitHub Student Pack (BGU email)

## Phase 1 — Simulation core (Nov 23 – Jan 3)
- [ ] Data model: product, BOM, machine, material, order
- [ ] Load config/factory.yaml
- [ ] SimPy machine process with job queue
- [ ] SMT route: paste print → pick & place → reflow → AOI → functional test (+ rework loop)
- [ ] AOI defects depend on reflow oven drift; rework or scrap
- [ ] Inventory consumption
- [ ] Random failures (MTBF, fixed seed)
- [ ] Simulated suppliers
- [ ] Unified event bus
- [ ] pytest for every component

## Phase 2 — Backend + DB (Jan 4 – Feb 28; exam period ≈ late Jan–Feb = maintenance mode, 1h/week)
- [ ] FastAPI skeleton + routers
- [ ] SQLAlchemy schema + Alembic
- [ ] Endpoints: orders, inventory, machines, events
- [ ] Simulation as background task (accelerated clock)
- [ ] WebSocket event stream
- [ ] API tests + CI

## Phase 3 — First agents + MCP (Mar 1 – Mar 28, semester break boost)
- [ ] MCP server with factory tools
- [ ] Model layer with fallback Gemini → OpenRouter → Ollama
- [ ] Orders agent (LangGraph)
- [ ] Inventory/procurement agent
- [ ] Event router → agents
- [ ] decisions table with rationale

## Phase 4 — Dashboard (Mar 29 – Apr 25, Passover break)
- [ ] React + Vite + TS skeleton
- [ ] Shop-floor screen
- [ ] Orders & inventory screen + charts
- [ ] Agent decision feed
- [ ] New order form

## Phase 5 — All agents + crises (Apr 26 – May 30)
- [ ] Planning agent (algorithm proposes 3 schedules, agent picks)
- [ ] Maintenance agent
- [ ] Supervisor
- [ ] Human approval (LangGraph interrupt) + dashboard button
- [ ] Scenarios: chip shortage, oven drift → yield drop, huge rush order
- [ ] LLM call counter + rate limiter
- [ ] C++: CMake + pybind11 skeleton callable from Python
- [ ] C++: port data structures (jobs, machines, routes)
- [ ] C++: implement scheduler + GoogleTest tests
- [ ] Parity test: same input → same schedule in Python and C++
- [ ] Benchmark 100 / 1,000 / 10,000 jobs, chart in README
- [ ] Build the C++ module in CI

## Phase 6 — Polish & present (May 31 – Jun 20)
- [ ] Langfuse self-hosted
- [ ] README with diagram + GIF
- [ ] 2-min demo video
- [ ] ADRs for major decisions
- [ ] CV line + LinkedIn post + interview answers
