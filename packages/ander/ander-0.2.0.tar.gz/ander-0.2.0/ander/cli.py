from pathlib import Path
from typing import List, Set

import fire


def get_elements(filename: str) -> Set[str]:
    if not Path(filename).exists():
        raise FileNotFoundError(f"Argument {filename} is not found.")
    with open(filename, "r") as f:
        lines: List[str] = [s for line in f.readlines() if (s := line.strip()) != ""]
    return set(lines)


def ander(*filenames: str) -> Set[str]:
    if len(filenames) < 2:
        raise ValueError("Number of Argument must be at least 2.")
    master_set: Set[str] = get_elements(filenames[0])
    for filename in filenames[1:]:
        master_set.intersection_update(get_elements(filename))
    return master_set


def main() -> int:
    fire.Fire(ander)
    return 0


if __name__ == "__main__":
    main()
