# -*- coding: utf-8 -*-
import imp
import os
import sys
from django.core.management import setup_environ

BOT_NAME = 'scraper'

ITEM_PIPELINES = {
	'scraper.pipelines.ScraperPipeline': 0,
}

SPIDER_MODULES = ['scraper.spiders']
NEWSPIDER_MODULE = 'scraper.spiders'

# Requirement: Django == 1.5
def setup_django_env(path_django_project):
	f, filename, desc = imp.find_module('settings', [path_django_project])
	setup_environ(imp.load_module('settings', f, filename, desc))
	sys.path.append(os.path.abspath(os.path.join(path_django_project, os.path.pardir)))

# The absolute path of django project
setup_django_env('C:/Users/dend/Desktop/Intergrate/mysite/mysite')


