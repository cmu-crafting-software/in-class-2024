import requests
r = requests.get('https://api.census.gov/data/2019/pep/charagegroups?get=NAME,POP&for=state:*')
print(r.text)