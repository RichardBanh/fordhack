from django.db import models
from django.conf import settings
# Create your models here.

from django.conf import settings


class CarModel(models.Model):
    vehicleId = models.CharField(max_length=255, blank=False, unique=True, primary_key=True)
    make = models.CharField(max_length=30, blank=False)
    modelName = models.CharField(max_length=30, blank=False)
    modelYear =  models.CharField(max_length=10, blank=False)
    color = models.CharField(max_length=50, blank=False)
    nickName = models.CharField(max_length=255, blank=False)
    modemEnabled = models.BooleanField(blank=False)
    vehicleAuthorizationIndicator = models.PositiveIntegerField()
    serviceCompatible = models.BooleanField(blank=False)
    registration_date = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f'vehicleId: {self.vehicleId}.'

    

#         if not account in self.friends.all():
#             self.friends.add(account)
#             self.save()

# class FriendListModel(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     friends= models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='friends')

#     def __str__(self):
#         return self.user.username

#     def add_friend(self, account):
#         if not account in self.friends.all():
#             self.friends.add(account)
#             self.save()

#     def remove_friend(self, account):
#         if account in self.friends.all():
#             self.friends.remove(account)
    
#     def unfriend(self, remove):
#         remover = self
#         remover.remove_friend(remove)
#         friendList = FriendListModel.objects.get(user = remove)
#         friendList.remove_friend(self.user)
    
# class FriendRequestModel(models.Model):
#     sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="sender")
#     reciever = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="reciever")
#     is_active = models.BooleanField(blank=True, null=False, default=True)
#     request_date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.sender.username
    
#     def accept(self):
#         reciever_friendList = FriendListModel.objects.get(user=self.reciever)
#         if reciever_friendList :
#             reciever_friendList.add_friend(self.sender)
#             sender_friendList = FriendListModel.objects.get(user=self.sender)
#             if sender_friendList:
#                 sender_friendList.add_friend(self.reciever)
#                 self.is_active = False
#                 self.save()
    
#     def decline(self):
#         self.is_active = False
#         self.save()

#     def cancel(self):
#         self.is_active = False
#         self.save()