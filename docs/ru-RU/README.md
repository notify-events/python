# Python клиент для Notify.Events

Простая Python-библиотека, которая призвана упростить процесс интеграции сервиса [Notify.Events](https://notify.events) в ваш проект,  с целью отправки сообщений в созданный канал.

#### Инструкции на других языках

- [English](/README.md)

# Установка

Вы можете установить Python клиент для Notify.Events из каталога [PyPI](https://pypi.org/project/notify_events/):

```
pip install notify_events
```

# Использование

Для использования этой библиотеки, вам необходимо подключить класс Message в ваш скрипт.

```python
from notify_events import Message
```

После этого вы можете создать объект сообщения, установить необходимые параметры и отправить сообщение в канал.

### Пример использования

```python
from notify_events import Message

# Create a message object.
message = Message('Some <b>important</b> message', 'Title', Message.PRIORITY_HIGH, Message.LEVEL_WARNING)

# Attach the file to the message.
message.add_file('path\to\local\file.zip', 'filename.zip')

# Send a message to your channel in Notify.Events.
message.send('XXXXXXXX')
```

[Список доступных функций](/docs/ru-RU/Message.md)