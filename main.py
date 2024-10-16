import sys

import PySide6
from PySide6.QtWidgets import (QApplication, QMainWindow, QApplication, QWidget, QComboBox, QLineEdit, QPushButton,
                               QHBoxLayout, QVBoxLayout, QLabel, QCompleter, QGridLayout)
from PySide6.QtCore import Qt, QAbstractItemModel, QSortFilterProxyModel
from PySide6.QtWidgets import QHeaderView, QTableView
from PySide6.QtSql import QSqlTableModel
from connection import Data
from py_ui.ui_main_side import Ui_MainWindow
from py_ui.ui_vistavka_entry import Ui_add_zapis_dialog


class ExponatDBMS(QMainWindow):
    def __init__(self):
        super(ExponatDBMS, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connection = Data()
        self.showMaximized()
        self.current_model = None  # Текущая модель для фильтрации
        self.filter_fields = {}  # Словарь для хранения полей фильтрации для каждого столбца
        self.ui.add_filters_cb.currentIndexChanged.connect(self.update_filter_input_field)

        # Initialize the filter input area
        self.filter_input_layout = QHBoxLayout()  # Layout for the filter input field
        self.ui.toplevel_layout.addLayout(self.filter_input_layout) # Добавляем его в главный макет
        self.init_tables()
        self.ui.tables_menu.triggered.connect(self.set_current_table)
        self.ui.create_btn.clicked.connect(self.open_create_entry_dialog)
        # Хранение состояния сортировки для каждой таблицы
        self.sort_states = {
            "vyst_mo_table": {},
            "vuz_table": {},
            "grntirub_table": {},
            "svod_table": {}
        }
        self.init_tables()
        self.ui.tables_menu.triggered.connect(self.set_current_table)
        self.ui.create_btn.clicked.connect(self.open_create_entry_dialog)



        self.vyst_mo_proxy_model = QSortFilterProxyModel(self)
        self.vuz_proxy_model = QSortFilterProxyModel(self)
        self.grntirub_proxy_model = QSortFilterProxyModel(self)
        self.svod_proxy_model = QSortFilterProxyModel(self)

        self.current_proxy_model = None  # Текущая прокси-модель для фильтрации

        self.ui.add_filters_cb.currentIndexChanged.connect(self.update_filter_input_field)
        self.init_tables()
        # Создаем виджет-контейнер для фильтров
        # self.filter_container_widget = QWidget()
        # self.filter_layout = QVBoxLayout(self.filter_container_widget)  # Layout для фильтров
        # self.ui.scrollArea.setWidget(self.filter_container_widget)  # Устанавливаем контейнер в QScrollArea
        # self.ui.scrollArea.setWidgetResizable(True)  # Делаем виджет растягиваемым

        # Добавляем combobox для фильтрации
        #self.ui.add_filters_cb.activated.connect(self.add_filter_field)

        # # # Кнопка для сброса фильтров
        # self.ui.tables_menu.triggered.connect(self.set_current_table)
        # self.ui.create_btn.clicked.connect(self.open_create_entry_dialog)
        # self.ui.delete_btn.clicked.connect(self.delete_record)

    def open_create_entry_dialog(self):
        self.new_dialog = PySide6.QtWidgets.QDialog()
        self.ui_create_entry_dialog = Ui_add_zapis_dialog()
        self.ui_create_entry_dialog.setupUi(self.new_dialog)
        self.ui_create_entry_dialog.save_btn.clicked.connect(self.create_entry)
        self.new_dialog.show()

    def create_entry(self):
        vuz = self.ui_create_entry_dialog.vuz.currentText()
        priznak = self.ui_create_entry_dialog.priznak.currentText()
        reg_number = self.ui_create_entry_dialog.reg_number.text()
        nir_name = self.ui_create_entry_dialog.nir_name.text()
        grnti = self.ui_create_entry_dialog.grnti.text()
        nir_ruk = self.ui_create_entry_dialog.grnti.text()
        nir_ruk_info = f"{self.ui_create_entry_dialog.ruk_doljnost.text()}, {self.ui_create_entry_dialog.ruk_zvanie.text()}, {self.ui_create_entry_dialog.ruk_stepen.text()}"
        exponat_est = self.ui_create_entry_dialog.exponat_est.currentText()
        vistavka = self.ui_create_entry_dialog.vistavka.text()
        exponat_name = self.ui_create_entry_dialog.exponat_name.text()

        if vuz and priznak and reg_number and nir_name and grnti and nir_ruk and nir_ruk_info and exponat_name and exponat_est and vistavka:
            row_count = self.vyst_mo_table_model.rowCount()
            self.vyst_mo_table_model.insertRow(row_count)
            self.vyst_mo_table_model.setData(self.vyst_mo_table_model.index(row_count, 1), vuz)
            self.vyst_mo_table_model.setData(self.vyst_mo_table_model.index(row_count, 2), priznak)
            self.vyst_mo_table_model.setData(self.vyst_mo_table_model.index(row_count, 3), reg_number)
            self.vyst_mo_table_model.setData(self.vyst_mo_table_model.index(row_count, 4), nir_name)
            self.vyst_mo_table_model.setData(self.vyst_mo_table_model.index(row_count, 5), grnti)
            self.vyst_mo_table_model.setData(self.vyst_mo_table_model.index(row_count, 6), nir_ruk)
            self.vyst_mo_table_model.setData(self.vyst_mo_table_model.index(row_count, 7), nir_ruk_info)
            self.vyst_mo_table_model.setData(self.vyst_mo_table_model.index(row_count, 8), exponat_est)
            self.vyst_mo_table_model.setData(self.vyst_mo_table_model.index(row_count, 9), vistavka)
            self.vyst_mo_table_model.setData(self.vyst_mo_table_model.index(row_count, 10), exponat_name)
            self.vyst_mo_table_model.submitAll()
            self.vyst_mo_table_model.select()
            #TODO

            row_count_2 = self.svod_table_model.rowCount()
            self.svod_table_model.insertRow(row_count)
            print(self.svod_table_model.index(row_count_2, 0))
            print(self.svod_table_model.index(row_count_2, 1))
            self.svod_table_model.setData(self.svod_table_model.index(row_count_2, 1), self.get_value_by_key(self.vuz_table_model, vuz, 0, 1))
            self.svod_table_model.setData(self.svod_table_model.index(row_count_2, 2), self.get_value_by_key(self.vuz_table_model, vuz, 0, 2))
            self.svod_table_model.setData(self.svod_table_model.index(row_count_2, 3), self.get_value_by_key(self.vuz_table_model, vuz, 0, 3))
            self.svod_table_model.setData(self.svod_table_model.index(row_count_2, 4), self.get_value_by_key(self.vuz_table_model, vuz, 0, 4))
            self.svod_table_model.setData(self.svod_table_model.index(row_count_2, 5), self.get_value_by_key(self.vuz_table_model, vuz, 0, 5))
            self.svod_table_model.setData(self.svod_table_model.index(row_count_2, 6), self.get_value_by_key(self.vuz_table_model, vuz, 0, 6))
            self.svod_table_model.setData(self.svod_table_model.index(row_count_2, 7), self.get_value_by_key(self.vuz_table_model, vuz, 0, 7))
            self.svod_table_model.setData(self.svod_table_model.index(row_count_2, 8), self.get_value_by_key(self.vuz_table_model, vuz, 0, 8))
            self.svod_table_model.setData(self.svod_table_model.index(row_count_2, 9), self.get_value_by_key(self.vuz_table_model, vuz, 0, 9))
            self.svod_table_model.setData(self.svod_table_model.index(row_count_2, 10), self.get_value_by_key(self.vuz_table_model, vuz, 0, 10))
            self.svod_table_model.setData(self.svod_table_model.index(row_count_2, 11), self.get_value_by_key(self.vuz_table_model, vuz, 0, 11))
            # self.svod_table_model.setData(self.svod_table_model.index(row_count, 1), (self.get_row_by_key(self.vuz_table_model, vuz, 0))[self.svod_table_model.headerData(1, Qt.Orientation.Horizontal)])
            # self.svod_table_model.setData(self.svod_table_model.index(row_count, 2), (self.get_row_by_key(self.vuz_table_model, vuz, 0))[self.svod_table_model.headerData(2, Qt.Orientation.Horizontal)])
            # self.svod_table_model.setData(self.svod_table_model.index(row_count, 3), (self.get_row_by_key(self.vuz_table_model, vuz, 0))[self.svod_table_model.headerData(3, Qt.Orientation.Horizontal)])
            # self.svod_table_model.setData(self.svod_table_model.index(row_count, 4), (self.get_row_by_key(self.vuz_table_model, vuz, 0))[self.svod_table_model.headerData(4, Qt.Orientation.Horizontal)])
            # self.svod_table_model.setData(self.svod_table_model.index(row_count, 5), (self.get_row_by_key(self.vuz_table_model, vuz, 0))[self.svod_table_model.headerData(5, Qt.Orientation.Horizontal)])
            # self.svod_table_model.setData(self.svod_table_model.index(row_count, 6), (self.get_row_by_key(self.vuz_table_model, vuz, 0))[self.svod_table_model.headerData(6, Qt.Orientation.Horizontal)])
            # self.svod_table_model.setData(self.svod_table_model.index(row_count, 7), (self.get_row_by_key(self.vuz_table_model, vuz, 0))[self.svod_table_model.headerData(7, Qt.Orientation.Horizontal)])
            # self.svod_table_model.setData(self.svod_table_model.index(row_count, 8), (self.get_row_by_key(self.vuz_table_model, vuz, 0))[self.svod_table_model.headerData(8, Qt.Orientation.Horizontal)])
            # self.svod_table_model.setData(self.svod_table_model.index(row_count, 9), (self.get_row_by_key(self.vuz_table_model, vuz, 0))[self.svod_table_model.headerData(9, Qt.Orientation.Horizontal)])
            # self.svod_table_model.setData(self.svod_table_model.index(row_count, 10), (self.get_row_by_key(self.vuz_table_model, vuz, 0))[self.svod_table_model.headerData(10, Qt.Orientation.Horizontal)])
            # self.svod_table_model.setData(self.svod_table_model.index(row_count, 11), (self.get_row_by_key(self.vuz_table_model, vuz, 0))[self.svod_table_model.headerData(11, Qt.Orientation.Horizontal)])
            self.svod_table_model.setData(self.svod_table_model.index(row_count_2, 12), priznak)
            self.svod_table_model.setData(self.svod_table_model.index(row_count_2, 13), reg_number)
            self.svod_table_model.setData(self.svod_table_model.index(row_count_2, 14), nir_name)
            self.svod_table_model.setData(self.svod_table_model.index(row_count_2, 15), grnti)
            self.svod_table_model.setData(self.svod_table_model.index(row_count_2, 16), nir_ruk)
            self.svod_table_model.setData(self.svod_table_model.index(row_count_2, 17), nir_ruk_info)
            self.svod_table_model.setData(self.svod_table_model.index(row_count_2, 18), exponat_est)
            self.svod_table_model.setData(self.svod_table_model.index(row_count_2, 19), vistavka)
            self.svod_table_model.setData(self.svod_table_model.index(row_count_2, 20), exponat_name)
            self.svod_table_model.submitAll()
            self.svod_table_model.select()

        self.new_dialog.close()


    def delete_record(self):
        current_table: QTableView = self.ui.db_tables.currentWidget().children()[0]
        # index = current_table.selectedIndexes()[0]
        # # selected = current_table.currentIndex()
        # if len(index) != 0:
        #     for i in range(len(index)):
        #         current_table.removeRow(i)
        #     current_table.submitAll()
        #     current_table.select()

        selected = current_table.currentIndex()
        model: QAbstractItemModel = current_table.model()
        if selected.row() != -1:
            model.removeRow(selected.row())
            model.submitAll()
            model.select()

    def get_value_by_key(self, model, key_value, key_column=0, target_column=1):
        """
        Возвращает значение из таблицы по ключу.

        :param model: QSqlTableModel - модель данных
        :param key_value: значение ключа (например, id)
        :param key_column: индекс столбца ключа (по умолчанию 0)
        :param target_column: индекс столбца, из которого нужно получить значение
        :return: Значение из указанного столбца или None, если запись не найдена
        """
        # Ищем индекс строки, соответствующий ключевому значению
        indexes = model.match(
            model.index(0, key_column),  # Начинаем поиск с первой строки в столбце ключа
            Qt.ItemDataRole.DisplayRole,  # Совпадение по точному значению
            key_value,  # Значение ключа для поиска
            1,  # Ищем только одно совпадение
            Qt.MatchFlag.MatchExactly
        )
        print(indexes)

        if indexes:  # Если нашлось совпадение
            row = indexes[0].row()  # Получаем индекс строки
            value = model.data(model.index(row, target_column))  # Получаем значение целевого столбца
            return value
        else:
            return None  # Если запись не найдена
    # def get_row_by_key(self, model, key_value, key_column=0):
    #     """
    #     Возвращает данные строки из QSqlTableModel по значению ключа.
    #
    #     :param model: QSqlTableModel - модель данных
    #     :param key_value: значение ключа (например, id)
    #     :param key_column: индекс столбца ключа (по умолчанию 0, если ключ - первый столбец)
    #     :return: Словарь с данными строки или None, если строка не найдена
    #     """
    #     # Ищем индекс строки, соответствующий ключевому значению
    #     indexes = model.match(
    #         model.index(0, key_column),  # Начинаем поиск с первой строки в столбце ключа
    #         1,  # Совпадение по точному значению PySide6.QtCore.Qt.MatchFlag.MatchExactly
    #         key_value,  # Значение ключа для поиска
    #         1,  # Ищем только одно совпадение
    #         PySide6.QtCore.Qt.MatchFlag.MatchExactly
    #     )
    #
    #     if indexes:  # Если нашлось совпадение
    #         row = indexes[0].row()  # Получаем индекс строки
    #
    #         # Создаем словарь с данными строки
    #         row_data = {}
    #         for column in range(model.columnCount()):
    #             field_name = model.headerData(column, Qt.Orientation.Horizontal)
    #             field_value = model.data(model.index(row, column))
    #             row_data[field_name] = field_value
    #
    #         return row_data
    #     else:
    #         return None  # Если не нашли совпадений

    def init_tables(self):
        # self.models = {
        #     "vyst_mo_table": self.create_model("vyst_mo"),
        #     "vuz_table": self.create_model("VUZ"),
        #     "grntirub_table": self.create_model("grntirub")
        # }
        self.vyst_mo_table_model = self.create_model("vyst_mo")
        self.vuz_table_model = self.create_model("VUZ")
        self.grntirub_table_model = self.create_model("grntirub")
        self.svod_table_model = self.create_model("svod")

        # Устанавливаем модели и заголовки
        self.ui.vyst_mo_table.setModel(self.vyst_mo_table_model)
        self.ui.vuz_table.setModel(self.vuz_table_model)
        self.ui.grntirub_table.setModel(self.grntirub_table_model)
        self.ui.svod_table.setModel(self.svod_table_model)


        # Отключаем сортировку по заголовкам при первом выводе
        self.ui.vyst_mo_table.setSortingEnabled(False)
        self.ui.vuz_table.setSortingEnabled(False)
        self.ui.grntirub_table.setSortingEnabled(False)
        self.ui.svod_table.setSortingEnabled(False)

        # Настройка заголовков
        self.set_custom_headers(self.vyst_mo_table_model, ["Код ВУЗа/организации",
                                                  "Признак  формы НИР", "Регистрационный номер НИР", "Наименование проекта/НИР",
                                                  "Коды  ГРНТИ", "Руководитель НИР", "Должность, ученое звание, ученая степень руководителя",
                                                  "Признак", "Выставки", "Название выставочного экспоната"])

        self.set_custom_headers(self.vuz_table_model, ["Код ВУЗа", "Название ВУЗа", "Полное наименование", "Сокращенное наименование",
                                               "Федеральный округ", 'Город', "Статус", "Номер области", "Область", "Категория", "Профиль"])

        self.set_custom_headers(self.grntirub_table_model, ["Код рубрики", "Наименование рубрики"])
        self.set_custom_headers(self.svod_table_model, ["Код ВУЗа/организации", "Название ВУЗа", "Полное наименование", "Сокращенное наименование",
                                               "Федеральный округ", 'Город', "Статус", "Номер области", "Область", "Категория", "Профиль",
                                                        "Признак  формы НИР", "Регистрационный номер НИР",
                                                        "Наименование проекта/НИР",
                                                        "Коды  ГРНТИ", "Руководитель НИР",
                                                        "Должность, ученое звание, ученая степень руководителя",
                                                        "Признак", "Выставки", "Название выставочного экспоната"
                                                        ])

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
        self.ui.svod_table.horizontalHeader().sectionClicked.connect(
            lambda index: self.handle_header_click(self.ui.svod_table, index)
        )

        # Устанавливаем режим растягивания заголовков
        for table in [self.ui.vyst_mo_table, self.ui.vuz_table, self.ui.grntirub_table, self.ui.svod_table]:
            header = table.horizontalHeader()
            header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
            # Устанавливаем автоматическое изменение ширины столбцов
            header.setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)

    def update_filter_input_field(self):
        selected_filter = self.ui.add_filters_cb.currentText()

        if selected_filter and selected_filter not in self.filter_fields:
            # Создаем новое поле для фильтрации
            new_filter = self.create_filter_input(selected_filter)
            self.filter_fields[selected_filter] = new_filter  # Сохраняем ссылку на поле
            self.filter_input_layout.addLayout(new_filter)  # Добавляем в макет

    def create_filter_input(self, label_text):
        """Создаем QLineEdit (или QComboBox для уникальных значений) и кнопку очистки."""
        layout = QHBoxLayout()

        # Label
        label = QLabel(label_text)
        layout.addWidget(label)

        # Создаем QComboBox для уникальных значений из выбранной колонки
        combo_box = QComboBox()
        unique_values = self.get_unique_values_for_column(label_text)

        if unique_values:
            combo_box.addItems(unique_values)
        combo_box.setEditable(True)  # Позволяем ручной ввод

        # Связываем действие при вводе значений
        combo_box.lineEdit().returnPressed.connect(self.apply_filters)

        layout.addWidget(combo_box)

        # Кнопка для очистки фильтра
        clear_button = QPushButton("✖️")
        clear_button.setFixedSize(25, 25)
        clear_button.clicked.connect(lambda: self.remove_filter_input(label_text, layout))
        layout.addWidget(clear_button)

        return layout

    def get_unique_values_for_column(self, column_name):
        """Извлекаем уникальные значения для выбранной колонки из текущей модели."""
        column_index = [self.current_model.headerData(i, Qt.Horizontal) for i in
                        range(self.current_model.columnCount())].index(column_name)

        unique_values = set()
        for row in range(self.current_model.rowCount()):
            index = self.current_model.index(row, column_index)
            value = self.current_model.data(index)
            if value:
                unique_values.add(str(value))  # Убедимся, что значения обрабатываются как строки

        return sorted(unique_values)

    # def apply_filters(self):
    #     """Apply filters based on selected values in the ComboBox inputs."""
    #     filter_conditions = {}
    #
    #     # Проходим по всем полям с фильтрами и собираем их условия
    #     for filter_key, filter_layout in self.filter_fields.items():
    #         combo_box = filter_layout.itemAt(1).widget()  # Это поле QComboBox с возможностью ввода
    #         filter_value = combo_box.currentText()
    #
    #         if filter_value:
    #             # Добавляем условие для фильтрации
    #             filter_conditions[filter_key] = filter_value
    #
    #     # Если нет условий фильтрации, показываем все строки
    #     if not filter_conditions:
    #         print("Resetting filters to show all rows")
    #         for row in range(self.current_model.rowCount()):
    #             self.ui.vyst_mo_table.showRow(row)
    #         return  # Выходим, так как фильтры не применяются
    #
    #     # Применяем фильтры
    #     self.filter_table(filter_conditions)

    def apply_filters(self):
        """Apply filters based on selected values in the ComboBox inputs."""
        filter_conditions = {}

        # Собираем условия фильтрации
        for filter_key, filter_layout in self.filter_fields.items():
            combo_box = filter_layout.itemAt(1).widget()  # QComboBox
            filter_value = combo_box.currentText()
            if filter_value:
                filter_conditions[filter_key] = filter_value

        # Если нет условий фильтрации, показываем все строки
        if not filter_conditions:
            self.show_all_rows()
            return

        # Применяем фильтры к текущей модели
        self.filter_table(filter_conditions)

    def show_all_rows(self):
        """Показать все строки в текущей таблице."""
        for row in range(self.current_model.rowCount()):
            self.ui.vyst_mo_table.showRow(row)
            self.ui.vuz_table.showRow(row)
            self.ui.grntirub_table.showRow(row)
            self.ui.svod_table.showRow(row)

    # def filter_table(self, filter_conditions):
    #     """Применяем фильтр ко всем строкам в таблице."""
    #     for row in range(self.current_model.rowCount()):
    #         show_row = True  # Флаг для отображения строки
    #
    #         for filter_key, filter_value in filter_conditions.items():
    #             column_index = [self.current_model.headerData(i, Qt.Horizontal) for i in
    #                             range(self.current_model.columnCount())].index(filter_key)
    #             index = self.current_model.index(row, column_index)
    #             data_value = self.current_model.data(index)
    #
    #             # Проверка на точное совпадение (с учетом регистра)
    #             if str(data_value) != str(filter_value):
    #                 show_row = False
    #                 break
    #
    #         if show_row:
    #             self.ui.vyst_mo_table.showRow(row)
    #         else:
    #             self.ui.vyst_mo_table.hideRow(row)

    def filter_table(self, filter_conditions):
        """Применяем фильтры ко всем строкам в текущей таблице."""
        for row in range(self.current_model.rowCount()):
            show_row = True  # Флаг для отображения строки

            for filter_key, filter_value in filter_conditions.items():
                column_index = [self.current_model.headerData(i, Qt.Horizontal) for i in
                                range(self.current_model.columnCount())].index(filter_key)
                index = self.current_model.index(row, column_index)
                data_value = self.current_model.data(index)

                # Проверка на точное совпадение (с учетом регистра)
                if str(data_value) != str(filter_value):
                    show_row = False
                    break

            if show_row:
                self.show_row_in_all_tables(row, True)
            else:
                self.show_row_in_all_tables(row, False)

    def show_row_in_all_tables(self, row, visible):
        """Показать или скрыть строку во всех таблицах."""
        for table in [self.ui.vyst_mo_table, self.ui.vuz_table, self.ui.grntirub_table, self.ui.svod_table]:
            if visible:
                table.showRow(row)
            else:
                table.hideRow(row)



    # def remove_filter_input(self, label_text, layout):
    #     """Удаляем поле ввода фильтра и сбрасываем фильтрацию по этой колонке."""
    #     if label_text in self.filter_fields:
    #         for i in reversed(range(layout.count())):
    #             widget = layout.itemAt(i).widget()
    #             if widget:
    #                 widget.deleteLater()
    #
    #         del self.filter_fields[label_text]
    #         self.apply_filters()  # Применяем фильтры заново

    def remove_filter_input(self, label_text, layout):
        """Удаляем поле ввода фильтра и сбрасываем фильтрацию по этой колонке."""
        if label_text in self.filter_fields:
            for i in reversed(range(layout.count())):
                widget = layout.itemAt(i).widget()
                if widget:
                    widget.deleteLater()

            del self.filter_fields[label_text]
            self.apply_filters()  # Применяем фильтры заново

    # def clear_all_filters(self):
    #     """Сбрасываем все фильтры и показываем все строки."""
    #     for row in range(self.current_model.rowCount()):
    #         self.ui.vyst_mo_table.showRow(row)
    #
    #     # Очистка всех полей фильтров
    #     for filter_key, layout in self.filter_fields.items():
    #         while layout.count():
    #             item = layout.takeAt(0)
    #             widget = item.widget()
    #             if widget:
    #                 widget.deleteLater()
    #
    #     self.filter_fields.clear()

    def clear_all_filters(self):
        """Сбрасываем все фильтры и показываем все строки во всех таблицах."""
        self.show_all_rows()
        self.filter_fields.clear()  # Сбросить поля фильтров

        # Очистить все QComboBox
        for filter_key, layout in self.filter_fields.items():
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.deleteLater()

    def create_model(self, table_name: str):
        model = QSqlTableModel(self)
        model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        model.setTable(table_name)
        model.select()
        return model

    # def apply_filters(self):
    #     filter_conditions = []
    #     for filter_key, filter_layout in self.filter_fields.items():
    #         input_field = filter_layout.itemAt(1).widget()
    #         filter_value = input_field.text()
    #         if filter_value:
    #             filter_conditions.append(f"{filter_key} LIKE '%{filter_value}%'")
    #
    #     if filter_conditions:
    #         self.current_model.setFilter(" AND ".join(filter_conditions))
    #     else:
    #         self.current_model.setFilter("")

    def update_filter_combobox(self):
        """Updates the ComboBox with currently active filters."""
        self.ui.add_filters_cb.clear()
        if self.current_model:
            headers = [self.current_model.headerData(i, Qt.Horizontal) for i in range(self.current_model.columnCount())]
            # Exclude currently selected filters
            for filter_key in self.filter_fields.keys():
                headers.remove(filter_key)
            self.ui.add_filters_cb.addItems(headers)

    def create_model(self, table_name: str):
        model = NonEditableSqlTableModel(self)
        model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        model.setTable(table_name)
        model.select()
        return model

    def set_custom_headers(self, model, headers):
        for index, header in enumerate(headers):
            model.setHeaderData(index, Qt.Horizontal, header)

    def set_current_table(self, checked_action):
        """Switches the current table and resets the filters."""
        # Reset filters and clear the input layout
        self.filter_fields.clear()
        while self.filter_input_layout.count():
            child = self.filter_input_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        # Switch the table
        text = checked_action.text()
        if text == "ГРНТИ":
            self.ui.db_tables.setCurrentIndex(3)
            self.current_model = self.grntirub_table_model
        elif text == "Выставки":
            self.ui.db_tables.setCurrentIndex(1)
            self.current_model = self.vyst_mo_table_model
        elif text == "ВУЗы":
            self.ui.db_tables.setCurrentIndex(2)
            self.current_model = self.vuz_table_model
        elif text == "Сводная таблица":
            self.ui.db_tables.setCurrentIndex(0)
            self.current_model = self.svod_table_model

        # Update the ComboBox with available columns
        self.update_filter_combobox()




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
    def flags(self, index):
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ExponatDBMS()
    window.show()
    sys.exit(app.exec())

