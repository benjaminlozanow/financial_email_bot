import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

load_dotenv("e_variables.env")

YAHOO_API_KEY = os.environ.get("YAHOO_API_KEY")

class YahooQuotes:
    url = "https://yfapi.net/v6/finance/quote"

    query = {"lang": "en",}

    headers = {
    'x-api-key': YAHOO_API_KEY
    }

    def __init__(self, type, *args):
        self.type = type
        self.ids = list(args)

    def __repr__(self):
        return self.type

    def make_request(self):
        self.query["symbols"] = ",".join(self.ids)
        r = requests.request("GET", self.url, headers=self.headers, params=self.query)
        self.json = r.json()

    def get_data(self):
        self.data = []
        for i in range(len(self.ids)):
            self.data.append({"name": self.json["quoteResponse"]["result"][i]["shortName"],
                              "percentage": round(self.json["quoteResponse"]["result"][i]["regularMarketChangePercent"], 2)})
        return self.data

stock = YahooQuotes("Stocks","AAPL", "TWTR", "TSLA", "FB")
index = YahooQuotes("Indexes", "^GSPC", "^N100", "^GDAXI", "000001.SS")
crypto = YahooQuotes("Crypto", "BTC-USD", "ETH-USD", "DOGE-USD", "SHIB-USD")

with open("base_email.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")
    soup.prettify()

def edit_html(instance):
    h3 = soup.new_tag("h3", style="font-size: 28px; margin:0 0 20px 0; font-family:Avenir;")
    h3.string = repr(instance)
    soup.find_all("td")[1].append(h3)

    for i in instance.data:
        new_tag = soup.new_tag("p", style="font-size: 20px;font-family:Avenir")
        new_tag.string = "{} has changed {} %".format(i["name"], i["percentage"])
        soup.find_all("td")[1].append(new_tag)

for ins in [stock, index, crypto]:
    ins.make_request()
    ins.get_data()
    edit_html(ins)

# save the file again
with open("out_email.html", "w") as outf:
    outf.write(str(soup))