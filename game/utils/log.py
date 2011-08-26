import csv
import re
from time import strftime
from quest import log_quest_progress

quest_regex = re.compile('(QUEST)\s+(\d+)\s*(.*)')

def parse_log(player_id, log_file):
	print player_id
	log_reader = csv.reader(log_file)
	
	for row in log_reader:
		if len(row) == 2:
			time = strftime(row[0])
			event = row[1]
			
			m = quest_regex.match(event)
			if m:
				print m.group(0)
				log_quest_progress(time, player_id, m.group(2), m.group(3))
