from .parse import get_parse_links
from .parse_product import main
from categories.models import TemporarilyLinksFasrshop


def fasrshop_parse():
    if not TemporarilyLinksFasrshop.objects.all():
        get_parse_links()
    main()
