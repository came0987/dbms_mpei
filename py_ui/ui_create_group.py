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
from PySide6.QtWidgets import (QApplication, QDialog, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_create_group_dialog(object):
    def setupUi(self, create_group_dialog):
        if not create_group_dialog.objectName():
            create_group_dialog.setObjectName(u"create_group_dialog")
        create_group_dialog.resize(363, 121)
        self.lineEdit = QLineEdit(create_group_dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(40, 30, 271, 41))
        font = QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.pushButton = QPushButton(create_group_dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(130, 80, 81, 31))

        self.retranslateUi(create_group_dialog)

        QMetaObject.connectSlotsByName(create_group_dialog)
    # setupUi

    def retranslateUi(self, create_group_dialog):
        create_group_dialog.setWindowTitle(QCoreApplication.translate("create_group_dialog", u"Dialog", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("create_group_dialog", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043d\u043e\u0432\u043e\u0439 \u0433\u0440\u0443\u043f\u043f\u044b", None))
        self.pushButton.setText(QCoreApplication.translate("create_group_dialog", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
    # retranslateUi

