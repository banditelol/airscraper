import requests
import re
import argparse
from bs4 import BeautifulSoup as bs

parser = argparse.ArgumentParser(description="Download CSV from Airtable Shared View Link, You can pass the result to file using '> name.csv'", prog="airscraper")

parser.add_argument('view_url', help="url generated from sharing view using link in airtable")
parser.add_argument('-l', '--locale', default='en', help="Your locale, default to 'en'")
parser.add_argument('-tz', '--timezone', default=r'Asia%2FJakarta', help="Your timezone, use URL encoded string, default to 'Asia/Jakarta'")
args = parser.parse_args()
# print(args)

table = args.view_url
locale = args.locale
timezone = args.timezone

if(__name__ == "__main__"):
    # print("Scraping the HTML for Necessary params")
    html = bs(requests.get(table).text, features='html.parser')
    script = html.title.find_next('script')

    view_id = re.search(r"(viw[a-zA-Z0-9]+)",str(script)).group(1)
    access_policy = re.search(r"accessPolicy=([a-zA-Z0-9%*]+)",str(script)).group(1)
    app_id = re.search(r"\"x-airtable-application-id\":\"(app[a-zA-Z0-9]+)",str(script)).group(1)

    params = {"x-time-zone":timezone, "x-user-locale":locale, "x-airtable-application-id":app_id , "accessPolicy":access_policy}

    # print("Building Request URL")
    csv_url = f"https://airtable.com/v0.3/view/{view_id}/downloadCsv?"

    for (k,v) in params.items():
        csv_url += k+"="+v+"&"
    csv_url = csv_url[:-1]
    r = requests.get(csv_url)
    r.encoding = "utf-8"
    print(r.text)
