from .parse import get_parse_links
from .parse_product import main
from categories.models import TemporarilyLinksHobbyCenter


def hobbycenter_parse():
    if not TemporarilyLinksHobbyCenter.objects.all():
        get_parse_links()
    main()

