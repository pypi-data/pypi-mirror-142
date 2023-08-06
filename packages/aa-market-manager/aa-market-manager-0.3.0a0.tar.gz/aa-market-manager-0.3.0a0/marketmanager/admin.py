from django.contrib import admin

from allianceauth.services.hooks import get_extension_logger
from esi.models import Token

from marketmanager.models import (
    Order, PrivateConfig, PublicConfig, Structure, WatchConfig, Webhook,
)

logger = get_extension_logger(__name__)


@admin.register(PublicConfig)
class PublicConfigAdmin(admin.ModelAdmin):
    list_display = ('id', )


@admin.register(PrivateConfig)
class PrivateConfigAdmin(admin.ModelAdmin):
    list_display = ('token', 'failed', 'failure_reason')
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "token":
            required_scopes = ['esi-markets.structure_markets.v1']
            kwargs["queryset"] = Token.objects.all().require_scopes(
            required_scopes
            )
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(WatchConfig)
class WatchConfigAdmin(admin.ModelAdmin):
    list_display = ('type', 'buy_order', 'volume', 'price', )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('eve_type', 'price', 'eve_solar_system', 'is_buy_order', 'issued_by_character', 'issued_by_corporation', 'updated_at')


@admin.register(Structure)
class StructureAdmin(admin.ModelAdmin):
    list_display = ('name', 'solar_system', 'eve_type', 'owner_id', 'pull_market', 'updated_at')


@admin.register(Webhook)
class WebhookAdmin(admin.ModelAdmin):
    list_display = ('name', )
