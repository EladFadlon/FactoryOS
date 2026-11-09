# ADR 0001: Code computes, agents decide

Date: 2026-11-09
Status: Accepted

## Context
LLM calls are slow, rate-limited on free tiers, and non-deterministic. A factory simulation needs reproducible, testable behaviour.

## Decision
The simulation, scheduling algorithms, inventory math and persistence are plain Python with tests. LLM agents are invoked only when an event occurs, receive pre-computed options from code, choose one, and record a short rationale.

## Consequences
- Runs stay reproducible (fixed seed) and cheap (calls only on events).
- Agents can be tested with a mocked model.
- The interesting part for reviewers is the orchestration and decision log, not prompt tricks.
