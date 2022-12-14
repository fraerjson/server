from django.shortcuts import get_list_or_404
from rest_framework import viewsets, generics
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import viewsets, generics, status, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend

from server_app.models import *
from server_app.serializers import *

@api_view(["GET"])
def health_check(request):
    return Response({"status": "Ok"}, status.HTTP_200_OK)


"""
БАЗА
"""

class ClanList(generics.ListCreateAPIView):
    queryset = Clan.objects.all()
    serializer_class = ClanSerializer


class UsersList(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class UsersRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class PromoCodesList(generics.ListCreateAPIView):
    queryset = PromoCodes.objects.all()
    serializer_class = PromoCodesSerializer


class WalletList(generics.ListCreateAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer

    def list(self, request, pk):
        wishlist = get_list_or_404(Wallet, user=pk)
        data = serializers.UserWishlistSerializer(wishlist).data
        return Response(data, status=status.HTTP_200_OK)


class TransactionsList(generics.ListCreateAPIView):
    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializer


"""
НЕ БАЗА
"""


class WalletTransactionsList(generics.ListCreateAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletTransactionsSerializer


class ClanUsersList(generics.ListCreateAPIView):
    queryset = Clan.objects.all()
    serializer_class = ClanUsersSerializer


class UsersWalletsList(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersWalletsSerializer


class UsersWalletsRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersWalletsSerializer


class UsersListView(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['phone_number', 'password']


class NameListView(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']


class PhoneNumberListView(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['phone_number']


class TgIdListView(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['tg_id']


