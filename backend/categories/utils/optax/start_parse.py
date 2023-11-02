from .parse import get_parse_links
from .parse_product import main
from categories.models import TemporarilyLinksOptax


def optax_parse():
    if not TemporarilyLinksOptax.objects.all():
        get_parse_links()
    main()

