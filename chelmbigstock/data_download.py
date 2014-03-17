#!/usr/bin/env python

# A python script to download csv file to be used in stock analysis
'''
Created on Mar 15, 2014

@author: Andy Webber
'''
from urllib import request
import datetime

def main():
    
    #stock_download('aapl')
    f = open('stock_symbols.txt', 'r')
    for stock_symbol in f:
        stock_symbol = stock_symbol.strip()
        stock_download(stock_symbol)
    f.close()

def stock_download(stock_symbol):

    #Compose the web page 
    page = "http://ichart.finance.yahoo.com/table.csv?s="
    page = ''.join([page, stock_symbol])
    now = datetime.datetime.now()
    page = ''.join([page, '&amp;d=', str(now.month)])
    page = ''.join([page, '&amp;e=', str(now.day)])
    page = ''.join([page, '&amp;f=', str(now.year)])
    page = ''.join([page, '&amp;g=d'])
    # Set the start date to Jan 1 1960 and the file will pick up data for as far
    # back as possible
    page = ''.join([page, '&amp;a=1'])
    page = ''.join([page, '&amp;b=1'])
    page = ''.join([page, '&amp;c=1960'])
    page = ''.join([page, '&amp;ignore=.csv'])
    print(page)
    response = request.urlopen(page)
    csv = response.read()

    # Save the string to a file
    csvstr = str(csv).strip("b'")
    out_file = "../data/"
    out_file = ''.join([out_file, stock_symbol, ".csv"])

    lines = csvstr.split("\\n")
#    #f = open("../data/historical.csv", "w")
    print(out_file)
    f = open(out_file, "w")
    for line in lines:
       f.write(line + "\n")
    f.close()

if __name__ == "__main__":
    main()