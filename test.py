import requests
import csv
import json
from bs4 import BeautifulSoup


url = 'https://realpython.github.io/fake-jobs/'
page = requests.get(url)
soup = requests.get(url)
soup = BeautifulSoup(page.content,"html.parser")
results = soup.find(id="ResultsContainer")

job_elements = results.find_all("div",class_="card-content")

l = []
for job_element in job_elements:
    link = job_element.find_all("a")[1]["href"]
    l.append(link)
    

for i in range(len(l)):
    page = requests.get(l[i])
    soup = requests.get(l[i])
    soup = BeautifulSoup(page.content,"html.parser")
    results = soup.find(id="ResultsContainer")
    title_element = results.find("h1")
    name_element = results.find("h2")
    desc_element = results.find("p")
    location_element = results.find("p",id="location")
    date_element = results.find("p",id="date")
    sweet = [{'title': title_element,'name': name_element,'desc': desc_element, 'location': location_element,'date': date_element}]
    print(sweet)
   



    
