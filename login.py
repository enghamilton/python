# from this site http://kazuar.github.io/scraping-tutorial/

import requests
from lxml import html

USERNAME = "<username>"
PASSWORD = "<password>"

LOGIN_URL = "https://github.com/login"
URL = "https://github.com/"

def main():
    session_requests = requests.session()

    # Get login csrf token
    result = session_requests.get(LOGIN_URL)
    tree = html.fromstring(result.text)
    #authenticity_token = list(set(tree.xpath("//input[@name='csrfToken']/@value")))[0]

    # Create payload
    payload = {
        "username": USERNAME, 
        "password": PASSWORD, 
        #"csrfmiddlewaretoken": authenticity_token
    }

    # Perform login
    result = session_requests.post(LOGIN_URL, data = payload, headers = dict(referer = LOGIN_URL))

    # Scrape url
    result = session_requests.get(URL, headers = dict(referer = URL))
    tree = html.fromstring(result.content)
    git_names = tree.xpath("//span[@class='flex-shrink-0']/text()")

    print(result.content)

if __name__ == '__main__':
    main()
