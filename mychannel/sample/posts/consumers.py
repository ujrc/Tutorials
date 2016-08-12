import json
from channels import Group

from .models import Blog


def connect_blog(message,slug):
	try:
		blog=Blog.objects.get(slug=slug)

	except Blog.DoesNotExist:
		message.reply_channel.send({
			"text":json.dumps({'error':'bad_slug'}),
		'close':True,})

		return

	Group(blog.group_name.add(message.reply_channel))


def disconnect_blog(message,slug):
	try:
		blog=Blog.objects.get(slug=slug)

	except Blog.DoesNotExist:
		return

	Group(blog.group_name).discard(message.reply_channel)