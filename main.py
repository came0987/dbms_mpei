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
        self.ui.delete_all_filters.clicked.connect(self.clear_all_filters)

        self.filter_input_layout = QGridLayout()  # Layout for the filter input field
        self.ui.toplevel_layout.addLayout(self.filter_input_layout)  # Добавляем его в главный макет


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
        self.set_custom_headers(self.svod_table_model, ["Код ВУЗа", "Сокр. наим. ВУЗа",
                                                        "Наименование НИР", "Коды  ГРНТИ", "Руководитель НИР", "Должность, ученое звание, ученая степень руководителя",
                                                        "Рег. номер НИР", "Выставки", "Выставочный экспонат", "Признак  формы НИР", "Признак", "Название ВУЗа", "Полное наименование",
                                               "Федеральный округ", 'Город', "Статус", "Номер области", "Область", "Категория", "Профиль"
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

        self.ui.vyst_mo_table.setColumnHidden(10, True)

    def update_filter_input_field(self):
        selected_filter = self.ui.add_filters_cb.currentText()

        if selected_filter and selected_filter not in self.filter_fields:
            # Создаем новое поле для фильтрации
            new_filter_layout = self.create_filter_input(selected_filter)
            self.filter_fields[selected_filter] = new_filter_layout  # Сохраняем ссылку на поле

            # Перестроение сетки после добавления нового фильтра
            self.rebuild_filter_grid()

    def remove_filter(self, filter_name):
        if filter_name in self.filter_fields:
            # Удаляем фильтр
            layout_to_remove = self.filter_fields.pop(filter_name)

            # Удаляем его из интерфейса
            for i in reversed(range(layout_to_remove.count())):
                widget = layout_to_remove.itemAt(i).widget()
                if widget is not None:
                    widget.setParent(None)

            # Перестроение сетки после удаления
            self.rebuild_filter_grid()

    def rebuild_filter_grid(self):
        # Удаляем все элементы из сетки
        for i in reversed(range(self.filter_input_layout.count())):
            layout_item = self.filter_input_layout.itemAt(i)
            if layout_item is not None:
                widget = layout_item.widget()
                if widget is not None:
                    widget.setParent(None)
                else:
                    self.filter_input_layout.removeItem(layout_item)

        # Заново добавляем все элементы
        filters_per_row = 4  # Количество фильтров в строке
        for index, (filter_name, filter_layout) in enumerate(self.filter_fields.items()):
            row = index // filters_per_row
            col = index % filters_per_row
            self.filter_input_layout.addLayout(filter_layout, row, col)

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

        # Добавляем отступы для улучшения внешнего вида
        layout.setContentsMargins(5, 5, 5, 5)
        layout.setSpacing(10)

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

    def apply_filters(self):
        """Apply filters based on selected values in the ComboBox inputs."""
        filter_conditions = {}

        # Gather filter conditions from the filter fields
        for filter_key, filter_layout in self.filter_fields.items():
            combo_box = filter_layout.itemAt(1).widget()  # This is the QComboBox with editable input
            filter_value = combo_box.currentText()

            if filter_value:
                # Split values in case of multiple inputs (e.g., by commas)
                filter_values = [val.strip() for val in filter_value.split(',') if val.strip()]
                filter_conditions[filter_key] = filter_values

        # Apply filters to the current model and show rows accordingly
        self.filter_table(filter_conditions)

    def filter_table(self, filter_conditions):
        """Apply filters to the currently selected table."""
        rows_to_hide = set()

        for row in range(self.current_model.rowCount()):
            show_row = True  # Flag to determine if the row should be shown

            for filter_key, filter_values in filter_conditions.items():
                # Находим индекс столбца по его имени
                column_index = [self.current_model.headerData(i, Qt.Horizontal) for i in
                                range(self.current_model.columnCount())].index(filter_key)
                index = self.current_model.index(row, column_index)
                data_value = self.current_model.data(index)

                # Проверяем, является ли значение числом (целое или с плавающей запятой)
                if self.is_numeric_column(column_index):
                    # Если это числовое поле, то проверяем строгое совпадение
                    if str(data_value) not in filter_values:
                        show_row = False
                        break
                else:
                    # Если это строковое поле, то проверяем вхождение подстроки
                    if not any(str(data_value).lower().find(val.lower()) != -1 for val in filter_values):
                        show_row = False
                        break

            if not show_row:
                rows_to_hide.add(row)  # Mark row for hiding

        # Показ или скрытие строк на основе результатов фильтрации
        for row in range(self.current_model.rowCount()):
            if row in rows_to_hide:
                self.show_row_in_all_tables(row, False)  # Hide row in all tables
            else:
                self.show_row_in_all_tables(row, True)  # Show

    def is_numeric_column(self, column_index):
        """Проверяет, является ли столбец числовым."""
        # Проходим по нескольким строкам, чтобы проверить тип данных
        for row in range(min(5, self.current_model.rowCount())):  # Проверяем первые 5 строк
            index = self.current_model.index(row, column_index)
            value = self.current_model.data(index)
            # Пытаемся преобразовать значение в число
            if value is not None and value != "":
                try:
                    float(value)  # Если удается преобразовать, то это числовой столбец
                    return True
                except ValueError:
                    return False
        return False

    def show_all_rows(self):
        """Show all rows in the current table."""
        for row in range(self.current_model.rowCount()):
            self.show_row_in_all_tables(row, True)  # Show row in all tables

    def show_row_in_all_tables(self, row, visible):
        """Show or hide a row in all tables."""
        for table in [self.ui.vyst_mo_table, self.ui.vuz_table, self.ui.grntirub_table, self.ui.svod_table]:
            if visible:
                table.showRow(row)
            else:
                table.hideRow(row)

    def remove_filter_input(self, label_text, layout):
        """Удаляем поле ввода фильтра и сбрасываем фильтрацию только для этой колонки."""
        if label_text in self.filter_fields:
            for i in reversed(range(layout.count())):
                widget = layout.itemAt(i).widget()
                if widget:
                    widget.deleteLater()

            # Удаляем фильтр из словаря
            del self.filter_fields[label_text]
            self.filter_input_layout.removeItem(layout)  # Убираем layout из отображения
            self.apply_filters()
    def clear_all_filters(self):
        """Сбрасываем все фильтры и показываем все строки во всех таблицах."""
        # Показываем все строки во всех таблицах
        self.show_all_rows()

        # Очищаем словарь фильтров
        self.filter_fields.clear()

        # Очищаем макет с полями ввода фильтров корректно
        while self.filter_input_layout.count() > 0:
            child = self.filter_input_layout.takeAt(0)
            if child is not None:
                # Удаляем вложенный макет, если он существует
                layout = child.layout()
                if layout is not None:
                    while layout.count():
                        item = layout.takeAt(0)
                        widget = item.widget()
                        if widget:
                            widget.deleteLater()

                # Удаляем сам виджет или макет
                if child.widget():
                    child.widget().deleteLater()

        # Обновляем комбобокс фильтров
        self.update_filter_combobox()


    def create_model(self, table_name: str):
        model = NonEditableSqlTableModel(self)
        model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        model.setTable(table_name)
        model.select()
        return model

    def update_filter_combobox(self):
        """Updates the ComboBox with currently active filters."""
        self.ui.add_filters_cb.clear()
        if self.current_model:
            headers = [self.current_model.headerData(i, Qt.Horizontal) for i in range(self.current_model.columnCount())]
            # Exclude currently selected filters
            for filter_key in self.filter_fields.keys():
                headers.remove(filter_key)
            self.ui.add_filters_cb.addItems(headers)


    def set_custom_headers(self, model, headers):
        for index, header in enumerate(headers):
            model.setHeaderData(index, Qt.Horizontal, header)

    def set_current_table(self, checked_action):
        """Switches the current table and resets the filters."""
        # Очистка полей ввода фильтров при переключении таблиц
        self.clear_filter_input_fields()

        # Смена таблицы
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

        # Обновление комбобокса с доступными колонками для фильтрации
        self.update_filter_combobox()

        # Показываем все строки при переключении таблиц
        self.show_all_rows()

    def clear_filter_input_fields(self):
        """Clears all filter input fields when switching tables."""
        # Удаление всех полей ввода фильтров из макета
        while self.filter_input_layout.count() > 0:
            child = self.filter_input_layout.takeAt(0)
            if child is not None:
                # Удаляем вложенный макет, если он существует
                layout = child.layout()
                if layout is not None:
                    while layout.count():
                        item = layout.takeAt(0)
                        widget = item.widget()
                        if widget:
                            widget.deleteLater()

                # Удаляем сам виджет или макет
                if child.widget():
                    child.widget().deleteLater()

        # Очищаем словарь фильтров
        self.filter_fields.clear()


    def handle_header_click(self, table, logicalIndex):
        """Handles the header click to sort the table."""
        # Получаем имя таблицы для правильного отслеживания состояния
        table_name = table.objectName()

        # Получаем текущее состояние сортировки для выбранного столбца
        current_sort_order = self.sort_states[table_name].get(logicalIndex, None)

        # Устанавливаем модель, связанную с таблицей
        model = table.model()

        # Устанавливаем следующее состояние сортировки
        if current_sort_order is None:
            model.sort(logicalIndex, Qt.SortOrder.AscendingOrder)

            self.sort_states[table_name][logicalIndex] = Qt.SortOrder.AscendingOrder
        elif current_sort_order == Qt.SortOrder.AscendingOrder:
            model.sort(logicalIndex, Qt.SortOrder.DescendingOrder)

            self.sort_states[table_name][logicalIndex] = Qt.SortOrder.DescendingOrder
        else:
            model.setSort(-1, Qt.SortOrder.AscendingOrder)  # Сбрасываем сортировку
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

