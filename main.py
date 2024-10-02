import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QLineEdit, QPushButton, QScrollArea, QWidget

import PySide6.QtWidgets
from PySide6.QtCore import Qt, QAbstractItemModel
from PySide6.QtWidgets import QApplication, QMainWindow, QHeaderView, QTableView
from PySide6.QtSql import QSqlTableModel
from PySide6.QtCore import Qt
from connection import Data
from ui_main_side import Ui_MainWindow
from ui_vistavka_entry import Ui_add_zapis_dialog

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
            "grntirub_table": {},
            "svod_table": {}
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
        self.ui.tables_menu.triggered.connect(self.set_current_table)
        self.ui.create_btn.clicked.connect(self.open_create_entry_dialog)
        self.ui.delete_btn.clicked.connect(self.delete_record)
        # self.ui.grnti.triggered.connect(self.set_current_table)
        # self.ui.vistavki.triggered.connect(self.set_current_table)
        # self.ui.vuz_2.triggered.connect(self.set_current_table)
        # self.ui.tables_combobox.activated.connect(self.set_current_table)

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
        text = checked_action.text()
        if text == "ГРНТИ":
            self.ui.db_tables.setCurrentIndex(3)
        elif text == "Выставки":
            self.ui.db_tables.setCurrentIndex(1)
        elif text == "ВУЗы":
            self.ui.db_tables.setCurrentIndex(2)
        elif text == "Сводная таблица":
            self.ui.db_tables.setCurrentIndex(0)

        self.update_filter_combobox()

    def update_filter_combobox(self):
        self.ui.add_filters_cb.clear()
        if self.current_model:
            headers = [self.current_model.headerData(i, Qt.Horizontal) for i in range(self.current_model.columnCount())]
            self.ui.add_filters_cb.addItems(headers)

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
