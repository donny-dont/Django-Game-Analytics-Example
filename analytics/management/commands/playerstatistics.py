from datetime import *
from django.core.management.base import BaseCommand, CommandError
from analytics.models import PlayerStatistics
from game.models import Player

class Command(BaseCommand):

    def handle(self, *args, **options):
		stats, created = PlayerStatistics.objects.get_or_create(date=date.today(), defaults={'count': 0})
		stats.count = Player.objects.count()
		
		stats.save()
