from PySide6.QtWidgets import QComboBox

from connection import Session, Data
from table_models import GroupListBase


class SearchableComboBox(QComboBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setEditable(True)
        self.setInsertPolicy(QComboBox.InsertPolicy.NoInsert)
        self._is_updating = False
        self.lineEdit().textChanged.connect(self.update_items)
        # Первоначальная загрузка записей
        self.refresh_items("")

    def refresh_items(self, search_text):
        print("пук")
        # self.blockSignals(True)
        self._is_updating = True
        self.clear()
        self.addItem("Добавить новую запись")  # Добавляем элемент кнопки
        current_text = self.lineEdit().text()

        Data.close_connection()
        with Session() as session:
        # Запрос к базе данных
            query = session.query(GroupListBase)
            if search_text:
                query = query.filter(GroupListBase.ui_table_name.ilike(f"%{search_text}%"))  # Фильтр по имени
            query = query.limit(20)  # Ограничение на 20 записей
            records = query.all()
        Data.create_connection()

        if records:
            for record in records:
                self.addItem(record.ui_table_name)  # Предполагается, что в GroupList есть поле name
        else:
            self.addItem("Нет данных")  # Сообщение, если ничего не найдено

        # self.blockSignals(False)
        self.lineEdit().blockSignals(True)
        self.lineEdit().setText(current_text)
        self.lineEdit().blockSignals(False)
        self._is_updating = False

    def update_items(self, text):
        if not self._is_updating:
            self.refresh_items(text)


class FilterComboBox(QComboBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setEditable(True)
        # self.items = items
        # self.addItems(items)

        # Сохранение последнего валидного выбора
        self.last_valid_text = ""

        # Подключаем фильтрацию
        # self.lineEdit().textEdited.connect(self.filter_items)
        self.lineEdit().editingFinished.connect(self.validate_text)

        self.add_items()


    def get_items(self):
        Data.close_connection()
        with Session() as session:
            # Запрос к базе данных
            records = session.query(GroupListBase.ui_table_name).all()  # Фильтр по имени
        Data.create_connection()
        return records

    def add_items(self):
        records = self.get_items()

        if records:
            for record in records:
                self.addItem(record.ui_table_name)  # Предполагается, что в GroupList есть поле name
        else:
            self.addItem("Нет данных")  # Сообщение, если ничего не найдено


    # def filter_items(self, text):
    #     """Фильтруем список в зависимости от введённого текста."""
    #     items = self.get_items()
    #
    #     self.clear()
    #     filtered_items = [item for item in items if text.lower() in item.lower()]
    #     self.addItems(filtered_items)
    #     # Показываем совпадения
    #     if filtered_items:
    #         self.showPopup()

    def validate_text(self):
        """Проверяем, введено ли допустимое значение."""
        items = self.get_items()

        current_text = self.currentText()
        if current_text not in items:
            # Если введённое значение недопустимо, возвращаемся к последнему валидному
            self.setCurrentText(self.last_valid_text)
        else:
            # Обновляем последнее валидное значение
            self.last_valid_text = current_text