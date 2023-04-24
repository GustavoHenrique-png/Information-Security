import requests

print(r"""
      /\
 __   \/   __
 \_\_\/\/_/_/
   _\_\/_/_
  __/_/\_\__
 /_/ /\/\ \_\
 Snow /\
      \/
""")


data = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0","Cookie":"cf_clearance=UtdbThPq84pdOn0t.3Z7CXuRQd90c6.rmU36P7XnnnE-1680797523-0-250"}

requisition = requests.get("http://www.bancocn.com/", headers= data)
if (requisition.status_code ==200):
    print("Access: granted\nStatus: ",requisition.status_code)
else:
     print("Access: denied\nStatus: ",requisition.status_code)