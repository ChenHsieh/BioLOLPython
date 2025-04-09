# bioLOLPython/cli.py
import sys
from bioLOLPython.interpreter import handle_line

def main():
    if len(sys.argv) < 2:
        print("Usage: bioLOL <script.lolz>")
        return
    with open(sys.argv[1]) as f:
        for line in f:
            handle_line(line.strip())