from .parse import get_parse_links
from .parse_product import main
from categories.models import TemporarilyLinksUltrarobox


def ultrarobox_parse():
    if not TemporarilyLinksUltrarobox.objects.all():
        get_parse_links()
    main()
