import sys

import PySide6.QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QHeaderView, QTableView
from PySide6.QtSql import QSqlTableModel
from connection import Data
from ui_main_side import Ui_MainWindow


class ExponatDBMS(QMainWindow):
    def __init__(self):
        super(ExponatDBMS, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connection = Data()

        # Хранение состояния сортировки для каждой таблицы
        self.sort_states = {
            "vyst_mo_table": {},
            "vuz_table": {},
            "grntirub_table": {}
        }

        self.init_tables()
        self.ui.tables.triggered.connect(self.set_current_table)
        self.ui.create_btn.clicked.connect(self.open_create_dialog)

        # self.ui.grnti.triggered.connect(self.set_current_table)
        # self.ui.vistavki.triggered.connect(self.set_current_table)
        # self.ui.vuz_2.triggered.connect(self.set_current_table)
        # self.ui.tables_combobox.activated.connect(self.set_current_table)

    def open_create_dialog(self):
        self.create_dialog = PySide6.QtWidgets.QDialog()

    def init_tables(self):
        self.models = {
            "vyst_mo_table": self.create_model("vyst_mo"),
            "vuz_table": self.create_model("VUZ"),
            "grntirub_table": self.create_model("grntirub")
        }

        # Устанавливаем модели и заголовки
        self.ui.vyst_mo_table.setModel(self.models["vyst_mo_table"])
        self.ui.vuz_table.setModel(self.models["vuz_table"])
        self.ui.grntirub_table.setModel(self.models["grntirub_table"])

        # Отключаем сортировку по заголовкам при первом выводе
        self.ui.vyst_mo_table.setSortingEnabled(False)
        self.ui.vuz_table.setSortingEnabled(False)
        self.ui.grntirub_table.setSortingEnabled(False)

        # Настройка заголовков
        self.set_custom_headers("vyst_mo_table", ["Код ВУЗа/организации",
                                                  "Признак  формы НИР", "Регистрационный номер НИР", "Наименование проекта/НИР",
                                                  "Коды  ГРНТИ", "Руководитель НИР", "Должность, ученое звание, ученая степень руководителя",
                                                  "Признак", "Выставки", "Название выставочного экспоната"])

        self.set_custom_headers("vuz_table", ["Код ВУЗа", "Название ВУЗа", "Полное наименование", "Сокращенное наименование",
                                               "Федеральный округ", 'Город', "Статус", "Номер области", "Область", "Категория", "Профиль"])

        self.set_custom_headers("grntirub_table", ["Код рубрики", "Наименование рубрики"])

        # Подключаем сортировку для каждой таблицы
        self.ui.vyst_mo_table.horizontalHeader().sectionClicked.connect(
            lambda index: self.handle_header_click(self.ui.vyst_mo_table, index)
        )
        self.ui.vuz_table.horizontalHeader().sectionClicked.connect(
            lambda index: self.handle_header_click(self.ui.vuz_table, index)
        )
        self.ui.grntirub_table.horizontalHeader().sectionClicked.connect(
            lambda index: self.handle_header_click(self.ui.grntirub_table, index)
        )

        # Устанавливаем режим растягивания заголовков
        for table in [self.ui.vyst_mo_table, self.ui.vuz_table, self.ui.grntirub_table]:
            header = table.horizontalHeader()
            header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
            # Устанавливаем автоматическое изменение ширины столбцов
            header.setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)

    def create_model(self, table_name: str):
        model = NonEditableSqlTableModel(self)
        model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        model.setTable(table_name)
        model.select()
        return model

    def set_custom_headers(self, table_name, headers):
        model = self.models[table_name]
        for index, header in enumerate(headers):
            model.setHeaderData(index, Qt.Horizontal, header)

    def set_current_table(self, checked_action):
        # Меняем текущую таблицу в зависимости от выбора в ComboBox
        text = checked_action.text()
        if text == "ГРНТИ":
            self.ui.db_tables.setCurrentIndex(2)
        elif text == "Выставки":
            self.ui.db_tables.setCurrentIndex(0)
        elif text == "ВУЗы":
            self.ui.db_tables.setCurrentIndex(1)

    def handle_header_click(self, table, logicalIndex):
        # Получаем имя таблицы для правильного отслеживания состояния
        table_name = table.objectName()

        # Получаем текущее состояние сортировки для выбранного столбца
        current_sort_order = self.sort_states[table_name].get(logicalIndex, None)

        # Устанавливаем модель, связанную с таблицей
        model = table.model()

        # Устанавливаем следующее состояние сортировки
        if current_sort_order is None:
            model.sort(logicalIndex, Qt.AscendingOrder)
            self.sort_states[table_name][logicalIndex] = Qt.AscendingOrder
        elif current_sort_order == Qt.AscendingOrder:
            model.sort(logicalIndex, Qt.DescendingOrder)
            self.sort_states[table_name][logicalIndex] = Qt.DescendingOrder
        else:
            model.setSort(-1, Qt.AscendingOrder)  # Сбрасываем сортировку
            model.select()  # Перезагружаем данные в исходном порядке
            self.sort_states[table_name][logicalIndex] = None


class NonEditableSqlTableModel(QSqlTableModel):
    # Переопределение метода для запрета редактирования ячеек
    def flags(self, index):
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ExponatDBMS()
    window.show()
    sys.exit(app.exec())

