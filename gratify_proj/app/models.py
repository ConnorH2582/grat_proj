from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from operator import itemgetter, attrgetter
from django.db import models
from django.utils.text import slugify
import datetime

# Create your models here.
def to_json(self):
    return {'username':self.username,'email':self.email}
User.add_to_class("to_json",to_json)



class Event(models.Model):
    title = models.CharField(unique=True,max_length=30)
    all_day =  models.BooleanField()
    start = models.DateTimeField()
    end = models.DateTimeField()
    attachment = models.FileField(default = None, upload_to='app/static/files', max_length=1000, blank=True, null=True) 
    owner = models.ForeignKey(User)
    slug = models.SlugField()

    def to_json(self):
        print(self.attachment)
        if self.attachment:
            return {'attachment':self.attachment.name.replace('app/static/files',''),'title':self.title,'owner':self.owner.username,'ownerID':self.owner.id,'start':self.start,'end':self.end,'allDay':self.all_day,'slug':self.slug}
        else:
            return {'attachment':None,'title':self.title,'owner':self.owner.username,'owner_id':self.owner.id,'start':self.start,'end':self.end,'allDay':self.all_day,'slug':slugify(self.title)}

    # is_public = models.BooleanField(default=True)

    def title_to_slug(self):
        self.slug = slugify(self.title)
        self.save()
        return self.slug
