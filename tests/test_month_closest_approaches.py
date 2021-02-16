from asteroids import __version__
import unittest
import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()
from asteroids.month_closest_approaches import month_closest_approaches

def test_version():
    assert __version__ == '0.1.0'

def test_month_closest_approaches():
  res = month_closest_approaches('2020-02') 

