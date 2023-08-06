"""Module managing the application views"""
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
import sys
import webbrowser
from os.path import isfile, expanduser
from typing import Any

from PySide2.QtCore import Slot, Qt, QSize
from PySide2.QtGui import QIcon, QFont, QCloseEvent
from PySide2.QtWidgets import QMainWindow, QFileDialog, QApplication, QMenuBar, QDialog, QLabel, QStatusBar, QGridLayout

from .form_view import UiFormWindow
from .web_view import UiWebWindow
from .. import gettext as _
from ..controllers.main_controller import ErrorMessage, Returns


def _get_current_screen():
    return QApplication.desktop().screenGeometry(
        QApplication.desktop().screenNumber(
            QApplication.desktop().cursor().pos()
        )
    )


def _about() -> None:
    dialog = QDialog()
    dialog.setWindowTitle(_("About"))
    dialog.setWindowModality(Qt.ApplicationModal)
    dialog.resize(200, 50)

    application = QApplication.instance()

    layout = QGridLayout()
    layout.setSpacing(20)

    label = QLabel()
    label.setPixmap(application.LOGO.pixmap(QSize(45, 45)))
    layout.addWidget(label, 0, 0, 2, 1)

    label_titre = QLabel("Ubiquity Student")
    label_titre.setFont(QFont("Arial", 15, QFont.Bold))
    layout.addWidget(label_titre, 0, 1, Qt.AlignCenter)

    layout.addWidget(QLabel(f'{_("Version:")} {application.VERSION}'), 1, 1, Qt.AlignCenter)
    layout.addWidget(QLabel(f'{_("License:")} Copyright '
                            f'(C) 2022  INSA Rouen Normandie - CIP'), 2, 1, Qt.AlignCenter)

    dialog.setLayout(layout)
    dialog.exec_()


def _help() -> None:
    webbrowser.open_new_tab("https://gitlab.insa-rouen.fr/cip/ubiquity/-/wikis/"
                            "Mode-d'emploi-de-l'application-%C3%A9tudiante")


class MainView(QMainWindow):
    """Class managing the main view"""
    def __init__(self, model: Any, main_controller: Any) -> None:
        super().__init__()

        self._model = model
        self._main_controller = main_controller
        self._ui = UiFormWindow()

        self.open_action = None
        self.close_action = None
        self.setMenuBar(self._menu_bar())

        self.setWindowTitle("Ubiquity Student")
        self.setWindowIcon(QIcon(QApplication.instance().LOGO))

        self._ui.directory_button.clicked.connect(self.search_directory)
        self._ui.submit_button.clicked.connect(self.submit)

        self._model.prefix_server_changed.connect(self.on_prefix_server_change)
        self._model.server_changed.connect(self.on_server_change)
        self._model.student_key_changed.connect(self.on_student_key_change)
        self._model.group_key_changed.connect(self.on_group_key_change)
        self._model.directory_changed.connect(self.on_directory_change)
        self._model.error_changed.connect(self.on_error_change)

        self._main_controller.init_values()
        self.setCentralWidget(self._ui)
        self.setStatusBar(QStatusBar())
        self.resize(self._ui.minimumWidth(), self._ui.minimumHeight())
        self._center()

    def _menu_bar(self) -> QMenuBar:
        menu_bar = QMenuBar(self)
        file_menu = menu_bar.addMenu(_('&File'))

        self.open_action = file_menu.addAction(_('&Open...'))
        self.open_action.triggered.connect(self._open_config)

        self.close_action = file_menu.addAction(_('&Close'))
        self.close_action.triggered.connect(self._close_project)

        quit_action = file_menu.addAction(_('&Exit'))
        quit_action.triggered.connect(self.close)

        help_menu = menu_bar.addMenu(_('&Help'))
        help_action = help_menu.addAction(_('&Help...'))
        help_action.triggered.connect(_help)
        about_action = help_menu.addAction(_('&About...'))
        about_action.triggered.connect(_about)

        self._update_menu_bar()
        return menu_bar

    def _update_menu_bar(self):
        is_form_view = isinstance(self._ui, UiFormWindow)
        self.close_action.setDisabled(is_form_view)
        self.open_action.setDisabled(not is_form_view)

    def _close_project(self) -> None:
        self._ui = UiFormWindow()
        self.setCentralWidget(self._ui)
        self._update_menu_bar()
        self.resize(self._ui.minimumWidth(), self._ui.minimumHeight())
        self._main_controller.init_values()
        self._ui.directory_button.clicked.connect(self.search_directory)
        self._ui.submit_button.clicked.connect(self.submit)
        self._center()
        self.setStatusBar(QStatusBar())
        self.show()

    def _open_config(self) -> None:
        self._ui.choice_dialog.btn_valid.clicked.connect(self._valid_dialog_config)
        self._ui.choice_dialog.init_list(self._main_controller.config)
        self._ui.choice_dialog.exec_()

    def _valid_dialog_config(self) -> None:
        data = self._ui.choice_dialog.get_data()
        if data:
            self._main_controller.update_with_config(data)
            self._ui.labels_style_default()
        self._ui.choice_dialog.close()

    @Slot(str)
    def on_prefix_server_change(self, value: str) -> None:
        """
        Method changing the content of the prefix server input
        :param value: Value to be defined as input
        """
        self._ui.combo_box_prefix_server.setCurrentText(value)

    @Slot(str)
    def on_server_change(self, value: str) -> None:
        """
        Method changing the content of the server input
        :param value: Value to be defined as input
        """
        self._ui.line_edit_server.setText(value)

    @Slot(str)
    def on_student_key_change(self, value: str) -> None:
        """
        Method changing the content of the student key input
        :param value: Value to be defined as input
        """
        self._ui.line_edit_student_key.setText(value)

    @Slot(str)
    def on_group_key_change(self, value: str) -> None:
        """
        Method changing the content of the group key input
        :param value: Value to be defined as input
        """
        self._ui.line_edit_group_key.setText(value)

    @Slot(str)
    def on_directory_change(self, value: str) -> None:
        """
        Method changing the content of the directory input
        :param value: Value to be defined as input
        """
        self._ui.line_edit_directory.setText(value)

    @Slot(object)
    def on_error_change(self, value: Any) -> None:
        """
        Method changing the content of the error message input
        :param value: Value to be defined as input
        """
        error_style = "color: red;"
        good_style = "color: green;"
        if value == ErrorMessage.EMPTY_FIELD:
            self._ui.line_edit_error(server=error_style, student_key=error_style,
                                     group_key=error_style, directory=error_style)
        elif value == ErrorMessage.CONNECTION_FAILED:
            self._ui.line_edit_error(server=error_style)
        elif value == ErrorMessage.INVALID_KEYS:
            self._ui.line_edit_error(server=good_style, student_key=error_style, group_key=error_style)
        elif value == ErrorMessage.DIRECTORY_DOES_NOT_EXIST:
            self._ui.line_edit_error(server=good_style, student_key=good_style,
                                     group_key=good_style, directory=error_style)
        if isinstance(value, str):
            self._ui.error_message.setText(value)
        else:
            self._ui.error_message.setText(value.value)

    def _show_web_view(self) -> None:
        self._ui = UiWebWindow(self._model.url_web_view())
        self.setCentralWidget(self._ui)
        self._update_menu_bar()
        screen = _get_current_screen()
        self.resize(screen.width()/2, screen.height())
        self.move(screen.center())
        self.statusBar().addWidget(QLabel(f'{_("Directory")} : {self._model.directory}'))
        self.show()

    def _center(self) -> None:
        screen = _get_current_screen()
        center = screen.center()
        self.move(center.x()-self.width()/2, center.y()-self.height()/2)

    def _file_changed(self, path: str) -> None:
        if isfile(path):
            self._main_controller.worker.post(path)
        else:
            self._main_controller.worker.delete(path)
        self._ui.do_refresh()

    def _directory_changed(self, path: str) -> None:
        self._main_controller.worker.add_new_files_in_directory(path)
        self._ui.do_refresh()

    def _reset_project(self):
        self._ui.new_or_not_dialog.close()
        self._ui.new_or_not_dialog.reset = True

    def _restore_project(self):
        self._ui.new_or_not_dialog.close()
        self._ui.new_or_not_dialog.restore = True

    def submit(self) -> None:
        """Method of action on the validation"""
        self._main_controller.change_prefix_server(self._ui.combo_box_prefix_server.currentText())
        self._main_controller.change_server(self._ui.line_edit_server.text())
        self._main_controller.change_student_key(self._ui.line_edit_student_key.text())
        self._main_controller.change_group_key(self._ui.line_edit_group_key.text())
        self._main_controller.change_directory(self._ui.line_edit_directory.text())
        response = self._main_controller.submit()
        if response == Returns.CHOICE:
            self._ui.new_or_not_dialog.btn_reset.clicked.connect(self._reset_project)
            self._ui.new_or_not_dialog.btn_restore.clicked.connect(self._restore_project)
            self._ui.new_or_not_dialog.btn_cancel.clicked.connect(self._ui.new_or_not_dialog.close)
            self._ui.new_or_not_dialog.exec_()
            if self._ui.new_or_not_dialog.restore:
                self._ui.new_or_not_dialog.restore = False
                self._main_controller.extract_zip(False)
                response = Returns.OK
            elif self._ui.new_or_not_dialog.reset:
                self._ui.new_or_not_dialog.reset = False
                self._main_controller.extract_zip()
                response = Returns.OK
        if response == Returns.OK:
            self._main_controller.run()
            self._main_controller.worker.file_system_watcher.fileChanged.connect(self._file_changed)
            self._main_controller.worker.file_system_watcher.directoryChanged.connect(self._directory_changed)
            self._show_web_view()

    def search_directory(self) -> None:
        """Method requesting a directory with a dialog box"""
        selected_directory = QFileDialog(parent=self).getExistingDirectory(parent=self, dir=expanduser("~"),
                                                                           options=QFileDialog.ShowDirsOnly)
        if selected_directory and selected_directory != "":
            self._ui.line_edit_directory.setText(selected_directory)

    def closeEvent(self, event: QCloseEvent) -> None:
        QApplication.instance().quit()
        sys.exit(0)
