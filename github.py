import requests
import urllib3

urllib3.disable_warnings()

user_info = input("What is your Github User Name? ")
github_token = input("Insert your GitHub Token: ")
get_user_info = f"https://api.github.com/users/{user_info}"
headers = {'Authorization': f'Bearer {github_token}'}

response = requests.get(get_user_info, headers=headers, verify=False)

if response.status_code != 200:
    print("Login Failed! Error: " + response.text)
else:
    print("Login Success")



