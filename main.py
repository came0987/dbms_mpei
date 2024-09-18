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

        self.ui.vyst_mo_table.setModel(self.create_model(table_name="vyst_mo"))
        self.ui.vuz_table.setModel(self.create_model(table_name="VUZ"))
        self.ui.grntirub_table.setModel(self.create_model(table_name="grntirub"))
        # self.ui.db_tables.setCurrentIndex(0)
        # self.ui.vuz_table.show()
        self.ui.tables_combobox.view().pressed.connect(self.set_current_table)
        # self.set_current_table()



    def create_model(self, table_name: str):
        model = QSqlTableModel(self)
        model.setEditStrategy(QSqlTableModel.EditStrategy.OnManualSubmit)
        model.setTable(table_name)
        model.select()
        return model
        # self.model = QStandardItemModel(self)
        # self.model.setHorizontalHeaderLabels()
        # self.model.setHeaderData(0, Qt.Orientation.Horizontal, "Name")
        # self.model.setHorizontalHeaderLabels()
        # self.ui.vyst_mo_table.setModel(self.model) #TODO оформить все выше в метод и передавать в параметры
        # header = QHeaderView(Qt.Orientation.Horizontal).headerDataChanged()
        # self.ui.vyst_mo_table.setHorizontalHeader()
        # self.ui.db_tables.setCurrentWidget(self.ui.vyst_mo)
        # self.ui.vyst_mo_table.show()
        # self.setCentralWidget(self.ui.vyst_mo_table)
        # self.ui.db_tables.show()

    def set_current_table(self, index):
        item = self.ui.tables_combobox.model().itemFromIndex(index)
        if item.text() == "ГРНТИ":
            self.ui.db_tables.setCurrentIndex(2)
        if item.text() == "Выставки":
            self.ui.db_tables.setCurrentIndex(0)
        if item.text() == "ВУЗы":
            self.ui.db_tables.setCurrentIndex(1)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ExponatDBMS()
    window.show()
    sys.exit(app.exec())
