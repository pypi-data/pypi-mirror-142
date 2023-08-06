# coinpricli

coinpricli is a package where you can easily monitor cryptocurrencies. It's using web scapping to get data from [coinmarketcap.com's web page](https://coinmarketcap.com).

![coinpricli show case](https://lh3.googleusercontent.com/miOqQq55bbCgZvzE6COSUtGfRM2S0diohZLBM6zXYEm5Hhljz9AjW7fVt0t6xDar0a2WiZUnqZgGOePegGpS-DVP1zdUyrXVrEy-LxzB46XXn1w86fAqgv7Rb_8Z9ticuR72A8wHUg=w2400)

## Installation
This project has been implemented using Python3, it's reqiured to install Python 3.8 or higher.

[Download Python here](https://www.python.org/downloads/)

```shell
pip install coinpricli
```

## Usage

See top 10 cryptocurrencies:
```shell
coinpricli
```

Set number of coins to display in table:
```shell
coinpricli --limit=4
```

Show simple table
```shell
coinpricli --simple
```

Help
```shell
coinpricli --help
```

## Future
- [ ] Support color for % Change
- [ ] Support more than 10 coins
