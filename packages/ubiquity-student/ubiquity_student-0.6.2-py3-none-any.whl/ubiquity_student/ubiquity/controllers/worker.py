"""Module managing the worker"""
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

from enum import unique, IntEnum
from json import loads
from os.path import split, join, abspath, isfile
from time import strftime, localtime
from typing import List

import requests
from PySide2.QtCore import QObject, QFileSystemWatcher

from ..model import Model


@unique
class StatusCode(IntEnum):
    """Enum class for status codes"""
    OK = 200
    CREATED = 201


def _get_current_time():
    return strftime("%H:%M:%S", localtime())


class Worker(QObject):
    """Class managing the worker"""

    def __init__(self, model: Model) -> None:
        super().__init__()
        self._model = model
        self._file_paths = self._get_file_paths()
        self.file_system_watcher = QFileSystemWatcher(self._file_paths + self._get_path_directories())
        self.delete_files_not_exist()
        self.post_all()

    def _get_file_paths(self) -> List[str]:
        response = requests.get(self._model.url_api_file_paths())
        content = loads(response.content)
        return [join(self._model.directory, file['file_path']) for file in content]

    def _get_file_paths_not_exist(self) -> List[str]:
        return [file_path for file_path in self._file_paths if file_path not in self.file_system_watcher.files()]

    def _get_path_directories(self) -> List[str]:
        return list(set([self._get_directory(file_path) for file_path in self._file_paths]))

    @staticmethod
    def _get_directory(file_path: str) -> str:
        return split(abspath(file_path))[0]

    def add_new_files_in_directory(self, path: str) -> None:
        """
        Method adding and sending the created files to follow
        :param path: The directory path
        """
        for file_path in self._get_file_paths_not_exist():
            if self._get_directory(file_path) == path and isfile(file_path):
                self.file_system_watcher.addPath(file_path)
                self.post(file_path)

    def delete_files_not_exist(self) -> None:
        """
        Method deleting and sending the not exist files to follow
        """
        for file_path in self._get_file_paths_not_exist():
            if not isfile(file_path):
                self.delete(file_path)

    def post(self, path: str) -> None:
        """
        Method sending a file by the path
        :param path: The file path
        """
        self.file_system_watcher.removePath(path)
        self.file_system_watcher.addPath(path)
        try:
            with open(path, "r", encoding='utf8') as file:
                data = {'code': file.read()}
            response = requests.post(self._model.url_api_action_file(path[len(self._model.directory):]), data=data)
            if response.status_code in [StatusCode.OK, StatusCode.CREATED]:
                if response.status_code == StatusCode.CREATED:
                    print(f'File {path} created successfully at {_get_current_time()}')
                if response.status_code == StatusCode.OK:
                    print(f'File {path} updated successfully at {_get_current_time()}')
        except UnicodeDecodeError:
            pass

    def post_all(self) -> None:
        """
        Method sending all files to follow
        """
        for path in self.file_system_watcher.files():
            self.post(path)

    def delete(self, path: str) -> None:
        """
        Method deleting a file by the path
        :param path: The file path
        """
        self.file_system_watcher.removePath(path)
        response = requests.delete(self._model.url_api_action_file(path[len(self._model.directory):]))
        if response.status_code == StatusCode.OK:
            print(f'File {path} deleted successfully at {_get_current_time()}')
