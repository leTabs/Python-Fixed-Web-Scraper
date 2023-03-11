from bs4 import BeautifulSoup
import requests, sys, time

print('''This is a web scraping program.
It scan a certain website ('letabs.github.io') for information regrading the
available projects curaintly on the site.

''')


html_site = requests.get('https://letabs.github.io/mainPanel.html').text
bowl = BeautifulSoup(html_site, 'html.parser')

def button_titles():
    index = 0
    for section in bowl.find_all('p', class_= 'l'):
        index +=1
        print(f'{index}) {section.text}')
button_titles()

def python_section():
    html_python = requests.get('https://letabs.github.io/pythonPanel.html').text
    python_soup = BeautifulSoup(html_python, 'html.parser')
    index = 0
    for title in python_soup.find_all('td', class_ = "name"):
        index+=1
        print(f'{index}) {title.text}')
def frontEnd_section():
    html_frontEnd= requests.get('https://letabs.github.io/frontEndPanel.html').text
    frontEnd_soup = BeautifulSoup(html_frontEnd, 'html.parser')
    index = 0
    for title in frontEnd_soup.find_all('td', class_ = "name"):
        index+=1
        print(f'{index}) {title.text}')
def sql_section():
    html_sql = requests.get('https://letabs.github.io/sqlPanel.html').text
    sql_soup = BeautifulSoup(html_sql, 'html.parser')
    index = 0
    for title in sql_soup.find_all('td', class_ = "name"):
        index +=1
        print(f'{index}) {title.text}')

def noSql_section():
    html_nosql = requests.get('https://letabs.github.io/nosqlPanel.html').text
    nosql_soup = BeautifulSoup(html_nosql, 'html.parser')
    index = 0
    for title in nosql_soup.find_all('td', class_ = "name"):
        index +=1
        print(f'{index}) {title.text}')

def networking_section():
    html_net = requests.get('https://letabs.github.io/networkingPanel.html').text
    net_soup = BeautifulSoup(html_net, 'html.parser')
    index = 0
    for title in net_soup.find_all('td', class_ = "name"):
        index +=1
        print(f'{index}) {title.text}')

def apis_section():
    html_api = requests.get('https://letabs.github.io/apisPanel.html').text
    api_soup = BeautifulSoup(html_api, 'html.parser')
    index = 0
    for title in api_soup.find_all('td', class_ = "name"):
        index +=1
        print(f'{index}) {title.text}')

def algorithms_section():
    html_algo = requests.get('https://letabs.github.io/algorithmsPanel.html').text
    algo_soup = BeautifulSoup(html_algo, 'html.parser')
    index = 0
    for title in algo_soup.find_all('td', class_ = "name"):
        index +=1
        print(f'{index}) {title.text}')
def multiProjects_section():
    html_mp = requests.get('https://letabs.github.io/multiProjectsPanel.html').text
    mp_soup = BeautifulSoup(html_mp, 'html.parser')
    index = 0
    for title in mp_soup.find_all('td', class_ = "name"):
        index +=1
        print(f'{index}) {title.text}')
def checking():
    if   choice == 1: python_section()
    elif choice == 2: frontEnd_section()
    elif choice == 3: sql_section()
    elif choice == 4: noSql_section()
    elif choice == 5: networking_section()
    elif choice == 6: apis_section()
    elif choice == 7: algorithms_section()
    elif choice == 8: multiProjects_section()
    else: print('The section you choosed does not exist.')
    print('_'*45)
print('_'*45)

while True:
    try:
        choice = int(input('Choose a section to inspect: '))
        print('_'*45)
        checking()
        break
    except ValueError:
        print('Please, use numbers.')
    continue
    print('_'*45)


print('_'*45)
time.sleep(5)
close = input('Type "Enter" to terminate:')
sys.exit()
