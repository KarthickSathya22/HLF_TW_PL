import requests
import json
import pandas as pd
#url = 'https://hlf-app.herokuapp.com/predict_api'
url = 'http://127.0.0.1:5000/predict_api'


#Requesting Parameters:
"""
data = [{'cus_Gender': 'M',
        'cus_Dependants': 0,
        'cus_CurrenStyYear': 18,
        'app_CustBankClosBal': 0, 
        'app_CustAssetValue': 265000,
        'app_CustProductCatTypeId': 1541,
        'app_CustIndustryTypeId': 1783,
        'app_CustTenure': 18,
        'app_CustInstalCount': 18,
        'app_CustChasAsset': 67112,
        'app_CustChasInitial': 27112,
        'app_CustChasFinance': 40000,
        'app_CustFinanInterest': 13.5,
        'app_CustEMI': 2672, 
        'app_CustTotInflow': 2500,
        'app_CustBrandTypeId': 1360,
        'cus_Age': 31,
        'cus_CurrenResTypeId': 2755, 
        'cus_MartialTypeId': 2750}]
"""

#Loading a dataset:
df = pd.read_csv('test data.csv')

#Droping class label column:
df.drop(['Label'],axis=1,inplace=True)

#Convert each record into json:
data = df.to_json(orient='records')
data = json.loads(str(data))
 
#Send request to the server with sample records:
r = requests.post(url,json=data[:50])

#Get the response from a server:
print(r.json())

res = r.json().get('result')
for i,j in enumerate(res):
    print(i,j)