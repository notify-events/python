# Available Functions


## Message
#### Message object creating

```python
def __init__(self, content: str = '', title: str = '', priority: str = Message.PRIORITY_NORMAL, level: str = Message.LEVEL_INFO)
```
Param | Type | Required | Description
------|------|----------|------------
**$content**  | String | No | Message text
**$title**    | String | No | Message title
**$priority** | String | No | Priority. Available values are listed in the `setPriority` function
**$level**    | String | No | Level. Available values are listed in the `setLevel` function


## setTitle
#### Set message title

```python
def set_title(self, title: str)
```
Param | Type | Required | Description
------|------|----------|------------
**$title** | String | Yes | Message title


## getTitle
#### Get message title

```python
def get_title(self) -> str
```


## setContent
#### Set message text
For recipients that do not support HTML, these tags will be ignored.
```python
def set_content(self, content: str)
```
Param | Type | Required | Description
------|------|----------|------------
**$content** | String | Yes | Message text. Available HTML tags: `<b>`, `<i>`, `<a>`, `<br>`


## getContent
#### Get message text

```python
def get_content(self) -> str
```


## setPriority
#### Define message priority
For recipients which supports priority, the message will be highlighted accordingly.

```python
def set_priority(self, priority: str)
```
Param | Type | Required | Description
------|------|----------|------------
**$priority** | String | Yes | Message priority

Available values:
```python
Message.PRIORITY_LOWEST
Message.PRIORITY_LOW
Message.PRIORITY_NORMAL
Message.PRIORITY_HIGH
Message.PRIORITY_HIGHEST 
```


## getPriority
#### Get message priority

```python
def get_priority(self) -> str
```


## setLevel
#### Define message level
For recipients which have differences in the display of messages at different levels, this level will be applied.

```python
def set_level(self, level: str)
```
Param | Type | Required | Description
------|------|----------|------------
**$level** | String | Yes | Message level

Available values:
```python
Message.LEVEL_VERBOSE
Message.LEVEL_INFO
Message.LEVEL_NOTICE
Message.LEVEL_WARNING
Message.LEVEL_ERROR
Message.LEVEL_SUCCESS
```


## getLevel
#### Get message level

```python
def get_level(self) -> str
```


## addFile
#### Attach local file

```python
def add_file(self, file_path: str, file_name: str, mime_type: str = None)
```
Param | Type | Required | Description
------|------|----------|------------
**$filePath** | String | Yes | Local file path
**$fileName** | String | No | File name and extension
**$mimeType** | String | No | File MimeType


## addFileFromContent
#### Attach file by content

```python
def add_file_from_content(self, content: str, file_name: str = None, mime_type: str = None)
```
Param | Type | Required | Description
------|------|----------|------------
**$content**  | String | Yes | File content
**$fileName** | String | No | File name and extension
**$mimeType** | String | No | File MimeType


## addFileFromUrl
#### Attach remote file

```python
def add_file_from_url(self, url: str, file_name: str = None, mime_type: str = None)
```
Param | Type | Required | Description
------|------|----------|------------
**$url**      | String | Yes | Remote file path
**$fileName** | String | No | File name and extension
**$mimeType** | String | No | File MimeType


## addImage
#### Attach local image

```python
def add_image(self, file_path: str, file_name: str, mime_type: str = None)
```
Param | Type | Required | Description
------|------|----------|------------
**$filePath** | String | Yes | Local file path
**$fileName** | String | No | File name and extension
**$mimeType** | String | No | File MimeType


## addImageFromContent
#### Attach image by content

```python
def add_image_from_content(self, content: str, file_name: str = None, mime_type: str = None)
```
Param | Type | Required | Description
------|------|----------|------------
**$content**  | String | Yes | File content
**$fileName** | String | No | File name and extension
**$mimeType** | String | No | File MimeType


## addImageFromUrl
#### Attach remote image

```python
def add_image_from_url(self, url: str, file_name: str = None, mime_type: str = None)
```
Param | Type | Required | Description
------|------|----------|------------
**$url**      | String | Yes | Remote file path
**$fileName** | String | No | File name and extension
**$mimeType** | String | No | File MimeType


## addAction
#### Add an action

```python
def add_action(
    self, name: str,
    title: str,
    callback_url: str = None,
    callback_method: str = None,
    callback_headers: dict = None,
    callback_content: str = None
)
```
Param | Type | Required | Description
------|------|----------|------------
**$name**            | String | Yes | Action code
**$title**           | String | No  | Button title
**callback_url**     | String | No  | Callback URL
**callback_method**  | String | No  | Callback request method
**callback_headers** | Dict   | No  | Callback headers
**callback_content** | String | No  | Callback payload 


## send
#### Send the message

You can get the source token when connecting the Python source to your channel on the [Notify.Events](https://notify.events) service side.

```python
def send(self, channel_token: str)
```
Param | Type | Required | Description
------|------|----------|------------
**$token** | String | Yes | Source token