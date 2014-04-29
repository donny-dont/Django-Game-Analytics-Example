from datetime import *
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseBadRequest
from models import *
from game.models import *
import json
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

		return HttpResponse(json.dumps(response), mimetype='application/javascript')
	
	return HttpResponseBadRequest()
	
def to_timespan(seconds):
	return str(timedelta(seconds=seconds))
	
def quest_statistics(request, quest_id):
	try:
		quest = Quest.objects.get(pk=quest_id)
		stats = QuestStatistics.objects.filter(quest=quest).latest('date')
		
		response_dict = {}
		response_dict['accepted'] = stats.accepted
		response_dict['rejected'] = stats.rejected
		response_dict['completed'] = stats.completed
		response_dict['not_encountered'] = stats.not_encountered
		response_dict['average_completion']  = to_timespan(stats.average_completion_time)
		response_dict['shortest_completion'] = to_timespan(stats.shortest_completion_time)
		response_dict['longest_completion']  = to_timespan(stats.longest_completion_time)

		response_dict['status'] = [
			{
				'label': 'Accepted',
				'data' : stats.accepted,
			},
			{
				'label': 'Rejected',
				'data' : stats.rejected
			},
			{
				'label': 'Completed',
				'data' : stats.completed
			},
			{
				'label': 'Not Encountered',
				'data' : stats.not_encountered
			}
		]

		return HttpResponse(json.dumps(response_dict), mimetype='application/javascript')

	except Quest.DoesNotExist:
		return HttpResponseBadRequest()
	except QuestStatistics.DoesNotExist:
		return HttpResponseBadRequest()
