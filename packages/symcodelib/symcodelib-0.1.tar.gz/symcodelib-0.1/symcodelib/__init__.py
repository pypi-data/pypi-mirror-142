import requests

url = 'https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json'
response = requests.get(url)
data = response.json()
result_list = []

class StockCode:

    def getStockCode(symbol):
        for x in data:
            if x['symbol'] == symbol:
                return x['token']
    
    def getStockCodeFormat(symbol_list):
        for sym in range(len(symbol_list)):
            for y in data:
                if y['symbol'] == symbol_list[sym]:
                    result_list.append('nse_cm|' + y['token'])
                    result_list.append('&')
        result_list.pop(-1)
        return ''.join(result_list)

