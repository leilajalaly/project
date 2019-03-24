from flask import Flask, request
import requests
import requests_cache

requests_cache.install_cache(
    'stock_api_cache', backend='sqlite', expire_after=36000)
app=Flask(__name__, instance_relative_config=True)

stock_url = 'https://financialmodelingprep.com/api/financials/income-statement/{stock}'


@app.route('/stockdata', methods=['GET'])
def stockIncome():

    stock = request.args.get('stock')
    url = stock_url.format(
        stock=stock)
    respons = requests.get(url)
    if respons.ok:
        stockData = respons.content
        return (stockData)
    else:
        print(respons.reason)


if __name__ == '__main__':
    app.run(port=8080, debug=True)
