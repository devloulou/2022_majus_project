import sys

from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow, QWidget, QApplication, QHBoxLayout, QVBoxLayout, QFileDialog

from helpers.movie_db import get_popular_movies
from helpers.file_helper import get_files

class MovieMetaLoader(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Movie Meta Loader')
        self.resize(1000, 800)
        self.showMaximized()

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)

        # main menü
        menu = self.menuBar()
        settings_menu = menu.addMenu("&Content")

        add_folder_action = QAction("Add Folder", settings_menu)
        add_folder_action.triggered.connect(self.add_folder_action)
        settings_menu.addAction(add_folder_action)

        add_popular_movies = QAction("Add Popular Movies", settings_menu)
        add_popular_movies.triggered.connect(self.add_popular_movies)
        settings_menu.addAction(add_popular_movies)

    def add_folder_action(self):
        folder = QFileDialog.getExistingDirectory(self, "Select folder:", "C:")

        # ide kellen majd az a megoldás, ami triggereli a letöltést és kirajzolást

    def add_popular_movies(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MovieMetaLoader()
    win.show()
    app.exec()