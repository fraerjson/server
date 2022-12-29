from django.contrib.auth.models import User, AbstractUser
from django.db import models


class Clan(models.Model):
    title = models.TextField(verbose_name="Название", max_length=20)
    clan_overall_balance = models.FloatField(verbose_name="Общий баланс клана", default=0)

    def __str__(self):
        return self.title


class Users(models.Model):
    TIERS = (
        ("U", "User"),
        ("B", "Bronze"),
        ("S", "Silver"),
        ("G", "Gold"),
        ("A", "Admin"),

    )
    name = models.TextField(verbose_name="Никнэйм", max_length=20)
    password = models.TextField(verbose_name="Пароль", max_length=100)
    phone_number = models.TextField(verbose_name="Номер телефона")
    tg_id = models.CharField(verbose_name="Телеграмм айди", max_length=100)
    data = models.DateTimeField(auto_now_add=True)
    tier = models.CharField(max_length=1, choices=TIERS, default="U")
    clan = models.ForeignKey(Clan, on_delete=models.CASCADE, null=True, blank=True, related_name='user')

    def __str__(self):
        return str(self.name)


class PromoCodes(models.Model):
    code = models.TextField(verbose_name='Промокоды', max_length=8)
    amount = models.TextField(verbose_name='Количество', max_length=20)


class Wallet(models.Model):
    CURRENCY = (
        ("USD", "dollar"),
        ("BTC", "bitcoin"),
        ("ETH", "ethereum"),
        ("ADA", "cardano"),
        ("BNB", "binance_coin"),
        ("XRP", "xrp"),
        ("DOGE", "dogecoin"),
    )
    currency = models.CharField(max_length=4, choices=CURRENCY, null=True, blank=True)
    users = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='wallets')
    amount = models.FloatField(verbose_name="Баланс", max_length=30)

    def __str__(self):
        return f"{str(self.users)} | {str(self.currency)}"


class Transactions(models.Model):
    CURRENCY = (
        ("USD", "dollar"),
        ("BTC", "bitcoin"),
        ("ETH", "ethereum"),
        ("ADA", "cardano"),
        ("BNB", "binance_coin"),
        ("XRP", "xrp"),
        ("DOGE", "dogecoin"),
    )
    date = models.DateTimeField(verbose_name='Дата оплаты', auto_now_add=True)
    sender = models.TextField(verbose_name='Отправитель')
    sender_currency = models.CharField(max_length=4, choices=CURRENCY, null=True, blank=True)
    send_amount = models.FloatField(verbose_name='Отпраленно средств', max_length=100, default=0)
    recipient = models.TextField(verbose_name='Получатель')
    recipient_currency = models.CharField(max_length=4, choices=CURRENCY, null=True, blank=True)
    received_amount = models.FloatField(verbose_name='Полученно стредств', max_length=100, default=0)
    commission = models.FloatField(verbose_name="Комисиия", max_length=100, default=0)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name="transactions")

    def __str__(self):
        return f"{self.sender} | {self.recipient} | {self.sender_currency} | {self.recipient_currency}"


# class Wallet(models.Model):
#     users = models.OneToOneField(Users, on_delete=models.CASCADE, related_name='wallets')
#     balance = models.FloatField(verbose_name="Баланс", max_length=30)
#     overall_balance = models.FloatField(verbose_name="Общий баланс", default=100000)
#     bitcoin = models.FloatField(verbose_name="Bitcoin", default=0)
#     ethereum = models.FloatField(verbose_name="Ethereum", default=0)
#     litecoin = models.FloatField(verbose_name="Litecoin", default=0)
#     binance_coin = models.FloatField(verbose_name="Binance Coin", default=0)
#     cardano = models.FloatField(verbose_name="Cardano", default=0)
#     solana = models.FloatField(verbose_name="Solana", default=0)
#
#     def __str__(self):
#         return str(self.users)
#
