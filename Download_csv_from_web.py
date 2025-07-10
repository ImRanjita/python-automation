import requests

url = f"https://cdn.wsform.com/wp-content/uploads/2020/06/industry_sic.csv"

"""use headers , if forbidden pops up while accessing, in this code, access is available hence not used"""
content = requests.get(url).content
print(content)

with open('data.csv', "wb") as file:
    file.write(content)