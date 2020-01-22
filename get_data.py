"""
This module downloads the financial data

Author: Daniel Clark
"""
import re
import json
import time

import requests
import pandas as pd
from alpha_vantage.timeseries import TimeSeries


with open('keys.json') as f:
    data = json.load(f)
    username = data['myKeys']['mongodb_username']
    password = data['myKeys']['mongodb_password']
    alpha_key = data['myKeys']['alphavantage_api_key']

def create_urls(file, base_url):
    """Create a url for each stock
    Create a url from the tickers located in the file. Use
    the base_url as the source to create the url from.

    :param file: CSV where tickers are located
    :type file: str
    :param base_url: URL base to build the other create_urls
    :type base_url: str
    :returns: list of unique urls
    :rtype: list of tuples containing (stock, url)
    """
    # Create dataframe from CSV
    df = pd.read_csv(file)
    tickers = df['Tickers']
    url_list = [re.sub(r'STOCK', stock, base_url) for stock in tickers]
    # Create a list of [(stock, url0]
    stocks = list(zip(tickers, url_list))
    return stocks


def get_request(url):
    """Get the request for the url.

    :param url: URL to request
    :type url: str
    :returns: Request of URL
    :rtype: Request Object
    """
    print(f'Making request for url: {url}')
    request = requests.get(url)
    # If the status code is a success
    if request.status_code >= 200 and request.status_code < 300:
        return request
    return False


def create_dict():
    """Create a dictionary with the requests data and stock

    :returns: a dictionary with {stock: {file: request}}
    """
    csv = 'stocks.csv'
    base_url = 'https://finance.yahoo.com/quote/STOCK/financials/'
    stock_dict = {}
    stocks = create_urls(csv, base_url)
    for stock in stocks:
        print(f'Starting Stock {stock[0]}')
        # URL is stock[1]
        request = get_request(stock[1])
        # Ticker is stock[0]
        priceData = get_stock_data(stock[0])
        if request:
            stock_dict[stock] = {'file': request.text}
        if priceData:
            stock_dict[stock] = priceData
        # Every 4 calls to the get_weekly function need to be separated by one minute
        print(f'{stock[0]} extractions complete.')
        time.sleep(15)
    return stock_dict


def get_stock_data(ticker):
    """Get the weekly stock data for the ticker

    :param ticker: Ticker to generate data for
    :type ticker: str
    :returns: weekly stock data for ticker
    :rtype: pd.df
    """
    print(f'Getting stock data for: {ticker}')
    ts = TimeSeries(key=alpha_key)
    data = ts.get_weekly(ticker)
    return {'priceData': data}


def main():
    r = create_dict()
    print(r)

main()