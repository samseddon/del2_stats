import os
import requests
from bs4 import BeautifulSoup


def input_download(url):
    #Headers to masquerade as a browser
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    
    # Download page HTML using requests
    response = requests.get(url, headers=headers)
    # Check valid response received
    if response.status_code == 200:
    
        # Parse HTML using Beautiful Soup
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.select("table", {"class":"shadow-sm:nth-child(1)"})
        overview = table[0].text

        shots = table[2].text
        #print(overview.replace(' ', ''))
        timeline = table[3]
        
        

        #print(score[0].text)
#
#def get_url(url):
#    #Headers to masquerade as a browser
#    headers = {
#        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
#
#    }
#    # Download page HTML using requests
#    response = requests.get(url, headers=headers)
#    # Check valid response received
#    if response.status_code == 200:
#    
#        # Parse HTML using Beautiful Soup
#        soup = BeautifulSoup(response.text, 'html.parser')
#        urls = soup.find("table", {"class":"shadow-sm:nth-child(1)"})
#
#        print(urls)
    

if __name__ == "__main__":
    url = "https://www.eurohockey.com/game/detail/258130-dresdner-eislwen--selber-wlfe.html"
    url = "https://www.eurohockey.com/game/detail/258092-esv-kaufbeuren-joker--dresdner-eislwen.html"
    url = "https://www.del-2.org/spiel/ec-kassel-huskies-vs-esv-kaufbeuren_7039"
    url = "https://www.del-2.org/spiel/ehc-freiburg-vs-eisbaren-regensburg_7040"
    input_download(url)
