import re
import logging
from django.db import models
from game.models import *

quest_regex = re.compile('(?P<code>\w+)\s+(?P<status>ACCEPTED|DECLINED|COMPLETED)')

logger = logging.getLogger(__name__)

def log_quest_progress(time, player_id, message):
	
	m = quest_regex.match(message)
	
	if m:
		quest_code = m.group('code')
		print quest_code
		
		try:
			player = Player.objects.get(id=player_id)
			quest = Quest.objects.get(code=quest_code)
		
			quest_state, created = QuestState.objects.get_or_create(player=player, quest=quest)
			
			status = m.group('status')
			
			if (status == 'DECLINED'):
				quest_state.status = QuestState.DECLINED_STATUS
			elif (status == 'ACCEPTED'):
				quest_state.status = QuestState.ACCEPTED_STATUS
				quest_state.start_time = time.total_seconds()
			else:
				quest_state.status = QuestState.COMPLETED_STATUS
				quest_state.end_time = time.total_seconds()
		
			quest_state.save()
			
		except Player.DoesNotExist as e:
			logger.error("Player does not exist")
		except Quest.DoesNotExist as e:
			logger.error("Quest does not exist")
	else:
		logger.error("Invalid message")
