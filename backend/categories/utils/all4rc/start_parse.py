from .parse import get_parse_links
from .parse_product import main
from categories.models import TemporarilyLinksAll4rc


def all4rc_parse():
    if not TemporarilyLinksAll4rc.objects.all():
        get_parse_links()
    main()

