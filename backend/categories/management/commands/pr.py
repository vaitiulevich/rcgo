from django.core.management.base import BaseCommand
from categories.utils.brrc.start_parse import brrc_parse
from categories.utils.fasrshop.start_parse import fasrshop_parse


class Command(BaseCommand):

    def handle(self, *args, **options):
        # fasrshop_parse()
        brrc_parse()

