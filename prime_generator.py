#!/usr/bin/env python3
"""Prime number generator.

This script generates prime numbers up to a specified limit using the
Sieve of Eratosthenes algorithm.

Usage:
    python3 prime_generator.py --limit 100
"""

import argparse
from typing import List


def primes_up_to(limit: int) -> List[int]:
    """Return a list of prime numbers up to *limit* (inclusive)."""
    if limit < 2:
        return []
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if is_prime[number]:
            for multiple in range(number*number, limit + 1, number):
                is_prime[multiple] = False
    return [number for number, prime in enumerate(is_prime) if prime]


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate prime numbers up to a limit")
    parser.add_argument("--limit", type=int, default=100, help="Upper bound for prime search")
    args = parser.parse_args()

    primes = primes_up_to(args.limit)
    print(primes)


if __name__ == "__main__":
    main()
