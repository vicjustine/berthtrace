# berthtrace

The dispatch service that keeps a running count of containers on each berth.
It reads a move feed and applies each arrival and departure to a rolling tally.

## Running it

The service waits for a debugger before it starts, so you can attach and watch
the tally as it moves:

```
python -m berthtrace
```

It prints `dispatch waiting for debugger on port 5678...` and pauses until a
client attaches.

## The feed

`data/moves.jsonl` holds 66 moves across three berths — one JSON object per
line, each with a berth, a container count and a direction.

## Known problem

Operations report that the end-of-run summary is wrong: **B2 finishes on a
negative count**, which is impossible, and the busiest-berth figure looks off
as a result. The feed is long enough that stepping through it by hand is not
practical.
