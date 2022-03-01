import requests

class SampleGitApi:
    def __init__(self) -> None:
        pass
    def getUser(self):
        headers_dict = {"Accept": "application/vnd.github.v3+json"}
        api_url = "https://api.github.com/users/AnanthaSNRao"
        response = requests.get(api_url, headers= headers_dict)
        r = response.json()
        print(r)
        return r