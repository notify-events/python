import requests
import mimetypes
import os


#
class Message:
    PRIORITY_LOWEST = 'lowest'
    PRIORITY_LOW = 'low'
    PRIORITY_NORMAL = 'normal'
    PRIORITY_HIGH = 'high'
    PRIORITY_HIGHEST = 'highest'

    LEVEL_VERBOSE = 'verbose'
    LEVEL_INFO = 'info'
    LEVEL_NOTICE = 'notice'
    LEVEL_WARNING = 'warning'
    LEVEL_ERROR = 'error'
    LEVEL_SUCCESS = 'success'

    _base_url = 'https://notify.events/api/v1/channel/source/%s/execute'

    _title = ''
    _content = ''
    _priority = PRIORITY_NORMAL
    _level = LEVEL_INFO

    FILE_TYPE_FILE = 'file'
    FILE_TYPE_CONTENT = 'content'
    FILE_TYPE_URL = 'url'

    _files = []
    _images = []

    def __init__(self, content: str = '', title: str = '', priority: str = PRIORITY_NORMAL, level: str = LEVEL_INFO):
        self \
            .set_title(title) \
            .set_content(content) \
            .set_priority(priority) \
            .set_level(level)

        self._files = []
        self._images = []

    def _prepare_files(self, array: list, field: str, files: list) -> list:
        for idx in files:
            file = files[idx]

            field = field + '[' + idx + ']'

            if file.type == self.FILE_TYPE_FILE:
                if not file.mime_type:
                    file.mime_type = mimetypes.read_mime_types(file.file_name)

                array[field] = (
                    file.file_name,
                    open(file.file_name, 'rb'),
                    file.mime_type
                )
            elif file.type == self.FILE_TYPE_CONTENT:
                if not file.file_name:
                    file.file_name = 'file.dat'

                if not file.mime_type:
                    file.mime_type = 'application/octet-stream'

                array[field] = (
                    file.file_name,
                    file.content,
                    file.mime_type
                )
            elif file.type == self.FILE_TYPE_URL:
                if not file.file_name:
                    file.file_name = os.path.basename(file.url)

                if not file.mime_type:
                    file.mime_type = 'application/octet-stream'

                response = requests.get(file.url)

                array[field] = (
                    file.file_name,
                    response.text,
                    file.mime_type
                )

        return array

    # Send message to Notify.Events
    #   channel_token - channel identification token
    def send(self, channel_token: str):
        data = {
            'content': self._content,
            'priority': self._priority,
            'level': self._level
        }

        if not self._title.isspace():
            data.title = self._title

        files = []
        files = self._prepare_files(files, 'files', self._files)
        files = self._prepare_files(files, 'images', self._images)

        url = self._base_url % channel_token

        requests.post(url, data=data, files=files)

    # Set message title
    def set_title(self, title: str):
        self._title = title

        return self

    # Get message title
    def get_title(self) -> str:
        return self._title

    # Set message content
    # allowed simple html tags: <a>, <b>, <i>, <br>
    def set_content(self, content: str):
        self._content = content

        return self

    # Get message content
    def get_content(self) -> str:
        return self._content

    # Set message priority
    # allowed predefined constants PRIORITY_*
    def set_priority(self, priority: str):
        if not (priority in [
            self.PRIORITY_LOWEST,
            self.PRIORITY_LOW,
            self.PRIORITY_NORMAL,
            self.PRIORITY_HIGH,
            self.PRIORITY_HIGHEST
        ]):
            raise Exception('Unknown priority value')

        self._priority = priority

        return self

    # Get message priority
    def get_priority(self) -> str:
        return self._priority

    # Set message level
    # allowed predefined constants LEVEL_*
    def set_level(self, level: str):
        if not (level in [
            self.LEVEL_VERBOSE,
            self.LEVEL_INFO,
            self.LEVEL_NOTICE,
            self.LEVEL_WARNING,
            self.LEVEL_ERROR,
            self.LEVEL_SUCCESS
        ]):
            raise Exception('Unknown level value')

        self._level = level

        return self

    # Get message level
    def get_level(self) -> str:
        return self._level

    # Add file to message
    #   file_name - absolute path to destination file
    #   mime_type - file mime type (optional)
    def add_file(self, file_name: str, mime_type: str = None):
        self._files.append({
            type: self.FILE_TYPE_FILE,
            file_name: file_name,
            mime_type: mime_type
        })

        return self

    # Add content as file to message
    #   content   - file content
    #   file_name - file name (optional)
    #   mime_type - file mime type (optional)
    def add_file_from_content(self, content: str, file_name: str = None, mime_type: str = None):
        self._files.append({
            type: self.FILE_TYPE_CONTENT,
            content: content,
            file_name: file_name,
            mime_type: mime_type
        })

        return self

    # Add file by url link to message
    #   url       - link to file
    #   file_name - file name (optional)
    #   mime_type - file mime type (optional)
    def add_file_from_url(self, url: str, file_name: str = None, mime_type: str = None):
        self._files.append({
            type: self.FILE_TYPE_URL,
            url: url,
            file_name: file_name,
            mime_type: mime_type
        })

        return self

    # Add image to message
    #   file_name - absolute path to destination image
    #   mime_type - image mime type (optional)
    def add_image(self, file_name: str, mime_type: str = None):
        self._images.append({
            type: self.FILE_TYPE_FILE,
            file_name: file_name,
            mime_type: mime_type
        })

        return self

    # Add content as image to message
    #   content   - image content
    #   file_name - image file name (optional)
    #   mime_type - image mime type (optional)
    def add_image_from_content(self, content: str, file_name: str = None, mime_type: str = None):
        self._images.append({
            type: self.FILE_TYPE_CONTENT,
            content: content,
            file_name: file_name,
            mime_type: mime_type
        })

        return self

    # Add image by url link to message
    #   url       - link to image
    #   file_name - image file name (optional)
    #   mime_type - image mime type (optional)
    def add_image_from_url(self, url: str, file_name: str = None, mime_type: str = None):
        self._images.append({
            type: self.FILE_TYPE_URL,
            url: url,
            file_name: file_name,
            mime_type: mime_type
        })

        return self
