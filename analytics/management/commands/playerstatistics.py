from datetime import *
from django.core.management.base import BaseCommand, CommandError
from analytics.models import PlayerStatistics
from game.models import Player

class Command(BaseCommand):

    def handle(self, *args, **options):
		stats = PlayerStatistics()
		stats.count = Player.objects.count()
		
		stats.save()
