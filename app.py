# from this site http://kazuar.github.io/scraping-tutorial/

import requests
from lxml import html
from flask import Flask

USERNAME = "enghamilton"
#PASSWORD = "*******7"

LOGIN_URL = "https://github.com/login"
URL = "https://github.com/"

def main():
    #session_requests = requests.session()

    # Create payload
    payload = {
        "login": USERNAME, 
        "password": PASSWORD
    }

	#https ://pybit.es/requests-session.html
    with requests.Session() as session:
		post = session.post(LOGIN_URL, data=payload)
		r = session.get(URL)
    
    return (r.content)	

if __name__ == '__main__':
    main()

app = Flask(__name__)

@app.route('/')
def source():
  if __name__ == '__main__':
  html = main()
  return html

@app.route('/login')
def login():
  return main()

app.run()
