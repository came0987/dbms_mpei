# import sys
#
# import PySide6.QtWidgets
# from PySide6.QtCore import Qt
# from PySide6.QtWidgets import QApplication, QMainWindow, QHeaderView, QTableView
# from PySide6.QtSql import QSqlTableModel
# from connection import Data
# from ui_main_side import Ui_MainWindow
#
#
# class ExponatDBMS(QMainWindow):
#     def __init__(self):
#         super(ExponatDBMS, self).__init__()
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)
#         self.connection = Data()
#
#         # Хранение состояния сортировки для каждой таблицы
#         self.sort_states = {
#             "vyst_mo_table": {},
#             "vuz_table": {},
#             "grntirub_table": {}
#         }
#
#         self.init_tables()
#         self.ui.tables.triggered.connect(self.set_current_table)
#         self.ui.create_btn.clicked.connect(self.open_create_dialog)
#
#         # self.ui.grnti.triggered.connect(self.set_current_table)
#         # self.ui.vistavki.triggered.connect(self.set_current_table)
#         # self.ui.vuz_2.triggered.connect(self.set_current_table)
#         # self.ui.tables_combobox.activated.connect(self.set_current_table)
#
#     def open_create_dialog(self):
#         self.create_dialog = PySide6.QtWidgets.QDialog()
#
#     def init_tables(self):
#         self.models = {
#             "vyst_mo_table": self.create_model("vyst_mo"),
#             "vuz_table": self.create_model("VUZ"),
#             "grntirub_table": self.create_model("grntirub")
#         }
#
#         # Устанавливаем модели и заголовки
#         self.ui.vyst_mo_table.setModel(self.models["vyst_mo_table"])
#         self.ui.vuz_table.setModel(self.models["vuz_table"])
#         self.ui.grntirub_table.setModel(self.models["grntirub_table"])
#
#         # Отключаем сортировку по заголовкам при первом выводе
#         self.ui.vyst_mo_table.setSortingEnabled(False)
#         self.ui.vuz_table.setSortingEnabled(False)
#         self.ui.grntirub_table.setSortingEnabled(False)
#
#         # Настройка заголовков
#         self.set_custom_headers("vyst_mo_table", ["Код ВУЗа/организации",
#                                                   "Признак  формы НИР", "Регистрационный номер НИР", "Наименование проекта/НИР",
#                                                   "Коды  ГРНТИ", "Руководитель НИР", "Должность, ученое звание, ученая степень руководителя",
#                                                   "Признак", "Выставки", "Название выставочного экспоната"])
#
#         self.set_custom_headers("vuz_table", ["Код ВУЗа", "Название ВУЗа", "Полное наименование", "Сокращенное наименование",
#                                                "Федеральный округ", 'Город', "Статус", "Номер области", "Область", "Категория", "Профиль"])
#
#         self.set_custom_headers("grntirub_table", ["Код рубрики", "Наименование рубрики"])
#
#         # Подключаем сортировку для каждой таблицы
#         self.ui.vyst_mo_table.horizontalHeader().sectionClicked.connect(
#             lambda index: self.handle_header_click(self.ui.vyst_mo_table, index)
#         )
#         self.ui.vuz_table.horizontalHeader().sectionClicked.connect(
#             lambda index: self.handle_header_click(self.ui.vuz_table, index)
#         )
#         self.ui.grntirub_table.horizontalHeader().sectionClicked.connect(
#             lambda index: self.handle_header_click(self.ui.grntirub_table, index)
#         )
#
#         # Устанавливаем режим растягивания заголовков
#         for table in [self.ui.vyst_mo_table, self.ui.vuz_table, self.ui.grntirub_table]:
#             header = table.horizontalHeader()
#             header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
#             # Устанавливаем автоматическое изменение ширины столбцов
#             header.setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
#
#     def create_model(self, table_name: str):
#         model = NonEditableSqlTableModel(self)
#         model.setEditStrategy(QSqlTableModel.OnManualSubmit)
#         model.setTable(table_name)
#         model.select()
#         return model
#
#     def set_custom_headers(self, table_name, headers):
#         model = self.models[table_name]
#         for index, header in enumerate(headers):
#             model.setHeaderData(index, Qt.Horizontal, header)
#
#     def set_current_table(self, checked_action):
#         # Меняем текущую таблицу в зависимости от выбора в ComboBox
#         text = checked_action.text()
#         if text == "ГРНТИ":
#             self.ui.db_tables.setCurrentIndex(2)
#         elif text == "Выставки":
#             self.ui.db_tables.setCurrentIndex(0)
#         elif text == "ВУЗы":
#             self.ui.db_tables.setCurrentIndex(1)
#
#     def handle_header_click(self, table, logicalIndex):
#         # Получаем имя таблицы для правильного отслеживания состояния
#         table_name = table.objectName()
#
#         # Получаем текущее состояние сортировки для выбранного столбца
#         current_sort_order = self.sort_states[table_name].get(logicalIndex, None)
#
#         # Устанавливаем модель, связанную с таблицей
#         model = table.model()
#
#         # Устанавливаем следующее состояние сортировки
#         if current_sort_order is None:
#             model.sort(logicalIndex, Qt.AscendingOrder)
#             self.sort_states[table_name][logicalIndex] = Qt.AscendingOrder
#         elif current_sort_order == Qt.AscendingOrder:
#             model.sort(logicalIndex, Qt.DescendingOrder)
#             self.sort_states[table_name][logicalIndex] = Qt.DescendingOrder
#         else:
#             model.setSort(-1, Qt.AscendingOrder)  # Сбрасываем сортировку
#             model.select()  # Перезагружаем данные в исходном порядке
#             self.sort_states[table_name][logicalIndex] = None
#
#
# class NonEditableSqlTableModel(QSqlTableModel):
#     # Переопределение метода для запрета редактирования ячеек
#     def flags(self, index):
#         return Qt.ItemIsSelectable | Qt.ItemIsEnabled
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = ExponatDBMS()
#     window.show()
#     sys.exit(app.exec())


#
# import sys
# from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QLineEdit, QPushButton, QScrollArea, QWidget
# from PySide6.QtSql import QSqlTableModel
# from PySide6.QtCore import Qt
# from connection import Data
# from ui_main_side import Ui_MainWindow
#
# class ExponatDBMS(QMainWindow):
#     def __init__(self):
#         super(ExponatDBMS, self).__init__()
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)
#         self.connection = Data()
#
#         self.current_model = None  # Текущая модель для фильтрации
#         self.filter_fields = {}  # Словарь для хранения полей фильтрации для каждого столбца
#
#         # Хранение состояния сортировки для каждой таблицы
#         self.sort_states = {
#             "vyst_mo_table": {},
#             "vuz_table": {},
#             "grntirub_table": {}
#         }
#
#         self.init_tables()
#         self.ui.tables.triggered.connect(self.set_current_table)
#         self.ui.create_btn.clicked.connect(self.open_create_dialog)
#
#         # Создаем виджет-контейнер для фильтров
#         self.filter_container_widget = QWidget()
#         self.filter_layout = QVBoxLayout(self.filter_container_widget)  # Layout для фильтров
#         self.ui.scrollArea.setWidget(self.filter_container_widget)  # Устанавливаем контейнер в QScrollArea
#         self.ui.scrollArea.setWidgetResizable(True)  # Делаем виджет растягиваемым
#
#         # Добавляем combobox для фильтрации
#         self.ui.add_filters_cb.activated.connect(self.add_filter_field)
#
#         # Кнопка для сброса фильтров
#         self.reset_filter_btn = QPushButton("Сбросить фильтры")
#         self.reset_filter_btn.clicked.connect(self.reset_filters)
#         self.filter_layout.addWidget(self.reset_filter_btn)
#
#     def open_create_dialog(self):
#         self.create_dialog = PySide6.QtWidgets.QDialog()
#
#     def init_tables(self):
#         self.models = {
#             "vyst_mo_table": self.create_model("vyst_mo"),
#             "vuz_table": self.create_model("VUZ"),
#             "grntirub_table": self.create_model("grntirub")
#         }
#
#         # Устанавливаем модели и заголовки
#         self.ui.vyst_mo_table.setModel(self.models["vyst_mo_table"])
#         self.ui.vuz_table.setModel(self.models["vuz_table"])
#         self.ui.grntirub_table.setModel(self.models["grntirub_table"])
#
#         # Настройка заголовков
#         self.set_custom_headers("vyst_mo_table", ["Код ВУЗа/организации",
#                                                   "Признак  формы НИР", "Регистрационный номер НИР", "Наименование проекта/НИР",
#                                                   "Коды  ГРНТИ", "Руководитель НИР", "Должность, ученое звание, ученая степень руководителя",
#                                                   "Признак", "Выставки", "Название выставочного экспоната"])
#
#         self.set_custom_headers("vuz_table", ["Код ВУЗа", "Название ВУЗа", "Полное наименование", "Сокращенное наименование",
#                                                "Федеральный округ", 'Город', "Статус", "Номер области", "Область", "Категория", "Профиль"])
#
#         self.set_custom_headers("grntirub_table", ["Код рубрики", "Наименование рубрики"])
#
#     def create_model(self, table_name: str):
#         model = NonEditableSqlTableModel(self)
#         model.setEditStrategy(QSqlTableModel.OnManualSubmit)
#         model.setTable(table_name)
#         model.select()
#         return model
#
#     def set_custom_headers(self, table_name, headers):
#         model = self.models[table_name]
#         for index, header in enumerate(headers):
#             model.setHeaderData(index, Qt.Horizontal, header)
#
#     def set_current_table(self, checked_action):
#         text = checked_action.text()
#         if text == "ГРНТИ":
#             self.ui.db_tables.setCurrentIndex(2)
#             self.current_model = self.models["grntirub_table"]
#         elif text == "Выставки":
#             self.ui.db_tables.setCurrentIndex(0)
#             self.current_model = self.models["vyst_mo_table"]
#         elif text == "ВУЗы":
#             self.ui.db_tables.setCurrentIndex(1)
#             self.current_model = self.models["vuz_table"]
#
#         self.update_filter_combobox()
#
#     def update_filter_combobox(self):
#         self.ui.add_filters_cb.clear()
#         if self.current_model:
#             headers = [self.current_model.headerData(i, Qt.Horizontal) for i in range(self.current_model.columnCount())]
#             self.ui.add_filters_cb.addItems(headers)
#
#     def add_filter_field(self):
#         selected_column = self.ui.add_filters_cb.currentText()
#
#         if selected_column not in self.filter_fields:
#             filter_layout = QVBoxLayout()
#             label = QLabel(f"Фильтр по {selected_column}:")
#             filter_input = QLineEdit()
#             apply_filter_btn = QPushButton("Применить фильтр")
#
#             apply_filter_btn.clicked.connect(lambda: self.apply_filter(selected_column, filter_input.text(), filter_layout))
#
#             filter_layout.addWidget(label)
#             filter_layout.addWidget(filter_input)
#             filter_layout.addWidget(apply_filter_btn)
#
#             # Добавляем кнопку для удаления фильтра
#             remove_filter_btn = QPushButton("Удалить фильтр")
#             remove_filter_btn.clicked.connect(lambda: self.remove_filter(selected_column, filter_layout))
#             filter_layout.addWidget(remove_filter_btn)
#
#             self.filter_layout.addLayout(filter_layout)
#             self.filter_fields[selected_column] = (filter_input, filter_layout)
#
#     def apply_filter(self, column, value, layout):
#         if self.current_model:
#             column_index = [self.current_model.headerData(i, Qt.Horizontal) for i in range(self.current_model.columnCount())].index(column)
#             filter_str = f"{self.current_model.record().fieldName(column_index)} LIKE '%{value}%'"
#             self.current_model.setFilter(filter_str)
#
#             # Обновляем все фильтры
#             self.update_all_filters()
#
#     def remove_filter(self, column, layout):
#         if self.current_model and column in self.filter_fields:
#             del self.filter_fields[column]
#             layout.deleteLater()  # Удаляем layout с фильтром
#             self.update_all_filters()
#
#     def reset_filters(self):
#         self.current_model.setFilter("")  # Убираем все фильтры
#         self.filter_fields.clear()  # Очищаем словарь фильтров
#         while self.filter_layout.count():
#             item = self.filter_layout.itemAt(0)
#             widget = item.widget()
#             if widget is not None:
#                 widget.deleteLater()  # Удаляем виджет фильтра
#         self.update_filter_combobox()  # Обновляем комбобокс фильтров
#
#     def update_all_filters(self):
#         combined_filter = []
#         for column, (input_field, _) in self.filter_fields.items():
#             value = input_field.text()
#             if value:
#                 column_index = [self.current_model.headerData(i, Qt.Horizontal) for i in range(self.current_model.columnCount())].index(column)
#                 filter_str = f"{self.current_model.record().fieldName(column_index)} LIKE '%{value}%'"
#                 combined_filter.append(filter_str)
#
#         # Обновляем фильтр в модели
#         if combined_filter:
#             self.current_model.setFilter(" AND ".join(combined_filter))
#         else:
#             self.current_model.setFilter("")
#
# class NonEditableSqlTableModel(QSqlTableModel):
#     def flags(self, index):
#         return Qt.ItemIsSelectable | Qt.ItemIsEnabled
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = ExponatDBMS()
#     window.show()
#     sys.exit(app.exec())
#
import sys

import PySide6
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QLineEdit, QPushButton, QScrollArea, \
    QWidget, QHeaderView
from PySide6.QtSql import QSqlTableModel
from PySide6.QtCore import Qt
from connection import Data
from ui_main_side import Ui_MainWindow

class ExponatDBMS(QMainWindow):
    def __init__(self):
        super(ExponatDBMS, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connection = Data()

        self.current_model = None  # Текущая модель для фильтрации
        self.filter_fields = {}  # Словарь для хранения полей фильтрации для каждого столбца

        # Хранение состояния сортировки для каждой таблицы
        self.sort_states = {
            "vyst_mo_table": {},
            "vuz_table": {},
            "grntirub_table": {}
        }

        self.init_tables()
        self.ui.tables.triggered.connect(self.set_current_table)
        self.ui.create_btn.clicked.connect(self.open_create_dialog)

        # Создаем виджет-контейнер для фильтров
        self.filter_container_widget = QWidget()
        self.filter_layout = QVBoxLayout(self.filter_container_widget)  # Layout для фильтров
        self.ui.scrollArea.setWidget(self.filter_container_widget)  # Устанавливаем контейнер в QScrollArea
        self.ui.scrollArea.setWidgetResizable(True)  # Делаем виджет растягиваемым

        # Добавляем combobox для фильтрации
        self.ui.add_filters_cb.activated.connect(self.add_filter_field)

        # # Кнопка для сброса фильтров
        # self.reset_filter_btn = QPushButton("Сбросить фильтры")
        # self.reset_filter_btn.clicked.connect(self.reset_filters)
        # self.filter_layout.addWidget(self.reset_filter_btn)

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
        text = checked_action.text()
        if text == "ГРНТИ":
            self.ui.db_tables.setCurrentIndex(2)
            self.current_model = self.models["grntirub_table"]
        elif text == "Выставки":
            self.ui.db_tables.setCurrentIndex(0)
            self.current_model = self.models["vyst_mo_table"]
        elif text == "ВУЗы":
            self.ui.db_tables.setCurrentIndex(1)
            self.current_model = self.models["vuz_table"]

        self.update_filter_combobox()

    def update_filter_combobox(self):
        self.ui.add_filters_cb.clear()
        if self.current_model:
            headers = [self.current_model.headerData(i, Qt.Horizontal) for i in range(self.current_model.columnCount())]
            self.ui.add_filters_cb.addItems(headers)

    def add_filter_field(self):
        selected_column = self.ui.add_filters_cb.currentText()

        if selected_column not in self.filter_fields:
            filter_layout = QVBoxLayout()
            label = QLabel(f"Фильтр по {selected_column}:")
            filter_input = QLineEdit()
            apply_filter_btn = QPushButton("Применить фильтр")

            apply_filter_btn.clicked.connect(lambda: self.apply_filter(selected_column, filter_input.text(), filter_layout))

            filter_layout.addWidget(label)
            filter_layout.addWidget(filter_input)
            filter_layout.addWidget(apply_filter_btn)

            # Добавляем кнопку для удаления фильтра
            remove_filter_btn = QPushButton("Удалить фильтр")
            remove_filter_btn.clicked.connect(lambda: self.remove_filter(selected_column, filter_layout))
            filter_layout.addWidget(remove_filter_btn)

            self.filter_layout.addLayout(filter_layout)
            self.filter_fields[selected_column] = (filter_input, filter_layout)

    def apply_filter(self, column, value, layout):
        if self.current_model:
            column_index = [self.current_model.headerData(i, Qt.Horizontal) for i in range(self.current_model.columnCount())].index(column)
            filter_str = f"{self.current_model.record().fieldName(column_index)} LIKE '%{value}%'"
            self.current_model.setFilter(filter_str)

            # Обновляем все фильтры
            self.update_all_filters()

    def remove_filter(self, column, layout):
        if self.current_model and column in self.filter_fields:
            # Удаляем фильтр из модели
            self.filter_fields[column][0].clear()  # Очищаем поле ввода
            column_index = [self.current_model.headerData(i, Qt.Horizontal) for i in range(self.current_model.columnCount())].index(column)
            self.current_model.setFilter("")  # Сбрасываем фильтр для текущей модели

            # Удаляем layout с фильтром
            filter_layout = self.filter_fields[column][1]
            while filter_layout.count():
                item = filter_layout.takeAt(0)  # Удаляем виджет из компоновки
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()  # Удаляем виджет

            del self.filter_fields[column]  # Удаляем запись о фильтре из словаря

            # Обновляем все фильтры
            self.update_all_filters()

    # def reset_filters(self):
    #     self.current_model.setFilter("")  # Убираем все фильтры
    #     self.filter_fields.clear()  # Очищаем словарь фильтров
    #     while self.filter_layout.count() > 1:  # Оставляем только кнопку сброса фильтров
    #         item = self.filter_layout.itemAt(0)
    #         widget = item.widget()
    #         if widget is not None:
    #             widget.deleteLater()  # Удаляем виджет фильтра
    #     self.update_filter_combobox()  # Обновляем комбобокс фильтров

    def update_all_filters(self):
        combined_filter = []
        for column, (input_field, _) in self.filter_fields.items():
            value = input_field.text()
            if value:
                column_index = [self.current_model.headerData(i, Qt.Horizontal) for i in range(self.current_model.columnCount())].index(column)
                filter_str = f"{self.current_model.record().fieldName(column_index)} LIKE '%{value}%'"
                combined_filter.append(filter_str)

        # Обновляем фильтр в модели
        if combined_filter:
            self.current_model.setFilter(" AND ".join(combined_filter))
        else:
            self.current_model.setFilter("")


class NonEditableSqlTableModel(QSqlTableModel):
    def flags(self, index):
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ExponatDBMS()
    window.show()
    sys.exit(app.exec())
