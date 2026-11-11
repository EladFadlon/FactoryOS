"""Session 3: one pick & place machine processing a queue of boards.

Run:  uv run --with simpy python simulation/playground/01_one_machine.py
"""
import random

import simpy

SEED = 42
PNP_MINUTES = 8           # dev_board time on pick & place (config/factory.yaml)
OVEN_MINUTES = 6
MEAN_ARRIVAL_MINUTES = 10 # a new board arrives every ~10 minutes on average
SHIFT_MINUTES = 480       # one 8-hour shift
MACHINES = 1              # try 2 (pnp-1 + pnp-2) and compare the waits

waits = []
busy_minutes = 0.0
oven_waits = []
oven_busy = 0


def board(env, name, pnp ,oven):
    """One board: wait in line for the machine, get processed, leave."""
    global busy_minutes, oven_busy
    arrived = env.now
    with pnp.request() as req:           # join the queue
        yield req                        # wait until the machine is free
        wait = env.now - arrived
        waits.append(wait)
        print(f"{env.now:6.1f}  {name} enters P&P  (waited {wait:4.1f} min, queue={len(pnp.queue)})")
        yield env.timeout(PNP_MINUTES)   # processing takes time
        busy_minutes += PNP_MINUTES
        oven_arrived = env.now
    with oven.request() as req:
        yield req
        wait = env.now - oven_arrived
        oven_waits.append(wait)
        print(f"{env.now:6.1f}  {name} enters Oven  (waited {wait:4.1f} min, queue={len(oven.queue)})")
        yield env.timeout(OVEN_MINUTES)
        oven_busy += OVEN_MINUTES
    print(f"{env.now:6.1f}  {name} done")

def arrivals(env, pnp, oven):
    """Generate boards at random intervals until the shift ends."""
    i = 0
    while True:
        yield env.timeout(random.expovariate(1 / MEAN_ARRIVAL_MINUTES))
        i += 1
        env.process(board(env, f"board-{i:03d}", pnp , oven))


def main():
    random.seed(SEED)                    # same seed -> same run, every time
    env = simpy.Environment()
    pnp = simpy.Resource(env, capacity=MACHINES)
    oven = simpy.Resource(env, capacity=1)
    env.process(arrivals(env, pnp, oven))
    env.run(until=SHIFT_MINUTES)

    print("\n--- end of shift ---")
    print(f"boards started:     {len(waits)}")
    print(f"average wait:       {sum(waits) / len(waits):.1f} min")
    print(f"longest wait:       {max(waits):.1f} min")
    print(f"still in queue:     {len(pnp.queue)}")
    print(f"machine utilization {busy_minutes / (SHIFT_MINUTES * MACHINES):.0%}")
    print(f"oven utilization {(oven_busy / SHIFT_MINUTES):.0%}")
if __name__ == "__main__":
    main()
