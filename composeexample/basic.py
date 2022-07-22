import re
from turtle import end_poly
from django import http
import requests

endpoint = "http://localhost:8000/apis/"

get_response = requests.get(endpoint, json={"query": "Hello World"})
print(get_response.text)
print(get_response.status_code)