import sys

from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QHeaderView
from PySide6.QtSql import QSqlTableModel
from PySide6.QtGui import QStandardItemModel, QStandardItem

from connection import Data
from ui_main_side import Ui_MainWindow


class ExponatDBMS(QMainWindow):
    def __init__(self):
        super(ExponatDBMS, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connection = Data()
        self.view_table(table_name="vyst_mo")

    def view_table(self, table_name: str):
        self.model = QSqlTableModel(self)
        # self.model = QStandardItemModel(self)
        # self.model.setHorizontalHeaderLabels()
        self.model.setEditStrategy(QSqlTableModel.EditStrategy.OnManualSubmit)
        self.model.setTable(table_name)
        # self.model.setHeaderData(0, Qt.Orientation.Horizontal, "Name")
        # self.model.setHorizontalHeaderLabels()
        self.model.select()
        self.ui.vyst_mo_table.setModel(self.model) #TODO оформить все выше в метод и передавать в параметры
        # header = QHeaderView(Qt.Orientation.Horizontal).headerDataChanged()
        # self.ui.vyst_mo_table.setHorizontalHeader()
        # self.ui.db_tables.setCurrentWidget(self.ui.vyst_mo)
        # self.ui.vyst_mo_table.show()
        # self.setCentralWidget(self.ui.vyst_mo_table)
        # self.ui.db_tables.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ExponatDBMS()
    window.show()

    sys.exit(app.exec())