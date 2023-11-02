from .parse import get_parse_links
from .parse_product import main
from categories.models import TemporarilyLinksNitrorcx


def nitrorcx_parse():
    if not TemporarilyLinksNitrorcx.objects.all():
        get_parse_links()
    main()

