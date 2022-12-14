from django.contrib import admin

from .models import *


@admin.register(Clan)
class ClanAdmin(admin.ModelAdmin):
    list_display = ("title", "clan_overall_balance")


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ("name", "tier", "phone_number")


@admin.register(PromoCodes)
class PromoCodesAdmin(admin.ModelAdmin):
    list_display = ("code", "amount")


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ("users", "balance")


@admin.register(Transactions)
class TransactionsAdmin(admin.ModelAdmin):
    list_display = ("sender", "recipient")



