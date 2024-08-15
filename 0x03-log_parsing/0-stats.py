#!/usr/bin/python3
import sys
import signal

# Initialize metrics
total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def print_statistics():
    """Prints the current statistics."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")


def handle_interrupt(signal, frame):
    """Handle keyboard interruption (CTRL + C)."""
    print_statistics()
    sys.exit(0)


# Attach the keyboard interrupt handler
signal.signal(signal.SIGINT, handle_interrupt)

# Read from stdin line by line
try:
    for line in sys.stdin:
        line_count += 1
        try:
            # Split the line into components
            parts = line.split()

            # Check for the correct format and extract values
            if len(parts) >= 9 and parts[2] == '"GET' and parts[3].startswith("/projects/260"):
                # Extract status code and file size
                status_code = int(parts[-2])
                file_size = int(parts[-1])

                # Update total file size
                total_file_size += file_size

                # Update status code count if valid
                if status_code in status_code_counts:
                    status_code_counts[status_code] += 1

            # Every 10 lines, print statistics
            if line_count % 10 == 0:
                print_statistics()

        except Exception:
            # Skip the line if there's an error parsing
            continue

except KeyboardInterrupt:
    # Handle any remaining output on keyboard interrupt
    print_statistics()
    sys.exit(0)

# Print the final statistics after the input ends
print_statistics()

