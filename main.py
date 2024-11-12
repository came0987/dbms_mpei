import sys

import PySide6
from PySide6.QtGui import QRegularExpressionValidator, QIntValidator, QFontMetrics
from PySide6.QtWidgets import (QApplication, QMainWindow, QApplication, QComboBox, QPushButton,
                               QHBoxLayout, QLabel, QCompleter, QGridLayout, QAbstractItemView,
                               QMessageBox, QDialog)
from PySide6.QtCore import Qt, QAbstractItemModel, QSortFilterProxyModel, QRegularExpression, QEvent
from PySide6.QtCore import Qt, QSortFilterProxyModel, QRegularExpression
from PySide6.QtWidgets import QHeaderView, QTableView
from PySide6.QtSql import QSqlTableModel

from connection import Session, Data

from py_ui.ui_main_side import Ui_MainWindow
from py_ui.ui_vistavka_entry import Ui_add_zapis_dialog
from py_ui.ui_cancel_confirm import Ui_Dialog
from table_models import VuzBase, VystMoBase, GrntiBase
from PySide6.QtGui import QIntValidator, QRegularExpressionValidator
from PySide6.QtCore import QRegularExpression, QEvent, Qt


class ExponatDBMS(QMainWindow):

    def __init__(self):
        super(ExponatDBMS, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connection = Data()
        # self.showMaximized()
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

        self.ui.create_btn.clicked.connect(self.open_create_entry_dialog)
        self.ui.delete_btn.clicked.connect(self.delete_button_action)
        self.ui.update_btn.clicked.connect(self.update_vyst_button_action)

#######################################__ДОБАВЛЕНИЕ ЗАПИСИ__###########################################################

    def open_create_entry_dialog(self):
        self.new_dialog = PySide6.QtWidgets.QDialog()
        self.ui_create_entry_dialog = Ui_add_zapis_dialog()
        self.ui_create_entry_dialog.setupUi(self.new_dialog)
        self.ui_create_entry_dialog.save_btn.clicked.connect(self.create_vyst_entry)

        self.ui_create_entry_dialog.vuz.currentIndexChanged.connect(self.sync_codvuz_combo)
        self.ui_create_entry_dialog.codvuz.currentIndexChanged.connect(self.sync_vuz_combo)

        self.ui_create_entry_dialog.vuz.setEditable(True)
        self.ui_create_entry_dialog.codvuz.setEditable(True)
        self.ui_create_entry_dialog.grnti.setValidator(QIntValidator(0, 99999999))
        self.ui_create_entry_dialog.grnti.textChanged.connect(self.validate_grnti_prefix)

        self.ui_create_entry_dialog.grnti.textChanged.connect(self.auto_insert_dots)
        regex = QRegularExpression(r"^[a-zA-Zа-яА-ЯёЁ\s\.\,\:\;]+$")  # Разрешаем только буквы и пробелы
        validator = QRegularExpressionValidator(regex, self.ui_create_entry_dialog.nir_ruk)
        self.ui_create_entry_dialog.nir_ruk.setValidator(validator)
        validator_1 = QRegularExpressionValidator(regex, self.ui_create_entry_dialog.ruk_doljnost)
        self.ui_create_entry_dialog.ruk_doljnost.setValidator(validator_1)
        validator_2 = QRegularExpressionValidator(regex, self.ui_create_entry_dialog.ruk_zvanie)
        self.ui_create_entry_dialog.ruk_zvanie.setValidator(validator_2)
        validator_3 = QRegularExpressionValidator(regex, self.ui_create_entry_dialog.ruk_stepen)
        self.ui_create_entry_dialog.ruk_stepen.setValidator(validator_3)

        Data.close_connection()
        with Session() as session:
        # Извлекаем все записи из таблицы Vuz
            vuz_records = session.query(VuzBase).all()
        Data.create_connection()
        # Заполняем оба ComboBox
        for vuz in vuz_records:
            self.ui_create_entry_dialog.vuz.addItem(vuz.z1, str(vuz.codvuz))
            self.ui_create_entry_dialog.codvuz.addItem(str(vuz.codvuz), vuz.z1)

        # Заполняем ComboBox значениями
        vuz_list = [vuz.z1 for vuz in vuz_records]
        codvuz_list = [str(vuz.codvuz) for vuz in vuz_records]

        # Настройка комплитеров после заполнения ComboBox
        vuz_completer = QCompleter(vuz_list, self.ui_create_entry_dialog.vuz)
        codvuz_completer = QCompleter(codvuz_list, self.ui_create_entry_dialog.codvuz)

        vuz_completer.setCompletionMode(QCompleter.CompletionMode.PopupCompletion)
        codvuz_completer.setCompletionMode(QCompleter.CompletionMode.PopupCompletion)

        self.ui_create_entry_dialog.vuz.setCompleter(vuz_completer)
        self.ui_create_entry_dialog.codvuz.setCompleter(codvuz_completer)

        # Ограничиваем ввод только существующими значениями
        self.ui_create_entry_dialog.vuz.lineEdit().editingFinished.connect(self.validate_vuz_input)
        self.ui_create_entry_dialog.codvuz.lineEdit().editingFinished.connect(self.validate_codvuz_input)

        # Регулярное выражение для разрешения только букв в nir_ruk
        regex = QRegularExpression(r"^[a-zA-Zа-яА-ЯёЁ\s\.\;]+$")
        validator = QRegularExpressionValidator(regex, self.ui_create_entry_dialog.nir_ruk)
        self.ui_create_entry_dialog.nir_ruk.setValidator(validator)

        self.new_dialog.setFixedSize(561, 664)
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
            self.ui_create_entry_dialog.grnti.blockSignals(True)
            self.ui_create_entry_dialog.grnti.setText(prefix)
            self.ui_create_entry_dialog.grnti.blockSignals(False)

    def validate_vuz_input(self):
        input_text = self.ui_create_entry_dialog.vuz.currentText()
        if self.ui_create_entry_dialog.vuz.findText(input_text) == -1:
            # Если введенное значение не найдено, сбрасываем поле
            self.ui_create_entry_dialog.vuz.setCurrentIndex(-1)

    def validate_codvuz_input(self):
        input_text = self.ui_create_entry_dialog.codvuz.currentText()
        if self.ui_create_entry_dialog.codvuz.findText(input_text) == -1:
            # Если введенное значение не найдено, сбрасываем поле
            self.ui_create_entry_dialog.codvuz.setCurrentIndex(-1)

    def setup_grnti_input(self):
        # Подключаем обработчик textChanged для жёсткой фильтрации текста
        self.ui_create_entry_dialog.grnti.textChanged.connect(self.filter_grnti_input)

    def filter_grnti_input(self):
        text = self.ui_create_entry_dialog.grnti.text()

        # Разрешаем только цифры, точки, точки с запятой и пробелы
        allowed_text = ''.join([ch for ch in text if ch.isdigit() or ch in ['.', ';', ' ']])

        # Проверяем, если текст был изменён (это значит, что были удалены недопустимые символы)
        if text != allowed_text:
            # Устанавливаем курсор на последнюю позицию, чтобы не сбивать пользователя
            cursor_position = self.ui_create_entry_dialog.grnti.cursorPosition()
            self.ui_create_entry_dialog.grnti.setText(allowed_text)
            self.ui_create_entry_dialog.grnti.setCursorPosition(min(cursor_position, len(allowed_text)))

        # Применяем автоформатирование для структуры "xx.xx.xx"
        self.auto_insert_dots()

    def auto_insert_dots(self):
        text = self.ui_create_entry_dialog.grnti.text()
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
        self.ui_create_entry_dialog.grnti.blockSignals(True)
        self.ui_create_entry_dialog.grnti.setText(final_text)
        self.ui_create_entry_dialog.grnti.blockSignals(False)
        self.ui_create_entry_dialog.grnti.setCursorPosition(len(final_text))

    def sync_codvuz_combo(self):
        # Получаем codvuz, связанный с текущим vuzname
        selected_codvuz = self.ui_create_entry_dialog.vuz.currentData()
        # Находим и устанавливаем соответствующий элемент в codvuz_combo
        if selected_codvuz is not None:
            index = self.ui_create_entry_dialog.codvuz.findText(selected_codvuz)
            if index != -1:
                self.ui_create_entry_dialog.codvuz.blockSignals(True)
                self.ui_create_entry_dialog.codvuz.setCurrentIndex(index)
                self.ui_create_entry_dialog.codvuz.blockSignals(False)

    def sync_vuz_combo(self):
        # Получаем vuzname, связанный с текущим codvuz
        selected_vuzname = self.ui_create_entry_dialog.codvuz.currentData()
        # Находим и устанавливаем соответствующий элемент в vuzname_combo
        if selected_vuzname is not None:
            index = self.ui_create_entry_dialog.vuz.findText(selected_vuzname)
            if index != -1:
                self.ui_create_entry_dialog.vuz.blockSignals(True)
                self.ui_create_entry_dialog.vuz.setCurrentIndex(index)
                self.ui_create_entry_dialog.vuz.blockSignals(False)

    def update_vyst_button_action(self):
        current_widget = self.ui.db_tables.currentWidget()  # Получаем текущий виджет
        if current_widget is not None:  # Проверяем, что текущий виджет существует
            current_table: QTableView = current_widget.children()[1]  # Получаем второй дочерний элемент
            model = current_table.selectionModel().model()
            if isinstance(current_table, QTableView):
                selected_row = current_table.selectionModel().currentIndex().row()

                if selected_row >= 0:  # Проверяем, что строка выделена
                    self.open_update_entry_dialog(model, selected_row)  # Передаем номер строки
                else:
                    QMessageBox.warning(self, "Ошибка", "Выберите строку в таблице.")
            else:
                QMessageBox.warning(self, "Ошибка", "Текущий виджет не является таблицей.")
        else:
            QMessageBox.warning(self, "Ошибка", "Нет активного виджета.")

    def open_update_entry_dialog(self, model, selected_row):
        self.new_dialog = PySide6.QtWidgets.QDialog()
        self.ui_create_entry_dialog = Ui_add_zapis_dialog()
        self.ui_create_entry_dialog.setupUi(self.new_dialog)
        self.ui_create_entry_dialog.save_btn.clicked.connect(self.update_vyst_entry)

        self.ui_create_entry_dialog.vuz.currentIndexChanged.connect(self.sync_codvuz_combo)
        self.ui_create_entry_dialog.codvuz.currentIndexChanged.connect(self.sync_vuz_combo)

        self.ui_create_entry_dialog.vuz.setEditable(True)
        self.ui_create_entry_dialog.codvuz.setEditable(True)
        self.ui_create_entry_dialog.grnti.setValidator(QIntValidator(0, 99999999))
        self.ui_create_entry_dialog.grnti.textChanged.connect(self.validate_grnti_prefix)

        self.ui_create_entry_dialog.grnti.textChanged.connect(self.auto_insert_dots)
        regex = QRegularExpression(r"^[a-zA-Zа-яА-ЯёЁ\s]+$")  # Разрешаем только буквы и пробелы
        validator = QRegularExpressionValidator(regex, self.ui_create_entry_dialog.nir_ruk)
        self.ui_create_entry_dialog.nir_ruk.setValidator(validator)
        validator_1 = QRegularExpressionValidator(regex, self.ui_create_entry_dialog.ruk_doljnost)
        self.ui_create_entry_dialog.ruk_doljnost.setValidator(validator_1)
        validator_2 = QRegularExpressionValidator(regex, self.ui_create_entry_dialog.ruk_zvanie)
        self.ui_create_entry_dialog.ruk_zvanie.setValidator(validator_2)
        validator_3 = QRegularExpressionValidator(regex, self.ui_create_entry_dialog.ruk_stepen)
        self.ui_create_entry_dialog.ruk_stepen.setValidator(validator_3)

        Data.close_connection()
        with Session() as session:
        # Извлекаем все записи из таблицы Vuz
            vuz_records = session.query(VuzBase).all()
        Data.create_connection()
        # Заполняем оба ComboBox
        for vuz in vuz_records:
            self.ui_create_entry_dialog.vuz.addItem(vuz.z1, str(vuz.codvuz))
            self.ui_create_entry_dialog.codvuz.addItem(str(vuz.codvuz), vuz.z1)

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

        self.ui_create_entry_dialog.codvuz.setCurrentText(str(row_data[1]))
        self.ui_create_entry_dialog.priznak.setCurrentText(prizn[row_data[2]])
        self.ui_create_entry_dialog.reg_number.setText(row_data[3])
        self.ui_create_entry_dialog.nir_name.setText(row_data[4])
        self.ui_create_entry_dialog.grnti.setText(row_data[5])
        self.ui_create_entry_dialog.nir_ruk.setText(row_data[6])
        self.ui_create_entry_dialog.ruk_doljnost.setText(row_data[7])
        self.ui_create_entry_dialog.ruk_zvanie.setText(row_data[8])
        self.ui_create_entry_dialog.ruk_stepen.setText(row_data[9])
        self.ui_create_entry_dialog.exponat_est.setCurrentText(exp_est[row_data[10]])
        self.ui_create_entry_dialog.vistavka.setText(row_data[11])
        self.ui_create_entry_dialog.exponat_name.setText(row_data[12])

        # Заполняем ComboBox значениями
        vuz_list = [vuz.z1 for vuz in vuz_records]
        codvuz_list = [str(vuz.codvuz) for vuz in vuz_records]

        # self.ui_create_entry_dialog.vuz.addItems(vuz_list)
        # self.ui_create_entry_dialog.codvuz.addItems(codvuz_list)

        # Настройка комплитеров после заполнения ComboBox
        vuz_completer = QCompleter(vuz_list, self.ui_create_entry_dialog.vuz)
        codvuz_completer = QCompleter(codvuz_list, self.ui_create_entry_dialog.codvuz)

        vuz_completer.setCompletionMode(QCompleter.CompletionMode.PopupCompletion)
        codvuz_completer.setCompletionMode(QCompleter.CompletionMode.PopupCompletion)

        self.ui_create_entry_dialog.vuz.setCompleter(vuz_completer)
        self.ui_create_entry_dialog.codvuz.setCompleter(codvuz_completer)

        # Ограничиваем ввод только существующими значениями
        self.ui_create_entry_dialog.vuz.lineEdit().editingFinished.connect(self.validate_vuz_input)
        self.ui_create_entry_dialog.codvuz.lineEdit().editingFinished.connect(self.validate_codvuz_input)

        # Регулярное выражение для разрешения только букв в nir_ruk
        regex = QRegularExpression(r"^[a-zA-Zа-яА-ЯёЁ\s]+$")
        validator = QRegularExpressionValidator(regex, self.ui_create_entry_dialog.nir_ruk)
        self.ui_create_entry_dialog.nir_ruk.setValidator(validator)

        Data.close_connection()
        current_obj = VystMoBase.get_by_name_2(row_data[1], row_data[3])
        Data.create_connection()
        print(row_data[1], row_data[3])
        print(current_obj)

        self.ui_create_entry_dialog.save_btn.clicked.connect(self.update_vyst_entry)
        self.current_obj = current_obj
        self.new_dialog.setFixedSize(561, 664)
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
        codvuz = self.ui_create_entry_dialog.codvuz.currentText()
        priznak = prizn[self.ui_create_entry_dialog.priznak.currentText()]
        reg_number = self.ui_create_entry_dialog.reg_number.text()
        nir_name = self.ui_create_entry_dialog.nir_name.text()
        grnti = self.ui_create_entry_dialog.grnti.text()
        nir_ruk = self.ui_create_entry_dialog.nir_ruk.text()
        ruk_doljnost = self.ui_create_entry_dialog.ruk_doljnost.text()
        ruk_zvanie = self.ui_create_entry_dialog.ruk_zvanie.text()
        ruk_stepen = self.ui_create_entry_dialog.ruk_stepen.text()
        exponat_est = exp_est[self.ui_create_entry_dialog.exponat_est.currentText()]
        vistavka = self.ui_create_entry_dialog.vistavka.text()
        exponat_name = self.ui_create_entry_dialog.exponat_name.text()

        Data.close_connection()

        # new_vyst = ExpositionBase(codvuz=codvuz, type=priznak, regnumber=reg_number, subject=nir_name,
        #                           grnti=grnti, bossname=nir_ruk, boss_position=ruk_doljnost,
        #                           boss_academic_rank=ruk_zvanie, boss_scientific_degree=ruk_stepen,
        #                           exhitype=exponat_est, vystavki=vistavka, exponat=exponat_name)

        with Session() as session:
            try:
                current_obj.codvuz = codvuz
                # print(codvuz)
                current_obj.type = priznak
                # print(priznak)
                current_obj.regnumber = reg_number
                # print(reg_number)
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

        self.new_dialog.close()

    def create_vyst_entry(self):
        exp_est = {
            "Есть": "Е",
            "Планируется": "П",
            "Нет": "Н"
        }
        prizn = {
            "Тематический план": "Е",
            "НТП": "М"
        }
        codvuz = self.ui_create_entry_dialog.codvuz.currentText()
        priznak = prizn[self.ui_create_entry_dialog.priznak.currentText()]
        reg_number = self.ui_create_entry_dialog.reg_number.text()
        nir_name = self.ui_create_entry_dialog.nir_name.text()
        grnti = self.ui_create_entry_dialog.grnti.text()
        nir_ruk = self.ui_create_entry_dialog.grnti.text()
        ruk_doljnost = self.ui_create_entry_dialog.ruk_doljnost.text()
        ruk_zvanie = self.ui_create_entry_dialog.ruk_zvanie.text()
        ruk_stepen = self.ui_create_entry_dialog.ruk_stepen.text()
        exponat_est = exp_est[self.ui_create_entry_dialog.exponat_est.currentText()]
        vistavka = self.ui_create_entry_dialog.vistavka.text()
        exponat_name = self.ui_create_entry_dialog.exponat_name.text()

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

        self.new_dialog.close()

    def open_delete_confirm_dialog(self, row_numbers):
        self.confirm_dialog = QDialog() # Теперь должно работать
        self.ui_confirm_dialog = Ui_Dialog()
        self.ui_confirm_dialog.setupUi(self.confirm_dialog)

        # Формируем текст с номерами строк
        row_numbers_str = ", ".join(str(number) for number in row_numbers)
        self.ui_confirm_dialog.label.setText(f"Удалить строки с номером {row_numbers_str}?")

        # Подключаем кнопку "OK" к функции delete_record
        self.ui_confirm_dialog.buttonBox.accepted.connect(lambda: self.delete_record(row_numbers))

        # Подключаем кнопку "Cancel" для закрытия диалога
        self.ui_confirm_dialog.buttonBox.rejected.connect(self.confirm_dialog.close)
        self.confirm_dialog.exec_()
        self.confirm_dialog.setModal(True)

    def delete_record(self, row_numbers):
        # Получаем текущий виджет QTableView
        current_table = self.ui.db_tables.currentWidget().children()[1]

        if isinstance(current_table, QTableView):
            model = current_table.model() # Получаем модель таблицы
        # Удаляем строки в обратном порядке, чтобы индексы не смещались
            for row_number in sorted(row_numbers, reverse=True):
                model.removeRow(row_number - 1) # Удаляем строку
            model.submitAll() # Применяем изменения
            model.select() # Обновляем данные в таблице

        self.confirm_dialog.close() # Закрываем диалог

    def init_tables(self):
        # self.models = {
        #     "vyst_mo_table": self.create_model("vyst_mo"),
        #     "vuz_table": self.create_model("VUZ"),
        #     "grntirub_table": self.create_model("grntirub")
        # }
        self.vyst_mo_table_model = self.create_model("vyst_mo")
        self.vuz_table_model = self.create_model("vuz")
        self.grntirub_table_model = self.create_model("grnti")
        self.svod_table_model = self.create_model("svod")

        # Устанавливаем модели и заголовки
        self.ui.vyst_mo_table.setModel(self.vyst_mo_table_model)
        self.ui.vuz_table.setModel(self.vuz_table_model)
        self.ui.grntirub_table.setModel(self.grntirub_table_model)
        self.ui.svod_table.setModel(self.svod_table_model)

        self.ui.svod_table.hideColumn(0)
        self.ui.vyst_mo_table.hideColumn(0)
        self.ui.grntirub_table.hideColumn(0)
        self.ui.vuz_table.hideColumn(0)

        # Отключаем сортировку по заголовкам при первом выводе
        self.ui.vyst_mo_table.setSortingEnabled(False)
        self.ui.vuz_table.setSortingEnabled(False)
        self.ui.grntirub_table.setSortingEnabled(False)
        self.ui.svod_table.setSortingEnabled(False)

        # Настройка заголовков
        self.set_custom_headers(self.vyst_mo_table_model, ["Код ВУЗа",
                                                           "Пр-к  ф. НИР", "Рег. ном. НИР", "Наименование НИР",
                                                           "Коды  ГРНТИ", "Руководитель НИР", "Должность",
                                                           "Ученое звание", "Ученая степень",
                                                           "Пр-к", "Выставки", "Выставочный экспонат"])

        self.set_custom_headers(self.vuz_table_model,
                                ["Код ВУЗа", "Название ВУЗа", "Полное наименование", "Сокр. наим.",
                                 "Федеральный округ", 'Город', "Статус", "№ обл.", "Область", "Категория", "Профиль"])

        self.set_custom_headers(self.grntirub_table_model, ["Код рубрики", "Наименование рубрики"])
        self.set_custom_headers(self.svod_table_model, ["Код ВУЗа", "Сокр. наим. ВУЗа",
                                                        "Наименование НИР", "Коды  ГРНТИ", "Рубрики ГРНТИ", "Руководитель НИР",
                                                        "Должность", "Ученое звание", "Ученая степень",
                                                        "Рег. номер НИР", "Выставки", "Выставочный экспонат",
                                                        "Признак  формы НИР", "Признак", "Название ВУЗа",
                                                        "Полное наименование",
                                                        "Федеральный округ", 'Город', "Статус", "Номер области",
                                                        "Область", "Категория", "Профиль"
                                                        ])

        self.ui.vyst_mo_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.ui.vuz_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.ui.grntirub_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.ui.svod_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

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
            #плавная прокрутка
            table.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)

            header = table.horizontalHeader()

            #ширину столбцов подстраивает
            font_metrics = QFontMetrics(table.font())

            header.setSectionResizeMode(QHeaderView.ResizeMode.Fixed)

            for col in range(header.count()):
                header_text = table.model().headerData(col, Qt.Orientation.Horizontal)
                header_width = font_metrics.horizontalAdvance(header_text) + 20
                table.setColumnWidth(col, header_width)

            header.setSectionResizeMode(QHeaderView.ResizeMode.Interactive)
            header.setStretchLastSection(False)
            table.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)

        # self.ui.vyst_mo_table.setColumnHidden(10, True)
        self.ui.vyst_mo_table.setEditTriggers(QAbstractItemView.EditTrigger.AllEditTriggers)

        while self.vyst_mo_table_model.canFetchMore():
            self.vyst_mo_table_model.fetchMore()

    def set_current_table(self, checked_action):
        """Switches the current table and resets the filters."""
        # Очистка полей ввода фильтров при переключении таблиц
        self.clear_filter_input_fields()

        # Смена таблицы
        text = checked_action.text()
        if text == "ГРНТИ":
            self.ui.db_tables.setCurrentIndex(3)
            self.current_model = self.grntirub_table_model
            self.ui.create_btn.setEnabled(True)
            self.ui.update_btn.setEnabled(True)
            self.ui.delete_btn.setEnabled(True)
            # print(self.get_column_values(self.ui.grntirub_table, "Код рубрики"))
        elif text == "Выставки":
            self.ui.db_tables.setCurrentIndex(1)
            self.current_model = self.vyst_mo_table_model
            self.ui.create_btn.setEnabled(True)
            self.ui.update_btn.setEnabled(True)
            self.ui.delete_btn.setEnabled(True)
            # print(self.get_column_values(self.ui.vyst_mo_table, "Признак  формы НИР"))
        elif text == "ВУЗы":
            self.ui.db_tables.setCurrentIndex(2)
            self.current_model = self.vuz_table_model
            self.ui.create_btn.setEnabled(True)
            self.ui.update_btn.setEnabled(True)
            self.ui.delete_btn.setEnabled(True)
            # print(self.get_column_values(self.ui.vuz_table, "Полное наименование"))
        elif text == "Сводная таблица":
            self.ui.db_tables.setCurrentIndex(0)
            self.current_model = self.svod_table_model
            self.ui.create_btn.setEnabled(False)
            self.ui.update_btn.setEnabled(False)
            self.ui.delete_btn.setEnabled(False)
            # print(self.get_column_values(self.ui.svod_table, "Руководитель НИР"))

            #TODO ATTENTION ТЫ ТЕСТИРОВАЛ НОЧЬЮ ФУНКЦИЮ GET_COLUMN_VALUES, ОНА РАБОТАЕТ, НО ПОЧЕМУ ТО 2 РАЗА ВЫВОДИЛА КОРОЧЕ РЕЗУЛЬТАТ,
            #СКОРЕЕ ВСЕГО СВЯЗАНО С КНОПКОЙ МЕНЮ

        # Обновление комбобокса с доступными колонками для фильтрации
        self.update_filter_combobox()

        # Показываем все строки при переключении таблиц
        self.show_all_rows()

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
        self.filter_table(filter_conditions)

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

    @staticmethod
    def set_custom_headers(model, headers):
        for index, header in enumerate(headers):
            model.setHeaderData(index + 1, Qt.Orientation.Horizontal, header)

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

    def delete_button_action(self):
        current_widget = self.ui.db_tables.currentWidget() # Получаем текущий виджет
        if current_widget is not None: # Проверяем, что текущий виджет существует
            current_table: QTableView = current_widget.children()[1] # Получаем второй дочерний элемент

            if isinstance(current_table, QTableView):
                selected_rows = current_table.selectionModel().selectedRows()

                if selected_rows:
                    row_numbers = [row.row() + 1 for row in selected_rows]
                    self.open_delete_confirm_dialog(row_numbers) # Передаем список номеров строк
                else:
                    QMessageBox.warning(self, "Ошибка", "Выберите строки в таблице.")
            else:
                QMessageBox.warning(self, "Ошибка", "Текущий виджет не является таблицей.")
        else:
            QMessageBox.warning(self, "Ошибка", "Нет активного виджета.")

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Выход', "Вы уверены, что хотите выйти?", QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)

        if reply == QMessageBox.Yes:
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
        if filter_name in self.filter_fields:
            layout_to_remove = self.filter_fields.pop(filter_name)

            # Удаляем элементы интерфейса
            for i in reversed(range(layout_to_remove.count())):
                widget = layout_to_remove.itemAt(i).widget()
                if widget is not None:
                    widget.setParent(None)

            # Перестроение сетки после удаления
            self.rebuild_filter_grid()


class NonEditableSqlTableModel(QSqlTableModel):
    def flags(self, index):
        return Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Data.create_connection()  # Устанавливаем соединение один раз в начале
    window = ExponatDBMS()
    window.show()
    sys.exit(app.exec())
