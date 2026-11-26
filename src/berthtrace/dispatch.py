"""Dispatch loop: reads moves from the feed and keeps the tally current."""

import json
import time
from pathlib import Path

from berthtrace.tally import Move, Tally

FEED = Path(__file__).resolve().parents[2] / "data" / "moves.jsonl"


def load_moves() -> list[Move]:
    moves = []
    for line in FEED.read_text().splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        moves.append(Move(row["berth"], row["containers"], row["direction"]))
    return moves


def run(pause: float = 0.4) -> Tally:
    tally = Tally()
    for index, move in enumerate(load_moves()):
        tally.apply(move)
        print(f"[{index:02d}] {move.direction:3} {move.containers:>3} at {move.berth}"
              f"  -> {move.berth}={tally.counts[move.berth]}  total={tally.total()}")
        time.sleep(pause)
    return tally
