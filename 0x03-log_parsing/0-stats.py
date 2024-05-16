#!/usr/bin/python3
"""
Module to work on stdin stats
"""
import re
import sys


def regex_gen(line):
    """function to return code and size"""
    pattern = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[([^\]]+)\] "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$'

    # Compile the pattern
    regex = re.compile(pattern)

    # Match the pattern with the log line
    match = regex.match(line)
    if match:
        code = match.group(3)
        size = match.group(4)
        return (code, size)
    return (None, None)


def main():
    """Main function"""
    count = 0
    total_size = 0
    statuses = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
    }
    while True:
        try:
            line = sys.stdin.readline()
            code, size = regex_gen(line)
            if not code or not size or code not in statuses:
                continue
            count += 1
            total_size += int(size)
            statuses[code] += 1
            if count == 10:
                print(f"File size: {total_size}")
                for code, num in statuses.items():
                    print(f"{code}: {num}")
                count = 0
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    main()
