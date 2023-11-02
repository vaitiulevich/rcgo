from .parse import get_parse_links
from .parse_product import main
from categories.models import TemporarilyLinksShopntoys


def shopntoys_parse():
    if not TemporarilyLinksShopntoys.objects.all():
        get_parse_links()
    main()
