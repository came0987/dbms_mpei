# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_create_vistavka_entry.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_add_zapis_dialog(object):
    def setupUi(self, add_zapis_dialog):
        if not add_zapis_dialog.objectName():
            add_zapis_dialog.setObjectName(u"add_zapis_dialog")
        add_zapis_dialog.resize(571, 468)
        self.label = QLabel(add_zapis_dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 10, 341, 31))
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pushButton = QPushButton(add_zapis_dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 430, 121, 31))
        font1 = QFont()
        font1.setPointSize(11)
        self.pushButton.setFont(font1)
        self.layoutWidget = QWidget(add_zapis_dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 50, 551, 371))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.comboBox = QComboBox(self.layoutWidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        font2 = QFont()
        font2.setPointSize(12)
        self.comboBox.setFont(font2)
        self.comboBox.setEditable(False)

        self.verticalLayout_2.addWidget(self.comboBox)

        self.comboBox_2 = QComboBox(self.layoutWidget)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setFont(font2)

        self.verticalLayout_2.addWidget(self.comboBox_2)

        self.lineEdit = QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setFont(font2)

        self.verticalLayout_2.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setFont(font2)

        self.verticalLayout_2.addWidget(self.lineEdit_2)

        self.lineEdit_3 = QLineEdit(self.layoutWidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setFont(font2)

        self.verticalLayout_2.addWidget(self.lineEdit_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit_4 = QLineEdit(self.layoutWidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setFont(font2)

        self.horizontalLayout.addWidget(self.lineEdit_4)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lineEdit_5 = QLineEdit(self.layoutWidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setFont(font2)

        self.verticalLayout.addWidget(self.lineEdit_5)

        self.lineEdit_6 = QLineEdit(self.layoutWidget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setFont(font2)

        self.verticalLayout.addWidget(self.lineEdit_6)

        self.lineEdit_7 = QLineEdit(self.layoutWidget)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setFont(font2)

        self.verticalLayout.addWidget(self.lineEdit_7)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.comboBox_3 = QComboBox(self.layoutWidget)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setFont(font2)

        self.verticalLayout_2.addWidget(self.comboBox_3)

        self.lineEdit_8 = QLineEdit(self.layoutWidget)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setFont(font2)

        self.verticalLayout_2.addWidget(self.lineEdit_8)

        self.lineEdit_9 = QLineEdit(self.layoutWidget)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setFont(font2)

        self.verticalLayout_2.addWidget(self.lineEdit_9)


        self.retranslateUi(add_zapis_dialog)

        QMetaObject.connectSlotsByName(add_zapis_dialog)
    # setupUi

    def retranslateUi(self, add_zapis_dialog):
        add_zapis_dialog.setWindowTitle("")
        self.label.setText(QCoreApplication.translate("add_zapis_dialog", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0437\u0430\u043f\u0438\u0441\u0438", None))
        self.pushButton.setText(QCoreApplication.translate("add_zapis_dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("add_zapis_dialog", u"1111", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("add_zapis_dialog", u"2222", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("add_zapis_dialog", u"11222", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("add_zapis_dialog", u"11123", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("add_zapis_dialog", u"3333", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("add_zapis_dialog", u"22233", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("add_zapis_dialog", u"2222344", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("add_zapis_dialog", u"3343", None))

        self.comboBox.setPlaceholderText(QCoreApplication.translate("add_zapis_dialog", u"\u0412\u0423\u0417", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("add_zapis_dialog", u"\u0415", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("add_zapis_dialog", u"\u041c", None))

        self.comboBox_2.setPlaceholderText(QCoreApplication.translate("add_zapis_dialog", u"\u041f\u0440\u0438\u0437\u043d\u0430\u043a \u0444\u043e\u0440\u043c\u044b \u041d\u0418\u0420", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("add_zapis_dialog", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u043e\u043d\u043d\u043d\u044b\u0439 \u043d\u043e\u043c\u0435\u0440 \u041d\u0418\u0420", None))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("add_zapis_dialog", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u041d\u0418\u0420", None))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("add_zapis_dialog", u"\u041a\u043e\u0434 \u0413\u0420\u041d\u0422\u0418", None))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("add_zapis_dialog", u"\u0420\u0443\u043a\u043e\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044c \u041d\u0418\u0420", None))
        self.lineEdit_5.setText("")
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("add_zapis_dialog", u"\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c \u0440\u0443\u043a\u043e\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044f", None))
        self.lineEdit_6.setText("")
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("add_zapis_dialog", u"\u0423\u0447\u0435\u043d\u043e\u0435 \u0437\u0432\u0430\u043d\u0438\u0435 \u0440\u0443\u043a\u043e\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044f", None))
        self.lineEdit_7.setText("")
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("add_zapis_dialog", u"\u0423\u0447\u0435\u043d\u0430\u044f \u0441\u0442\u0435\u043f\u0435\u043d\u044c \u0440\u0443\u043a\u043e\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044f", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("add_zapis_dialog", u"\u0415\u0441\u0442\u044c", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("add_zapis_dialog", u"\u041f\u043b\u0430\u043d\u0438\u0440\u0443\u0435\u0442\u0441\u044f", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("add_zapis_dialog", u"\u041d\u0435\u0442", None))

        self.comboBox_3.setPlaceholderText(QCoreApplication.translate("add_zapis_dialog", u"\u041d\u0430\u043b\u0438\u0447\u0438\u0435 \u044d\u043a\u0441\u043f\u043e\u043d\u0430\u0442\u0430", None))
        self.lineEdit_8.setText("")
        self.lineEdit_8.setPlaceholderText(QCoreApplication.translate("add_zapis_dialog", u"\u0412\u044b\u0441\u0442\u0430\u0432\u043a\u0430", None))
        self.lineEdit_9.setText("")
        self.lineEdit_9.setPlaceholderText(QCoreApplication.translate("add_zapis_dialog", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u042d\u043a\u0441\u043f\u043e\u043d\u0430\u0442\u0430", None))
    # retranslateUi

