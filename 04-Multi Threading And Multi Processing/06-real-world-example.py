'''
# Real World Example: Using Multithreading for I/O-bound tasks
Task: Web Scraping
Problem: task includes server response and n/w req, (waiting time++) 
Solution: Multithreading allows multiple webpages fetched concurently
'''
import threading
import requests
from bs4 import BeautifulSoup
