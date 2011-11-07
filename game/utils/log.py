import csv
import re
from datetime import timedelta
from time import strftime
from quest import log_quest_progress

log_functions = {
	'QUEST_STATUS': log_quest_progress,
}

def parse_log(player_id, log_file):
	print player_id
	log_reader = csv.reader(log_file)
	
	for row in log_reader:
		if len(row) == 3:
			hrs, min, sec = map(int, row[0].split(':'))
			time = timedelta(hours=hrs, minutes=min, seconds=sec)

			event = row[1]
			
			if log_functions.has_key(event):
				func = log_functions[event]
				message = row[2]
				func(time, player_id, message)
