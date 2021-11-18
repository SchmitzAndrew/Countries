from flask import Flask, render_template, url_for

# additional libraries
import pandas as pd
import numpy as np

# df code
from data import clean

# loading the df
countries = pd.read_csv("countries.csv")
countries = clean(countries)

# App
app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')


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
