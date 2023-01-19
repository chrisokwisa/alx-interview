#!/usr/bin/python3
""" Reads stdin line by line and computes metrics """


import sys

# Initialize variables
total_size = 0
status_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_counter = 0

# Iterate over lines in stdin
for line in sys.stdin:
    try:
        # Parse line to extract data
        parts = line.strip().split(" ")
        ip_address = parts[0]
        date = parts[3][1:]
        request = parts[5]
        status = int(parts[8])
        file_size = int(parts[9])

        # Update total size and status count
        total_size += file_size
        if status in status_count:
            status_count[status] += 1

        line_counter += 1
        if line_counter % 10 == 0:
            # Print statistics
            print("Total file size: " + str(total_size))
            for status in sorted(status_count.keys()):
                if status_count[status] > 0:
                    print(str(status) + ": " + str(status_count[status]))
    except (ValueError, IndexError):
        # Skip lines with invalid format
        continue

    except KeyboardInterrupt:
        print("Total file size: " + str(total_size))
        for status in sorted(status_count.keys()):
            if status_count[status] > 0:
                print(str(status) + ": " + str(status_count[status]))
        break
