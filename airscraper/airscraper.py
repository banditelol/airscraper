import re
import requests
import argparse
import pandas as pd
from io import StringIO
from bs4 import BeautifulSoup as bs

# TODO: Create Docstring for the class and each methods
class AirScraper:
    def __init__(self, url: str, sess: requests.Session = None, password: str = None, locale: str = 'en', tz=r'Asia%2FJakarta'):
        self.url = url
        self.locale = locale
        self.tz = tz
        self.params = {}
        if sess is None:
            self.sess = requests.Session()
        else:
            self.sess = sess
        self.password = password
        self.page = None

        if self._is_passwd_protected():
            self.login()

        self.update_params()

    def _get_shareId(self):
        try:
            return re.search(r"(shr[^/]+)", self.url).group(1)
        except:
            raise ValueError(
                "malformed url, expecting url with share ID (shr*)")

    def _is_passwd_protected(self):
        try:
            res = self.sess.get(self.url)
            if res.status_code == 200:
                return "passwordProtectedShareFormContainer" in res.text
            else:
                res.raise_for_status()
        except:
            raise

    def login(self):
        res = self.sess.get(self.url)
        shareId = self._get_shareId()
        csrf = re.search(r'csrfToken":"([^"]+)', res.text).group(1)
        data = {
            "shareId": shareId,
            "OriginalUrl": "/"+shareId,
            "_csrf": csrf,
            "password": self.password
        }
        self.page = self.sess.post(
            f"https://airtable.com/{shareId}/submitPassword", data=data)

    def update_params(self):
        if self.page is None:
            self.page = self.sess.get(self.url)

        html = bs(self.page.text, features='html.parser')
        try:
            script = html.title.find_next('script')
            self.view_id = re.search(
                r"(viw[a-zA-Z0-9]+)", str(script)).group(1)
            access_policy = re.search(
                r"accessPolicy=([a-zA-Z0-9%*]+)", str(script)).group(1)
            app_id = re.search(
                r"\"x-airtable-application-id\":\"(app[a-zA-Z0-9]+)", str(script)).group(1)
            self.params = {"x-time-zone": self.tz, "x-user-locale": self.locale,
                           "x-airtable-application-id": app_id, "accessPolicy": access_policy}
        except:
            raise ConnectionError(
                "Unauthorized Access, please try again by providing password, i.e. Airscraper(url,password=password)")

    def get_csv(self):
        self.csv_url = f"https://airtable.com/v0.3/view/{self.view_id}/downloadCsv?"
        # TODO: use native parameter to uri parsing
        for (k, v) in self.params.items():
            self.csv_url += k+"="+v+"&"
        self.csv_url = self.csv_url[:-1]
        r = self.sess.get(self.csv_url)
        r.encoding = "utf-8"
        return r.text

    def get_table(self):
        """Alias for get_csv

        Returns:
            str: string containing comma separated value of the table
        """
        return self.get_csv()

    def get_df(self):
        
        return pd.read_csv(StringIO(self.get_csv()))


def main():
    parser = argparse.ArgumentParser(
        description="Download CSV from Airtable Shared View Link, You can pass the result to file using '> name.csv'", prog="airscraper")

    parser.add_argument(
        'view_url', help="url generated from sharing view using link in airtable")
    parser.add_argument('-l', '--locale', default='en',
                        help="Your locale, default to 'en'")
    parser.add_argument('-tz', '--timezone', default=r'Asia%2FJakarta',
                        help="Your timezone, use URL encoded string, default to 'Asia/Jakarta'")
    parser.add_argument(
        '-p', '--password', help="Fill with shared link password, not your airtable password")
    args = parser.parse_args()
    # print(args)

    client = AirScraper(args.view_url)
    print(client.get_csv())


if __name__ == "__main__":
    main()
