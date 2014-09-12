import requests
# -*- coding: utf-8 -*-

class image:

	def __init__(self, title, auth_author, resourceURL="none", resource_facet = "none",**other_kwargs):
		self.title = title
		self.author = auth_author
		self.resourceUrl = resourceURL
		
		if resource_facet == "Resource available online":
			r = requests.head(self.resourceUrl[0])

			#check if image exists
			if r.status_code == 404:
				print(r.status_code)
				self.online = False
			else:
				self.online = True
		else:
			self.online = False

		self.other_kwargs = other_kwargs

	def __repr__(self):
		return '<%s, %s, %s>' % (self.title, self.author, self.resourceUrl)
