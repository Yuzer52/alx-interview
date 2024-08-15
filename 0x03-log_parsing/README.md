# Log Analyzer Script

## Description
This script reads log lines from `stdin` and computes the total file size and the count of specific HTTP status codes. It prints statistics every 10 lines and upon keyboard interruption (CTRL + C).

## Usage
Run the script by feeding it log entries via `stdin`:

```bash
./0-generator.py | ./0-stats.py

