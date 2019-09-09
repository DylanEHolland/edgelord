# EdgeLord

## Install

`pip install edgelord`

## About

EdgeLord is a Python 3 module for non-voodoo analysis of equities.  Current development focuses on straight forward indicators and signals as opposed to fancy TA indicators that are more akin to strategies themselves or already part of something like ta-lib.  So this module will not be having a `trend_line()` routine or pattern recognition.

It is designed with stocks in mind but will work for any tradable equity with an open, close, low, high and volume; as well the data tested on comes from [Tiingo](https://www.tiingo.com/) but you can generate a proper csv file from just about any api or dataset (and I'm not above someone else sending a PR with a script for say iex.)