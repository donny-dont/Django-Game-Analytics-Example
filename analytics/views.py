from datetime import *
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import simplejson
from django.http import HttpResponse, HttpResponseBadRequest
from models import *
from game.models import *
import random

def quests(request):
	quests = Quest.objects.all()

	return render_to_response(
		'quest_statistics.html',
		{ 'quests': quests, 'quest_selected': True},
		context_instance=RequestContext(request))
		
def players(request):
	return render_to_response(
		'player_statistics.html',
		{ 'players_selected': True},
		context_instance=RequestContext(request))
	

def to_date(year_str, month_str, day_str):
	year = int(year_str)
	month = int(month_str)
	day = int(day_str)
	
	return date(year, month, day)
	
def player_statistics(request, start_year, start_month, start_day, end_year, end_month, end_day):
	start_date = to_date(start_year, start_month, start_day)
	end_date = to_date(end_year, end_month, end_day)
	
	if (start_date < end_date):
		player_statistics = PlayerStatistics.objects.filter(date__range=(start_date, end_date))
	
		response = []
		
		for statistic in player_statistics:
			response.append({'date': str(statistic.date), 'count': statistic.count})

		return HttpResponse(simplejson.dumps(response), mimetype='application/javascript')
	
	return HttpResponseBadRequest()
	
def random_timespan(min_secs, max_secs):
	return str(timedelta(seconds=random.randint(min_secs, max_secs)))
	
def quest_statistics(request):
	response_dict = {}
	response_dict['average_completion']  = random_timespan( 6000,  9000)
	response_dict['shortest_completion'] = random_timespan( 1500,  4500)
	response_dict['longest_completion']  = random_timespan(12000, 15000)

	response_dict['status'] = [
		{
			'label': 'Accepted',
			'data' : random.randint(100,1000),
		},
		{
			'label': 'Declined',
			'data' : random.randint(100,1000),
		},
		{
			'label': 'Completed',
			'data' : random.randint(100,1000),
		},
	]

	return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')
