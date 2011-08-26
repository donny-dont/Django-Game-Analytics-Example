from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseBadRequest
from forms import LogForm
from utils.log import parse_log

def upload_log(request):
	if request.method == 'POST':
		form = LogForm(request.POST, request.FILES)
		if form.is_valid():
			player_id = form.cleaned_data['player']
			log_file = request.FILES['file']
			
			parse_log(player_id, log_file)
		
			return HttpResponse()
		else:
			return HttpResponseBadRequest()
		
	return render_to_response('upload_log.html', {'form': LogForm()})