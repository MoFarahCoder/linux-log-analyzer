# linux-log-analyzer

Python CLI tool that scans a Linux syslog-style file and prints any line containing *error*, *fail*, *critical*, or *panic*.

## Usage
```bash
python logscan.py        # default log: /var/log/syslog
