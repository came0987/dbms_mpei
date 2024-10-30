import PySide6
from PySide6.QtCore import QAbstractTableModel, Qt


class CustomTableModel(QAbstractTableModel):
    def __init__(self, session, model, parent=None):
        super().__init__(parent)
        self.model = model
        self.session = session
        self.loadData()

    def loadData(self):
        # Запрашиваем все записи из таблицы vuz
        self.data = self.session.query(self.model).all()
        self.layoutChanged.emit()  # Обновляет данные таблицы при изменении

    def rowCount(self, parent=None):
        return len(self.data)

    def columnCount(self, parent=None):
        return len(self.model.__table__.columns)

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if not index.isValid():
            return None
        if role == Qt.ItemDataRole.DisplayRole:
            row = self.data[index.row()]
            column_name = list(self.model.__table__.columns.keys())[index.column()]
            return getattr(row, column_name)
        return None

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return list(self.model.__table__.columns.keys())[section]
            elif orientation == Qt.Orientation.Vertical:
                return section + 1
        return None
