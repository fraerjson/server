from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import *


urlpatterns = [
    path('ping/', health_check),

    path('clans/', ClanList.as_view()),
    path('users/', UsersList.as_view()),
    path('user/<int:pk>', UsersRetrieve.as_view()),
    path('promocodes/', PromoCodesList.as_view()),
    path('wallets/', WalletList.as_view()),
    path('transactions/', TransactionsList.as_view()),

    path('wallettransactions/', WalletTransactionsList.as_view()),
    path('clanusers/', ClanUsersList.as_view()),
    path('userwallet/', UsersWalletsList.as_view()),
    path('userwallet/<int:pk>', UsersWalletsRetrieve.as_view()),
    # АВТОРИЗАЦИЯ
    path('authorization/', UsersListView.as_view()),
    path('password/', GetPasswordListView.as_view()),

    path('name/', NameListView.as_view()),
    path('phone_number/', PhoneNumberListView.as_view()),
    path('tg_id/', TgIdListView.as_view()),

    path('walletid/', WalletIdListView.as_view()),

    path('walletid/<int:pk>', WalletsRetrieve.as_view()),

]
