from enum import unique
from django.db import models
from userint.models import CustomUser
from userint.views import add_user_activity
# Create your models here.

class InventoryGroup(models.Model):
    created_by=models.ForeignKey(CustomUser, null=True, related_name="inventory_groups",
    on_delete=models.SET_NULL)
    name = models.CharField(max_length=100,unique=True)
    belongs_to =models.ForeignKey('self',null=True,on_delete=models.SET_NULL,related_name="group_relations")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering =("-created_at")
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.old_name = self.name    
    def save(self, *args, **kwargs):
        action = f"add new group - '{self.name}'"
        if self.pk is not None:
            action = f"updated group from - '{self.old_name}' to '{self.name}'" 
        super().save(*args,**kwargs)   
        add_user_activity(self.created_by,action=action)

    def delete(self,*args,**kwargs):
        created_by=self.created_by
        action = f"deleted group - '{self.name}'"
        super().delete(*args,**kwargs)
        add_user_activity(created_by,action=action)        

    def __str__(self):
        return self.name


class Inventory(models.Model):
    created_by=models.ForeignKey(CustomUser, null=True, related_name="inventory_groups",
    on_delete=models.SET_NULL)

    code =models.CharField(max_length=10,unique=True,null=True)
    photo =models.TextField(blank=True,null=True)
    group = models.ForeignKey(InventoryGroup,related_name="inventories",null=True,on_delete=models.SET_NULL)
    total =models.PositiveIntegerField()
    remaining =models.PositiveIntegerField(null=True)
    name =models.CharField(max_length=355)
    price = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering =("-created_at")

        



