from django.shortcuts import render
import pdb
from .classShortUrl import ShortUrl
from shorturl.models import Url


def index(request):
	urls = Url.objects.all().order_by('-id')
	context = {
		'urls':urls
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
