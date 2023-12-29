from django.contrib.auth.models import User
from django.db import models

from item.models import Items 
# Create your models here.

class Conversation(models.Model):
    item = models.ForeignKey(Items, related_name= 'conversations', on_delete= models.CASCADE)
    members = models.ManyToManyField(User, related_name = 'conversations')
    created_at = models.DateTimeField(auto_now_add= True)
    modified_at = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ('-modified_at',)
    def __str__(self):
        return self.item.Name # item.Name mentioned messaging about this product

class ConversationMessage(models.Model):
    conversation = models.ForeignKey(Conversation, related_name= 'messages', on_delete= models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add= True)
    created_by = models.ForeignKey(User, related_name= 'created_messages', on_delete= models.CASCADE)

    class Meta:
        ordering = ('created_at',) # created_at mentioned date & time fields
    def __str__(self):
        return self.created_by # created_by mentioned who send message