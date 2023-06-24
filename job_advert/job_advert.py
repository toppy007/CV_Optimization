import requests
from bs4 import BeautifulSoup
import json

class JobAdvert:
    def job_ad_scrapper(url):
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find the script element with type="application/ld+json"
            script_element = soup.find("script", attrs={"type": "application/ld+json"})

            if script_element:
                script_content = script_element.string
                data = json.loads(script_content)
                return data
        return None

