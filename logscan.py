#!/usr/bin/env python3
"""
linux-log-analyzer
Scans /var/log/syslog (or chosen file) and prints lines containing error keywords.
"""

import re, datetime, pathlib, sys
LOG_FILE = pathlib.Path("/var/log/syslog")           # adjust as needed
ERROR_PATTERNS = (r"error", r"fail", r"critical", r"panic")

def scan(path: pathlib.Path) -> None:
    with path.open() as f:
        for line in f:
            if any(re.search(p, line, re.I) for p in ERROR_PATTERNS):
                print(line.rstrip())

if __name__ == "__main__":
    print(f"--- Log scan {datetime.datetime.now().isoformat(timespec='seconds')} ---")
    if LOG_FILE.exists():
        scan(LOG_FILE)
    else:
        sys.exit(f"Log file {LOG_FILE} not found")
