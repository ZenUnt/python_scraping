import requests

url = 'https://api.aoikujira.com/time/get.php'
result = requests.get(url)
print("ok=", result.ok)
if result.ok:
    print("text=", result.text)
print("status_code=", result.status_code)
