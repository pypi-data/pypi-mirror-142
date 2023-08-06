#!/usr/bin/python3
"""Module managing the application"""
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
import os.path
import signal
import sys

from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QApplication

from .controllers.main_controller import MainController
from .model import Model
from .views.main_view import MainView

from . import __version__


class App(QApplication):
    """Class managing the application"""

    VERSION = __version__
    LOGO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images/ubiquity_icon.png")

    def __init__(self, sys_argv):
        super().__init__(sys_argv)
        self.model = Model()
        self.main_controller = MainController(self.model)
        self.main_view = MainView(self.model, self.main_controller)
        self.LOGO = QIcon(self.LOGO)
        self.setWindowIcon(self.LOGO)
        self.show_view()

    def show_view(self) -> None:
        """Method showing the main view"""
        self.main_view.show()

    def exec(self) -> int:
        """
        Method running the application
        :return: The return code
        """
        return self.exec_()


def main():
    # SIGINT => Ctrl + C
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    app = App(sys.argv)
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
