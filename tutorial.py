#Going through this tutorial > https://realpython.com/beautiful-soup-web-scraper-python/

#Libraries
import requests
from pprint import pprint #instead of just import pprint so I don't have to do pprint.pprint()
from bs4 import BeautifulSoup

#Make Request Object
URL = 'https://www.monster.com/jobs/search?q=Technical+Writer&where=Los+Angeles+County%2C+CA&remote=true'
page = requests.get(URL)
print(page.status_code) #just to check that we are getting a nice 200 for the page
#pprint(page.content) #its a fuck ton

#Make Soup Object
soup = BeautifulSoup(page.content, 'html.parser')

#Make results object
results = soup.find(id='app')
print(results)

#Find all
job_elems = results.find_all("div", class_='results-page container')
print(job_elems)

#for job_elem in job_elems:
    #print(job_elem, end='\n'*2)
#print(job_elems)

for job_elem in job_elems:
    # Each job_elem is a new BeautifulSoup object.
    # You can use the same methods on it as you did before.
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
    print(title_elem)
    print(company_elem)
    print(location_elem)
    print()