from django.db import models
from game.models import *

class PlayerStatistics(models.Model):
	date = models.DateField(auto_now_add=True)
	count = models.IntegerField(default=0)
	
class QuestStatistics(models.Model):
	quest = models.ForeignKey(Quest)
	date = models.DateField(auto_now_add=True)
	accepted = models.IntegerField(default=0)
	rejected = models.IntegerField(default=0)
	completed = models.IntegerField(default=0)
	not_encountered = models.IntegerField(default=0)
	average_completion_time = models.IntegerField(default=0)
	shortest_completion_time = models.IntegerField(default=0)
	longest_completion_time = models.IntegerField(default=0)
	
class QuestCompletionTimes(models.Model):
	min_time = models.IntegerField()
	max_time = models.IntegerField()
	count = models.IntegerField()
	quest_statistics = models.ForeignKey(QuestStatistics)
