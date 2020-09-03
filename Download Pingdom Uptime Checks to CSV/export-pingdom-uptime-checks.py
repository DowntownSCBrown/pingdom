## For a detailed explanation of this code, check out my blog post at https://stevenbrown.us/connecting-to-the-pingdom-api-with-python/.

import requests
import json
import csv

csvFile = 'C:\YouTube\PingdomChecks.csv'
csvHead = ['Name', 'Status']

api = "https://api.pingdom.com/api/3.1/checks"

head = {'Authorization':'Bearer -Db5nZmkeyHfj3BFfyolq_EGhO9IwMdDJV41Hcc_8XUd_ks_ojSqlxxxxxxxxxxxxxxxxx'}

pingdomChecks = requests.get(api, headers=head).json()

with open(csvFile, 'w', newline='') as pChecksList:
    csvwriter = csv.writer(pChecksList)
    csvwriter.writerow(csvHead)

    for check in pingdomChecks['checks']:
        csvwriter.writerow((check['name'], check['status']))

pChecksList.close()