import random
from typing import Union

from django.core.exceptions import ObjectDoesNotExist

from allianceauth.eveonline.models import EveCharacter, EveCorporationInfo
from esi.models import Token

from marketmanager.models import PrivateConfig, Structure

from .providers import get_characters_character_id_roles_from_token


def get_corp_token(corporation_id: int, scopes: list, req_roles: list) -> Token:
    """
    Helper method to get a token for a specific character from a specific corp with specific scopes
    :param corp_id: Corp to filter on.
    :param scopes: array of ESI scope strings to search for.
    :param req_roles: roles required on the character.
    :return: :class:esi.models.Token or False
    """
    if 'esi-characters.read_corporation_roles.v1' not in scopes:
        scopes.append("esi-characters.read_corporation_roles.v1")

    char_ids = EveCharacter.objects.filter(
        corporation_id=corporation_id).values('character_id')
    tokens = Token.objects \
        .filter(character_id__in=char_ids) \
        .require_scopes(scopes)

    for token in tokens:
        roles = get_characters_character_id_roles_from_token(token)
        has_roles = False
        for role in roles.get('roles', []):
            if role in req_roles:
                has_roles = True

        if has_roles:
            return token
        else:
            pass  # TODO Maybe remove token?

    return False


def get_random_market_token() -> Token:
    """Very specific edge case, we need _any_ token in order to view data on public structures.

    Args:
        scopes: array of ESI scope strings to search for.

    Returns:
        Matching token
    """
    required_scopes = ['esi-markets.structure_markets.v1']
    random_token = random.choice(
        Token.objects.all().require_scopes(
            required_scopes
            )
        )
    return random_token


def is_existing_order(order, current_orders):
    try:
        existing_order = current_orders.get(order_id=order["order_id"])
        return existing_order
    except ObjectDoesNotExist:
        return False

def get_matching_privateconfig_token(structure_id: int) -> Union[Token, bool]:
    structure = Structure.objects.get(structure_id = structure_id)

    configured_tokens = PrivateConfig.objects.filter(valid_structures = structure)
    if configured_tokens.count() == 0:
        try:
            structure = Structure.objects.get(structure_id = structure_id)
            corporation = EveCorporationInfo.objects.get(corporation_id=structure.owner_id)
        except ObjectDoesNotExist:
            return False
        configured_tokens = PrivateConfig.objects.filter(valid_corporations = corporation)
    try:
        return random.choice(configured_tokens).token
    except IndexError:
        return False
