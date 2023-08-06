#!/usr/bin/env python3
from texttable import Texttable

from .fetch_coins import fetch_crypto_data
from .args_parser import parse_args


def generate_table(headers, data):
    t = Texttable(max_width=0)
    headersRow = []
    for h in headers:
        headersRow.append(h['title'])
    dataRow = []
    for index, item in enumerate(data):
        result = []
        for h in headers:
            if(h['title'] == '#'):
                result.append(index + 1)
            else:
                result.append(item[h['key']])
        dataRow.append(result)
    t.add_rows([headersRow] + dataRow)
    return t


full_headers = [
    {'title': '#'},
    {'title': 'Name', 'key': 'name'},
    {'title': 'Price', 'key': 'price'},
    {'title': '24h %', 'key': 'today_change'},
    {'title': '7d %', 'key': 'week_change'},
    {'title': 'Market Cap', 'key': 'market_cap'},
    {'title': 'Volume', 'key': 'volume'}
]


simple_headers = [
    {'title': '#'},
    {'title': 'Name', 'key': 'name'},
    {'title': 'Price', 'key': 'price'},
]


def main():
    args = parse_args()
    data = fetch_crypto_data(vars(args))
    headers = full_headers
    if (args.simple):
        headers = simple_headers
    print('Currency: USD')
    print(generate_table(headers, data).draw())


if __name__ == '__main__':
    main()
