# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_grnti.ui'
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
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(340, 263)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 10, 251, 41))
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 220, 91, 31))
        font1 = QFont()
        font1.setPointSize(12)
        self.pushButton.setFont(font1)
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 140, 301, 56))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.verticalLayout.addWidget(self.label_3)

        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setFont(font1)

        self.verticalLayout.addWidget(self.lineEdit_2)

        self.widget1 = QWidget(Dialog)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(20, 80, 151, 56))
        self.verticalLayout_2 = QVBoxLayout(self.widget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_2)

        self.lineEdit = QLineEdit(self.widget1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setFont(font1)

        self.verticalLayout_2.addWidget(self.lineEdit)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043d\u043e\u0432\u043e\u0433\u043e \u0413\u0420\u041d\u0422\u0418", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0440\u0443\u0431\u0440\u0438\u043a\u0438", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0418\u0441\u0442\u043e\u0440\u0438\u044f \u0434\u0440\u0435\u0432\u043d\u0435\u0439 \u0410\u0442\u043b\u0430\u043d\u0442\u0438\u0434\u044b", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u0434 \u0413\u0420\u041d\u0422\u0418", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"02", None))
    # retranslateUi

