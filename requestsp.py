from bs4 import BeautifulSoup
import requests
from config import username,password
from pprint import pprint


def main():
    url = 'https://labmanageapp.herokuapp.com/login'

    with requests.session() as session:
        client = requests.session()

        # Retrieve the CSRF token first
        client.get(url)  # sets cookie
        if 'csrftoken' in client.cookies:
            # Django 1.6 and up
            csrftoken = client.cookies['csrftoken']
        else:
            # older versions
            csrftoken = client.cookies['csrf']


        data = {'username':username, 'password':password,'csrfmiddlewaretoken':csrftoken, 'next':'/home'}
        r_post = session.post(url,data=data,headers=dict(Referer=url))
        soup = BeautifulSoup(r_post.text, 'html.parser')
        print(soup.text)


if __name__ == '__main__':
    main()