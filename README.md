# Python client for Notify.Events

A simple Python extension that simplifies the process of integrating your project with the [Notify.Events](https://notify.events) service to send messages to your channels.

#### Instruction on another languages

- [Русский](/docs/ru-RU/README.md)

# Installation

You can install the Python client for Notify.Events from [PyPI](https://pypi.org/project/notify_events/):

```
pip install notify_events
```

# Usage

To use this extension, you need to import the Message class into your script.

```python
from notify_events import Message
```

After that, you can create a Message object, set the necessary parameters and send the message to the channel.

### Usage example

```python
from notify_events import Message

# Create a message object.
message = Message('Some <b>important</b> message', 'Title', Message.PRIORITY_HIGH, Message.LEVEL_WARNING)

# Attach the file to the message.
message.add_file('path\to\local\file.zip', 'filename.zip')

# Send a message to your channel in Notify.Events.
message.send('XXXXXXXX')
```

[List of all available functions](/docs/en-US/Message.md)