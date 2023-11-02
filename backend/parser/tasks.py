from categories.utils.brrc.start_parse import brrc_parse
from categories.utils.fasrshop.start_parse import fasrshop_parse
from categories.utils.all4rc.start_parse import all4rc_parse
from categories.utils.hobbycenter.start_parse import hobbycenter_parse
from categories.utils.rcstore.start_parse import rcstore_parse
from categories.utils.nitrorcx.start_parse import nitrorcx_parse
from categories.utils.optax.start_parse import optax_parse
from categories.utils.shopntoys.start_parse import shopntoys_parse
from categories.utils.ultrarobox.start_parse import ultrarobox_parse
from celery import shared_task
import re
import requests
from bs4 import BeautifulSoup
from django.core.cache import cache
from products.models import Rates


@shared_task(name="get_rates")
def get_rates():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    }
    response = requests.get('https://tb.by/individuals/', headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    soup = soup.find('table', class_='table-course')
    soup = soup.getText().replace('\n', '')
    rate = Rates.objects.first()
    rate.usd = float(re.findall(r'(\d.\d+)EUR', soup)[0])
    rate.rus = float(re.findall(r'(\d.\d+)CNY', soup)[0])
    rate.save()


@shared_task(name="start_parsing_brrc")
def parse_brrc():
    brrc_parse()


@shared_task(name="start_parsing_fasrshop")
def parse_fasrshop():
    fasrshop_parse()


@shared_task(name="start_parsing_all4rc")
def parse_all4rc():
    all4rc_parse()


@shared_task(name="start_parsing_hobbycenter")
def parse_hobbycenter():
    hobbycenter_parse()


@shared_task(name="start_parsing_rcstore")
def parse_rcstore():
    rcstore_parse()


@shared_task(name="start_parsing_nitrorcx")
def parse_nitrorcx():
    nitrorcx_parse()


@shared_task(name="start_parsing_optax")
def parse_optax():
    optax_parse()


@shared_task(name="start_parsing_shopntoys")
def parse_shopntoys():
    shopntoys_parse()


@shared_task(name="start_parsing_ultrarobox")
def parse_ultrarobox():
    ultrarobox_parse()


@shared_task(name='cache_clean')
def cache_clean():
    cache.clear()
