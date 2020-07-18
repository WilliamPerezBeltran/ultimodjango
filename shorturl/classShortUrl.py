import hashlib
import pdb
import base62

class ShortUrl():
	def __init__(self,url):
		self.url = url

	def convert_url(self):
		md5 = hashlib.md5(self.url.encode('utf-8'))
		hex_number =md5.hexdigest()
		decimal_number = int(hex_number,16)
		return base62.encode(decimal_number)
