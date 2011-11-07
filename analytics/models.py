from django.db import models
from game.models import *

class PlayerStatistics(models.Model):
	date = models.DateField()
	count = models.IntegerField()
	
class QuestStatistics(models.Model):
	date = models.DateField()
	accepted = models.IntegerField()
	rejected = models.IntegerField()
	completed = models.IntegerField()
	not_encountered = models.IntegerField()
	average_completion_time = models.IntegerField()
	shortest_completion_time = models.IntegerField()
	longest_completion_time = models.IntegerField()
	quest = models.ForeignKey(Quest)
	
class QuestCompletionTimes(models.Model):
	min_time = models.IntegerField()
	max_time = models.IntegerField()
	count = models.IntegerField()
	quest_statistics = models.ForeignKey(QuestStatistics)
