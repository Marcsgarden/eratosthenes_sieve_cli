# Eratosthenes sieve

Simple CLI that allows easy work evaluation of "is N a prime" or "what are first N primes" etc.

## Usage:

```
usage: main.py [-h]
               (--get_nth GET_NTH | --get_first_n GET_FIRST_N | --is_prime IS_PRIME | --next_prime_greater_than NEXT_PRIME_GREATER_THAN | --prev_prime_less_than PREV_PRIME_LESS_THAN | --count_primes_less_or_equal COUNT_PRIMES_LESS_OR_EQUAL | --iter_all_primes)

Program to calculate primes using eratosthenes sieve

options:
  -h, --help            show this help message and exit
  --get_nth GET_NTH     will print n-th prime (2 is 1st prime so --get_nth 1 is 2)
  --get_first_n GET_FIRST_N
                        will get the first N primes
  --is_prime IS_PRIME   checks if the number specified is prime
  --next_prime_greater_than NEXT_PRIME_GREATER_THAN
                        prints next prime that is greater that the given int
  --prev_prime_less_than PREV_PRIME_LESS_THAN
                        prints gretest prime that is less that the given int
  --count_primes_less_or_equal COUNT_PRIMES_LESS_OR_EQUAL
                        counts the number of primes in the specified range
  --iter_all_primes     Infinite loop to get as much primes as you need
```

