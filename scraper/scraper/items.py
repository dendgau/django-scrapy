# -*- coding: utf-8 -*-
from scrapy_djangoitem import DjangoItem
from scrap.models import ScrapyData


class ScraperItem(DjangoItem):
	django_model = ScrapyData
