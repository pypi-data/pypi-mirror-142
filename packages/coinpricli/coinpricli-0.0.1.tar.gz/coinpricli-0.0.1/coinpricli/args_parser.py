import argparse
from . import __version__


def limit_validator(arg):
    try:
        n = int(arg)
        assert n > 0
        assert n <= 10
        return n
    except (ValueError, AssertionError):
        raise argparse.ArgumentTypeError('%s is not valid, it should be between 1 - 10' % arg)


def parse_args():
    parser = argparse.ArgumentParser(description='Crypto in terminal ')

    parser.add_argument('-l', '--limit', type=limit_validator, default=5,
                        metavar='N', help='number of coins to display, max is 10')
    parser.add_argument(
        '-v', '--version', action='version', version=f"coinpricli: {__version__}")
    parser.add_argument('-s', '--simple', action='store_true',
                        help='show simple table instead')

    return parser.parse_args()
