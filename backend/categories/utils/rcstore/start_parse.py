from .parse import get_parse_links
from .parse_product import main
from categories.models import TemporarilyLinksRcstore


def rcstore_parse():
    if not TemporarilyLinksRcstore.objects.all():
        get_parse_links()
    main()

