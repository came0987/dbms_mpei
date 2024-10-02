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
        self.save_btn = QPushButton(add_zapis_dialog)
        self.save_btn.setObjectName(u"save_btn")
        self.save_btn.setGeometry(QRect(10, 430, 121, 31))
        font1 = QFont()
        font1.setPointSize(11)
        self.save_btn.setFont(font1)
        self.layoutWidget = QWidget(add_zapis_dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 50, 551, 371))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.vuz = QComboBox(self.layoutWidget)
        self.vuz.addItem("")
        self.vuz.addItem("")
        self.vuz.addItem("")
        self.vuz.addItem("")
        self.vuz.addItem("")
        self.vuz.addItem("")
        self.vuz.addItem("")
        self.vuz.addItem("")
        self.vuz.setObjectName(u"vuz")
        font2 = QFont()
        font2.setPointSize(12)
        self.vuz.setFont(font2)
        self.vuz.setEditable(False)

        self.verticalLayout_2.addWidget(self.vuz)

        self.priznak = QComboBox(self.layoutWidget)
        self.priznak.addItem("")
        self.priznak.addItem("")
        self.priznak.setObjectName(u"priznak")
        self.priznak.setFont(font2)

        self.verticalLayout_2.addWidget(self.priznak)

        self.reg_number = QLineEdit(self.layoutWidget)
        self.reg_number.setObjectName(u"reg_number")
        self.reg_number.setFont(font2)

        self.verticalLayout_2.addWidget(self.reg_number)

        self.nir_name = QLineEdit(self.layoutWidget)
        self.nir_name.setObjectName(u"nir_name")
        self.nir_name.setFont(font2)

        self.verticalLayout_2.addWidget(self.nir_name)

        self.grnti = QLineEdit(self.layoutWidget)
        self.grnti.setObjectName(u"grnti")
        self.grnti.setFont(font2)

        self.verticalLayout_2.addWidget(self.grnti)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.nir_ruk = QLineEdit(self.layoutWidget)
        self.nir_ruk.setObjectName(u"nir_ruk")
        self.nir_ruk.setFont(font2)

        self.horizontalLayout.addWidget(self.nir_ruk)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.ruk_doljnost = QLineEdit(self.layoutWidget)
        self.ruk_doljnost.setObjectName(u"ruk_doljnost")
        self.ruk_doljnost.setFont(font2)

        self.verticalLayout.addWidget(self.ruk_doljnost)

        self.ruk_zvanie = QLineEdit(self.layoutWidget)
        self.ruk_zvanie.setObjectName(u"ruk_zvanie")
        self.ruk_zvanie.setFont(font2)

        self.verticalLayout.addWidget(self.ruk_zvanie)

        self.ruk_stepen = QLineEdit(self.layoutWidget)
        self.ruk_stepen.setObjectName(u"ruk_stepen")
        self.ruk_stepen.setFont(font2)

        self.verticalLayout.addWidget(self.ruk_stepen)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.exponat_est = QComboBox(self.layoutWidget)
        self.exponat_est.addItem("")
        self.exponat_est.addItem("")
        self.exponat_est.addItem("")
        self.exponat_est.setObjectName(u"exponat_est")
        self.exponat_est.setFont(font2)

        self.verticalLayout_2.addWidget(self.exponat_est)

        self.vistavka = QLineEdit(self.layoutWidget)
        self.vistavka.setObjectName(u"vistavka")
        self.vistavka.setFont(font2)

        self.verticalLayout_2.addWidget(self.vistavka)

        self.exponat_name = QLineEdit(self.layoutWidget)
        self.exponat_name.setObjectName(u"exponat_name")
        self.exponat_name.setFont(font2)

        self.verticalLayout_2.addWidget(self.exponat_name)


        self.retranslateUi(add_zapis_dialog)

        QMetaObject.connectSlotsByName(add_zapis_dialog)
    # setupUi

    def retranslateUi(self, add_zapis_dialog):
        add_zapis_dialog.setWindowTitle("")
        self.label.setText(QCoreApplication.translate("add_zapis_dialog", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0437\u0430\u043f\u0438\u0441\u0438", None))
        self.save_btn.setText(QCoreApplication.translate("add_zapis_dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.vuz.setItemText(0, QCoreApplication.translate("add_zapis_dialog", u"1111", None))
        self.vuz.setItemText(1, QCoreApplication.translate("add_zapis_dialog", u"2222", None))
        self.vuz.setItemText(2, QCoreApplication.translate("add_zapis_dialog", u"11222", None))
        self.vuz.setItemText(3, QCoreApplication.translate("add_zapis_dialog", u"11123", None))
        self.vuz.setItemText(4, QCoreApplication.translate("add_zapis_dialog", u"3333", None))
        self.vuz.setItemText(5, QCoreApplication.translate("add_zapis_dialog", u"22233", None))
        self.vuz.setItemText(6, QCoreApplication.translate("add_zapis_dialog", u"2222344", None))
        self.vuz.setItemText(7, QCoreApplication.translate("add_zapis_dialog", u"3343", None))

        self.vuz.setPlaceholderText(QCoreApplication.translate("add_zapis_dialog", u"\u0412\u0423\u0417", None))
        self.priznak.setItemText(0, QCoreApplication.translate("add_zapis_dialog", u"\u0415", None))
        self.priznak.setItemText(1, QCoreApplication.translate("add_zapis_dialog", u"\u041c", None))

        self.priznak.setPlaceholderText(QCoreApplication.translate("add_zapis_dialog", u"\u041f\u0440\u0438\u0437\u043d\u0430\u043a \u0444\u043e\u0440\u043c\u044b \u041d\u0418\u0420", None))
        self.reg_number.setText("")
        self.reg_number.setPlaceholderText(QCoreApplication.translate("add_zapis_dialog", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u043e\u043d\u043d\u043d\u044b\u0439 \u043d\u043e\u043c\u0435\u0440 \u041d\u0418\u0420", None))
        self.nir_name.setText("")
        self.nir_name.setPlaceholderText(QCoreApplication.translate("add_zapis_dialog", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u041d\u0418\u0420", None))
        self.grnti.setText("")
        self.grnti.setPlaceholderText(QCoreApplication.translate("add_zapis_dialog", u"\u041a\u043e\u0434 \u0413\u0420\u041d\u0422\u0418", None))
        self.nir_ruk.setText("")
        self.nir_ruk.setPlaceholderText(QCoreApplication.translate("add_zapis_dialog", u"\u0420\u0443\u043a\u043e\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044c \u041d\u0418\u0420", None))
        self.ruk_doljnost.setText("")
        self.ruk_doljnost.setPlaceholderText(QCoreApplication.translate("add_zapis_dialog", u"\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c \u0440\u0443\u043a\u043e\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044f", None))
        self.ruk_zvanie.setText("")
        self.ruk_zvanie.setPlaceholderText(QCoreApplication.translate("add_zapis_dialog", u"\u0423\u0447\u0435\u043d\u043e\u0435 \u0437\u0432\u0430\u043d\u0438\u0435 \u0440\u0443\u043a\u043e\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044f", None))
        self.ruk_stepen.setText("")
        self.ruk_stepen.setPlaceholderText(QCoreApplication.translate("add_zapis_dialog", u"\u0423\u0447\u0435\u043d\u0430\u044f \u0441\u0442\u0435\u043f\u0435\u043d\u044c \u0440\u0443\u043a\u043e\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044f", None))
        self.exponat_est.setItemText(0, QCoreApplication.translate("add_zapis_dialog", u"\u0415\u0441\u0442\u044c", None))
        self.exponat_est.setItemText(1, QCoreApplication.translate("add_zapis_dialog", u"\u041f\u043b\u0430\u043d\u0438\u0440\u0443\u0435\u0442\u0441\u044f", None))
        self.exponat_est.setItemText(2, QCoreApplication.translate("add_zapis_dialog", u"\u041d\u0435\u0442", None))

        self.exponat_est.setPlaceholderText(QCoreApplication.translate("add_zapis_dialog", u"\u041d\u0430\u043b\u0438\u0447\u0438\u0435 \u044d\u043a\u0441\u043f\u043e\u043d\u0430\u0442\u0430", None))
        self.vistavka.setText("")
        self.vistavka.setPlaceholderText(QCoreApplication.translate("add_zapis_dialog", u"\u0412\u044b\u0441\u0442\u0430\u0432\u043a\u0430", None))
        self.exponat_name.setText("")
        self.exponat_name.setPlaceholderText(QCoreApplication.translate("add_zapis_dialog", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u042d\u043a\u0441\u043f\u043e\u043d\u0430\u0442\u0430", None))
    # retranslateUi

