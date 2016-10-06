from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from operator import itemgetter, attrgetter

# Create your models here.
def to_json(self):
    return {'username':self.username,'email':self.email}
User.add_to_class("to_json",to_json)



class Event(models.Model):
    title = models.CharField(max_length=100)
    all_day =  models.BooleanField(default=False)
    start = models.DateTimeField()
    end = models.DateTimeField()
    # image = models.ImageField(default = None, upload_to='app/static/images', max_length=1000, blank=True, null=True) 
    attachment = models.FileField(default = None, upload_to='app/static/files', max_length=1000, blank=True, null=True) 
    owner = models.ForeignKey(User)


    def to_json(self):

        if self.attachment:
            return {'attachment':self.attachment.name.replace('app/static/images',''),'title':self.title,'owner':self.owner.username,'ownerID':self.owner.id,'start':self.start,'end':self.end,'allDay':self.all_day}

        return {'attachment':None,'title':self.title,'owner':self.owner.username,'owner_id':self.owner.id,'start':self.start,'end':self.end,'allDay':self.all_day}


