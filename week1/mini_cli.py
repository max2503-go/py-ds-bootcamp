#!/usr/bin/env python3
"""
Mini CLI – Day 6 capstone
Commands: greet, fizzbuzz, duplicate?
"""

def greet(name):
    return f"Hello {name}, welcome to Python!"

def fizzbuzz_list(n):
    return [
        "FizzBuzz" if i % 15 == 0 else
        "Fizz"     if i % 3  == 0 else
        "Buzz"     if i % 5  == 0 else
        str(i)
        for i in range(1, n + 1)
    ]

def has_duplicate(nums):
    return len(nums) != len(set(nums))

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python mini_cli.py <command> [args]")
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "greet":
        name = sys.argv[2] if len(sys.argv) > 2 else "World"
        print(greet(name))

    elif cmd == "fizzbuzz":
        n = int(sys.argv[2]) if len(sys.argv) > 2 else 15
        print(fizzbuzz_list(n))

    elif cmd == "dup":
        nums = list(map(int, sys.argv[2:]))
        print(has_duplicate(nums))

    else:
        print("Unknown command")
