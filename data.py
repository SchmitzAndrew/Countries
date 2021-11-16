import pandas as pd


def clean(countries):
    countries["Country"] = countries["Country"].str.strip()

    countries = countries.set_index("Country")
    return countries




