from dataclasses import fields
from typing_extensions import Required
from .models import InventoryGroup,Inventory,Shop,Invoice,InvoiceItem
from userint.serializers import CustomUserSerializer
from rest_framework import serializers

class InventoryGroupSerializer(serializers.ModelSerializer):
    created_by = CustomUserSerializer(read_only=True)
    created_by_id = serializers.CharField(write_only=True,required=False)
    belongs_to = serializers.SerializerMethodField(read_only=True)
    belongs_to_id = serializers.CharField(write_only=True)
    total_items = serializers.CharField(read_only=True, required=False)


    class Meta:
        model = InventoryGroup
        fields = "__all__"

    def get_belongs_to(self,obj):
        if obj.belongs_to is not None:
            return InventoryGroupSerializer(obj.belongs_to).data
        return None

class InventorySerializer(serializers.ModelSerializer):
    created_by = CustomUserSerializer(read_only=True)
    created_by_id = serializers.CharField(write_only=True,required=False)
    # price= serializers.FloatField(Required=True)
    group = InventoryGroupSerializer(read_only=True)
    group_id =serializers.CharField(write_only=True)


    class Meta:
        model =Inventory
        fields = "__all__"

class ShopSerializer(serializers.ModelSerializer):
    created_by = CustomUserSerializer(read_only=True)
    created_by_id = serializers.CharField(write_only=True,required=False)
    amount_total = serializers.CharField(required=False,read_only=True)
    count_total = serializers.CharField(required=False,read_only=True)
    class Meta:
        model =Shop
        fields = "__all__"
class InvoiceItemSerializer(serializers.ModelSerializer):
    invoice = serializers.CharField(read_only=True)
    invoice_id = serializers.CharField(write_only=True)
    item = InventorySerializer(read_only=True)
    item_id = serializers.CharField(write_only=True)
    class Meta:
        model =InvoiceItem
        fields ="__all__"

