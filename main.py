import argparse

from eratosthenes_sieve.array import PrimeArraySieve

parser = argparse.ArgumentParser(description="Program to calculate primes using eratosthenes sieve")


def check_positive(value: int):
    value = int(value)
    if value > 0:
        return value
    raise argparse.ArgumentTypeError(f"{value} is not valid index of a prime")


group = parser.add_mutually_exclusive_group(required=True)

group.add_argument(
    "--get_nth",
    type=check_positive,
    help="will print n-th prime (2 is 1st prime so --get_nth 1 is 2)",
)

group.add_argument("--get_first_n", type=check_positive, help="will get the first N primes")

group.add_argument("--is_prime", type=str, help="checks if the number specified is prime")

group.add_argument(
    "--next_prime_greater_than",
    type=check_positive,
    help="prints next prime that is greater that the given int",
)

group.add_argument(
    "--prev_prime_less_than",
    type=check_positive,
    help="prints gretest prime that is less that the given int",
)

group.add_argument(
    "--count_primes_less_or_equal",
    type=str,
    help="counts the number of primes in the specified range",
)

group.add_argument(
    "--iter_all_primes",
    action="store_true",
    help="Infinite loop to get as much primes as you need",
)


def main(args):
    sieve = PrimeArraySieve()
    x = None
    if get_nth := args.get_nth:
        x = sieve[get_nth - 1]
    if get_first := args.get_first_n:
        x = sieve[:get_first]
    if is_prime := args.is_prime:
        is_prime = eval(is_prime)
        x = is_prime in sieve
    if next_prime_greater_than := args.next_prime_greater_than:
        x = sieve.next_prime_greater_than(next_prime_greater_than)
    if prev_prime_less_than := args.prev_prime_less_than:
        x = sieve.prev_prime_less_than(prev_prime_less_than)
    if count_primes_less_or_equal := args.count_primes_less_or_equal:
        count_primes_less_or_equal = eval(count_primes_less_or_equal)
        x = sieve.count_primes_less_or_equal(count_primes_less_or_equal)
    if args.iter_all_primes:
        x = sieve.iter_all_primes()
        for y in x:
            print(y)
    return x


if __name__ == "__main__":
    args = parser.parse_args()
    x = main(args)
    print(x)
