'''
# Real World Example: Using Multithreading for I/O-bound tasks
Task: Web Scraping
Problem: task includes server response and n/w req, (waiting time++) 
Solution: Multithreading allows multiple webpages fetched concurently
'''
import threading
import requests
from bs4 import BeautifulSoup

urls=[
    'https://portfolio-shivamdevhere.vercel.app/', 
    'https://www.langchain.com/',
]

def fetch_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(f'Fetched {len(soup.text)} characters from {url}')

threads = []

for url in urls:
    thread = threading.Thread(target=fetch_content, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All Web Pages Fetched")