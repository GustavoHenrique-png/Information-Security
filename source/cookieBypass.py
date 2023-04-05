import requests
data = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0", "Cookie": "cf_clearance=u34gBLtHQhaRMb9MYEF_gGH6tQL.zMoGfdRC9Vffr9s-1680725687-0-250"}

requisition = requests.get("http://www.bancocn.com/", headers=data)
print (requisition.status_code)


