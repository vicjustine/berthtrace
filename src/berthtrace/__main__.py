"""Entry point. Started by the operator, then attached to with a debugger."""

import debugpy

from berthtrace.dispatch import run


def main() -> None:
    debugpy.listen(5678)
    print("dispatch waiting for debugger on port 5678...", flush=True)
    debugpy.wait_for_client()
    print("debugger attached, starting dispatch", flush=True)

    tally = run()
    print(f"\nfinal total: {tally.total()}")
    print(f"busiest berth: {tally.busiest()}")


if __name__ == "__main__":
    main()
