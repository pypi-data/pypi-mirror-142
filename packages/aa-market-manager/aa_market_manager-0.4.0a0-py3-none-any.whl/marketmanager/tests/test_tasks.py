from django.test.testcases import TestCase

from marketmanager.tasks import (
    fetch_all_character_orders, fetch_all_corporation_orders,
    fetch_all_corporations_structures, fetch_characters_character_id_orders,
    fetch_corporations_corporation_id_orders,
    fetch_corporations_corporation_id_structures,
    fetch_markets_region_id_orders, fetch_markets_structures_structure_id,
    fetch_public_market_orders, fetch_public_structures,
    fetch_universe_structures_structure_id,
)
