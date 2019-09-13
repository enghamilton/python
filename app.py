# from this site http://kazuar.github.io/scraping-tutorial/

import requests
from lxml import html
from flask import Flask

USERNAME = "enghamilton"
PASSWORD = "p4dcGj97"

LOGIN_URL = "https://github.com/login"
URL = "https://github.com/"

def main():
    session_requests = requests.session()

    # Get login csrf token
    result = session_requests.get(LOGIN_URL)
    tree = html.fromstring(result.text)

    # Create payload
    payload = {
        "username": USERNAME, 
        "password": PASSWORD
    }

    # Perform login
    result = session_requests.post(LOGIN_URL, data = payload, headers = dict(referer = LOGIN_URL))

    # Scrape url
    result = session_requests.get(URL, headers = dict(referer = URL))
    tree = html.fromstring(result.content)
    bucket_names = tree.xpath("//span[@class='ver text here']/a/text()")

    return (result.content)

f = open("myscraped.txt", "w")
f.write(main())
f.close()		

if __name__ == '__main__':
    main()

app = Flask(__name__)

@app.route('/')
def source():
  if __name__ == '__main__':
  html = main()
  return html

if __name__ == "__main__":
    app.run()
