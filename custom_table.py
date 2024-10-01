from typing import List

import PySide6
from PySide6 import QtCore
from PySide6.QtCore import Qt
from PySide6.QtSql import QSqlTableModel
from PySide6.QtWidgets import QTableView, QHeaderView

from main import Tables


class CustomModel(QSqlTableModel):

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return 'Column {}'.format(section + 1)
        return super().headerData(section, orientation, role)


    def __init__(self, sql_table_name, columns: List = None):
        super().__init__()
        self.setModel(self.create_model(sql_table_name))
        # Отключаем сортировку по заголовкам при первом выводе
        self.setSortingEnabled(False)
        self.setHeaderData(columns)
        self.horizontalHeader().sectionClicked.connect(self.handle_header_click)
        # Устанавливаем режим растягивания заголовков. Устанавливаем автоматическое изменение ширины столбцов
        self.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch, QHeaderView.ResizeMode.ResizeToContents
        )

    def flags(self, index):
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled

    def setHeaderData(self, columns):
        self.columns = columns
        return self



    # Настройка заголовков
    # self.set_custom_headers("vyst_mo_table", ["Код ВУЗа/организации", "Краткое название ВУЗа/организации",
    #                                           "Признак  формы НИР", "Регистрационный номер НИР",
    #                                           "Наименование проекта/НИР",
    #                                           "Коды  ГРНТИ", "Руководитель НИР",
    #                                           "Должность, ученое звание, ученая степень руководителя",
    #                                           "Признак", "Выставки", "Название выставочного экспоната"])
    #
    # self.set_custom_headers("vuz_table",
    #                         ["Код ВУЗа", "Название ВУЗа", "Полное наименование", "Сокращенное наименование",
    #                          "Федеральный округ", 'Город', "Статус", "Номер области", "Область", "Категория",
    #                          "Профиль"])
    #
    # self.set_custom_headers("grntirub_table", ["Код рубрики", "Наименование рубрики"])

    # Подключаем сортировку для каждой таблицы
    # self.ui.vyst_mo_table.horizontalHeader().sectionClicked.connect(self.handle_header_click)
    # self.ui.vuz_table.horizontalHeader().sectionClicked.connect(self.handle_header_click)
    # self.ui.grntirub_table.horizontalHeader().sectionClicked.connect(self.handle_header_click)

    # Устанавливаем режим растягивания заголовков
    # for table in [self.ui.vyst_mo_table, self.ui.vuz_table, self.ui.grntirub_table]:
    #     header = table.horizontalHeader()
    #     header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
    #     # Устанавливаем автоматическое изменение ширины столбцов
    #     header.setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)

    def create_model(self, table_name: str):
        model = self.NonEditableSqlTableModel(self)
        model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        model.setTable(table_name)
        model.select()
        return model

    # def set_custom_headers(self, table_name, headers):
    #     # model = self.models[table_name]
    #     for index, header in enumerate(headers):
    #         model.setHeaderData(index, Qt.Horizontal, header)


    # def handle_header_click(self, logicalIndex):
    #     # Получаем имя таблицы для правильного отслеживания состояния
    #     print(self)
    #     table_name = self.ui..objectName()
    #
    #     # Получаем текущее состояние сортировки для выбранного столбца
    #     current_sort_order = self.sort_states[table_name].get(logicalIndex, None)
    #
    #     # Устанавливаем модель, связанную с таблицей
    #     model = table.model()
    #
    #     # Устанавливаем следующее состояние сортировки
    #     if current_sort_order is None:
    #         model.sort(logicalIndex, Qt.AscendingOrder)
    #         self.sort_states[table_name][logicalIndex] = Qt.AscendingOrder
    #     elif current_sort_order == Qt.AscendingOrder:
    #         model.sort(logicalIndex, Qt.DescendingOrder)
    #         self.sort_states[table_name][logicalIndex] = Qt.DescendingOrder
    #     else:
    #         model.setSort(-1, Qt.AscendingOrder)  # Сбрасываем сортировку
    #         model.select()  # Перезагружаем данные в исходном порядке
    #         self.sort_states[table_name][logicalIndex] = None