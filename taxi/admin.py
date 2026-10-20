from django.contrib import admin
from .models import Profile, Tariff

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')

    list_filter = ('role',)

    search_fields = ('user__username',)

@admin.register(Tariff)
class TariffAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'base_price',
        'price_per_km',
        'is_active',
    )

    list_filter = ('is_active',)

    search_fields = ('name',)