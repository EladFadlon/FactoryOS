# ADR 0002: Python core, C++ scheduling engine, TypeScript dashboard

Date: 2026-11-09
Status: Accepted

## Context
The agent and simulation ecosystems (LangGraph, SimPy, MCP SDK, FastAPI) are strongest in Python. The author studies Java, C and C++ in his degree. Production scheduling is the most compute-heavy part of the system.

## Decision
- Python for simulation, backend and agents.
- C++17 for the scheduling engine, exposed to Python via pybind11. Written after the Python reference version works.
- TypeScript + React for the dashboard.
- Java is not used, to keep the project at three languages.

## Consequences
- The Python scheduler is the correctness oracle: a parity test checks both versions return the same schedule.
- A benchmark (100 / 1,000 / 10,000 jobs) shows the measured speed-up.
- The build needs CMake and a C++ compiler; CI builds and tests the module.
