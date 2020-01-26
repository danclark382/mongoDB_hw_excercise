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

from mondb import MongoDatabase


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
    stock_dict = {'key': []}
    stocks = create_urls(csv, base_url)
    for stock in stocks:
        document = {stock[0]: {'file': ''}, 'priceData': ''}
        print(f'Starting Stock {stock[0]}')
        # URL is stock[1]
        request = get_request(stock[1])
        # Ticker is stock[0]
        priceData = get_stock_data(stock[0])
        if request:
            document[stock[0]]['file'] = request.text
        if priceData:
            document[stock[0]]['priceData'] = priceData
        stock_dict['key'].append(document)
        # Every 4 calls to the get_weekly function need to be separated by one minute
        print(f'{stock[0]} extractions complete.')
        return stock_dict
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
    data = format(data)
    return data

def format(data):
    """Format returned stock data to match mongodb standards"""
    new_dict = {}
    for k in data[0]:
        new_dict[k] = {}
        for key in data[0][k]:
            tmp = data[0][k][key]
            v = key.split(' ')[-1]
            new_dict[k][v] = tmp
    return new_dict



def main():
    r = create_dict()
    print(r)
    db = MongoDatabase('Test2')
    db.insert_document('stock', r)
    print(r)

main()