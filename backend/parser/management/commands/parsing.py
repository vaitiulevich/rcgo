from django.core.management.base import BaseCommand
import json
from django.utils import timezone
from django_celery_beat.models import PeriodicTask, IntervalSchedule

from parser.utils.brrc.brrc import parse_csv as brrc
from parser.utils.fasrshop.fasrshop_parser import parse_product_file as fasrshop
from parser.utils.optax.optax import main as optax
from backend.parser.utils.hobbycenter.parse_hobbycenter import main as hobbycenter


class Command(BaseCommand):

    def handle(self, *args, **options):
        def parse():
            pass
            # brrc()
            # fasrshop()
            # optax()
            # hobbycenter()
        # parse()
