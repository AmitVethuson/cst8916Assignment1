from flask import Flask, jsonify, request


app = Flask(__name__)

stockMarketData = {
   
    '1': {"name": "TechGenius Inc.", "ticker_symbol": "TGX", "current_price": 110.50},
    '2': {"name": "Global Innovations Co.", "ticker_symbol": "GINC", "current_price": 80.25},
    '3': {"name": "SolarWave Corp.", "ticker_symbol": "SWC", "current_price": 130.75},
    '4': {"name": "Quantum Systems Ltd.", "ticker_symbol": "QSYS", "current_price": 55.10},
    '5': {"name": "MegaFoods Ltd.", "ticker_symbol": "MFL", "current_price": 95.75},
    '6': {"name": "AeroTech Solutions Inc.", "ticker_symbol": "ATS", "current_price": 45.90},
    '7': {"name": "BioHealth Innovators", "ticker_symbol": "BHI", "current_price": 70.15},
    '8': {"name": "RenewaPower Corp.", "ticker_symbol": "RNP", "current_price": 125.20},
    '9': {"name": "SustainableTech Ltd.", "ticker_symbol": "STL", "current_price": 105.80},
    '10': {"name": "FutureWave Technologies", "ticker_symbol": "FWT", "current_price": 85.50},

}

@app.route('/')
def running():
    return "<p>Stock Market RESTapi</p>"


#get all stocks
@app.route('/stocks',methods=['GET'])
def getAllStocks():
    stock_info = {}
    allStocks = stockMarketData
    for i in allStocks:
        name = allStocks[i].get('name',{})
        current_price =allStocks[i].get('current_price',{})
        stock_info.update( {str(i) : {'name': name, 'current_price':current_price}})
    return stock_info
    


#create stocks
@app.route('/stocks', methods=['POST'])
def createStock():
    newId = (len(stockMarketData)+1)
    new_stock = {
        str(newId ): {'name':request.json['name'], 'ticker':request.json['ticker'],'current_price': request.json['current_price']}
    }
    stockMarketData.update(new_stock)
    return new_stock


if __name__ == '__main__':
    app.run(debug=True)