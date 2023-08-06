import requests

# TODO Get the user agent from the environment variable
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}


def get_page_content(url):
    return requests.get(url, headers=headers).content
