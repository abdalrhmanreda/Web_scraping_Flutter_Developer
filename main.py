import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

page1 = requests.get('https://wuzzuf.net/search/jobs/?q=flutter%20Developer&start=0')
page2 = requests.get('https://wuzzuf.net/search/jobs/?q=flutter%20Developer&start=1')
page3 = requests.get('https://wuzzuf.net/search/jobs/?q=flutter%20Developer&start=2')
con = page1.content + page2.content + page3.content

soup = BeautifulSoup(con, 'html.parser')

job_title = soup.find_all('h2', {'class': 'css-m604qf'})
company_name = soup.find_all('a', {'class': 'css-17s97q8'})
company_address = soup.find_all('span', {'class': 'css-5wys0k'})
skill = soup.find_all('div', {'class': 'css-y4udm8'})

job_titles = []
nameOfCompany = []
addressOfCompany = []
links = []
salaries = []
skills = []
complete_link = ['https://wuzzuf.net']

for i in range(len(job_title)):
    job_titles.append(job_title[i].text)
    nameOfCompany.append(company_name[i].text)
    addressOfCompany.append(company_address[i].text)
    links.append(job_title[i].find('a', {'class': 'css-o171kl'}).get('href'))
    skills.append(skill[i].text)
    print(job_titles[i], ' ---- ', nameOfCompany[i], ' ---- ', addressOfCompany[i], ' ---- ', skills[i], ' ---- ',
          complete_link[0] + links[i], '\n')
print((len(skills)))

# for i in range(len(skills)):
# print(job_titles[i], ' ---- ', nameOfCompany[i], ' ---- ', addressOfCompany[i], ' ---- ', skills[i], ' ---- ',
#   listt[0] + links[i], '\n')
