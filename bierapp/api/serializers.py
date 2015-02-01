from rest_framework import serializers

from bierapp.accounts.models import User, Site
from bierapp.core.models import Product, Transaction, TransactionItem

import math


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = ("name", )


class ProductSerializer(serializers.ModelSerializer):
    logo = serializers.SerializerMethodField("get_logo")

    class Meta:
        model = Product
        exclude = ("site", "is_app_visible")

    def get_logo(self, product):
        request = self.context["request"]

        if product.logo:
            return request.build_absolute_uri(product.logo.url)


class TransactionItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionItem
        exclude = ("id", "transaction", "product_group", "value")


class TransactionSerializer(serializers.ModelSerializer):
    transaction_items = TransactionItemSerializer(many=True)

    class Meta:
        model = Transaction
        exclude = ("site", )


class BalanceSerializer(serializers.Serializer):
    product = serializers.Field()
    count = serializers.Field()
    value = serializers.Field()

    estimated_count = serializers.SerializerMethodField("get_estimated_count")

    def get_estimated_count(self, info):
        try:
            return int(
                math.floor(info["total_value"] / info["product__value"]))
        except ZeroDivisionError:
            return 0


class UserInfoSerializer(serializers.Serializer):
    id = serializers.Field()
    xp = serializers.Field()

    balance = BalanceSerializer(many=True)


class UserSerializer(serializers.ModelSerializer):
    user_type = serializers.Field()
    avatar = serializers.SerializerMethodField("get_avatar")
    # product_info = ProductInfoSerializer()

    class Meta:
        model = User
        fields = (
            "id", "first_name", "last_name", "avatar", "avatar_height",
            "avatar_width", "user_type", "date_changed")

    def get_avatar(self, user):
        request = self.context["request"]

        if user.avatar:
            return request.build_absolute_uri(user.avatar.url)