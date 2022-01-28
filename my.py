#!/usr/bin/env python
'''Description here'''

from notify_events import Message

if __name__ == "__main__":

    # Create a message object.
    message = Message('Some <b>important</b> message', 'Title', Message.PRIORITY_HIGH, Message.LEVEL_WARNING)

    # Attach the file to the message.
    # message.add_file('path\to\local\file.zip', 'filename.zip')

    message.add_action('bla', 'Bla', 'http:\\yandex.ru')

    # Send a message to your channel in Notify.Events.
    message.send('XXXXXXXX')
