"""Product Spider"""
from scrapy import Spider, Request
from scrapy.http.response.html import HtmlResponse

from scraper.scraper.items import ProductItem


class ProductSpider(Spider):
    """Product Spider Class"""

    name = "products"
    start_urls = ["https://world.openfoodfacts.org/"]

    def parse(self, response: HtmlResponse, **kwargs):
        products = response.css("div#search_results").css("li")
        for product in products:
            url = response.urljoin(product.css("a::attr(href)").get())
            product_name = str(product.css("span::text").get()).replace("\xa0", " ")
            yield Request(
                url,
                cb_kwargs={"url": url, "product_name": product_name},
                callback=self.parse_product,
            )

    def parse_product(self, response, url, product_name):
        """Scrap Each Product"""
        product = ProductItem()
        product["url"] = url
        product["code"] = response.css("p#barcode_paragraph").css("span::text").get()
        product["barcode"] = product["code"] + " (EAN / EAN-13) "
        product["product_name"] = (
            response.css("span#field_generic_name_value").css("span::text").get()
            or product_name
        )
        product["quantity"] = response.css("span#field_quantity_value::text").get()
        product["packaging"] = ", ".join(
            response.css("span#field_packaging_value").css("a::text").getall()
        )
        product["brands"] = ", ".join(
            response.css("span#field_brands_value").css("a::text").getall()
        )
        product["categories"] = ", ".join(
            response.css("span#field_categories_value").css("a::text").getall()
        )
        product["image_url"] = response.css('img.product_image::attr("src")').get()
        yield product
