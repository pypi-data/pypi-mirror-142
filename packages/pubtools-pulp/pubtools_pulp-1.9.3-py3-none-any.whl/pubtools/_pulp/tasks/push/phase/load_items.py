import logging

from pushsource import Source

from .base import Phase
from ..items import PulpPushItem


LOG = logging.getLogger("pubtools.pulp")


class LoadPushItems(Phase):
    """Phase for loading push items.

    This should be the very first phase, as it is responsible for discovering
    the content which should be operated on by all the later phases.

    Input queue:
    - none.

    Output queue:
    - items which should be pushed by this task. The items might be missing
      checksums and will definitely be missing any info regarding the Pulp state.

    Side-effects:
    - populates items_known, items_count on the context.
    """

    def __init__(self, context, source_urls, **_):
        super(LoadPushItems, self).__init__(context, name="Load push items")
        self._source_urls = source_urls

    def run(self):
        count = 0

        for source_url in self._source_urls:
            with Source.get(source_url) as source:
                LOG.info("Loading items from %s", source_url)
                for item in source:
                    pulp_item = PulpPushItem.for_item(item)
                    if pulp_item:
                        self.put_output(pulp_item)
                        count += 1
                    else:
                        LOG.info("Skipping unsupported type: %s", item)

        # We know exactly how many items we're dealing with now.
        # Set this on the context, which allows for more accurate progress
        # info.
        self.context.items_count = count
        self.context.items_known.set()
