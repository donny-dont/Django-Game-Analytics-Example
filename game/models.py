from django.db import models

class Player(models.Model):
	name = models.CharField(max_length=100)
	
class Quest(models.Model):
	name = models.CharField(max_length=100)
	code = models.CharField(max_length=100, unique=True)
		
class QuestState(models.Model):
	DECLINED_STATUS = 1
	ACCEPTED_STATUS = 2
	COMPLETED_STATUS = 3
	
	QUEST_STATUS = (
		(DECLINED_STATUS, 'Declined'),
		(ACCEPTED_STATUS, 'Accepted'),
		(COMPLETED_STATUS, 'Completed')
	)

	player = models.ForeignKey(Player)
	quest = models.ForeignKey(Quest)
	status = models.IntegerField(choices=QUEST_STATUS, null=True)
	start_time = models.IntegerField(null=True)
	end_time = models.IntegerField(null=True)
	completion_time = models.IntegerField(null=True)
