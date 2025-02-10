# v1
# from flask import Flask, render_template, request
# import pandas as pd
# app = Flask(__name__)

# # # Dummy data for flights and hotels
# # flights = [
# #     {"id": 1, "from": "Mumbai", "to": "Delhi", "price": 5000, "airline": "IndiGo"},
# #     {"id": 2, "from": "Bangalore", "to": "Kolkata", "price": 7000, "airline": "Air India"},
# #     {"id": 3, "from": "Chennai", "to": "Mumbai", "price": 4500, "airline": "SpiceJet"}
# # ]

# # hotels = [
# #     {"id": 1, "city": "Delhi", "name": "The Taj Hotel", "price": 8000},
# #     {"id": 2, "city": "Mumbai", "name": "Oberoi Hotel", "price": 7000},
# #     {"id": 3, "city": "Kolkata", "name": "ITC Sonar", "price": 6000}
# # ]
# # loading the dataset:
# flights_df=pd.read_csv("D:\\Flask_tutorial\\mytrip\\flights.csv")
# hotels_df=pd.read_csv("D:\\Flask_tutorial\\mytrip\\hotels.csv")

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/search_flights', methods=['POST'])
# def search_flights():
#     source = request.form.get('source', '').strip()
#     destination = request.form.get('destination', '').strip()
#     results = flights_df[(flights_df["DepartingCity"].str.lower()==source.lower()) & (flights_df["ArrivingCity"].str.lower()==destination.lower())].to_dict(orient='records')
#     return render_template('results.html', results=results, type='flight')

# @app.route('/search_hotels', methods=['POST'])
# def search_hotels():
#     city = request.form.get('city', '').strip()
#     results = hotels_df[hotels_df["city"].str.lower() == city.lower()].to_dict(orient='records')
#     return render_template('results.html', results=results, type='hotel')

# if __name__ == '__main__':
#     app.run(debug=True)

# v2
# from flask import Flask, render_template, request
# import pandas as pd

# app = Flask(__name__)

# # Loading the dataset:
# flights_df = pd.read_csv("D:\\Flask_tutorial\\mytrip\\flight_data_BOM_BLR.csv")
# hotels_df = pd.read_csv("D:\\Flask_tutorial\\mytrip\\hotels.csv")

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/search_flights', methods=['POST'])
# def search_flights():
#     source = request.form.get('source', '').strip()
#     destination = request.form.get('destination', '').strip()
    
#     results = flights_df[(flights_df["DepartingCity"].str.lower() == source.lower()) & 
#                          (flights_df["ArrivingCity"].str.lower() == destination.lower())]
    
#     return render_template('results.html', results=results.to_dict(orient='records'), type='flight')

# @app.route('/search_hotels', methods=['POST'])
# def search_hotels():
#     city = request.form.get('city', '').strip()
#     results = hotels_df[hotels_df["city"].str.lower() == city.lower()].to_dict(orient='records')
#     return render_template('results.html', results=results, type='hotel')

# if __name__ == '__main__':
#     app.run(debug=True)

#v3
from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)

# Loading the dataset:
flights_df = pd.read_csv(r"flight_data_BOM_BLR.csv")
hotels_df = pd.read_csv(r'indian_hotel_bookings.csv')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search_flights', methods=['POST'])
def search_flights():
    source = request.form.get('source', '').strip()
    destination = request.form.get('destination', '').strip()
    
    results = flights_df[(flights_df["DepartingCity"].str.lower() == source.lower()) & 
                         (flights_df["ArrivingCity"].str.lower() == destination.lower())]
    
    results = results.rename(columns={
        "FlightName": "airline",
        "FlightCode": "FlightCode",
        "DepartingTime": "DepartingTime",
        "ArrivingTime": "ArrivalTime",
        "Price": "price"
    })
    
    results["price"] = results["price"].astype(str).str.replace(",", "")
    
    return render_template('results.html', results=results.to_dict(orient='records'), type='flight')

@app.route('/search_hotels', methods=['POST'])
def search_hotels():
    city = request.form.get('city', '').strip()
    results = hotels_df[hotels_df["Arriving City"].str.lower() == city.lower()].to_dict(orient='records')
    return render_template('results.html', results=results, type='hotel')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
    ## if run locally then:
    # app.run(debug=True)