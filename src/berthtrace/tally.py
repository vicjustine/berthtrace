"""Rolling tally of container moves, consumed by the dispatch service."""

from dataclasses import dataclass, field


@dataclass
class Move:
    berth: str
    containers: int
    direction: str          # "in" or "out"


@dataclass
class Tally:
    """Running count of containers currently on each berth."""

    counts: dict[str, int] = field(default_factory=dict)

    def apply(self, move: Move) -> None:
        current = self.counts.get(move.berth, 0)
        if move.direction == "in":
            self.counts[move.berth] = current + move.containers
        else:
            if move.containers > current: 
                raise ValueError(
                    f"{move.berth}: cannot remove {move.containers} from {current}"
                )
            self.counts[move.berth] = current - move.containers

    def total(self) -> int:
        return sum(self.counts.values())

    def busiest(self) -> str:
        return max(self.counts, key=lambda b: self.counts[b])

