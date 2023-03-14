import requests
from datetime import datetime

class Tweet:
	def __init__(self, id):
		self.id = id
		try:
			self.__data= requests.get("https://cdn.syndication.twimg.com/tweet-result?id="+str(id)).json()
		except:
			self.__data=dict()
		self.__dict__.update(self.__data)
		if 'created_at' in self.__data.keys():
			self.created_at = datetime.strptime(self.created_at,'%Y-%m-%dT%H:%M:%S.%fZ')
		if 'user' in self.__data.keys():
			self.user = User(self.user)
		if 'parent' in self.__data.keys():
			self.parent = Parent(self.parent)
		if 'entities' in self.__data.keys():
			self.entities = Entities(self.entities)
		
	def __str__(self):
		return f"tweet id: {self.id}"


class User:
	def __init__(self, data):
		try:
			self.__data= data
		except:
			self.__data=dict()
		self.__dict__.update(self.__data)

class Parent:
	def __init__(self, data):
		try:
			self.__data= data
		except:
			self.__data=dict()
		self.__dict__.update(self.__data)
		if 'created_at' in self.__data.keys():
			self.created_at = datetime.strptime(self.created_at,'%Y-%m-%dT%H:%M:%S.%fZ')
		if 'user' in self.__data.keys():
			self.user = User(self.user)
		if 'entities' in self.__data.keys():
			self.entities = Entities(self.entities)

class Entities:
	def __init__(self, data):
		try:
			self.__data= data
		except:
			self.__data=dict()		
		self.__dict__.update(self.__data)
		


