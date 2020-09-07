import requests
import re
import argparse
from bs4 import BeautifulSoup as bs

class AirScraper:

    def __init__(self, url, locale = 'en', tz=r'Asia%2FJakarta'):
        self.url = url
        self.locale = locale
        self.tz = tz
        self.params = {}

        self.update_params()

    def update_params(self):
        html = bs(requests.get(self.url).text, features='html.parser')
        script = html.title.find_next('script')
        self.view_id = re.search(r"(viw[a-zA-Z0-9]+)",str(script)).group(1)
        access_policy = re.search(r"accessPolicy=([a-zA-Z0-9%*]+)",str(script)).group(1)
        app_id = re.search(r"\"x-airtable-application-id\":\"(app[a-zA-Z0-9]+)",str(script)).group(1)
        self.params = {"x-time-zone":self.tz, "x-user-locale":self.locale, "x-airtable-application-id":app_id , "accessPolicy":access_policy}

    def get_table(self):
        self.csv_url = f"https://airtable.com/v0.3/view/{self.view_id}/downloadCsv?"
        for (k,v) in self.params.items():
            self.csv_url += k+"="+v+"&"
        self.csv_url = self.csv_url[:-1]
        r = requests.get(self.csv_url)
        r.encoding = "utf-8"
        return r.text

def main():
    parser = argparse.ArgumentParser(description="Download CSV from Airtable Shared View Link, You can pass the result to file using '> name.csv'", prog="airscraper")

    parser.add_argument('view_url', help="url generated from sharing view using link in airtable")
    parser.add_argument('-l', '--locale', default='en', help="Your locale, default to 'en'")
    parser.add_argument('-tz', '--timezone', default=r'Asia%2FJakarta', help="Your timezone, use URL encoded string, default to 'Asia/Jakarta'")
    args = parser.parse_args()
    # print(args)

    client = AirScraper(args.view_url)
    print(client.get_table())

if __name__ == "__main__":
    main()
