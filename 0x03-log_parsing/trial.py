#!/usr/bin/python3

statuses = {
    "403": 0, 
    "301": 30, 
    "200": 20,
    "400": 10, 
    "401": 80,
    "404": 0,
    "500": 50,
    "405": 40,
}

for code, count in statuses.items():
    print(f"{code} {count}")