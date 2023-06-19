""" Scraper Settings """
import os
import logging

LOG_FILENAME = "./scraper/logs/output.log"
os.makedirs(os.path.dirname(LOG_FILENAME), exist_ok=True)

logging.basicConfig(
    filename=LOG_FILENAME,
    format=" %(message)s",
    level=logging.WARN,
)

BOT_NAME = "scraper"

SPIDER_MODULES = ["scraper.scraper.spiders"]
NEWSPIDER_MODULE = "scraper.scraper.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/74.0.3729.169 Safari/537.36"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# replace this with your actual user-agent value

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# update the pipelines to this
ITEM_PIPELINES = {"scraper.scraper.pipelines.DjangoPipeline": 300}

LOG_LEVEL = "WARNING"
