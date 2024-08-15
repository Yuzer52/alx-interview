#!/usr/bin/python3
"""
Log parsing
"""

import sys
import signal

# Initialize metrics
filesize, count = 0, 0
codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
stats = {code: 0 for code in codes}


def print_stats(stats: dict, filesize: int) -> None:
    """Prints the current statistics."""
    print("File size: {:d}".format(filesize))
    for code, value in sorted(stats.items()):
        if value:
            print("{}: {}".format(code, value))


def handle_interrupt(signal, frame):
    """Handle keyboard interruption (CTRL + C)."""
    print_stats(stats, filesize)
    sys.exit(0)


# Attach the keyboard interrupt handler
signal.signal(signal.SIGINT, handle_interrupt)

# Read from stdin line by line
try:
    for line in sys.stdin:
        count += 1
        data = line.split()
        try:
            # Extract status code and update counts
            status_code = data[-2]
            if status_code in stats:
                stats[status_code] += 1
        except Exception:
            pass

        try:
            # Extract and accumulate file size
            filesize += int(data[-1])
        except Exception:
            pass

        # Print stats every 10 lines
        if count % 10 == 0:
            print_stats(stats, filesize)

    # Print final stats after input ends
    print_stats(stats, filesize)

except KeyboardInterrupt:
    # Handle any remaining output on keyboard interrupt
    print_stats(stats, filesize)
    raise

