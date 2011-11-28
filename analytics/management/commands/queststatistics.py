from datetime import *
from django.core.management.base import BaseCommand, CommandError
from django.db.models import Avg, Min, Max
from analytics.models import *
from game.models import *

class Command(BaseCommand):

    def handle(self, *args, **options):
		player_count = Player.objects.count()
		quests = Quest.objects.all()
		
		for quest in quests:
			print 'Quest\n'
			stats = QuestStatistics(quest=quest)

			# Get statistics for the various states
			completion_query = QuestState.objects.filter(quest=quest, status=QuestState.COMPLETED_STATUS)
			stats.completed = completion_query.count()
			stats.accepted = QuestState.objects.filter(quest=quest, status=QuestState.ACCEPTED_STATUS).count()
			stats.rejected = QuestState.objects.filter(quest=quest, status=QuestState.DECLINED_STATUS).count()
			stats.not_encountered = player_count - stats.accepted - stats.rejected - stats.completed
			
			# Get statistics for the completion times
			if stats.completed > 0:
				result = completion_query.aggregate(Avg('completion_time'))
				stats.average_completion_time = result['completion_time__avg']

				result = completion_query.aggregate(Min('completion_time'))
				stats.shortest_completion_time = result['completion_time__min']

				result = completion_query.aggregate(Max('completion_time'))
				stats.longest_completion_time = result['completion_time__max']
			
			stats.save()
			
