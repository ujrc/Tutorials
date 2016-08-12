import logging
import json
import re
from channels import Group
from channels.sessions import channel_session

from .models import Room

log = logging.getLogger(__name__)


@channel_session
def ws_connect(message):
    try:
        prefix, label = message['path'].strip('/').split('/')
        if prefix != 'chat':
            log.debug('invalid ws path=%s', message['path'])
            return
        room = Room.objects.get(label=label)
    except ValueError:
        log.debug('invalid ws path=%s', message['path'])
        return
    except Room.DoesNotExist:
        log.debug('ws room does not exist label=%s', label)
        return
    log.debug('chat connect room=%s client=%s:%s',
     room.label, message['client'][0], message['client'][1])
    Group('chat-' + label,
          channel_layer=message.channel_layer).add(message.reply_channel)
    message.channel_session['room'] = room.label


@channel_session
def ws_receive(message):
    try:
        label = message.channel_session['room']
        room = Room.objects.get(label=label)
    except KeyError:
        log.debug('no room in channel_session')
        return
    except Room.DoesNotExist:
        log.debug('recieved message,  room does not exist label=%s', label)
        return
    try:
        data = json.loads(message['text'])
    except ValueError:
        log.debug("ws message isn't json text=%s", text)
        return

        if set(data.keys()) != set(('handle', 'message')):
            log.debug("ws message unexpected format data=%s", data)
            return
        if data:
            log.debug('chat message room=%s handle=%s message=%s',
                      room.label, data['handle'], data['message'])
        msg = room.messages.create(**data)
        Group('chat-' + label, channel_layer=message.channel_layer).send(
            {'text': json.dumps(msg.as_dict())})


@channel_session
def ws_disconnect(message):
    try:
        label = message.channel_session['room']
        room.Room.objects.get(label=label)
        Group('chat-' + label,
              channel_layer=message.channel_layer).discard(message.reply_channel)
    except(KeyError, Room.DoesNotExist):
        pass
