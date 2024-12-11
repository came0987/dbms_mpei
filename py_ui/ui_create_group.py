# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_group.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_create_group_dialog(object):
    def setupUi(self, create_group_dialog):
        if not create_group_dialog.objectName():
            create_group_dialog.setObjectName(u"create_group_dialog")
        create_group_dialog.resize(310, 209)
        self.group_name = QLineEdit(create_group_dialog)
        self.group_name.setObjectName(u"group_name")
        self.group_name.setGeometry(QRect(20, 110, 271, 41))
        font = QFont()
        font.setPointSize(12)
        self.group_name.setFont(font)
        self.save_btn = QPushButton(create_group_dialog)
        self.save_btn.setObjectName(u"save_btn")
        self.save_btn.setGeometry(QRect(210, 170, 81, 31))
        self.label = QLabel(create_group_dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 80, 121, 31))
        font1 = QFont()
        font1.setPointSize(11)
        self.label.setFont(font1)
        self.label_2 = QLabel(create_group_dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 10, 231, 51))
        font2 = QFont()
        font2.setPointSize(14)
        self.label_2.setFont(font2)
        self.error_text = QLabel(create_group_dialog)
        self.error_text.setObjectName(u"error_text")
        self.error_text.setGeometry(QRect(20, 150, 271, 16))
        self.error_text.setStyleSheet(u"color: rgb(255, 0, 0)")

        self.retranslateUi(create_group_dialog)

        QMetaObject.connectSlotsByName(create_group_dialog)
    # setupUi

    def retranslateUi(self, create_group_dialog):
        create_group_dialog.setWindowTitle(QCoreApplication.translate("create_group_dialog", u"Dialog", None))
        self.group_name.setText("")
        self.group_name.setPlaceholderText(QCoreApplication.translate("create_group_dialog", u"\u0413\u0440\u0443\u043f\u043f\u0430 7", None))
        self.save_btn.setText(QCoreApplication.translate("create_group_dialog", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("create_group_dialog", u"\u0418\u043c\u044f \u0433\u0440\u0443\u043f\u043f\u044b", None))
        self.label_2.setText(QCoreApplication.translate("create_group_dialog", u"\u0421\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u043d\u043e\u0432\u043e\u0439 \u0433\u0440\u0443\u043f\u043f\u044b", None))
        self.error_text.setText("")
    # retranslateUi

