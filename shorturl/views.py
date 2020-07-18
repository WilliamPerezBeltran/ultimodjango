from django.shortcuts import render
import pdb
from .classShortUrl import ShortUrl
from shorturl.models import Url


def index(request):
	return render(request,'shorturl/index.html')

def convert_url(request):
	print(request)
	print(request)
	print(request)
	url = request.POST['url']
	urlinstance = ShortUrl('wiliamfalfkafjafkafjk')
	short_url = urlinstance.convert_url()

	print("****************************************+")
	print(short_url)
	print(short_url)
	print(short_url)
	# pdb.set_trace()


	return render(request,'shorturl/index.html')
