"""Regenerate every figure in the book.

Run from the repository root:  python make_all_figures.py
Each fig_partN.py script writes PNGs into book/partN/figures/ and prints
the verification numbers quoted in the corresponding chapters' prose.
"""

import subprocess
import sys
from pathlib import Path

SCRIPTS_DIR = Path(__file__).parent / "figures" / "scripts"

def main() -> int:
    scripts = sorted(SCRIPTS_DIR.glob("fig_part*.py"))
    if not scripts:
        print("No figure scripts found in", SCRIPTS_DIR)
        return 1
    for script in scripts:
        print(f"=== {script.name} ===")
        result = subprocess.run([sys.executable, script.name],
                                cwd=SCRIPTS_DIR)
        if result.returncode != 0:
            print(f"FAILED: {script.name}")
            return result.returncode
    print("All figures regenerated.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
