# nature-crawler
A tool for crawling papers on nature.com.

This script only supports crawling abstract of Article-type papers now.  
Crawling full-text, including Letter-type papers, will be supported soon.

## Requirement
* Python 2.7.x
* [Scrapy](https://scrapy.org/)

## Usage
### 1. Install Scrapy

```
$ pip install Scrapy
```

See [documantation of Scrapy](https://doc.scrapy.org/en/1.3/intro/install.html) for more information about how to install Scrapy.

### 1. Clone this repository

```
$ git clone git@github.com:nkmrtty/nature-crawler.git
```

Then, move to the directory `nature-crawler`:

```
$ cd nature-crawler
```

### 3. Run spider

```
$ scrapy crawl nature -o nature.json
```

By default, this script crawl abstract of articles published in the latest month, then store the result as `nature.json`.  
If you need articles published in the specific month, use `-a ym=YYYYMM` option as follows:

```
$ scrapy crawl nature -o nature.json -a ym=201702
```
