from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseBadRequest
from forms import LogForm

def upload_log(request):
	if request.method == 'POST':
		form = LogForm(request.POST)
		if form.is_valid:
			return HttpResponse()
		else:
			return HttpResponseBadRequest()
		
	return render_to_response('upload_log.html', {'form': LogForm()})