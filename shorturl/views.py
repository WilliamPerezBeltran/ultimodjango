from django.shortcuts import render
import pdb
from .classShortUrl import ShortUrl
from shorturl.models import Url


def index(request):
	# pdb.set_trace()
	urls = Url.objects.all().order_by('-id')
	context = {
		'urls':urls,
		'host':request.META['HTTP_HOST'] 
	}
	if request.method == 'POST':
		url_string = request.POST['url']
		urlinstance = ShortUrl(url_string)
		# pdb.set_trace()
		short_url = urlinstance.convert_url()
		url = Url(url=url_string,shortUrl=short_url)
		try:
			if url.save():
				return render(request,'shorturl/index.html',context)
		except Exception as e:
			return e
	return render(request,'shorturl/index.html',context)

def get_url(request,short_url):
	try:
		url_string = Url.objects.filter(shortUrl=short_url)[0]
	except Exception as e:
		context = {
			'url':"no se encontro"
		}
		return render(request,'shorturl/original_url.html',context)
	else:

		context = {
			'url':url_string
		}
		return render(request,'shorturl/original_url.html',context)



