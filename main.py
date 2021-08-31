from time import sleep
from selenium import webdriver
import random

# imports
from instapy import InstaPy
from instapy import smart_run
from dotenv import load_dotenv
import os

#files
from follow import follow
from comment import comment

load_dotenv()
# login credentials

insta_username = os.getenv("USERNAME")
insta_password = os.getenv("PASSWORD")

session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

follow(session, "kanyewest")


