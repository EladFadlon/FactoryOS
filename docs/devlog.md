# Devlog

End every session with three lines: what I did, where I stopped, the next step.

## 2026-11-09
- Did: project plan written, folder skeleton created.
- Stopped at: Phase 0, nothing installed yet.
- Decided: PCB assembly factory (ADR 0003); C++ scheduling engine (ADR 0002).
- Next: create the public GitHub repo and push this folder.

## 09-11-2026
- Did: pushed the skeleton to github.com/EladFadlon/factoryos (PAT auth, Apple sign-in issue solved).
- Stopped at: Phase 0, session 1 done.
- Next: session 2 – install Python 3.12, Node 22, uv and Docker Desktop (Intel, no brew), run docker compose up.

## 09-11-2026
- Did: uv + Python 3.12, Node 26 LTS, Docker Desktop verified; docker compose up brings up Postgres. Phase 0 exit criterion met.
- Stopped at: Phase 0 – remaining: SimPy tutorial, LangGraph quickstart, API keys, Student Pack.
- Next: session 3 – SimPy tutorial, ending with one machine processing a job queue.

## 11-11-2026
- Did: SimPy basics; 01_one_machine + 02_two_stations (P&P → oven), written myself.
- Learned: oven queue always 0, P&P is the bottleneck; read env.now, don't compute times by hand.
- Next: lead time per board in 02_two_stations.

## 15-11-20261
- Did: oven avg wait + lead time per board in 02_two_stations (51 done, avg 33.8, max 60.5).
       compared running times with 1 P&P machine and 2 P&P machines.
       Results : - 1 P&P machine -
                    boards started:     53
                    average wait:       21.1 min
                    longest wait:       57.0 min
                    still in queue:     4
                    machine utilization 87%
                    oven utilization    64%
                    Board Count:        51
                    avg lead time:      33.8
                    max lead time:      60.5
                 - 2 P&P machines -
                    boards started:     57
                    average wait:       2.2 min
                    longest wait:       13.0 min
                    still in queue:     0
                    machine utilization 48%
                    oven utilization    68%
                    Board Count:        54
                    avg lead time:      23.6 min 
                    max lead time:      47.0 min
- Learned: boards unfinished at shift end aren't counted (censoring).
- Next: LangGraph quickstart.

