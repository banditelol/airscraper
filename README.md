# Airscraper
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/banditelol/airscraper/blob/master/notebook/Airtable%20Scraping%20CSV.ipynb)
[![PyPI version](https://badge.fury.io/py/airscraper.svg)](https://badge.fury.io/py/airscraper)

A simple scraper to download csv from any airtable shared view programatically, think of it as a programatic way of downloading csv from airtable shared view.
Use it if:
- You want to download a shared view periodically
- You don't mind the shared view to be accessed basically without authorization

## Requirements
Because its a simple scraper, basically only beautifulsoup is needed
- BeautifulSoup4

## Installation

### Using pip (Recommended)

`pip install airscraper`

### Build From Source
- Install build dependencies:
``` Bash
pip install --upgrade pip setuptools wheel
pip install tqdm
pip install --user --upgrade twine
```
- Build the Package
  - `python setup.py bdist_wheel`
- Install the built Package
  - `pip install --upgrade dist/airscraper-0.1-py3-none-any.whl `
- Use it without adding python in front of it
  - `airscraper [url]`

### Direct Execution (Testing Purpose)
- Clone this project
- Install the requirements
  - `pip install -r requirements.txt`
- run the code
  - `python airscraper/airscraper.py [url]`

## Usage

Create a [shared view link](https://support.airtable.com/hc/en-us/articles/205752117-Creating-a-base-share-link-or-a-view-share-link#viewsharelink) and use that link to download the shared view into csv. All `[url]` mentioned in the examples are referring to the shared view link you get from this step.

### As CLI

``` Bash
# Print Result to Terminal
python airscraper/airscraper.py [url]

# Pipe the result to csv file
python airscraper/airscraper.py [url] > [filename].csv

```

### As Python Package

``` Python
from airscraper import AirScraper

client = AirScraper([url])
data = client.get_table().text

# print the result
print(data)

# save as file
with open('data.csv','w') as f:
  f.write(data)

# use it with pandas
from io import StringIO
import pandas as pd

df = pd.read_csv(StringIO(data), sep=',')
df.head()
```

## Help
```
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
- ✅ Making this installed package
- Adds accessibility to use it in FaaS Platform (most use case I could thought of are related to this)
- ✅ Create a proper package that can be imported (so I could use it in my ETL script)
- ✅ Fill in LICENSE and setup.py, (to be honest I have no idea yet what to put into it)
  - It turns out there are a lot of resources [out there](https://dzone.com/articles/executable-package-pip-install) if you know what to look for :)

## Contributing
If you have similar problem oor have any idea to improve this package please let me know in the issues or just hit me up on twitter [@BanditelolRP](https://twitter.com/banditelolRP)
