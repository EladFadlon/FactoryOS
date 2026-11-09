# ADR 0003: The factory assembles PCBs on an SMT line

Date: 2026-11-09
Status: Accepted (replaces the initial wooden-furniture example)

## Context
The product must create real agent decisions: shared machines, several materials from several suppliers, and interesting failure modes. It should also be easy to explain in an interview and relevant to hardware companies such as NVIDIA.

## Decision
A PCB assembly factory with one SMT line of 7 stations (paste printer, 2× pick & place, reflow oven, AOI, functional test, rework) producing a dev board, a sensor module and a power supply.

## Consequences
- Pick & place is the bottleneck, so scheduling matters.
- Quality becomes part of the story: AOI defect rate depends on reflow oven drift, giving the maintenance agent a data signal to act on.
- Chip supply has a cheap/slow distributor and an expensive/fast broker, enabling a "chip shortage" scenario.
