# Airscraper
A simple scraper to download csv from any airtable shared view programatically, think of it as a programatic way of downloading csv from airtable shared view.
Use it if:
- You want to download a shared view periodically
- You don't mind the shared view to be accessed basically without authorization
If You want to know how it works, feel free to fire up the notebooks [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](banditelol/airscraper/blob/master/notebook/Airtable%20Scraping%20CSV.ipynb]


## Requirements
Because its a simple scraper, basically only beautifulsoup is needed
- BeautifulSoup4

## Usage
- Clone this project
- Install the requirements
  - `pip install -r requirements.txt`
- run the code
    `python airscraper.py [url]`

## Examples
``` Bash
# Print Result to Terminal
python airscraper.py [url]

# Pipe the result to csv file
python airscraper.py [url] > [filename].csv

```

## Help
``` Bash
usage: airscraper [-h] [-l LOCALE] [-tz TIMEZONE] view_url

Download CSV from Airtable Shared View Link, You can pass the result to file using
'> name.csv'

positional arguments:
  view_url              url generated from sharing view using link in airtable

optional arguments:
  -h, --help            show this help message and exit
  -l LOCALE, --locale LOCALE
                        Your locale, default to 'en'
  -tz TIMEZONE, --timezone TIMEZONE
                        Your timezone, use URL encoded string, default to
                        'Asia/Jakarta'
```

## What's next
Currently I'm thinking of several things in mind:
- Making this installed package
- Adds accessibility to use it in FaaS Platform (most use case I could thought of are related to this)
- Create a proper package that can be imported (so I could use it in my ETL script)
- Fill in LICENSE and setup.py, (to be honest I have no idea yet what to put into the setup.py)

## Contributing
If you have similar problem oor have any idea to improve this package please let me know in the issues or just hit me up on twitter [@BanditelolRP](https://twitter.com/banditelolRP)
