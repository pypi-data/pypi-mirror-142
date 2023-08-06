"""Module model managing the application states"""
#      ubiquity
#      Copyright (C) 2022  INSA Rouen Normandie - CIP
#
#      This program is free software: you can redistribute it and/or modify
#      it under the terms of the GNU General Public License as published by
#      the Free Software Foundation, either version 3 of the License, or
#      (at your option) any later version.
#
#      This program is distributed in the hope that it will be useful,
#      but WITHOUT ANY WARRANTY; without even the implied warranty of
#      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#      GNU General Public License for more details.
#
#      You should have received a copy of the GNU General Public License
#      along with this program.  If not, see <https://www.gnu.org/licenses/>.

from PySide2.QtCore import QObject, Signal


class Model(QObject):
    """Class managing the states"""
    prefix_server_changed = Signal(str)
    server_changed = Signal(str)
    student_key_changed = Signal(str)
    group_key_changed = Signal(str)
    directory_changed = Signal(str)
    error_changed = Signal(object)

    def __init__(self) -> None:
        super().__init__()
        self._name = ''
        self._prefix_server = ''
        self._server = ''
        self._student_key = ''
        self._group_key = ''
        self._directory = ''
        self._error = ''

    @property
    def name(self) -> str:
        """Get the name"""
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """Set the name"""
        self._name = value

    @property
    def prefix_server(self) -> str:
        """Get the url server"""
        return self._prefix_server

    @prefix_server.setter
    def prefix_server(self, value: str) -> None:
        """Set the url server"""
        self._prefix_server = value
        self.prefix_server_changed.emit(value)

    @property
    def server(self) -> str:
        """Get the url server"""
        return self._server

    @server.setter
    def server(self, value: str) -> None:
        """Set the url server"""
        self._server = value
        self.server_changed.emit(value)

    @property
    def student_key(self) -> str:
        """Get the student key"""
        return self._student_key

    @student_key.setter
    def student_key(self, value: str) -> None:
        """Set the student key"""
        self._student_key = value
        self.student_key_changed.emit(value)

    @property
    def group_key(self) -> str:
        """Get the group key"""
        return self._group_key

    @group_key.setter
    def group_key(self, value: str) -> None:
        """Set the group key"""
        self._group_key = value
        self.group_key_changed.emit(value)

    @property
    def directory(self) -> str:
        """Get the directory"""
        return self._directory

    @directory.setter
    def directory(self, value: str) -> None:
        """Set the directory"""
        self._directory = value
        self.directory_changed.emit(value)

    @property
    def error(self) -> str:
        """Get the error"""
        return self._error

    @error.setter
    def error(self, value: str) -> None:
        """Set the error"""
        self._error = value
        self.error_changed.emit(value)

    def _url_api_server(self) -> str:
        return f'{self._prefix_server}{self._server}/api'

    def url_api_connection_check(self) -> str:
        """
        Method returning the url for the connection verification to the api
        :return: The string url
        """
        return f'{self._url_api_server()}/check/{self._student_key}/{self._group_key}'

    def url_api_get_student_environment(self) -> str:
        """
        Method returning the url for get student environment
        :return: The string url
        """
        return f'{self._url_api_server()}/{self._student_key}/{self._group_key}'

    def url_api_restore_student_environment(self) -> str:
        """
        Method returning the url for get student environment restored
        :return: The string url
        """
        return f'{self._url_api_server()}/restore/{self._student_key}/{self._group_key}'

    def url_api_file_paths(self) -> str:
        """
        Method returning the url for get path files to follow
        :return: The string url
        """
        return f'{self._url_api_server()}/{self._group_key}'

    def url_api_action_file(self, file_name: str) -> str:
        """
        Method returning the url for the file's action
        :return: The string url
        """
        if len(file_name) > 0 and file_name[0] == '/':
            file_name = file_name[1:]
        return f'{self._url_api_server()}/{self._student_key}/{self._group_key}/code_file/{file_name}'

    def url_web_view(self) -> str:
        """
        Method returning the url for the web view
        :return: The string url
        """
        return f'{self._prefix_server}{self._server}/client/{self._student_key}/{self._group_key}'
