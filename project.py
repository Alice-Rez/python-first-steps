import requests


def define_query(languages, min_stars=50000):
    query = f"stars:>{min_stars} "

    for language in languages:
        query += f"language:{language} "

    return query


def get_gh_repo(languages, sort="stars", order="desc"):

    url = "https://api.github.com/search/repositories"

    query = define_query(languages)

    params = {"q": query, "sort": sort, "order": order}

    response = requests.get(url, params)
    status = response.status_code

    if status == 403:
        raise RuntimeError(
            f"Rate limit rreached. Please wait a minute and try again.")
    elif status != 200:
        raise RuntimeError(f"An error ocurred with status code: {status}")
    else:
        return response.json()["items"]


if __name__ == "__main__":
    languages = ["Python", "Javascript", "Ruby"]
    results = get_gh_repo(languages)

    for result in results:
        name = result["name"]
        language = result["language"]
        stars = result["stargazers_count"]

        print(f"-> {name} is a {language} repo with {stars} stars.")
