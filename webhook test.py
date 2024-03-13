import requests

url = "https://services.leadconnectorhq.com/hooks/AVLmkufe6O29tqQJpgcN/webhook-trigger/b8dfa74e-8ecf-4ec5-8ef8-6406134e2984"
body = {
    "data": {
        "full_name": "phil saroka",
        }
    }
response = requests.post(url, json=body) 
print(response.text) # Access the value of the cell
