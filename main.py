from time import sleep
from selenium import webdriver
import random

# imports
from instapy import InstaPy
from instapy import smart_run
from dotenv import load_dotenv
import os


load_dotenv()
# login credentials

insta_username = os.getenv("USERNAME")
insta_password = os.getenv("PASSWORD")

session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

with smart_run(session):
    """ Activity flow """
    #settings
    session.set_relationship_bounds(enabled=True, delimit_by_numbers=True, max_followers= 5000, min_followers=50, min_following=50)

    #activities
    session.follow_user_followers(['kanyewest'], amount=1000, randomize=False, interact=False)
