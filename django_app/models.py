from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

# class BaseModel(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     created_by = models.ForeignKey(
#         User,
#         related_name="%(class)s_createdby",
#         on_delete=models.CASCADE,
#         null=True,
#     )
#     updated_by = models.ForeignKey(
#         User,
#         related_name="%(class)s_updatedby",
#         on_delete=models.CASCADE,
#         null=True,
#     )
#     class Meta:
#         abstract = True

# class Site(BaseModel):
#     site_id = models.IntegerField(max_length=100, primary_key=True)
#     site_name = models.CharField(max_length=100, null=False)
#     address = models.CharField(max_length=100, null=False)
#     _state = models.CharField(max_length=100, null=False)
#     country = models.CharField(max_length=100, null=False)
#     zipcode = models.IntegerField(null=True)

#     def __str__(self):
#         return self.site_name
    
# class Order(BaseModel):
#     customer_id = models.CharField(max_length=100, null=False)
#     order_id = models.IntegerField(max_length=100, primary_key=True)
#     purchase_id = models.IntegerField(max_length=100, null=False)
#     quantity = models.IntegerField(max_length=100, null=False)
#     device_type = models.CharField(max_length=100, name=False)
#     status = (
#         ('Pending', 'Pending'),
#         ('In_transit', 'In_transit'),
#         ('Delivered', 'Delivered')
#     )

#     def __str__(self):
#         return self.order_id
        
    
class IAP(models.Model):
    site_id = models.IntegerField(primary_key=True)
    site_name = models.CharField(max_length=50,null=False)
    country = models.CharField(max_length=50,null=False)
    order_id = models.IntegerField(null=False)
    purchase_id = models.IntegerField(null=False)
    csm_name = models.CharField(max_length=50)
    serial = models.CharField(max_length=50)
    ip_address = models.CharField(max_length=20)
    model = models.CharField(max_length=50)
    macaddr = models.CharField(max_length=30)

    def __str__(self):
        return self.serial_num
    
# class Switch(BaseModel):
#     serial_num = models.IntegerField(max_length=100, primary_key=True)
#     ip_address = models.CharField(max_length=15, null=False)
#     mac_address = models.CharField(max_length=17, null=False)
#     model = models.CharField(max_length=100, null=False)
#     status = models.BooleanField(null= False)
#     #site_id = models.IntegerField(max_length=100, null=False)
#     site_id = models.ForeignKey( Site, related_name='switchpersite', on_delete=models.CASCADE)
#     #order_id = models.IntegerField(max_length=100, null=False)
#     order_id = models.ForeignKey( Order, related_name='switchorder', on_delete=models.CASCADE)


#     def __str__(self):
#         return self.serial_num

