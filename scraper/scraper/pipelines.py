# -*- coding: utf-8 -*-

class ScraperPipeline(object):

	@classmethod
	def process_item(cls, item, spider):
		# TODO: Filter data here
		item.save()
		return item
