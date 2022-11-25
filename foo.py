import re
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 4:
        print("Invalid argument(s)")
        exit()
    with open(sys.argv[1], "r") as f:
        print(f"Reading {sys.argv[1]}")
        new_lines = ""
        pattern = r"[A-Z][a-z]+ ([a-z]+)"
        repl = lambda x: x.group(1).capitalize()
        for l in f:
            new_lines += re.sub(pattern, repl, l)
    with open(sys.argv[2] or sys.argv[1], "w") as f:
        print(f"Writing into '{sys.argv[2] or sys.argv[1]}'")
        f.write(new_lines)
