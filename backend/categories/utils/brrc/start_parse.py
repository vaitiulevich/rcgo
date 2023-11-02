from .parse import get_parse_links
from .parse_product import main
from categories.models import TemporarilyLinksBRRC


def brrc_parse():
    if not TemporarilyLinksBRRC.objects.all():
        get_parse_links()
    main()

