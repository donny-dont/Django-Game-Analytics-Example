from django.db import models

class Player(models.Model):
	name = models.CharField(max_length=100)
	
class Quest(models.Model):
	name = models.CharField(max_length=100)
	
QUEST_STATUS = (
	(1, 'Declined'),
	(2, 'Accepted'),
	(3, 'Completed')
)
	
class QuestState(models.Model):
	player = models.ForeignKey(Player)
	quest = models.ForeignKey(Quest)
	status = models.IntegerField(choices=QUEST_STATUS, null=True)
	start_time = models.IntegerField(null=True)
	end_time = models.IntegerField(null=True)
