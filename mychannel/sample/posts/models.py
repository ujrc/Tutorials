# Create your models here.
import json
import random
import string

from django.db import models
from django.core.urlresolvers import reverse
from django.template.defaultfilters import linebreaks_filter, slugify
from django.utils.six import python_2_unicode_compatible
from channels import Group


def gen_word():
    word = ''.join([random.choice(string.ascii_letters + string.digits)
                    for n in range(8)])
    return word


@python_2_unicode_compatible
class Blog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = ''.join((slugify(self.title), slugify(gen_word())))
        super(Blog, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('posts:blog', kwargs={'slug': self.slug})

    @property
    def group_name(self):
        return "post-%s" % self.id


@python_2_unicode_compatible
class Post(models.Model):
    blog = models.ForeignKey(Blog, related_name='posts',
                             on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s,%s' % (self.id, self.intro_body())

    def intro_body(self):
        """ First few lines of the body"""
        return self.body[:50]

    def html_body(self):
        return linebreaks_filter(self.body)

    def send_notifications(self):
        """
        Sends a notification to everyone in our Liveblog's group with our
        content.
        """
        notification = {'id': self.id,
                        'html': self.html_body(),
                        'created': self.created.strftime('%a %d %b %Y %H:%M'), }

        Group(self.blog.group_name).send({
            # WebSocket text frame, with JSON content
            "text": json.dumps(notification),
        })

    def save(self, *args, **kwargs):
        """
        Hooking send_notification into the save of the object
        """
        obj = super(Post, self).save(*args, **kwargs)
        self.send_notifications()
        return obj
