import os
import sys
from datetime import datetime
from pathlib import Path

import pandas as pd
from PySide6.QtGui import QFontMetrics, QIntValidator, QRegularExpressionValidator, QFont, QStandardItemModel
from PySide6.QtWidgets import (QApplication, QMainWindow, QApplication, QComboBox, QPushButton,
                               QHBoxLayout, QLabel, QCompleter, QGridLayout, QAbstractItemView,
                               QMessageBox, QDialog, QLineEdit, QHeaderView, QTableView, QStyledItemDelegate)
from PySide6.QtCore import QSortFilterProxyModel, QItemSelectionModel, QTimer, QRegularExpression, Qt, QCoreApplication
from PySide6.QtSql import QSqlTableModel
from openpyxl.workbook import Workbook
from sqlalchemy import tuple_, and_, or_, text

from connection import Session, Data, engine
from create_db import create_db_and_tables
from py_ui.add_to_group_dialog import Ui_add_to_group_dialog
from searchable_cb import SearchableComboBox, FilterComboBox
from table_models import VuzBase, VystMoBase, GrntiBase, GroupListBase, SvodBase

from py_ui.ui_create_group import Ui_create_group_dialog
from py_ui.ui_create_vuz import Ui_create_vuz_dialog
from py_ui.ui_main_side import Ui_MainWindow
from py_ui.ui_vistavka_entry import Ui_add_zapis_dialog
from py_ui.ui_cancel_confirm import Ui_Dialog

class Regex:
    common_regex = QRegularExpression(r"^[a-zA-Zа-яА-ЯёЁ\s\.\;\"\']+$")
    num_regex = QRegularExpression(r"^\d+$")
    rus_regex = QRegularExpression(r"^[А-Яа-яЁё\s\.\;\"\']+$")
    upper_rus_regex = QRegularExpression(r"^[А-ЯЁ]+$")


# class SemicolonFormattingDelegate(QStyledItemDelegate):
#     def displayText(self, value, locale):
#         print(f"Formatting value: {value} (type: {type(value)})")
#         if value is None:
#             return ""
#         if isinstance(value, str):
#             return value.replace(";", "; ")
#         return str(value)

class SemicolonDelegate(QStyledItemDelegate):
    def displayText(self, value, locale):
        # Проверяем, что значение является строкой
        if isinstance(value, str):
            # Заменяем ";" на "; " (если "; " уже есть, ничего не изменится)
            return value.replace(";", "; ")
        return super().displayText(value, locale)


class ExponatDBMS(QMainWindow):

    def __init__(self):
        create_db_and_tables()
        super(ExponatDBMS, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connection = Data()
        self.current_model = None  # Текущая модель для фильтрации
        self.filter_fields = {}  # Словарь для хранения полей фильтрации для каждого столбца
        self.ui.add_filters_cb.currentIndexChanged.connect(self.update_filter_input_field)
        self.ui.delete_all_filters.clicked.connect(self.clear_all_filters)

        self.filter_input_layout = QGridLayout()  # Layout for the filter input field
        self.ui.toplevel_layout.addLayout(self.filter_input_layout)  # Добавляем его в главный макет

        # self.setup_group_cb() # TODO удалить это если не нужно

        self.init_tables()
        self.setFixedSize(1200, 751)

        self.ui.tables_menu.triggered.connect(self.set_current_table)
        self.ui.groups_menu.triggered.connect(self.open_group_list)

        # Хранение состояния сортировки для каждой таблицы
        self.sort_states = {
            "vyst_mo_table": {},
            "vuz_table": {},
            "grntirub_table": {},
            "svod_table": {}
        }

        self.vyst_mo_proxy_model = QSortFilterProxyModel(self)
        self.vuz_proxy_model = QSortFilterProxyModel(self)
        self.grntirub_proxy_model = QSortFilterProxyModel(self)
        self.svod_proxy_model = QSortFilterProxyModel(self)

        self.current_proxy_model = None  # Текущая прокси-модель для фильтрации

        self.ui.add_filters_cb.currentIndexChanged.connect(self.update_filter_input_field)
        self.init_tables()

        self.ui.delete_btn.clicked.connect(self.delete_button_action)

        # self.ui.db_tables.currentWidget().children()[1].setVerticalScrollMode(
        #     QAbstractItemView.ScrollMode.ScrollPerPixel)

        self.top_scroll_func()

        self.ui.pages_.setCurrentIndex(0)
        self.ui.groups_pages.setCurrentIndex(0)
        self.current_model = self.svod_table_model
        self.ui.current_table_label.setText("Сводная таблица")
        self.ui.create_btn.setEnabled(False)
        self.ui.update_btn.setEnabled(False)
        self.ui.add_to_group_btn.setEnabled(True)
        self.ui.delete_btn.setEnabled(False)
        self.clear_filter_input_fields()
        self.update_filter_combobox()
        self.show_all_rows()

        self.ui.create_group_btn.clicked.connect(self.open_create_group_dialog)
        self.ui.delete_group_btn.clicked.connect(self.delete_group_button_action)
        self.ui.add_to_group_btn.clicked.connect(self.open_add_to_group_dialog)
        self.ui.back_to_group_list_page_btn.clicked.connect(self.open_group_list)
        # self.ui.group_list_table.doubleClicked.connect(self.open_group_table)


    def create_report(self, group_name):
        print(group_name)
        print(type(group_name))
        # Получение данных из GroupList
        group_list_query = f"SELECT * FROM grouplist WHERE ui_table_name='{group_name}'"
        group_list_df = pd.read_sql(group_list_query, engine)
        print(group_list_df)
        print(group_list_df.columns)

        if group_list_df.empty:
            print("Группа не найдена.")
            return

        group_info = group_list_df.iloc[0]
        db_view_name = group_info['db_view_name']

        # Получение данных из view
        view_query = f"SELECT * FROM {db_view_name}"
        view_df = pd.read_sql(view_query, engine)

        reports_dir = "Отчеты"
        if not os.path.exists(reports_dir):
            os.makedirs(reports_dir)

        # Создание Excel файла
        # file_name = f"report_{group_name}.xlsx"
        base_file_name = f"Отчет_{group_name}.xlsx"
        file_name = os.path.join(reports_dir, base_file_name)
        i = 1

        # Проверка на существование файла и добавление числового суффикса
        while os.path.exists(file_name):
            file_name = os.path.join(reports_dir, f"Отчет_{group_name}({i}).xlsx")
            i += 1

        wb = Workbook()
        ws = wb.active
        ws.title = "Отчет"

        # Заполнение данных в нужном формате
        ws.append(["Дата:", datetime.now().strftime("%Y-%m-%d")])
        ws.append([])

        # Данные из GroupList в столбик
        ws.append(["Название группы:", group_info['ui_table_name']])
        ws.append(["Рубрики ГРНТИ:", group_info['unique_grnti']])
        ws.append(["Регионы:", group_info['unique_regions']])
        ws.append(["Количество выставок:", group_info['record_count']])
        ws.append([])

        # Заголовок для данных из view
        ws.append([
            "Код вуза", "Краткое название", "Тема",
            "Имя руководителя", "Город", "Статус экспоната"
        ])

        # Добавление данных из view
        for index, row in view_df.iterrows():
            ws.append([
                row['codvuz'], row['z2'], row['subject'],
                row['bossname'], row['city'], row['exhitype']
            ])

        # Добавление подписей в столбик
        ws.append([])
        ws.append(["Дата"])
        ws.append(["Подпись"])

        # Сохранение файла
        wb.save(file_name)
        print(f"Отчет сохранен как {file_name}")

        QMessageBox.information(self, "Успех", f"Отчет сохранен в {file_name[7:]}.")

    # def delete_group_button_action_2(self):
    #     current_table: QTableView = self.ui.group_list_table
    #     self.open_delete_group_confirm_dialog_2(message)
    #
    def open_delete_group_confirm_dialog_2(self, row):
        self.confirm_dialog = QDialog()
        self.ui_confirm_dialog = Ui_Dialog()
        self.ui_confirm_dialog.setupUi(self.confirm_dialog)
        self.ui_confirm_dialog.label.setText("Удалить текущую группу?")

    # Подключаем кнопку "OK" к функции delete_record
        self.ui_confirm_dialog.buttonBox.accepted.connect(lambda: self.delete_group_record_2(row))

    # Подключаем кнопку "Cancel" для закрытия диалога
        self.ui_confirm_dialog.buttonBox.rejected.connect(self.confirm_dialog.close)
        self.confirm_dialog.exec_()
        self.confirm_dialog.setModal(True)


    def delete_group_record_2(self, row):
        current_table = self.ui.group_list_table

        if isinstance(current_table, QTableView):
            model = current_table.model()
        #     selected_rows = current_table.selectionModel().selectedRows()

            model.removeRow(row)

        self.apply_filters()
        self.update_all_tables(model)
        self.ui.groups_pages.setCurrentWidget(self.ui.group_list_page)
        QMessageBox.information(self, "Успех", f"Группа удалена!") #{self.group_list_table_model.data(self.group_list_table_model.index(row, 0))}
        self.confirm_dialog.close()

    def open_group_view_page(self, index):
        row = index.row()

        # ui_view_name = self.group_list_table_model.data(self.group_list_table_model.index(row, 4))
        print(self.group_list_table_model.data(self.group_list_table_model.index(row, 0)))

        self.ui.export_btn.clicked.disconnect()
        self.ui.delete_group_btn_2.clicked.disconnect()
        self.ui.export_btn.clicked.connect(lambda: self.create_report(self.group_list_table_model.data(self.group_list_table_model.index(row, 0))))
        self.ui.delete_group_btn_2.clicked.connect(lambda: self.open_delete_group_confirm_dialog_2(row))



        self.ui.groups_pages.setCurrentWidget(self.ui.group_view_page)
        self.ui.group_name.setText(
            f"Группа '{self.group_list_table_model.data(self.group_list_table_model.index(row, 0))}'")
        if self.group_list_table_model.data(self.group_list_table_model.index(row, 5)): #false if str is null
            records_composite_keys = self.group_list_table_model.index(row, 5).data()
            view_name = self.group_list_table_model.index(row, 4).data()

            if not records_composite_keys or not view_name:
                return

            # Разделяем ключи и создаём представление
            composite_keys = records_composite_keys.split(";")
            self.create_view_from_composite_keys(view_name, composite_keys)
            print(f"View {view_name} создано с записями для ключей: {composite_keys}")

            model = self.create_model(view_name)
            self.ui.group_view_table.setModel(model)
            self.set_custom_headers(model, ["Код ВУЗа", "Сокращенное наименование ВУЗа",
                                                        "Наименование НИР", "Код  ГРНТИ", "Рубрика ГРНТИ", "Руководитель НИР",
                                                        "Регистрационный номер НИР", "Признак  формы НИР", "Должность",
                                                        "Ученое звание", "Ученая степень", "Признак",
                                                        "Выставки", "Выставочный экспонат", "Название ВУЗа",
                                                        "Полное наименование ВУЗа",
                                                        "Федеральный округ", 'Город', "Статус", "Номер области",
                                                        "Область", "Категория", "Профиль"
                                                        ])
            self.ui.group_view_table.horizontalHeader().sectionClicked.connect(
                lambda index: self.handle_header_click(self.ui.group_view_table, index)
            )
            header = self.ui.group_view_table.horizontalHeader()

            font_metrics = QFontMetrics(self.ui.group_view_table.font())

            header.setSectionResizeMode(QHeaderView.ResizeMode.Fixed)
            for col in range(header.count()):
                header_text = self.ui.group_view_table.model().headerData(col, Qt.Orientation.Horizontal)
                header_width = font_metrics.horizontalAdvance(header_text) + 20
                self.ui.group_view_table.setColumnWidth(col, header_width)
            header.setSectionResizeMode(QHeaderView.ResizeMode.Interactive)
            header.setStretchLastSection(False)
            self.ui.group_view_table.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)

    @staticmethod
    def create_view_from_composite_keys(view_name, composite_keys):
        """
        Создаёт представление в базе данных на основе составных ключей.

        :param view_name: Имя представления
        :param composite_keys: Список составных ключей в формате ["codvuz:regnumber", ...]
        """
        conditions = []
        for key in composite_keys:
            codvuz, regnumber = key.split(":")
            conditions.append(f"(codvuz = {codvuz} AND regnumber = '{regnumber}')")

        condition_query = " OR ".join(conditions)
        create_view_query = f"""
            CREATE VIEW {view_name} AS
            SELECT *
            FROM svod
            WHERE {condition_query};
        """
        Data.close_connection()
        with engine.connect() as connection:
            connection.execute(text(f"DROP VIEW IF EXISTS {view_name}"))  # Удаляем старое представление, если оно есть
            connection.execute(text(create_view_query))
        Data.create_connection()

    def open_add_to_group_dialog(self):
        selected_ids = self.get_selected_rows(self.ui.svod_table)

        if not selected_ids:
            QMessageBox.warning(self, "Предупреждение", "Выберите хотя бы одну строку для добавления.")
            return

        self.add_to_group_dialog = QDialog()
        self.ui_add_to_group_dialog = Ui_add_to_group_dialog()
        self.ui_add_to_group_dialog.setupUi(self.add_to_group_dialog)
        self.ui_add_to_group_dialog.create_new_group_btn.clicked.connect(self.open_create_group_dialog)
        self.ui_add_to_group_dialog.buttonBox.accepted.connect(self.create_group_list_record)
        self.setup_group_cb()


        self.add_to_group_dialog.setFixedSize(401, 249)
        self.add_to_group_dialog.setModal(True)
        self.add_to_group_dialog.show()


    @staticmethod
    def get_selected_rows(table: QTableView):
        selection_model = table.selectionModel()
        if not selection_model.hasSelection():
            return []

        selected_indexes = selection_model.selectedRows()
        selected_keys = []
        for index in selected_indexes:
            codvuz = index.sibling(index.row(), 0).data()
            regnumber = index.sibling(index.row(), 6).data()
            if codvuz is not None and regnumber is not None:
                selected_keys.append((codvuz, regnumber))
        return selected_keys

    def create_group_list_record(self):
        selected_keys = self.get_selected_rows(self.ui.svod_table)
        current_ui_table_name = self.ui_add_to_group_dialog.groups_list_cb.currentText()
        print(current_ui_table_name)
        try:
            Data.close_connection()
            with Session() as session:
                conditions = [and_(SvodBase.codvuz == key[0], SvodBase.regnumber == key[1]) for key in selected_keys]

                # Получение выбранных записей из таблицы Svod
                selected_records = session.query(SvodBase).filter(or_(*conditions)).all()
            Data.create_connection()

            unique_regions = ";".join(sorted(set(record.region for record in selected_records if record.region)))

            # Уникальные GRNTI
            grnti_values = set()
            for record in selected_records:
                if record.grnti:
                    grnti_values.update(record.grnti.split(';'))
            unique_grnti = ";".join(sorted(grnti_values))

            # Количество записей
            record_count = len(selected_records)

            # Композитные ключи
            records_composite_keys = ";".join(f"{record.codvuz}:{record.regnumber}" for record in selected_records if
                                              record.codvuz and record.regnumber)

            Data.close_connection()
            with Session() as session:
                group_record = session.query(GroupListBase).filter_by(ui_table_name=current_ui_table_name).first()
                group_record.unique_regions = unique_regions
                group_record.unique_grnti = unique_grnti
                group_record.record_count = record_count
                group_record.records_composite_keys = records_composite_keys

                session.commit()
            Data.create_connection()
            if not self.group_list_table_model.submitAll():
                print("Ошибка добавления записи:", self.group_list_table_model.lastError().text())
            if self.group_list_table_model.select():
                print("kaef")
            self.apply_filters()
            self.top_scroll_func()

            QMessageBox.information(self, "Успех", "Данные успешно добавлены в список Групп.")


        except Exception as e:
            Data.close_connection()
            with Session() as session:
                session.rollback()
            Data.create_connection()
            QMessageBox.critical(self, "Ошибка", f"Произошла ошибка: {str(e)}")



    def setup_group_cb(self):
        font = QFont()
        font.setPointSize(11)

        self.ui_add_to_group_dialog.groups_list_cb = FilterComboBox(self.ui_add_to_group_dialog.widget)
        self.ui_add_to_group_dialog.groups_list_cb.setObjectName(u"groups_list_cb")
        self.ui_add_to_group_dialog.groups_list_cb.setFont(font)

        self.ui_add_to_group_dialog.verticalLayout.addWidget(self.ui_add_to_group_dialog.groups_list_cb)


    def top_scroll_func(self):
        self.ui.db_tables.currentWidget().children()[1].setVerticalScrollMode(
            QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.ui.db_tables.currentWidget().children()[1].scrollToBottom()
        self.ui.db_tables.currentWidget().children()[1].scrollToTop()

    def open_create_group_dialog(self):
        self.create_group_dialog = QDialog()
        self.ui_create_group_dialog = Ui_create_group_dialog()
        self.ui_create_group_dialog.setupUi(self.create_group_dialog)
        self.ui_create_group_dialog.save_btn.clicked.connect(self.create_group)

        # self.set_validation(Regex.common_regex, self.ui_create_group_dialog.group_name)

        self.create_group_dialog.setFixedSize(310, 209)
        self.create_group_dialog.setModal(True)
        self.create_group_dialog.show()

    def create_group(self):
        Data.close_connection()
        with Session() as session:
        # Извлекаем все записи из таблицы Vuz
            table_name_rec = session.query(GroupListBase.ui_table_name).all()
        Data.create_connection()

        ui_table_names = [row[0] for row in table_name_rec]

        name = self.ui_create_group_dialog.group_name.text()

        if name in ui_table_names:
            self.ui_create_group_dialog.error_text.setText("группа с таким именем уже существует")
            # QMessageBox.warning(self, "Ошибка", "Группа с таким именем уже существует.")
        else:
            Data.close_connection()
            new_group = GroupListBase(
                ui_table_name=name
            )
            with Session() as session:
                try:
                    session.add(new_group)
                except:
                    session.rollback()
                    raise
                else:
                    session.commit()

            ui_table_name = session.query(GroupListBase.ui_table_name).where(GroupListBase.ui_table_name==name).scalar()
            print(ui_table_name)
            print("ui_table_name:", ui_table_name, type(ui_table_name))

            Data.create_connection()


            if not self.group_list_table_model.submitAll():
                print("Ошибка добавления записи:", self.group_list_table_model.lastError().text())
            if self.group_list_table_model.select():
                print("kaef")
            self.apply_filters()

            if hasattr(self, "ui_add_to_group_dialog"):
                self.ui_add_to_group_dialog.groups_list_cb.clear()
                self.ui_add_to_group_dialog.groups_list_cb.add_items()
            self.create_group_dialog.close()


    #######################################__ДОБАВЛЕНИЕ ЗАПИСИ__###########################################################
    def validate_entry_fields(self):
        # Retrieve the input values
        vuz = self.ui_create_vyst_dialog.vuz.currentText()
        grnti = self.ui_create_vyst_dialog.grnti.text()
        nir_ruk = self.ui_create_vyst_dialog.nir_ruk.text()
        nir_name = self.ui_create_vyst_dialog.nir_name.text()
        reg_number = self.ui_create_vyst_dialog.reg_number.text()

        Data.close_connection()
        with Session() as session:
        # Извлекаем все записи из таблицы Vuz
            vuz_records = session.query(VuzBase.z1).all()
        Data.create_connection()
        vuz_names_list = [row[0] for row in vuz_records]

        # Initialize a flag to track if any errors are found
        error_found = False

        # Validate codvuz by checking if it exists in the list of valid names
        valid_vuz_names = vuz_names_list
        if vuz not in valid_vuz_names:
            self.ui_create_vyst_dialog.vuz_error.setText("Несуществующее название")
            self.ui_create_vyst_dialog.vuz_error.setStyleSheet("color: red;")
            error_found = True
        else:
            self.ui_create_vyst_dialog.vuz_error.setText("")

        # Validate grnti to ensure it contains only digits
        if not grnti.isdigit():
            self.ui_create_vyst_dialog.grnti_error.setText("Неверный код")
            self.ui_create_vyst_dialog.grnti_error.setStyleSheet("color: red;")
            error_found = True
        else:
            self.ui_create_vyst_dialog.grnti_error.setText("")

        if not reg_number:
            self.ui_create_vyst_dialog.reg_number_error.setText("Заполните поле!")
            self.ui_create_vyst_dialog.reg_number_error.setStyleSheet("color: red;")
            error_found = True
        else:
            self.ui_create_vyst_dialog.reg_number_error.setText("")

        # Check if other required fields are filled
        if not nir_ruk:
            self.ui_create_vyst_dialog.bossname_error.setText("Заполните поле!")
            self.ui_create_vyst_dialog.bossname_error.setStyleSheet("color: red;")
            error_found = True
        else:
            self.ui_create_vyst_dialog.bossname_error.setText("")

        if not nir_name:
            self.ui_create_vyst_dialog.nir_error.setText("Заполните поле!")
            self.ui_create_vyst_dialog.nir_error.setStyleSheet("color: red;")
            error_found = True
        else:
            self.ui_create_vyst_dialog.nir_error.setText("")

        # Return True if any errors are found, otherwise False
        return error_found

    def validate_vuz_fields(self):
        # Retrieve the input values
        vuz_short_name = self.ui_create_vuz_dialog.vuz_short_name.text()
        vuz_name = self.ui_create_vuz_dialog.vuz_name.text()
        vuz_full_name = self.ui_create_vuz_dialog.vuz_full_name.text()
        city = self.ui_create_vuz_dialog.city.text()
        vuz_status = self.ui_create_vuz_dialog.vuz_status.text()
        federal_region = self.ui_create_vuz_dialog.federal_region_cb.currentText()
        federal_subject = self.ui_create_vuz_dialog.federal_subject_cb.currentText()
        federal_subject_code = self.ui_create_vuz_dialog.federal_subject_code_cb.currentText()

        Data.close_connection()
        with Session() as session:
        # Извлекаем все записи из таблицы Vuz
            vuz_records = session.query(VuzBase.z2).all()
        Data.create_connection()
        vuz_names_list = [row[0] for row in vuz_records]
        print(vuz_names_list)
        # Initialize a flag to track if any errors are found
        error_found = False

        # Validate codvuz by checking if it exists in the list of valid names
        valid_vuz_names = vuz_names_list

        if not vuz_short_name:
            self.ui_create_vuz_dialog.vuz_short_name_err.setText("Заполните поле!")
            self.ui_create_vuz_dialog.vuz_short_name_err.setStyleSheet("color: red;")
            error_found = True
        else:
            if vuz_short_name in valid_vuz_names:
                self.ui_create_vuz_dialog.vuz_short_name_err.setText("Такой ВУЗ уже существует")
                self.ui_create_vuz_dialog.vuz_short_name_err.setStyleSheet("color: red;")
                error_found = True
            else:
                self.ui_create_vuz_dialog.vuz_short_name_err.setText("")

        # Validate grnti to ensure it contains only digits
        # if not grnti.isdigit():
        #     self.ui_create_vyst_dialog.grnti_error.setText("Неверный код")
        #     self.ui_create_vyst_dialog.grnti_error.setStyleSheet("color: red;")
        #     error_found = True
        # else:
        #     self.ui_create_vyst_dialog.grnti_error.setText("")

        # if not vuz_short_name:
        #     self.ui_create_vuz_dialog.vuz_short_name_err.setText("Заполните поле!")
        #     self.ui_create_vuz_dialog.vuz_short_name_err.setStyleSheet("color: red;")
        #     error_found = True
        # else:
        #     self.ui_create_vuz_dialog.vuz_short_name_err.setText("")

        # Check if other required fields are filled
        if not vuz_name:
            self.ui_create_vuz_dialog.vuz_name_err.setText("Заполните поле!")
            self.ui_create_vuz_dialog.vuz_name_err.setStyleSheet("color: red;")
            error_found = True
        else:
            self.ui_create_vuz_dialog.vuz_name_err.setText("")

        if not vuz_full_name:
            self.ui_create_vuz_dialog.vuz_full_name_err.setText("Заполните поле!")
            self.ui_create_vuz_dialog.vuz_full_name_err.setStyleSheet("color: red;")
            error_found = True
        else:
            self.ui_create_vuz_dialog.vuz_full_name_err.setText("")

        if not federal_region:
            self.ui_create_vuz_dialog.federal_region_err.setText("Заполните поле!")
            self.ui_create_vuz_dialog.federal_region_err.setStyleSheet("color: red;")
            error_found = True
        else:
            self.ui_create_vuz_dialog.federal_region_err.setText("")

        if not city:
            self.ui_create_vuz_dialog.city_err.setText("Заполните поле!")
            self.ui_create_vuz_dialog.city_err.setStyleSheet("color: red;")
            error_found = True
        else:
            self.ui_create_vuz_dialog.city_err.setText("")

        if not federal_subject:
            self.ui_create_vuz_dialog.federal_subject_err.setText("Заполните поле!")
            self.ui_create_vuz_dialog.federal_subject_err.setStyleSheet("color: red;")
            error_found = True
        else:
            self.ui_create_vuz_dialog.federal_subject_err.setText("")

        if not federal_subject_code:
            self.ui_create_vuz_dialog.federal_subject_code_err.setText("Заполните поле!")
            self.ui_create_vuz_dialog.federal_subject_code_err.setStyleSheet("color: red;")
            error_found = True
        else:
            self.ui_create_vuz_dialog.federal_subject_code_err.setText("")

        if not vuz_status:
            self.ui_create_vuz_dialog.vuz_status_err.setText("Заполните поле!")
            self.ui_create_vuz_dialog.vuz_status_err.setStyleSheet("color: red;")
            error_found = True
        else:
            self.ui_create_vuz_dialog.vuz_status_err.setText("")

        # Return True if any errors are found, otherwise False
        return error_found

    def open_create_vyst_dialog(self):
        self.new_dialog = QDialog()
        self.ui_create_vyst_dialog = Ui_add_zapis_dialog()
        self.ui_create_vyst_dialog.setupUi(self.new_dialog)
        self.ui_create_vyst_dialog.save_btn.clicked.connect(self.create_vyst_entry)

        self.ui_create_vyst_dialog.vuz.currentIndexChanged.connect(self.sync_codvuz_combo)
        self.ui_create_vyst_dialog.codvuz.currentIndexChanged.connect(self.sync_vuz_combo)

        self.ui_create_vyst_dialog.vuz.setEditable(True)
        self.ui_create_vyst_dialog.codvuz.setEditable(True)
        self.ui_create_vyst_dialog.grnti.setValidator(QIntValidator(0, 99999999))
        self.ui_create_vyst_dialog.grnti.textChanged.connect(self.validate_grnti_prefix)

        self.ui_create_vyst_dialog.grnti.textChanged.connect(self.auto_insert_dots)
        # Разрешаем только буквы и пробелы
        self.set_validation(Regex.rus_regex, self.ui_create_vyst_dialog.nir_ruk)
        self.set_validation(Regex.rus_regex, self.ui_create_vyst_dialog.ruk_doljnost)
        self.set_validation(Regex.rus_regex, self.ui_create_vyst_dialog.ruk_zvanie)
        self.set_validation(Regex.rus_regex, self.ui_create_vyst_dialog.ruk_stepen)
        self.set_validation(Regex.num_regex, self.ui_create_vyst_dialog.grnti)
        # self.set_validation(Regex.num_regex, self.ui_create_vyst_dialog.codvuz)
        # self.set_validation(Regex.rus_regex, self.ui_create_vyst_dialog.vuz)
        # self.set_validation(Regex.num_regex, self.ui_create_vyst_dialog.reg_number)
        # self.set_validation(Regex.common_regex, self.ui_create_vyst_dialog.vistavka)
        # self.set_validation(Regex.common_regex, self.ui_create_vyst_dialog.exponat_name)

        Data.close_connection()
        with Session() as session:
        # Извлекаем все записи из таблицы Vuz
            vuz_records = session.query(VuzBase).all()
        Data.create_connection()
        # Заполняем оба ComboBox
        for vuz in vuz_records:
            self.ui_create_vyst_dialog.vuz.addItem(vuz.z1, str(vuz.codvuz))
            self.ui_create_vyst_dialog.codvuz.addItem(str(vuz.codvuz), vuz.z1)

        # Заполняем ComboBox значениями
        vuz_list = [vuz.z1 for vuz in vuz_records]
        codvuz_list = [str(vuz.codvuz) for vuz in vuz_records]

        # Настройка комплитеров после заполнения ComboBox
        vuz_completer = QCompleter(vuz_list, self.ui_create_vyst_dialog.vuz)
        codvuz_completer = QCompleter(codvuz_list, self.ui_create_vyst_dialog.codvuz)

        vuz_completer.setCompletionMode(QCompleter.CompletionMode.PopupCompletion)
        codvuz_completer.setCompletionMode(QCompleter.CompletionMode.PopupCompletion)

        self.ui_create_vyst_dialog.vuz.setCompleter(vuz_completer)
        self.ui_create_vyst_dialog.codvuz.setCompleter(codvuz_completer)

        # Ограничиваем ввод только существующими значениями
        self.ui_create_vyst_dialog.vuz.lineEdit().editingFinished.connect(
            lambda elem=self.ui_create_vyst_dialog.vuz: self.validate_cb_input(elem)
        )
        self.ui_create_vyst_dialog.codvuz.lineEdit().editingFinished.connect(
            lambda elem=self.ui_create_vyst_dialog.codvuz: self.validate_cb_input(elem)
        )

        self.new_dialog.setFixedSize(561, 689)
        self.new_dialog.setModal(True)
        self.new_dialog.show()

    def validate_grnti_prefix(self, text):
        # Проверка длины текста и завершение проверки, если недостаточно символов
        if len(text) < 2:
            return

        # Извлекаем первые две цифры
        prefix = text[:2]

        # Проверяем наличие префикса в базе данных
        Data.close_connection()
        with Session() as session:
            exists = session.query(GrntiBase).filter_by(codrub=int(prefix)).first() is not None
        Data.create_connection()

        if not exists:
            # Если префикс отсутствует в базе данных, запрещаем дальнейший ввод
            self.ui_create_vyst_dialog.grnti.blockSignals(True)
            self.ui_create_vyst_dialog.grnti.setText(prefix)
            self.ui_create_vyst_dialog.grnti.blockSignals(False)

    # def validate_vuz_input(self):
    #     input_text = self.ui_create_vyst_dialog.vuz.currentText()
    #     if self.ui_create_vyst_dialog.vuz.findText(input_text) == -1:
    #         # Если введенное значение не найдено, сбрасываем поле
    #         self.ui_create_vyst_dialog.vuz.setCurrentIndex(-1)
    #
    # def validate_codvuz_input(self):
    #     input_text = self.ui_create_vyst_dialog.codvuz.currentText()
    #     if self.ui_create_vyst_dialog.codvuz.findText(input_text) == -1:
    #         # Если введенное значение не найдено, сбрасываем поле
    #         self.ui_create_vyst_dialog.codvuz.setCurrentIndex(-1)

    @staticmethod
    def validate_cb_input(element: QComboBox):
        input_text = element.currentText()
        # if element.findText(input_text) == -1:
        #     element.setCurrentIndex(-1)

    def setup_grnti_input(self):
        # Подключаем обработчик textChanged для жёсткой фильтрации текста
        self.ui_create_vyst_dialog.grnti.textChanged.connect(self.filter_grnti_input)

    def filter_grnti_input(self):
        text = self.ui_create_vyst_dialog.grnti.text()

        # Разрешаем только цифры, точки, точки с запятой и пробелы
        allowed_text = ''.join([ch for ch in text if ch.isdigit() or ch in ['.', ';', ' ']])

        # Проверяем, если текст был изменён (это значит, что были удалены недопустимые символы)
        if text != allowed_text:
            # Устанавливаем курсор на последнюю позицию, чтобы не сбивать пользователя
            cursor_position = self.ui_create_vyst_dialog.grnti.cursorPosition()
            self.ui_create_vyst_dialog.grnti.setText(allowed_text)
            self.ui_create_vyst_dialog.grnti.setCursorPosition(min(cursor_position, len(allowed_text)))

        # Применяем автоформатирование для структуры "xx.xx.xx"
        self.auto_insert_dots()

    def auto_insert_dots(self):
        text = self.ui_create_vyst_dialog.grnti.text()
        segments = text.split(";")  # Разделяем на отдельные коды по ";"
        formatted_segments = []

        for segment in segments:
            # Очищаем сегмент от всех точек и пробелов перед форматированием
            clean_segment = segment.replace(".", "").replace(" ", "")
            formatted_text = ""

            # Форматируем текст как "xx.xx.xx"
            for i in range(len(clean_segment)):
                if i > 0 and i % 2 == 0:
                    formatted_text += "."
                formatted_text += clean_segment[i]

            # Ограничиваем длину сегмента до 8 символов
            if len(formatted_text) > 8:
                formatted_text = formatted_text[:8]

            formatted_segments.append(formatted_text)

        # Объединяем отформатированные сегменты, разделённые "; "
        final_text = "; ".join(formatted_segments)

        # Обновляем текст в поле и устанавливаем курсор в конец
        self.ui_create_vyst_dialog.grnti.blockSignals(True)
        self.ui_create_vyst_dialog.grnti.setText(final_text)
        self.ui_create_vyst_dialog.grnti.blockSignals(False)
        self.ui_create_vyst_dialog.grnti.setCursorPosition(len(final_text))

    def sync_codvuz_combo(self):
        # Получаем codvuz, связанный с текущим vuzname
        selected_codvuz = self.ui_create_vyst_dialog.vuz.currentData()
        # Находим и устанавливаем соответствующий элемент в codvuz_combo
        if selected_codvuz is not None:
            index = self.ui_create_vyst_dialog.codvuz.findText(selected_codvuz)
            if index != -1:
                self.ui_create_vyst_dialog.codvuz.blockSignals(True)
                self.ui_create_vyst_dialog.codvuz.setCurrentIndex(index)
                self.ui_create_vyst_dialog.codvuz.blockSignals(False)

    def sync_vuz_combo(self):
        # Получаем vuzname, связанный с текущим codvuz
        selected_vuzname = self.ui_create_vyst_dialog.codvuz.currentData()
        # Находим и устанавливаем соответствующий элемент в vuzname_combo
        if selected_vuzname is not None:
            index = self.ui_create_vyst_dialog.vuz.findText(selected_vuzname)
            if index != -1:
                self.ui_create_vyst_dialog.vuz.blockSignals(True)
                self.ui_create_vyst_dialog.vuz.setCurrentIndex(index)
                self.ui_create_vyst_dialog.vuz.blockSignals(False)

    def update_button_action(self, func):
        current_widget = self.ui.db_tables.currentWidget()  # Получаем текущий виджет
        if current_widget is not None:  # Проверяем, что текущий виджет существует
            current_table: QTableView = current_widget.children()[1]  # Получаем второй дочерний элемент
            model = current_table.selectionModel().model()
            if isinstance(current_table, QTableView):
                selected_row = current_table.selectionModel().currentIndex().row()

                if selected_row >= 0:  # Проверяем, что строка выделена
                    func(model, selected_row)  # Передаем номер строки
                else:
                    QMessageBox.warning(self, "Ошибка", "Выберите строку в таблице.")
            else:
                QMessageBox.warning(self, "Ошибка", "Текущий виджет не является таблицей.")
        else:
            QMessageBox.warning(self, "Ошибка", "Нет активного виджета.")

    def open_update_vyst_dialog(self, model, selected_row):
        self.new_dialog = QDialog()
        self.ui_create_vyst_dialog = Ui_add_zapis_dialog()
        self.ui_create_vyst_dialog.setupUi(self.new_dialog)
        self.ui_create_vyst_dialog.save_btn.clicked.connect(self.update_vyst_entry)
        self.ui_create_vyst_dialog.dialog_label.setText("Редактирование записи выставки")


        self.ui_create_vyst_dialog.vuz.currentIndexChanged.connect(self.sync_codvuz_combo)
        self.ui_create_vyst_dialog.codvuz.currentIndexChanged.connect(self.sync_vuz_combo)

        self.ui_create_vyst_dialog.vuz.setEditable(True)
        self.ui_create_vyst_dialog.codvuz.setEditable(True)
        self.ui_create_vyst_dialog.grnti.setValidator(QIntValidator(0, 99999999))
        self.ui_create_vyst_dialog.grnti.textChanged.connect(self.validate_grnti_prefix)

        self.ui_create_vyst_dialog.grnti.textChanged.connect(self.auto_insert_dots)

        self.set_validation(Regex.common_regex, self.ui_create_vyst_dialog.nir_ruk)
        self.set_validation(Regex.common_regex, self.ui_create_vyst_dialog.ruk_doljnost)
        self.set_validation(Regex.common_regex, self.ui_create_vyst_dialog.ruk_zvanie)
        self.set_validation(Regex.common_regex, self.ui_create_vyst_dialog.ruk_stepen)

        self.ui_create_vyst_dialog.nir_name.textChanged.connect(
            lambda: self.add_tooltip(self.ui_create_vyst_dialog.nir_name)
        )
        self.ui_create_vyst_dialog.nir_name.editingFinished.connect(
            lambda: self.ui_create_vyst_dialog.nir_name.setCursorPosition(0)
        )

        self.ui_create_vyst_dialog.vistavka.textChanged.connect(
            lambda: self.add_tooltip(self.ui_create_vyst_dialog.vistavka)
        )
        self.ui_create_vyst_dialog.vistavka.editingFinished.connect(
            lambda: self.ui_create_vyst_dialog.vistavka.setCursorPosition(0)
        )

        self.ui_create_vyst_dialog.exponat_name.textChanged.connect(
            lambda : self.add_tooltip(self.ui_create_vyst_dialog.exponat_name)
        )

        self.ui_create_vyst_dialog.exponat_name.editingFinished.connect(
            lambda: self.ui_create_vyst_dialog.exponat_name.setCursorPosition(0)
        )

        Data.close_connection()
        with Session() as session:
        # Извлекаем все записи из таблицы Vuz
            vuz_records = session.query(VuzBase).all()
        Data.create_connection()
        # Заполняем оба ComboBox
        for vuz in vuz_records:
            self.ui_create_vyst_dialog.vuz.addItem(vuz.z1, str(vuz.codvuz))
            self.ui_create_vyst_dialog.codvuz.addItem(str(vuz.codvuz), vuz.z1)

        row_data = self.get_selected_row_data(model, selected_row)
        exp_est = {
            "Е": "Есть",
            "П": "Планируется",
            "Н": "Нет"
        }
        prizn = {
            "Е": "Тематический план",
            "М": "НТП"
        }

        self.ui_create_vyst_dialog.codvuz.setCurrentText(str(row_data[1]))
        self.ui_create_vyst_dialog.priznak.setCurrentText(prizn[row_data[2]])
        self.ui_create_vyst_dialog.reg_number.setText(row_data[3])
        self.ui_create_vyst_dialog.nir_name.setText(row_data[4])
        self.ui_create_vyst_dialog.grnti.setText(row_data[5])
        self.ui_create_vyst_dialog.nir_ruk.setText(row_data[6])
        self.ui_create_vyst_dialog.ruk_doljnost.setText(row_data[7])
        self.ui_create_vyst_dialog.ruk_zvanie.setText(row_data[8])
        self.ui_create_vyst_dialog.ruk_stepen.setText(row_data[9])
        self.ui_create_vyst_dialog.exponat_est.setCurrentText(exp_est[row_data[10]])
        self.ui_create_vyst_dialog.vistavka.setText(row_data[11])
        self.ui_create_vyst_dialog.exponat_name.setText(row_data[12])

        self.ui_create_vyst_dialog.nir_name.setCursorPosition(0)
        self.ui_create_vyst_dialog.vistavka.setCursorPosition(0)
        self.ui_create_vyst_dialog.exponat_name.setCursorPosition(0)


        # Заполняем ComboBox значениями
        vuz_list = [vuz.z1 for vuz in vuz_records]
        codvuz_list = [str(vuz.codvuz) for vuz in vuz_records]

        # Настройка комплитеров после заполнения ComboBox
        vuz_completer = QCompleter(vuz_list, self.ui_create_vyst_dialog.vuz)
        codvuz_completer = QCompleter(codvuz_list, self.ui_create_vyst_dialog.codvuz)

        vuz_completer.setCompletionMode(QCompleter.CompletionMode.PopupCompletion)
        codvuz_completer.setCompletionMode(QCompleter.CompletionMode.PopupCompletion)

        self.ui_create_vyst_dialog.vuz.setCompleter(vuz_completer)
        self.ui_create_vyst_dialog.codvuz.setCompleter(codvuz_completer)

        # Ограничиваем ввод только существующими значениями
        self.ui_create_vyst_dialog.vuz.lineEdit().editingFinished.connect(
            lambda elem=self.ui_create_vyst_dialog.vuz: self.validate_cb_input(elem)
        )
        self.ui_create_vyst_dialog.codvuz.lineEdit().editingFinished.connect(
            lambda elem=self.ui_create_vyst_dialog.codvuz: self.validate_cb_input(elem)
        )

        Data.close_connection()
        current_obj = VystMoBase.get_by_name_2(row_data[1], row_data[3])
        Data.create_connection()
        # print(row_data[1], row_data[3])
        # print(current_obj)

        self.ui_create_vyst_dialog.save_btn.clicked.connect(self.update_vyst_entry)
        self.current_obj = current_obj
        self.new_dialog.setFixedSize(561, 689)
        self.new_dialog.setModal(True)
        self.new_dialog.show()

    @staticmethod
    def get_selected_row_data(model, selected_row):
        if selected_row is not None:
            # Получаем данные из всех столбцов выбранной строки
            record = model.record(selected_row)
            row_data = [record.value(i) for i in range(model.columnCount())]
            print("Данные выбранной строки:", row_data)
            return row_data
        else:
            print("Строка не выбрана")
            return []

    def update_vyst_entry(self):
        if self.validate_entry_fields():
            return

        current_obj = self.current_obj
        exp_est = {
            "Есть": "Е",
            "Планируется": "П",
            "Нет": "Н"
        }
        prizn = {
            "Тематический план": "Е",
            "НТП": "М"
        }
        codvuz = self.ui_create_vyst_dialog.codvuz.currentText()
        priznak = prizn[self.ui_create_vyst_dialog.priznak.currentText()]
        reg_number = self.ui_create_vyst_dialog.reg_number.text()
        nir_name = self.ui_create_vyst_dialog.nir_name.text()
        grnti = self.ui_create_vyst_dialog.grnti.text()
        nir_ruk = self.ui_create_vyst_dialog.nir_ruk.text()
        ruk_doljnost = self.ui_create_vyst_dialog.ruk_doljnost.text()
        ruk_zvanie = self.ui_create_vyst_dialog.ruk_zvanie.text()
        ruk_stepen = self.ui_create_vyst_dialog.ruk_stepen.text()
        exponat_est = exp_est[self.ui_create_vyst_dialog.exponat_est.currentText()]
        vistavka = self.ui_create_vyst_dialog.vistavka.text()
        exponat_name = self.ui_create_vyst_dialog.exponat_name.text()

        Data.close_connection()

        with Session() as session:
            try:
                current_obj.codvuz = codvuz
                current_obj.type = priznak
                current_obj.regnumber = reg_number
                current_obj.subject = nir_name
                current_obj.grnti = grnti
                current_obj.bossname = nir_ruk
                current_obj.boss_position = ruk_doljnost
                current_obj.boss_academic_rank = ruk_zvanie
                current_obj.boss_scientific_degree = ruk_stepen
                current_obj.exhitype = exponat_est
                current_obj.vystavki = vistavka
                current_obj.exponat = exponat_name
                session.merge(current_obj)
            except:
                session.rollback()
                raise
            else:
                session.commit()
        Data.create_connection()

        if not self.vyst_mo_table_model.submitAll():
            print("Ошибка добавления записи:", self.vyst_mo_table_model.lastError().text())
        if self.vyst_mo_table_model.select():
            print("kaef")

        if not self.svod_table_model.submitAll():
            print("Ошибка добавления записи:", self.svod_table_model.lastError().text())
        if self.svod_table_model.select():
            print("kaef")

        self.apply_filters()
        self.new_dialog.close()

    def create_vyst_entry(self):
        if self.validate_entry_fields():
            return

        exp_est = {
            "Есть": "Е",
            "Планируется": "П",
            "Нет": "Н"
        }
        prizn = {
            "Тематический план": "Е",
            "НТП": "М"
        }
        codvuz = self.ui_create_vyst_dialog.codvuz.currentText()
        priznak = prizn[self.ui_create_vyst_dialog.priznak.currentText()]
        reg_number = self.ui_create_vyst_dialog.reg_number.text()
        nir_name = self.ui_create_vyst_dialog.nir_name.text()
        grnti = self.ui_create_vyst_dialog.grnti.text()
        nir_ruk = self.ui_create_vyst_dialog.nir_ruk.text()
        ruk_doljnost = self.ui_create_vyst_dialog.ruk_doljnost.text()
        ruk_zvanie = self.ui_create_vyst_dialog.ruk_zvanie.text()
        ruk_stepen = self.ui_create_vyst_dialog.ruk_stepen.text()
        exponat_est = exp_est[self.ui_create_vyst_dialog.exponat_est.currentText()]
        vistavka = self.ui_create_vyst_dialog.vistavka.text()
        exponat_name = self.ui_create_vyst_dialog.exponat_name.text()

        Data.close_connection()

        new_vyst = VystMoBase(codvuz=codvuz, type=priznak, regnumber=reg_number, subject=nir_name,
                              grnti=grnti, bossname=nir_ruk, boss_position=ruk_doljnost,
                              boss_academic_rank=ruk_zvanie, boss_scientific_degree=ruk_stepen,
                              exhitype=exponat_est, vystavki=vistavka, exponat=exponat_name)

        with Session() as session:
            try:
                session.add(new_vyst)
            except:
                session.rollback()
                raise
            else:
                session.commit()
        Data.create_connection()

        if not self.vyst_mo_table_model.submitAll():
            print("Ошибка добавления записи:", self.vyst_mo_table_model.lastError().text())
        if self.vyst_mo_table_model.select():
            print("kaef")

        if not self.svod_table_model.submitAll():
            print("Ошибка добавления записи:", self.svod_table_model.lastError().text())
        if self.svod_table_model.select():
            print("kaef")

        self.apply_filters()
        self.new_dialog.close()
        self.top_scroll_func()

        QTimer.singleShot(150, lambda: self.scroll_to_bottom(self.ui.vyst_mo_table, self.vyst_mo_table_model))
        # self.ui.vyst_mo_table.setFocus()
        #
        # row_count = self.vyst_mo_table_model.rowCount()
        # if row_count == 0:
        #     return  # Если таблица пуста, ничего не делаем
        #
        # # Определяем индекс последней строки
        # last_row_index = self.vyst_mo_table_model.index(row_count - 1, 0)  # Первый столбец последней строки
        #
        # # Прокручиваем к последней строке
        # self.ui.vyst_mo_table.scrollTo(last_row_index, QAbstractItemView.ScrollHint.PositionAtCenter)
        #
        # # Устанавливаем выделение для всей последней строки
        # self.ui.vyst_mo_table.selectionModel().select(
        #     last_row_index,
        #     QItemSelectionModel.SelectionFlag.Select | QItemSelectionModel.SelectionFlag.Rows
        # )
        #
        # self.ui.vyst_mo_table.viewport().update()
        # self.ui.vyst_mo_table.repaint()
        #
        # self.ui.vyst_mo_table.setFocus()

    def scroll_to_bottom(self, table, model):
        table.setFocus()

        row_count = model.rowCount()
        if row_count == 0:
            return  # Если таблица пуста, ничего не делаем

        # Определяем индекс последней строки
        last_row_index = model.index(row_count - 1, 0)  # Первый столбец последней строки

        # Прокручиваем к последней строке
        table.scrollTo(last_row_index, QAbstractItemView.ScrollHint.PositionAtBottom)
        table.selectRow(row_count - 1)

        # Устанавливаем выделение для всей последней строки
        table.selectionModel().select(
            last_row_index,
            QItemSelectionModel.SelectionFlag.Select | QItemSelectionModel.SelectionFlag.Rows
        )

        table.setFocus()


    def open_delete_confirm_dialog(self, message):
        self.confirm_dialog = QDialog()
        self.ui_confirm_dialog = Ui_Dialog()
        self.ui_confirm_dialog.setupUi(self.confirm_dialog)
        self.ui_confirm_dialog.label.setText(message)

    # Подключаем кнопку "OK" к функции delete_record
        self.ui_confirm_dialog.buttonBox.accepted.connect(self.delete_record)

    # Подключаем кнопку "Cancel" для закрытия диалога
        self.ui_confirm_dialog.buttonBox.rejected.connect(self.confirm_dialog.close)
        self.confirm_dialog.exec_()
        self.confirm_dialog.setModal(True)


    def open_delete_group_confirm_dialog(self, message):
        self.confirm_dialog = QDialog()
        self.ui_confirm_dialog = Ui_Dialog()
        self.ui_confirm_dialog.setupUi(self.confirm_dialog)
        self.ui_confirm_dialog.label.setText(message)

    # Подключаем кнопку "OK" к функции delete_record
        self.ui_confirm_dialog.buttonBox.accepted.connect(self.delete_group_record)

    # Подключаем кнопку "Cancel" для закрытия диалога
        self.ui_confirm_dialog.buttonBox.rejected.connect(self.confirm_dialog.close)
        self.confirm_dialog.exec_()
        self.confirm_dialog.setModal(True)


    def delete_group_record(self):
        current_table = self.ui.group_list_table

        if isinstance(current_table, QTableView):
            model = current_table.model()
            selected_rows = current_table.selectionModel().selectedRows()

            for row in sorted(selected_rows, reverse=True):
                model.removeRow(row.row())

        self.apply_filters()
        self.update_all_tables(model)
        self.confirm_dialog.close()


    def delete_record(self):
        current_table = self.ui.db_tables.currentWidget().children()[1]

        if isinstance(current_table, QTableView):
            model = current_table.model()
            selected_rows = current_table.selectionModel().selectedRows()

            if model is self.vuz_table_model:
                rows_list = [
                    model.data(model.index(index.row(), 0))
                    for index in selected_rows
                ]
                Data.close_connection()
                with Session() as session:
                    try:
                        for codvuz in rows_list:
                            vuz_record = session.query(VuzBase).filter_by(codvuz=codvuz).first()
                            if vuz_record:
                                session.delete(vuz_record)
                        session.commit()
                    except Exception as e:
                        QMessageBox.critical(self, "Ошибка", f"Не удалось удалить записи: {e}")
                        session.rollback()
                        return
                Data.create_connection()
            else:
                for row in sorted(selected_rows, reverse=True):
                    model.removeRow(row.row())

        self.apply_filters()
        self.update_all_tables(model)
        self.confirm_dialog.close()


    def init_tables(self):
        # self.models = {
        #     "vyst_mo_table": self.create_model("vyst_mo"),
        #     "vuz_table": self.create_model("VUZ"),
        #     "grntirub_table": self.create_model("grntirub")
        # }
        self.vyst_mo_table_model = self.create_model("vyst_mo")
        self.vuz_table_model = self.create_model("vuz")
        self.grntirub_table_model = self.create_model("grntirub")
        self.svod_table_model = self.create_model("svod")
        self.group_list_table_model = self.create_model("grouplist")

        # Устанавливаем модели и заголовки
        self.ui.vyst_mo_table.setModel(self.vyst_mo_table_model)
        self.ui.vuz_table.setModel(self.vuz_table_model)
        self.ui.grntirub_table.setModel(self.grntirub_table_model)
        self.ui.svod_table.setModel(self.svod_table_model)
        self.ui.group_list_table.setModel(self.group_list_table_model)

        # self.ui.svod_table.hideColumn(0)
        self.ui.svod_table.hideColumn(23)
        self.ui.vyst_mo_table.hideColumn(0)
        # self.ui.grntirub_table.hideColumn(0)
        # self.ui.vuz_table.hideColumn(0)
        # self.ui.group_list_table.hideColumn(0)
        self.ui.group_list_table.hideColumn(4)
        self.ui.group_list_table.hideColumn(5)

        # Отключаем сортировку по заголовкам при первом выводе
        self.ui.vyst_mo_table.setSortingEnabled(False)
        self.ui.vuz_table.setSortingEnabled(False)
        self.ui.grntirub_table.setSortingEnabled(False)
        self.ui.svod_table.setSortingEnabled(False)
        self.ui.group_list_table.setSortingEnabled(False)
        self.ui.group_view_table.setSortingEnabled(False)

        # Настройка заголовков
        self.set_custom_headers(self.vyst_mo_table_model, ["Код ВУЗа",
                                                           "Признак  формы  НИР", "Рег. номер НИР", "Наименование НИР",
                                                           "Код  ГРНТИ", "Руководитель НИР", "Должность",
                                                           "Ученое звание", "Ученая степень",
                                                           "Признак", "Выставки", "Выставочный экспонат"])

        self.set_custom_headers(self.vuz_table_model,
                                ["Код ВУЗа", "Название ВУЗа", "Полное наименование", "Сокр. наим.",
                                 "Федеральный округ", 'Город', "Статус", "Код субъекта", "Субъект РФ", "Категория", "Профиль"])

        self.set_custom_headers(self.grntirub_table_model, ["Код рубрики", "Наименование рубрики"])
        self.set_custom_headers(self.svod_table_model, ["Код ВУЗа", "Сокращенное наименование ВУЗа",
                                                        "Наименование НИР", "Код  ГРНТИ", "Рубрика ГРНТИ", "Руководитель НИР",
                                                        "Регистрационный номер НИР", "Признак  формы НИР", "Должность",
                                                        "Ученое звание", "Ученая степень", "Признак",
                                                        "Выставки", "Выставочный экспонат", "Название ВУЗа",
                                                        "Полное наименование ВУЗа",
                                                        "Федеральный округ", 'Город', "Статус", "Номер области",
                                                        "Область", "Категория", "Профиль"
                                                        ])
        self.set_custom_headers(self.group_list_table_model, ["Имя группы", "Федеральные округа", "Рубрики ГРНТИ", "Количество выставок"])

        self.ui.vyst_mo_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.ui.vuz_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.ui.grntirub_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.ui.svod_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.ui.group_list_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.ui.group_view_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

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
        self.ui.group_list_table.horizontalHeader().sectionClicked.connect(
            lambda index: self.handle_header_click(self.ui.group_list_table, index)
        )
        self.ui.group_view_table.horizontalHeader().sectionClicked.connect(
            lambda index: self.handle_header_click(self.ui.group_view_table, index)
        )

        # Устанавливаем режим растягивания заголовков
        for table in [self.ui.vyst_mo_table, self.ui.vuz_table, self.ui.grntirub_table, self.ui.svod_table, self.ui.group_list_table, self.ui.group_view_table]:
            #плавная прокрутка
            table.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)

            header = table.horizontalHeader()

            #ширину столбцов подстраивает
            font_metrics = QFontMetrics(table.font())

            header.setSectionResizeMode(QHeaderView.ResizeMode.Fixed)

            if table is self.ui.group_list_table:
                table.setColumnWidth(0, 250)

                header_text = table.model().headerData(1, Qt.Orientation.Horizontal)
                header_width = font_metrics.horizontalAdvance(header_text) + 20
                table.setColumnWidth(1, header_width)

                table.setColumnWidth(2, 620)

                header_text = table.model().headerData(3, Qt.Orientation.Horizontal)
                header_width = font_metrics.horizontalAdvance(header_text) + 20
                table.setColumnWidth(3, header_width)

            else:
                for col in range(header.count()):
                    header_text = table.model().headerData(col, Qt.Orientation.Horizontal)
                    header_width = font_metrics.horizontalAdvance(header_text) + 20
                    table.setColumnWidth(col, header_width)

            header.setSectionResizeMode(QHeaderView.ResizeMode.Interactive)
            header.setStretchLastSection(False)
            table.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)

        self.ui.vyst_mo_table.setEditTriggers(QAbstractItemView.EditTrigger.AllEditTriggers)

        while self.vyst_mo_table_model.canFetchMore():
            self.vyst_mo_table_model.fetchMore()
# TODO
        while self.svod_table_model.canFetchMore():
            self.svod_table_model.fetchMore()

        self.ui.group_list_table.doubleClicked.connect(self.open_group_view_page)

        # columns_to_format = [1, 2]  # Индексы столбцов, в которых нужно форматировать данные
        # for column in columns_to_format:
        #     delegate = SemicolonFormattingDelegate()
        #     self.ui.group_list_table.setItemDelegateForColumn(column, delegate)

        delegate = SemicolonDelegate(self.ui.group_list_table)

        # Устанавливаем делегат для нужных столбцов
        column_with_semicolons = [1, 2]  # замените на номера ваших столбцов
        for column in column_with_semicolons:
            self.ui.group_list_table.setItemDelegateForColumn(column, delegate)


    def open_group_list(self):
        if self.ui.pages_.currentIndex() != 1:
            self.ui.pages_.setCurrentIndex(1)

        self.ui.groups_pages.setCurrentWidget(self.ui.group_list_page)

    def set_current_table(self, checked_action):
        """Switches the current table and resets the filters."""
        # Очистка полей ввода фильтров при переключении таблиц
        self.clear_filter_input_fields()

        if self.ui.pages_.currentIndex() != 0:
            self.ui.pages_.setCurrentIndex(0)

        text = checked_action.text()
        if text == "ГРНТИ":
            self.ui.db_tables.setCurrentIndex(3)
            self.current_model = self.grntirub_table_model
            self.ui.current_table_label.setText("Таблица «ГРНТИ»")
            self.top_scroll_func()
            self.ui.create_btn.setEnabled(False)
            self.ui.update_btn.setEnabled(False)
            self.ui.add_to_group_btn.setEnabled(False)
            self.ui.delete_btn.setEnabled(True)
        elif text == "Выставки":
            self.ui.db_tables.setCurrentIndex(1)
            self.current_model = self.vyst_mo_table_model
            self.ui.current_table_label.setText("Таблица «Выставки»")
            self.top_scroll_func()
            self.ui.create_btn.setEnabled(True)
            self.ui.update_btn.setEnabled(True)
            self.ui.add_to_group_btn.setEnabled(False)
            self.ui.delete_btn.setEnabled(True)

            self.ui.create_btn.clicked.disconnect()
            self.ui.update_btn.clicked.disconnect()
            self.ui.create_btn.clicked.connect(self.open_create_vyst_dialog)
            self.ui.update_btn.clicked.connect(
                lambda: self.update_button_action(func=self.open_update_vyst_dialog)
            )
        elif text == "ВУЗы":
            self.ui.db_tables.setCurrentIndex(2)
            self.current_model = self.vuz_table_model
            self.ui.current_table_label.setText("Таблица «ВУЗы»")
            self.top_scroll_func()
            self.ui.create_btn.setEnabled(True)
            self.ui.update_btn.setEnabled(True)
            self.ui.add_to_group_btn.setEnabled(False)
            self.ui.delete_btn.setEnabled(True)

            self.ui.create_btn.clicked.disconnect()
            self.ui.update_btn.clicked.disconnect()
            self.ui.create_btn.clicked.connect(self.open_create_vuz_dialog)
            self.ui.update_btn.clicked.connect(
                lambda: self.update_button_action(func=self.open_update_vuz_dialog)
            )
        elif text == "Сводная таблица":
            self.ui.db_tables.setCurrentIndex(0)
            self.current_model = self.svod_table_model
            self.ui.current_table_label.setText("Сводная таблица")
            self.top_scroll_func()
            self.ui.create_btn.setEnabled(False)
            self.ui.update_btn.setEnabled(False)
            self.ui.add_to_group_btn.setEnabled(True)
            self.ui.delete_btn.setEnabled(False)

        self.update_filter_combobox()

        # Показываем все строки при переключении таблиц
        self.show_all_rows()

    @staticmethod
    def read_txt_to_list(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                lst = [line.strip() for line in file if line.strip()]
            return lst
        except FileNotFoundError:
            print(f"Файл {file_path} не найден.")
            return []
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            return []

    def open_create_vuz_dialog(self):
        subj_list = list(" ")
        subj_list.extend(self.read_txt_to_list('data/federal_obj.txt'))
        codes_list = list(" ")
        codes_list.extend(self.read_txt_to_list('data/region_codes.txt'))
        federal_regions = list(" ")
        federal_regions.extend(self.read_txt_to_list('data/federal_regions.txt'))

        self.new_dialog = QDialog()
        self.ui_create_vuz_dialog = Ui_create_vuz_dialog()
        self.ui_create_vuz_dialog.setupUi(self.new_dialog)
        self.ui_create_vuz_dialog.save_btn.clicked.connect(self.create_vuz)

        self.ui_create_vuz_dialog.vuz_full_name.textChanged.connect(
            lambda: self.add_tooltip(self.ui_create_vuz_dialog.vuz_full_name)
        )
        self.ui_create_vuz_dialog.vuz_full_name.editingFinished.connect(
            lambda: self.ui_create_vuz_dialog.vuz_full_name.setCursorPosition(0)
        )

        self.ui_create_vuz_dialog.vuz_name.textChanged.connect(
            lambda: self.add_tooltip(self.ui_create_vuz_dialog.vuz_full_name)
        )
        self.ui_create_vuz_dialog.vuz_name.editingFinished.connect(
            lambda: self.ui_create_vuz_dialog.vuz_full_name.setCursorPosition(0)
        )

        self.ui_create_vuz_dialog.federal_subject_cb.addItems(subj_list)
        self.ui_create_vuz_dialog.federal_subject_code_cb.addItems(codes_list)
        self.ui_create_vuz_dialog.federal_region_cb.addItems(federal_regions)

        self.ui_create_vuz_dialog.federal_subject_cb.currentIndexChanged.connect(self.sync_federal_code_combo)
        self.ui_create_vuz_dialog.federal_subject_code_cb.currentIndexChanged.connect(self.sync_federal_name_combo)

        self.ui_create_vuz_dialog.federal_subject_cb.setEditable(True)
        self.ui_create_vuz_dialog.federal_subject_code_cb.setEditable(True)
        self.ui_create_vuz_dialog.federal_region_cb.setEditable(False)

        self.set_validation(Regex.rus_regex, self.ui_create_vuz_dialog.vuz_short_name)
        self.set_validation(Regex.num_regex, self.ui_create_vuz_dialog.vuz_code)
        self.set_validation(Regex.rus_regex, self.ui_create_vuz_dialog.vuz_name)
        self.set_validation(Regex.common_regex, self.ui_create_vuz_dialog.vuz_full_name)
        self.set_validation(Regex.rus_regex, self.ui_create_vuz_dialog.city)
        self.set_validation(Regex.rus_regex, self.ui_create_vuz_dialog.vuz_status)
        self.set_validation(Regex.upper_rus_regex, self.ui_create_vuz_dialog.vuz_category)
        self.set_validation(Regex.upper_rus_regex, self.ui_create_vuz_dialog.vuz_profile)
        self.set_validation(Regex.rus_regex, self.ui_create_vuz_dialog.federal_subject_cb.lineEdit())
        self.set_validation(Regex.num_regex, self.ui_create_vuz_dialog.federal_subject_code_cb.lineEdit())

        # Настройка комплитеров после заполнения ComboBox
        subject_name_completer = QCompleter(subj_list, self.ui_create_vuz_dialog.federal_subject_cb)
        subject_code_completer = QCompleter(codes_list, self.ui_create_vuz_dialog.federal_subject_code_cb)
        federal_regions_completer = QCompleter(federal_regions, self.ui_create_vuz_dialog.federal_region_cb)

        subject_name_completer.setCompletionMode(QCompleter.CompletionMode.PopupCompletion)
        subject_code_completer.setCompletionMode(QCompleter.CompletionMode.PopupCompletion)
        federal_regions_completer.setCompletionMode(QCompleter.CompletionMode.PopupCompletion)

        self.ui_create_vuz_dialog.federal_subject_cb.setCompleter(subject_name_completer)
        self.ui_create_vuz_dialog.federal_subject_code_cb.setCompleter(subject_code_completer)
        self.ui_create_vuz_dialog.federal_region_cb.setCompleter(federal_regions_completer)

        # Ограничиваем ввод только существующими значениями
        self.ui_create_vuz_dialog.federal_subject_cb.lineEdit().editingFinished.connect(
            lambda elem = self.ui_create_vuz_dialog.federal_subject_cb: self.validate_cb_input(elem)
        )
        self.ui_create_vuz_dialog.federal_subject_code_cb.lineEdit().editingFinished.connect(
            lambda elem = self.ui_create_vuz_dialog.federal_subject_code_cb: self.validate_cb_input(elem)
        )

        self.new_dialog.setFixedSize(468, 573)
        self.new_dialog.setModal(True)
        self.new_dialog.show()

    def open_update_vuz_dialog(self, model, selected_row):
        subj_list = [w for w in Path("federal_obj.txt").read_text(encoding="utf-8").replace("\n", " ").split()]
        codes_list = [w for w in Path("region_codes.txt").read_text(encoding="utf-8").replace("\n", " ").split()]
        federal_regions = [w for w in Path("federal_regions.txt").read_text(encoding="utf-8").replace("\n", " ").split()]

        self.new_dialog = QDialog()
        self.ui_create_vuz_dialog = Ui_create_vuz_dialog()
        self.ui_create_vuz_dialog.setupUi(self.new_dialog)
        self.ui_create_vuz_dialog.save_btn.clicked.connect(self.update_vuz)
        self.ui_create_vuz_dialog.dialog_label.setText("Редактирование записи ВУЗа")

        self.ui_create_vuz_dialog.vuz_full_name.textChanged.connect(
            lambda: self.add_tooltip(self.ui_create_vuz_dialog.vuz_full_name)
        )
        self.ui_create_vuz_dialog.vuz_full_name.editingFinished.connect(
            lambda: self.ui_create_vuz_dialog.vuz_full_name.setCursorPosition(0)
        )
        self.ui_create_vuz_dialog.vuz_name.textChanged.connect(
            lambda: self.add_tooltip(self.ui_create_vuz_dialog.vuz_full_name)
        )
        self.ui_create_vuz_dialog.vuz_name.editingFinished.connect(
            lambda: self.ui_create_vuz_dialog.vuz_full_name.setCursorPosition(0)
        )

        self.ui_create_vuz_dialog.federal_subject_cb.addItem("").addItems(subj_list)
        self.ui_create_vuz_dialog.federal_subject_code_cb.addItem("").addItems(codes_list)
        self.ui_create_vuz_dialog.federal_region_cb.addItem("").addItems(federal_regions)

        self.ui_create_vuz_dialog.federal_subject_cb.currentIndexChanged.connect(self.sync_federal_code_combo)
        self.ui_create_vuz_dialog.federal_subject_code_cb.currentIndexChanged.connect(self.sync_federal_name_combo)

        self.ui_create_vuz_dialog.federal_subject_cb.setEditable(True)
        self.ui_create_vuz_dialog.federal_subject_code_cb.setEditable(True)
        self.ui_create_vuz_dialog.federal_region_cb.setEditable(True)

        self.set_validation(Regex.rus_regex, self.ui_create_vuz_dialog.vuz_short_name)
        self.set_validation(Regex.num_regex, self.ui_create_vuz_dialog.vuz_code)
        self.set_validation(Regex.rus_regex, self.ui_create_vuz_dialog.vuz_name)
        self.set_validation(Regex.common_regex, self.ui_create_vuz_dialog.vuz_full_name)
        self.set_validation(Regex.rus_regex, self.ui_create_vuz_dialog.city)
        self.set_validation(Regex.rus_regex, self.ui_create_vuz_dialog.vuz_status)
        self.set_validation(Regex.upper_rus_regex, self.ui_create_vuz_dialog.vuz_category)
        self.set_validation(Regex.upper_rus_regex, self.ui_create_vuz_dialog.vuz_profile)

        # Настройка комплитеров после заполнения ComboBox
        subject_name_completer = QCompleter(subj_list, self.ui_create_vuz_dialog.federal_subject_cb)
        subject_code_completer = QCompleter(codes_list, self.ui_create_vuz_dialog.federal_subject_code_cb)
        federal_regions_completer = QCompleter(federal_regions, self.ui_create_vuz_dialog.federal_region_cb)

        subject_name_completer.setCompletionMode(QCompleter.CompletionMode.PopupCompletion)
        subject_code_completer.setCompletionMode(QCompleter.CompletionMode.PopupCompletion)
        federal_regions_completer.setCompletionMode(QCompleter.CompletionMode.PopupCompletion)

        self.ui_create_vuz_dialog.federal_subject_cb.setCompleter(subject_name_completer)
        self.ui_create_vuz_dialog.federal_subject_code_cb.setCompleter(subject_code_completer)
        self.ui_create_vuz_dialog.federal_region_cb.setCompleter(federal_regions_completer)

        # Ограничиваем ввод только существующими значениями
        self.ui_create_vuz_dialog.federal_subject_cb.lineEdit().editingFinished.connect(
            lambda elem=self.ui_create_vuz_dialog.federal_subject_cb: self.validate_cb_input(elem)
        )
        self.ui_create_vuz_dialog.federal_subject_code_cb.lineEdit().editingFinished.connect(
            lambda elem=self.ui_create_vuz_dialog.federal_subject_code_cb: self.validate_cb_input(elem)
        )
        self.ui_create_vuz_dialog.federal_region_cb.lineEdit().editingFinished.connect(
            lambda elem=self.ui_create_vuz_dialog.federal_region_cb: self.validate_cb_input(elem)
        )

        row_data = self.get_selected_row_data(model, selected_row)

        self.ui_create_vuz_dialog.vuz_code.setText(str(row_data[0]))
        self.ui_create_vuz_dialog.vuz_name.setText(row_data[1])
        self.ui_create_vuz_dialog.vuz_full_name.setText(row_data[2])
        self.ui_create_vuz_dialog.vuz_short_name.setText(row_data[3])
        self.ui_create_vuz_dialog.federal_region_cb.setCurrentText(row_data[4])
        self.ui_create_vuz_dialog.city.setText(row_data[5])
        self.ui_create_vuz_dialog.vuz_status.setText(row_data[6])
        self.ui_create_vuz_dialog.federal_subject_code_cb.setCurrentText(str(row_data[7]))
        self.ui_create_vuz_dialog.federal_subject_cb.setCurrentText(row_data[8])
        self.ui_create_vuz_dialog.vuz_category.setText(row_data[9])
        self.ui_create_vuz_dialog.vuz_profile.setText(row_data[10])

        self.ui_create_vuz_dialog.vuz_full_name.setCursorPosition(0)
        self.ui_create_vuz_dialog.vuz_name.setCursorPosition(0)

        Data.close_connection()
        current_obj = VuzBase.get_by_name(row_data[0])
        Data.create_connection()

        self.current_obj = current_obj

        self.new_dialog.setFixedSize(468, 573)
        self.new_dialog.setModal(True)
        self.new_dialog.show()

    def sync_federal_code_combo(self, index):
        # При изменении subj_name выбираем соответствующий элемент в subj_code
        combobox = self.ui_create_vuz_dialog.federal_subject_code_cb
        combobox.blockSignals(True)  # Блокируем сигнал, чтобы не вызывать обратное обновление
        combobox.setCurrentIndex(index)
        combobox.blockSignals(False)

    def sync_federal_name_combo(self, index):
        # При изменении subj_code выбираем соответствующий элемент в subj_name
        combobox = self.ui_create_vuz_dialog.federal_subject_cb
        combobox.blockSignals(True)  # Блокируем сигнал, чтобы не вызывать обратное обновление
        combobox.setCurrentIndex(index)
        combobox.blockSignals(False)

    @staticmethod
    def add_tooltip(element: QLineEdit):
        element.setToolTip(element.text())

    def create_vuz(self):
        if self.validate_vuz_fields():
            return

        short_name = self.ui_create_vuz_dialog.vuz_short_name.text()
        code = self.ui_create_vuz_dialog.vuz_code.text()
        name = self.ui_create_vuz_dialog.vuz_name.text()
        full_name = self.ui_create_vuz_dialog.vuz_full_name.text()
        federal_region = self.ui_create_vuz_dialog.federal_region_cb.currentText()
        city = self.ui_create_vuz_dialog.city.text()
        federal_subject = self.ui_create_vuz_dialog.federal_subject_cb.currentText()
        federal_subject_code = self.ui_create_vuz_dialog.federal_subject_code_cb.currentText()
        status = self.ui_create_vuz_dialog.vuz_status.text()
        category = self.ui_create_vuz_dialog.vuz_category.text()
        profile = self.ui_create_vuz_dialog.vuz_profile.text()

        Data.close_connection()
        new_vuz = VuzBase(
            codvuz=code, z1=name, z1full=full_name, z2=short_name,
            region=federal_region, city=city, status=status,
            obl=federal_subject_code, oblname=federal_subject,
            gr_ved=category, prof=profile
        )
        with Session() as session:
            try:
                session.add(new_vuz)
            except:
                session.rollback()
                raise
            else:
                session.commit()
        Data.create_connection()

        if not self.vuz_table_model.submitAll():
            print("Ошибка добавления записи:", self.vuz_table_model.lastError().text())
        if self.vuz_table_model.select():
            print("kaef")

        self.apply_filters()
        self.new_dialog.close()
        self.top_scroll_func()
        QTimer.singleShot(150, lambda: self.scroll_to_bottom(self.ui.vuz_table, self.vuz_table_model))

    def update_vuz(self):
        current_obj = self.current_obj

        if self.validate_vuz_fields():
            return

        short_name = self.ui_create_vuz_dialog.vuz_short_name.text()
        code = self.ui_create_vuz_dialog.vuz_code.text()
        name = self.ui_create_vuz_dialog.vuz_name.text()
        full_name = self.ui_create_vuz_dialog.vuz_full_name.text()
        federal_region = self.ui_create_vuz_dialog.federal_region_cb.currentText()
        city = self.ui_create_vuz_dialog.city.text()
        federal_subject = self.ui_create_vuz_dialog.federal_subject_cb.currentText()
        federal_subject_code = self.ui_create_vuz_dialog.federal_subject_code_cb.currentText()
        status = self.ui_create_vuz_dialog.vuz_status.text()
        category = self.ui_create_vuz_dialog.vuz_category.text()
        profile = self.ui_create_vuz_dialog.vuz_profile.text()

        Data.close_connection()

        with Session() as session:
            try:
                current_obj.codvuz = code
                current_obj.z1 = name
                current_obj.z1full = full_name
                current_obj.z2 = short_name
                current_obj.region = federal_region
                current_obj.city = city
                current_obj.status = status
                current_obj.obl = federal_subject_code
                current_obj.oblname = federal_subject
                current_obj.gr_ved = category
                current_obj.prof = profile

                session.merge(current_obj)
            except:
                session.rollback()
                raise
            else:
                session.commit()

        Data.create_connection()

        if not self.vuz_table_model.submitAll():
            print("Ошибка добавления записи:", self.vuz_table_model.lastError().text())
        if self.vuz_table_model.select():
            print("kaef")

        if not self.svod_table_model.submitAll():
            print("Ошибка добавления записи:", self.svod_table_model.lastError().text())
        if self.svod_table_model.select():
            print("kaef")

        self.apply_filters()
        self.new_dialog.close()

    @staticmethod
    def set_validation(regex: QRegularExpression, element: QLineEdit):
        validator = QRegularExpressionValidator(regex, element)
        element.setValidator(validator)

    ################################################__ФИЛЬТРЫ__#############################################
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
        label = QLabel(label_text, self)
        layout.addWidget(label)

        # Создаем QComboBox для уникальных значений из выбранной колонки
        combo_box = QComboBox(self)
        unique_values = self.get_unique_values_for_column(label_text)

        if unique_values:
            combo_box.addItems(unique_values)

        combo_box.setEditable(True)  # Позволяем ручной ввод
        combo_box.setCurrentText("")  # Устанавливаем пустое значение по умолчанию

        # Устанавливаем подсказку в поле ввода
        combo_box.lineEdit().setPlaceholderText("вводите через точку с запятой")

        # Связываем действие при вводе значений
        combo_box.lineEdit().returnPressed.connect(self.apply_filters)

        layout.addWidget(combo_box)

        # Кнопка для очистки фильтра
        clear_button = QPushButton("✖️", self)
        clear_button.setFixedSize(25, 25)
        clear_button.clicked.connect(lambda: self.remove_filter_input(label_text, layout))
        layout.addWidget(clear_button)

        # Добавляем отступы для улучшения внешнего вида
        layout.setContentsMargins(5, 5, 5, 5)
        layout.setSpacing(10)

        return layout

    def get_unique_values_for_column(self, column_name):
        """Извлекаем уникальные значения для выбранной колонки из текущей модели."""
        column_index = [self.current_model.headerData(i, Qt.Orientation.Horizontal) for i in
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
                filter_values = [val.strip() for val in filter_value.split(';') if val.strip()]
                filter_conditions[filter_key] = filter_values

        # Apply filters to the current model and show rows accordingly
        self.top_scroll_func()
        self.filter_table(filter_conditions)
        self.top_scroll_func()

    def filter_table(self, filter_conditions):
        """Apply filters to the currently selected table."""
        rows_to_hide = set()

        for row in range(self.current_model.rowCount()):
            show_row = True  # Flag to determine if the row should be shown

            for filter_key, filter_values in filter_conditions.items():
                # Находим индекс столбца по его имени
                column_index = [self.current_model.headerData(i, Qt.Orientation.Horizontal) for i in
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

        self.top_scroll_func()
        self.show_all_rows()

        self.top_scroll_func()

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
        model.setEditStrategy(QSqlTableModel.EditStrategy.OnManualSubmit)
        model.setTable(table_name)
        model.select()
        return model

    def update_filter_combobox(self):
        """Updates the ComboBox with currently active filters."""
        self.ui.add_filters_cb.clear()
        if self.current_model:
            headers = [self.current_model.headerData(i, Qt.Orientation.Horizontal) for i in
                       range(1, self.current_model.columnCount())]
            # Exclude currently selected filters
            for filter_key in self.filter_fields.keys():
                headers.remove(filter_key)
            self.ui.add_filters_cb.addItems(headers)

    def set_custom_headers(self, model, headers):
        if model is self.vyst_mo_table_model:
            for index, header in enumerate(headers):
                model.setHeaderData(index + 1, Qt.Orientation.Horizontal, header)
        else:
            for index, header in enumerate(headers):
                model.setHeaderData(index, Qt.Orientation.Horizontal, header)

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

    def update_all_tables(self, model):
        if not model.submitAll():
            print("model error:", model.lastError().text())
        if model.select():
            print("kaef - model")

        if not self.vuz_table_model.submitAll():
            print("vuz error:", self.vuz_table_model.lastError().text())
        if self.vuz_table_model.select():
            print("kaef - vuz")

        if not self.vyst_mo_table_model.submitAll():
            print("vyst_mo error:", self.vyst_mo_table_model.lastError().text())
        if self.vyst_mo_table_model.select():
            print("kaef - vyst")

        if not self.svod_table_model.submitAll():
            print("svod error:", self.svod_table_model.lastError().text())
        if self.svod_table_model.select():
            print("kaef - svod")

    def delete_group_button_action(self):
        current_table: QTableView = self.ui.group_list_table

        if isinstance(current_table, QTableView):
            selected_rows = current_table.selectionModel().selectedRows()

            if selected_rows:
                # Получаем номера выбранных строк
                row_numbers = [row.row() + 1 for row in selected_rows]

                # Формируем текст для диалогового окна
                message = self.format_row_numbers(row_numbers)

                # Открываем диалог подтверждения
                self.open_delete_group_confirm_dialog(message)
            else:
                QMessageBox.warning(self, "Ошибка", "Выберите строки в таблице.")
        else:
            QMessageBox.warning(self, "Ошибка", "Текущий виджет не является таблицей.")

    def delete_button_action(self):

        current_widget = self.ui.db_tables.currentWidget() # Получаем текущий виджет
        if current_widget is not None: # Проверяем, что текущий виджет существует
            current_table: QTableView = current_widget.children()[1] # Получаем второй дочерний элемент

            if isinstance(current_table, QTableView):
                selected_rows = current_table.selectionModel().selectedRows()

                if selected_rows:
          # Получаем номера выбранных строк
                    row_numbers = [row.row() + 1 for row in selected_rows]

          # Формируем текст для диалогового окна
                    message = self.format_row_numbers(row_numbers)

          # Открываем диалог подтверждения
                    self.open_delete_confirm_dialog(message)
                else:
                    QMessageBox.warning(self, "Ошибка", "Выберите строки в таблице.")
            else:
                QMessageBox.warning(self, "Ошибка", "Текущий виджет не является таблицей.")
        else:
            QMessageBox.warning(self, "Ошибка", "Нет активного виджета.")

    def format_row_numbers(self, row_numbers):
        """Форматирует список номеров строк для вывода в диалоговом окне."""
        row_numbers.sort()
        formatted_numbers = []
        current_range = []

        for i, number in enumerate(row_numbers):
            if i == 0 or number == row_numbers[i - 1] + 1:
                current_range.append(number)
            else:
                if len(current_range) > 1:
                    formatted_numbers.append(f"{current_range[0]}-{current_range[-1]}")
                elif len(current_range) == 1:
                    formatted_numbers.append(str(current_range[0]))
                current_range = [number]

        if len(current_range) > 1:
            formatted_numbers.append(f"{current_range[0]}-{current_range[-1]}")
        elif len(current_range) == 1:
            formatted_numbers.append(str(current_range[0]))

        return f"Удалить строки с номерами {', '.join(formatted_numbers)}?"

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Выход', "Вы уверены, что хотите выйти?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                     QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
            self.close_all_windows()
            event.accept()
        else:
            event.ignore()

    def close_all_windows(self):
        QApplication.closeAllWindows()

    def update_filter_input_field(self):
        selected_filter = self.ui.add_filters_cb.currentText()

        # Удаляем пустые поля перед добавлением нового фильтра
        self.remove_empty_filter_fields()

        # Добавляем новый фильтр, если его еще нет
        if selected_filter and selected_filter not in self.filter_fields:
            new_filter_layout = self.create_filter_input(selected_filter)
            self.filter_fields[selected_filter] = new_filter_layout
            self.rebuild_filter_grid()

    def remove_empty_filter_fields(self):
        # Удаляем все пустые поля фильтров
        empty_filters = [key for key, layout in self.filter_fields.items()
                         if not layout.itemAt(1).widget().currentText().strip()]

        for filter_name in empty_filters:
            self.remove_filter(filter_name)

    def remove_filter(self, filter_name):
        self.top_scroll_func()
        if filter_name in self.filter_fields:
            layout_to_remove = self.filter_fields.pop(filter_name)

            # Удаляем элементы интерфейса
            for i in reversed(range(layout_to_remove.count())):
                widget = layout_to_remove.itemAt(i).widget()
                if widget is not None:
                    widget.setParent(None)
            self.top_scroll_func()
            # Перестроение сетки после удаления
            self.rebuild_filter_grid()
            self.top_scroll_func()


class NonEditableSqlTableModel(QSqlTableModel):
    def flags(self, index):
        return Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Data.create_connection()  # Устанавливаем соединение один раз в начале
    window = ExponatDBMS()
    window.show()
    sys.exit(app.exec())
