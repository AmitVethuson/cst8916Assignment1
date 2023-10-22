from ariadne import QueryType, make_executable_schema, load_schema_from_path
from graphql_server.flask import GraphQLView
from flask import Flask

#initalize flask app
app = Flask(__name__)

#stock data
stocks = [
    {"id":1, "name": "TechGenius Inc.","historical_price": [152.13 ,143.58, 149.66, 132.13, 183.17], 'highest_price': 183.17, 'lowest_price': 132.13 ,"trade_volume":1231},
    {"id":2, "name": "Global Innovations Co.", "historical_price": [101.85, 103.17, 195.16, 196.68, 166.30], 'highest_price': 196.68, 'lowest_price': 101.85 ,"trade_volume":676},
    {"id":3, "name": "SolarWave Corp.", "historical_price": [130.93, 135.11, 111.77, 184.08, 193.70], 'highest_price': 193.7, 'lowest_price': 111.77 ,"trade_volume":78},
    {"id":4, "name": "Quantum Systems Ltd.", "historical_price":[152.23, 186.24, 197.07, 156.35, 170.19], 'highest_price': 197.07, 'lowest_price': 152.23,"trade_volume":478678},
    {"id":5, "name": "MegaFoods Ltd.", "historical_price": [174.03, 161.41, 112.80 ,117.15 ,190.85], 'highest_price': 190.85, 'lowest_price': 112.8 ,"trade_volume":4},
    {"id":6, "name": "AeroTech Solutions Inc.", "historical_price": [106.58, 150.19 ,195.59 ,159.38 ,190.57], 'highest_price': 195.59, 'lowest_price': 106.58,"trade_volume":4300},
    {"id":7, "name": "BioHealth Innovators", "historical_price": [185.64 ,120.64 ,180.54 ,140.47 ,100.53], 'highest_price': 185.64, 'lowest_price': 100.53,"trade_volume":4000},
    {"id":8, "name": "RenewaPower Corp.", "historical_price": [157.50 ,167.94 ,116.26 ,138.23 ,119.56], 'highest_price': 167.94, 'lowest_price': 116.26,"trade_volume":1000},
    {"id":9, "name": "SustainableTech Ltd.", "historical_price": [147.30 ,103.10 ,144.47 ,153.56 ,142.54],'highest_price': 153.56, 'lowest_price': 103.1 ,"trade_volume":7500},
    {"id":10,"name": "FutureWave Technologies", "historical_price": [125.12, 111.31, 121.48, 154.11 ,168.07], 'highest_price': 168.07, 'lowest_price': 111.31,"trade_volume":40000000},

]


# load graphql schema from a file
type_defs = load_schema_from_path("schema.graphql")

# define query types for graphql schema
query = QueryType()



# ------------ Resolver Functions ----------------


#resolver function to fetch all stock information
@query.field("stocks")
def resolve_stocks(*_):
    return stocks



#resolver function to fetch stock based on the name
@query.field("getStockByName")
def resolver_stock(_, info,name):
    for stock in stocks:
        if stock["name"] == name:
            return stock
    return None


#resolver function to fetch stock based on the id
@query.field("getStockById")
def resolver_stock(_, info,id):
    for stock in stocks:
        if stock["id"] == id:
            return stock
    return None


# ---------------Creating executable -------------


# Creating an executable GraphQL schema using type definitions and resolvers
schema = make_executable_schema(type_defs, query)


# adding an url rule
app.add_url_rule("/graphql", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True))


# Running the Flask app 
if __name__ == '__main__':
    app.run(debug=True)