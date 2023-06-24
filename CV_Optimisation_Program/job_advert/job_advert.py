import requests

from bs4 import BeautifulSoup

class JobAdvert:
    def job_ad_scrapper(url):
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
        else:
            print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return response.text


