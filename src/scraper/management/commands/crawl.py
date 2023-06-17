"""Configuration for Crawl Django Command"""
from django.core.management.base import BaseCommand
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from scraper.scraper import settings as my_settings
from scraper.scraper.spiders.productspider import ProductSpider


class Command(BaseCommand):
    """Craw Command Class"""

    help = "Release spider"

    def handle(self, *args, **options):
        crawler_settings = Settings()
        crawler_settings.setmodule(my_settings)

        process = CrawlerProcess(settings=crawler_settings)

        process.crawl(ProductSpider)
        process.start()
