# -*- coding: utf-8 -*-

class image:

	def __init__(self, title, auth_author, resourceURL="none", **other_kwargs):
		self.title = title
		self.author = auth_author
		self.url = resourceURL
		self.other_kwargs = other_kwargs

	def __repr__(self):
		return '<%s, %s, %s>' % (self.title, self.author, self.url)
