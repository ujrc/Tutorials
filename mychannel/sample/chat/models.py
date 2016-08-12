# Create your models here.
import random
import string
from django.core.urlresolvers import reverse
from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.utils.six import python_2_unicode_compatible


def gen_word():
    word = ''.join([random.choice(string.ascii_letters + string.digits)
                    for n in range(10)])
    return word


@python_2_unicode_compatible
class Room(models.Model):
    name = models.CharField(max_length=60)
    label= models.SlugField(unique=True)

    def __str__(self):
        return self.name

    # def save(self, *args, **kwargs):

    #     self.label='-'.join((slugify(gen_word()),slugify(self.name))) 
    #     super(Room, self).save(*args, **kwargs)

    # def get_absolute_url(self):
    #     return reverse('chat:chat_room', kwargs={'label': self.label})


@python_2_unicode_compatible
class Message(models.Model):
    room = models.ForeignKey(
        Room, related_name='messages', on_delete=models.CASCADE)
    handle = models.TextField()
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '[{timestamp}] {handle} {message}'.format(**self.my_dict())
    @property
    def format_timestamp(self):
        return self.timestamp.strftime('%b %-d %-I:%M %p')

    def my_dict(self):
        return {'handle': self.handle, 'message': self.message, 'timestamp': self.timestamp}
