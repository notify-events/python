# Доступные функции


## Message
#### Создать объект сообщения

```python
def __init__(self, content: str = '', title: str = '', priority: str = Message.PRIORITY_NORMAL, level: str = Message.LEVEL_INFO)
```
Параметр | Тип | Обязательный | Описание
---------|-----|--------------|---------
**$content**  | String | Нет | Текст сообщения
**$title**    | String | Нет | Заголовок сообщения
**$priority** | String | Нет | Приоритет. Допустимые значения описаны в функции `setPriority`
**$level**    | String | Нет | Уровень. Допустимые значения описаны в функции `setLevel`


## setTitle
#### Задать заголовок сообщения

```python
def set_title(self, title: str)
```
Параметр | Тип | Обязательный | Описание
---------|-----|--------------|---------
**$title** | String | Да | Заголовок сообщения


## getTitle
#### Получить установленный заголовок сообщения

```python
def get_title(self) -> str
```


## setContent
#### Задать текст сообщения
Для получателей, которые не поддерживают отображение HTML, теги будут игнорироваться.
```python
def set_content(self, content: str)
```
Параметр | Тип | Обязательный | Описание
---------|-----|--------------|---------
**$content** | String | Да | Текст сообщения. Допустимые HTML-теги: `<b>`, `<i>`, `<a>`, `<br>`


## getContent
#### Получить установленный текст сообщения

```python
def get_content(self) -> str
```


## setPriority
#### Установить приоритет сообщения
Для получателей, которые имеют поддержку приоритезации, сообщение будет выделено соответствующим образом.

```python
def set_priority(self, priority: str)
```
Параметр | Тип | Обязательный | Описание
---------|-----|--------------|---------
**$priority** | String | Да | Приоритет сообщения

Список возможных значений:
```php
Message.PRIORITY_LOWEST  - Незначительный
Message.PRIORITY_LOW     - Низкий
Message.PRIORITY_NORMAL  - Нормальный
Message.PRIORITY_HIGH    - Высокий
Message.PRIORITY_HIGHEST - Критичный 
```


## getPriority
#### Получить установленный приоритет сообщения

```python
def get_priority(self) -> str
```


## setLevel
#### Установить уровень сообщения
Для получателей, которые имеют различия в отображении разных уровней сообщений, будет учитываться установленный уровень.

```python
def set_level(self, level: str)
```
Параметр | Тип | Обязательный | Описание
---------|-----|--------------|---------
**$level** | String | Да | Уровень сообщения

Список возможных значений:
```php
Message.LEVEL_VERBOSE - Подробный
Message.LEVEL_INFO    - Информация
Message.LEVEL_NOTICE  - Уведомление
Message.LEVEL_WARNING - Предупреждение
Message.LEVEL_ERROR   - Ошибка
Message.LEVEL_SUCCESS - Успешно
```


## getLevel
#### Получить установленный уровень сообщения

```python
def get_level(self) -> str
```


## addFile
#### Прикрепить локальный файл

```python
def add_file(self, file_path: str, file_name: str, mime_type: str = None)
```
Параметр | Тип | Обязательный | Описание
---------|-----|--------------|---------
**$filePath** | String | Да | Путь к локальному файлу
**$fileName** | String | Нет | Название файла с расширением
**$mimeType** | String | Нет | MimeType файла


## addFileFromContent
#### Прикрепить файл, передав его содержимое

```python
def add_file_from_content(self, content: str, file_name: str = None, mime_type: str = None)
```
Параметр | Тип | Обязательный | Описание
---------|-----|--------------|---------
**$content**  | String | Да | Содержимое файла
**$fileName** | String | Нет | Название файла с расширением
**$mimeType** | String | Нет | MimeType файла


## addFileFromUrl
#### Прикрепить файл, расположенный по указанному URL

```python
def add_file_from_url(self, url: str, file_name: str = None, mime_type: str = None)
```
Параметр | Тип | Обязательный | Описание
---------|-----|--------------|---------
**$url**      | String | Да | Путь к удалённому файлу
**$fileName** | String | Нет | Название файла с расширением
**$mimeType** | String | Нет | MimeType файла


## addImage
#### Прикрепить локальное изображение

```python
def add_image(self, file_path: str, file_name: str, mime_type: str = None)
```
Параметр | Тип | Обязательный | Описание
---------|-----|--------------|---------
**$filePath** | String | Да | Путь к локальному файлу
**$fileName** | String | Нет | Название файла с расширением
**$mimeType** | String | Нет | MimeType файла


## addImageFromContent
#### Прикрепить изображение, передав его содержимое

```python
def add_image_from_content(self, content: str, file_name: str = None, mime_type: str = None)
```
Параметр | Тип | Обязательный | Описание
---------|-----|--------------|---------
**$content**  | String | Да | Содержимое файла
**$fileName** | String | Нет | Название файла с расширением
**$mimeType** | String | Нет | MimeType файла


## addImageFromUrl
#### Прикрепить файл, расположенный по указанному URL

```python
def add_image_from_url(self, url: str, file_name: str = None, mime_type: str = None)
```
Параметр | Тип | Обязательный | Описание
---------|-----|--------------|---------
**$url**      | String | Да | Путь к удалённому файлу
**$fileName** | String | Нет | Название файла с расширением
**$mimeType** | String | Нет | MimeType файла


## send
#### Отправить сообщение

Токен источника вы можете получить при поключении источника Python на ваш канал на стороне сервиса [Notify.Events](https://notify.events).

```python
def send(self, channel_token: str)
```
Параметр | Тип | Обязательный | Описание
---------|-----|--------------|---------
**$token** | String | Да | Токен источника
