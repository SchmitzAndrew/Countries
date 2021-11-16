from flask import Flask

# additional libraries
import pandas as pd
import numpy as np

# df code
from data import clean

# loading the df
countries = pd.read_csv("countries.csv")
countries = clean(countries)
print(countries.loc["Albania"]["Population"])

#App
app = Flask(__name__)

@app.route('/')
def index():  # put application's code here
    return '<h1>Welcome to the country database explorer.  </h1> <h2>There are ' + str(countries.shape[0]) + ' countries in the world<h2>'

# Displays infromation about one country
@app.route('/<name>')
def country_info(name):

    return '<h1>' + name + ': </h1> <h2> Population: ' + str(countries.loc[name]["Population"])


# Compares two countries
@app.route('/<country1>/<country2>')
def compare_countries():
    pass


if __name__ == '__main__':
    app.run(debug=True)
