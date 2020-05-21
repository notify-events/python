import requests
import mimetypes
import os


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
        """Message constructor.

        :param str content:  Message text
        :param str title:    Message title
        :param str priority: Priority
        :param str level:    Level
        """

        self \
            .set_title(title) \
            .set_content(content) \
            .set_priority(priority) \
            .set_level(level)

        self._files = []
        self._images = []

    def _prepare_files(self, array: dict, field: str, files: list) -> dict:
        """Prepares a message file.

        :param dict array: Result array to fill
        :param str  field: Type of files to prepare
        :param list files: List of files to prepare

        :returns: Prepared files
        """

        for idx, file in enumerate(files):
            key = field + '[' + str(idx) + ']'

            if file['type'] == self.FILE_TYPE_FILE:
                if not file['mime_type']:
                    file['mime_type'] = mimetypes.read_mime_types(file['file_name'])

                if not file['file_name']:
                    file['file_name'] = os.path.basename(file['file_path'])

                array[key] = (
                    file['file_name'],
                    open(file['file_path'], 'rb'),
                    file['mime_type']
                )
            elif file['type'] == self.FILE_TYPE_CONTENT:
                if not file['file_name']:
                    file['file_name'] = 'file.dat'

                if not file['mime_type']:
                    file['mime_type'] = 'application/octet-stream'

                array[key] = (
                    file['file_name'],
                    file['content'],
                    file['mime_type']
                )
            elif file['type'] == self.FILE_TYPE_URL:
                if not file['file_name']:
                    file['file_name'] = os.path.basename(file['url'])

                if not file['mime_type']:
                    file['mime_type'] = 'application/octet-stream'

                response = requests.get(file['url'])

                array[key] = (
                    file['file_name'],
                    response.content,
                    file['mime_type']
                )

        return array

    def send(self, channel_token: str):
        """Sends the message to the specified channel.

        You can get the source token when connecting the Python source
        to your channel on the Notify.Events service side.

        :param str channel_token: Source token
        """

        data = {
            'content': self._content,
            'priority': self._priority,
            'level': self._level
        }

        if not self._title.isspace():
            data['title'] = self._title

        files = {}
        files = self._prepare_files(files, 'files', self._files)
        files = self._prepare_files(files, 'images', self._images)

        url = self._base_url % channel_token

        requests.post(url, data=data, files=files)

    def set_title(self, title: str):
        """Sets the value of the Title property.

        :param str title: Message title

        :returns: Message
        """
        self._title = title

        return self

    def get_title(self) -> str:
        """Returns the value of the Title property.

        :returns: Message title
        """
        return self._title

    def set_content(self, content: str):
        """Sets the value of the Content property.

        Allowed html tags: <a>, <b>, <i>, <br>

        :param str content: Message content

        :returns: Message title
        """
        self._content = content

        return self

    def get_content(self) -> str:
        """Returns the value of the Content property.

        :returns: Message content
        """
        return self._content

    def set_priority(self, priority: str):
        """Sets the value of the Priority property.

        For recipients which supports priority, the message will be highlighted accordingly.
        This method checks that priority param is in the list of available message priorities.

        :param str priority: Message priority

        :returns: Message
        """
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

    def get_priority(self) -> str:
        """Returns the value of the Priority property.

        :returns: Message priority
        """
        return self._priority

    def set_level(self, level: str):
        """Sets the value of the Level property.

        This method checks that level param is in the list of available message levels.
        For recipients which have differences in the display of messages at different levels, this level will be applied.

        :param str level: Message Level

        :returns: Message
        """
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

    def get_level(self) -> str:
        """Returns the value of the Level property.

        :returns: Message level
        """
        return self._level

    def add_file(self, file_path: str, file_name: str, mime_type: str = None):
        """Adds a new File by local file path to the massage attached files list.

        :param str file_path: Local file path
        :param str file_name: Attachment file name
        :param str mime_type: Attachment file MimeType

        :returns: Message
        """
        self._files.append({
            'type': self.FILE_TYPE_FILE,
            'file_path': file_path,
            'file_name': file_name,
            'mime_type': mime_type
        })

        return self

    def add_file_from_content(self, content: str, file_name: str = None, mime_type: str = None):
        """Adds a new File by content to the massage attached files list.

        :param str content:   File content
        :param str file_name: Attachment file name
        :param str mime_type: Attachment file MimeType

        :returns: Message
        """
        self._files.append({
            'type': self.FILE_TYPE_CONTENT,
            'content': content,
            'file_name': file_name,
            'mime_type': mime_type
        })

        return self

    def add_file_from_url(self, url: str, file_name: str = None, mime_type: str = None):
        """Adds a new File by URL to the massage attached files list.

        :param str url:       File remote URL
        :param str file_name: Attachment file name
        :param str mime_type: Attachment file MimeType

        :returns: Message
        """
        self._files.append({
            'type': self.FILE_TYPE_URL,
            'url': url,
            'file_name': file_name,
            'mime_type': mime_type
        })

        return self

    def add_image(self, file_path: str, file_name: str, mime_type: str = None):
        """Adds a new Image by local file path to the massage attached images list.

        :param str file_path: Local file path
        :param str file_name: Attachment file name
        :param str mime_type: Attachment file MimeType

        :returns: Message
        """
        self._images.append({
            'type': self.FILE_TYPE_FILE,
            'file_path': file_path,
            'file_name': file_name,
            'mime_type': mime_type
        })

        return self

    def add_image_from_content(self, content: str, file_name: str = None, mime_type: str = None):
        """Adds a new Image by content to the massage attached images list.

        :param str content:   File content
        :param str file_name: Attachment file name
        :param str mime_type: Attachment file MimeType

        :returns: Message
        """
        self._images.append({
            'type': self.FILE_TYPE_CONTENT,
            'content': content,
            'file_name': file_name,
            'mime_type': mime_type
        })

        return self

    def add_image_from_url(self, url: str, file_name: str = None, mime_type: str = None):
        """Adds a new Image by URL to the massage attached images list.

        :param str url:       File remote URL
        :param str file_name: Attachment file name
        :param str mime_type: Attachment file MimeType

        :returns: Message
        """
        self._images.append({
            'type': self.FILE_TYPE_URL,
            'url': url,
            'file_name': file_name,
            'mime_type': mime_type
        })

        return self
