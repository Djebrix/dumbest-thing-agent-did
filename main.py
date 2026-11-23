"""Write the dumbest-thing-my-agent-did-today line to entry.txt.

Stdlib only, no network, deterministic: the same line every run.
"""

import os

LINE = "My agent sealed a recording to prove it wrote 2,385 lines of code — it caught three."


def main() -> None:
    line = LINE.strip()
    assert 1 <= len(line) <= 200, f"line must be 1-200 chars, got {len(line)}"
    assert line.strip(), "line must not be only whitespace"
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
