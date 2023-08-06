import datetime
import json
from decimal import Decimal

import requests
from eveuniverse.models import (
    EveConstellation, EveRegion, EveSolarSystem, EveType,
)

from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from allianceauth.eveonline.models import EveCharacter, EveCorporationInfo
from esi.models import Token


class General(models.Model):
    """Meta model for app permissions"""

    class Meta:
        managed = False
        default_permissions = ()
        permissions = (
            ("basic_market_browser", "Can access the Standard Market Browser"),
            ("order_highlight_user", "Market orders owned by the user's characters may be highlighted in the standard/basic Market Browser"),
            ("order_highlight_corporation", "Market orders owned by any corporation a user is a member of may be highlighted in the standard/basic Market Browser WARNING: This has no checks for Corporation Roles."),
            ("advanced_market_browser", "Can access the Avanced Market Browser"),
            ("can_add_token_character", "Can add a Character Token with required scopes"),
            ("can_add_token_corporation", "Can add a Corpration Token with required scopes"),
            )


class Order(models.Model):
    """An EVE Market Order"""
    order_id = models.PositiveBigIntegerField(
        _("Order ID"),
        help_text="Unique order ID",
        primary_key=True)
    eve_type = models.ForeignKey(
        EveType,
        verbose_name=_("Type"),
        on_delete=models.CASCADE)
    duration = models.PositiveIntegerField(
        _("Duration"),
        help_text="Number of days the order was valid for (starting from the issued date). An order expires at time issued + duration")
    is_buy_order = models.BooleanField(
        _("Buy Order"),
        default=False,
        help_text="True if the order is a bid (buy) order",
        db_index=True)
    issued = models.DateTimeField(
        _("Issued"),
        help_text="Date and time when this order was issued",
        auto_now=False,
        auto_now_add=False)
    location_id = models.PositiveBigIntegerField(
        _("Location ID"),
        help_text="ID of the location where order was placed")
    eve_solar_system = models.ForeignKey(
        EveSolarSystem,
        verbose_name=_("System"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,)
    eve_region = models.ForeignKey(
        EveRegion,
        verbose_name=_("Region"),
        on_delete=models.CASCADE)
    min_volume = models.PositiveIntegerField(
        _("Minimum Volume"),
        null=True,
        blank=True,
        help_text="For buy orders, the minimum quantity that will be accepted in a matching sell order")
    price = models.DecimalField(
        _("Price"),
        max_digits=20,
        decimal_places=2,
        help_text="Cost per unit for this order")
    escrow = models.DecimalField(
        _("Escrow"),
        max_digits=20,
        decimal_places=2,
        null=True,
        blank=True,
        help_text="For buy orders, the amount of ISK in escrow")
    RANGE_CHOICES = [
        ('1', '1'), ('10', '10'), ('2', '2'), ('20', '20'), ('3', '3'),
        ('30', '30'), ('4', '4'), ('40', '40'), ('5', '5'),
        ('region', _('Region')),
        ('solarsystem', _('Solar System')),
        ('station', _('Station'))]
    range = models.CharField(
        _("Order Range"),
        max_length=20,
        choices=RANGE_CHOICES,
        help_text="Valid order range, numbers are ranges in jumps")
    volume_remain = models.PositiveIntegerField(
        _("Volume Remaining"),
        help_text="Quantity of items still required or offered")
    volume_total = models.PositiveIntegerField(
        _("Volume Total"),
        help_text="Quantity of items required or offered at time order was placed")
    is_corporation = models.BooleanField(
        _("Is Corporation"),
        default=False,
        help_text="Signifies whether the buy/sell order was placed on behalf of a corporation.")
    wallet_division = models.PositiveSmallIntegerField(
        _("Wallet Division"),
        null=True,
        blank=True,
        help_text="The corporation wallet division used for this order.")
    issued_by_character = models.ForeignKey(
        EveCharacter,
        verbose_name=_("Character"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True)
    issued_by_corporation = models.ForeignKey(
        EveCorporationInfo,
        verbose_name=_("Corporation"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,)
    STATE_CHOICES = [
        ('', ''),
        ('cancelled', _('Cancelled')),
        ('expired ', _('Expired'))]
    state = models.CharField(
        _("Order State"),
        max_length=20,
        choices=STATE_CHOICES,
        help_text="Current order state, Only valid for Authenticated order History. Will not update from Public Market Data.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    source_public = models.BooleanField(
        _("Sourced From Public Market Data"),
        default=False)
    source_private = models.BooleanField(
        _("Sourced From Public Market Data"),
        default=False)
    source_character = models.BooleanField(
        _("Sourced From Character API Market Data"),
        default=False)
    source_corporation = models.BooleanField(
        _("Sourced From Corporation API Market Data"),
        default=False)

    class Meta:
        """
        Meta definitions
        """
        default_permissions = ()

    @property
    def expiry(self):
        return self.issued + datetime.timedelta(days=self.duration)


class Structure(models.Model):
    """An EVE Online Upwell Structure"""
    structure_id = models.PositiveBigIntegerField(
        _("Structure ID"),
        primary_key=True)
    name = models.CharField(
        _("Name"),
        max_length=100)
    owner_id = models.IntegerField(_("Owner Corporation ID"))
    solar_system = models.ForeignKey(
        EveSolarSystem,
        verbose_name=_("Solar System"),
        on_delete=models.CASCADE)
    eve_type = models.ForeignKey(
        EveType,
        verbose_name=_("Type"),
        on_delete=models.CASCADE)
    pull_market = models.BooleanField(
        _("Pull Market Orders"),
        help_text="Useful to ignore specific structures for _reasons_",
        default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    class Meta:
        """
        Meta definitions
        """
        default_permissions = ()



class Webhook(models.Model):
    name = models.CharField(
        _("Name"),
        max_length=100)
    url = models.URLField(
        _("URL"),
        max_length=200)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def send_embed(self, embed):
        custom_headers = {'Content-Type': 'application/json'}
        data = '{"embeds": [%s]}' % json.dumps(embed)
        r = requests.post(self.url, headers=custom_headers,
                            data=data)
        r.raise_for_status()

    class Meta:
        """
        Meta definitions
        """
        default_permissions = ()


class WatchConfig(models.Model):
    """Rules to Watch"""
    buy_order = models.BooleanField(_("Buy Order"))
    eve_type = models.ForeignKey(
        EveType,
        verbose_name=_("EVE Type"),
        on_delete=models.CASCADE)
    # Location Rules, Combined
    location = models.ManyToManyField(
        Structure,
        verbose_name=_("Structure"),
        blank=True)
    solar_system = models.ManyToManyField(
        EveSolarSystem,
        verbose_name=_("Solar System"),
        blank=True)
    constellation = models.ManyToManyField(
        EveConstellation,
        verbose_name=_("Constellation"),
        blank=True
    )
    region = models.ManyToManyField(
        EveRegion,
        verbose_name=_("Region"),
        blank=True)
    # Filter
    structure_type = models.ManyToManyField(
        EveType,
        help_text="Filter by structure Type/Size/Docking (ie, forts/keeps for cap fuel)",
        verbose_name=_("Structure Type Filter"),
        related_name="structure_type",
        blank=True)
    # Settings
    volume = models.IntegerField(
        _("Volume"),
        help_text="Set to Zero to check ANY/EVERY order against Price",
        default=1,
        blank=False)
    price = models.IntegerField(
        _("Price"),
        help_text="Set to Zero to skip this filter",
        default=0,
        blank=False)
    jita_compare_percent = models.DecimalField(
        _("Jita Comparison %"),
        help_text="If set ignores Flat price value",
        max_digits=3,
        decimal_places=0,
        default=Decimal(0),
        validators=[MinValueValidator(0), MaxValueValidator(100)])
    CONFIG_TYPE_CHOICES = [
        ("Supply", _("Supply Check")),
        ("Bargain", _("Bargain Finder")),
        ("Scalp", _("Scalp Finder"))]
    config_type = models.CharField(
        _("Config Type"),
        max_length=10,
        choices=CONFIG_TYPE_CHOICES,
        help_text="The type of WatchConfig, check documentation for more.",
        blank=False,
        default="Supply")

    # Type
        # Supply Check, Ensure there is available Volume at the Given Price with conditions
        # Bargain Finder, Highlight orders that fall under the given thresholds.
        # Scalp Finder, Highlight orders that breach conditions.

    # Destinations

    webhooks = models.ManyToManyField(
        Webhook,
        verbose_name=_("Webhooks"),
        blank=True)

    debug_webhooks = models.ManyToManyField(
        Webhook,
        verbose_name=_("Debug Webhook"),
        related_name="debug_webhooks",
        blank=True,
        help_text="Primarily for Testing/Debugging Purposes. This webhook will receive updates on WatchConfigs that _dont_ notify. Because their Configs didnt Meet/Breach.")

    class Meta:
        """
        Meta definitions
        """
        default_permissions = ()


class PublicConfig(models.Model):
    fetch_regions = models.ManyToManyField(
        EveRegion,
        verbose_name=_("Fetch Regions")
    )

    def save(self, *args, **kwargs):
        if not self.pk and PublicConfig.objects.exists():
            # Force a single object
            raise ValidationError('There is can be only one \
                                    AnalyticsIdentifier instance')
        self.pk = self.id = 1  # If this happens to be deleted and recreated, force it to be 1
        return super().save(*args, **kwargs)

    class Meta:
        """
        Meta definitions
        """
        default_permissions = ()


class PrivateConfig(models.Model):
    token = models.OneToOneField(
        Token,
        verbose_name=_("ESI Token"),
        on_delete=models.CASCADE
        )
    valid_corporations = models.ManyToManyField(
        EveCorporationInfo,
        verbose_name=_("Valid Corporation Markets for this Token"),
        blank=True,
        )
    valid_structures = models.ManyToManyField(
        Structure,
        verbose_name=_("Valid Structure Markets for this Token"),
        blank=True,
        )
    failed = models.BooleanField(_("Disabled due to Failure, Check reason, adjust config and re-enable"))
    failure_reason = models.CharField(
        _("Failure Reason"),
        max_length=100,
        blank=True,
        default="")

    class Meta:
        """
        Meta definitions
        """
        default_permissions = ()
