import requests
# -*- coding: utf-8 -*-

class image:

	def __init__(self, title="none", auth_author="none", resourceURL="none", resource_facet = "none",**other_kwargs):
		self.title = title
		self.author = auth_author
		self.resourceUrl = resourceURL
		
		if resource_facet == "Resource available online":
			self.online = True
		else:
			self.online = False

		self.other_kwargs = other_kwargs

	def __repr__(self):
		return '<%s, %s, %s>' % (self.title, self.author, self.resourceUrl)
