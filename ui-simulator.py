import requests

url = 'http://localhost:8080/rest/data/cppi/conf'

data = '{"floorObjective":100.0,"riskAppetite":2.0,"maxRiskFraction":0.9,"investement":100.0,"timeHorizon":365.0,"account":"itbm-devs","r":0.05}'
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

response = requests.post(url, data=data, headers=headers)
