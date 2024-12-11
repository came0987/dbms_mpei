# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_to_group_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_add_to_group_dialog(object):
    def setupUi(self, add_to_group_dialog):
        if not add_to_group_dialog.objectName():
            add_to_group_dialog.setObjectName(u"add_to_group_dialog")
        add_to_group_dialog.resize(401, 249)
        self.buttonBox = QDialogButtonBox(add_to_group_dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(20, 200, 361, 41))
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.create_new_group_btn = QPushButton(add_to_group_dialog)
        self.create_new_group_btn.setObjectName(u"create_new_group_btn")
        self.create_new_group_btn.setGeometry(QRect(20, 80, 171, 31))
        font = QFont()
        font.setPointSize(11)
        self.create_new_group_btn.setFont(font)
        self.label = QLabel(add_to_group_dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 20, 281, 41))
        font1 = QFont()
        font1.setPointSize(14)
        self.label.setFont(font1)
        self.widget = QWidget(add_to_group_dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 130, 361, 53))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout.addWidget(self.label_2)


        self.retranslateUi(add_to_group_dialog)
        self.buttonBox.accepted.connect(add_to_group_dialog.accept)
        self.buttonBox.rejected.connect(add_to_group_dialog.reject)

        QMetaObject.connectSlotsByName(add_to_group_dialog)
    # setupUi

    def retranslateUi(self, add_to_group_dialog):
        add_to_group_dialog.setWindowTitle(QCoreApplication.translate("add_to_group_dialog", u"Dialog", None))
        self.create_new_group_btn.setText(QCoreApplication.translate("add_to_group_dialog", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043d\u043e\u0432\u0443\u044e \u0433\u0440\u0443\u043f\u043f\u0443", None))
        self.label.setText(QCoreApplication.translate("add_to_group_dialog", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0437\u0430\u043f\u0438\u0441\u0435\u0439 \u0432 \u0433\u0440\u0443\u043f\u043f\u0443", None))
        self.label_2.setText(QCoreApplication.translate("add_to_group_dialog", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0433\u0440\u0443\u043f\u043f\u0443", None))
    # retranslateUi

