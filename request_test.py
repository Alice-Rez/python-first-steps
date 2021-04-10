import requests


def get_dogs():
    api_url = "http://shibe.online/api/shibes"
    params = {"count": 10}
    response = requests.get(api_url, params)
    status = response.status_code
    response_json = response.json()
    print(response.json())
    print(len(response_json))


def get_users(number=3):
    api_url = "https://randomuser.me/api"
    params = {"results": number}
    response = requests.get(api_url, params)
    return list(response.json()["results"])


def get_covid():
    api_url = "https://onemocneni-aktualne.mzcr.cz/api/v2/covid-19/zakladni-prehled.json"
    response = requests.get(api_url)
    response_json = response.json()
    print(response.text)
    print(len(response_json))


def print_users(results):
    for index, result in enumerate(results):
        name = result['name']
        if name["title"] == "Miss":
            print(
                f"Person nr. {index} {name['title']}.{name['first']} {name['last']} ")
        elif name["title"] == "Mrs":
            print(f"Person nr. {index} is married women")
        else:
            print(f"Person nr. {index} is not a women")


# get_dogs()
print_users(get_users(10))
# get_covid()
