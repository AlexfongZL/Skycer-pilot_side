import requests

#payload are the data from pilot to the server.
payload = {"var_1": "111","var_2": "222","var_3": "333","var_4": "444"}

r = requests.post("http://localhost:8000/api/from_pilot", data = payload)

print r.status_code
print r.text