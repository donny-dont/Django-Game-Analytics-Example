from game.models import *

def log_quest_progress(time, player_id, quest_id, description):

	player = Player.objects.get(id=player_id)
	quest = Quest.objects.get(id=quest_id)
	
	print player
	print quest.name
	
	quest_state = QuestState.objects.get_or_create(player=player, quest=quest)
		
	if description == 'ACCEPTED':
		#quest_state.status = 2
		quest_state.start_time = time
	elif description == 'DECLINED':
		print quest_state.player
		#quest_state.status = 1
	elif description == 'COMPLETED':
		#quest_state.status = 3
		quest_state.end_time = time
	else:
		print description
		
	quest_state.save()