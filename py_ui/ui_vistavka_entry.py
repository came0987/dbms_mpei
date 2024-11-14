# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_vistavka_entry.ui'
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
        add_zapis_dialog.resize(561, 689)
        self.dialog_label = QLabel(add_zapis_dialog)
        self.dialog_label.setObjectName(u"dialog_label")
        self.dialog_label.setGeometry(QRect(90, 10, 381, 31))
        font = QFont()
        font.setPointSize(16)
        self.dialog_label.setFont(font)
        self.dialog_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.save_btn = QPushButton(add_zapis_dialog)
        self.save_btn.setObjectName(u"save_btn")
        self.save_btn.setGeometry(QRect(10, 650, 121, 31))
        font1 = QFont()
        font1.setPointSize(11)
        self.save_btn.setFont(font1)
        self.layoutWidget = QWidget(add_zapis_dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 50, 401, 61))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setPointSize(10)
        self.label_2.setFont(font2)

        self.verticalLayout_2.addWidget(self.label_2)

        self.vuz = QComboBox(self.layoutWidget)
        self.vuz.setObjectName(u"vuz")
        font3 = QFont()
        font3.setPointSize(12)
        self.vuz.setFont(font3)
        self.vuz.setEditable(False)

        self.verticalLayout_2.addWidget(self.vuz)

        self.layoutWidget1 = QWidget(add_zapis_dialog)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 530, 271, 74))
        self.verticalLayout = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.layoutWidget1)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 16777215))
        self.label_7.setFont(font2)

        self.verticalLayout.addWidget(self.label_7)

        self.nir_ruk = QLineEdit(self.layoutWidget1)
        self.nir_ruk.setObjectName(u"nir_ruk")
        self.nir_ruk.setFont(font3)

        self.verticalLayout.addWidget(self.nir_ruk)

        self.layoutWidget2 = QWidget(add_zapis_dialog)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(290, 470, 261, 171))
        self.verticalLayout_10 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_10.setSpacing(6)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_8 = QLabel(self.layoutWidget2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)

        self.verticalLayout_7.addWidget(self.label_8)

        self.ruk_doljnost = QLineEdit(self.layoutWidget2)
        self.ruk_doljnost.setObjectName(u"ruk_doljnost")
        self.ruk_doljnost.setFont(font3)

        self.verticalLayout_7.addWidget(self.ruk_doljnost)


        self.verticalLayout_10.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_9 = QLabel(self.layoutWidget2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font2)

        self.verticalLayout_8.addWidget(self.label_9)

        self.ruk_zvanie = QLineEdit(self.layoutWidget2)
        self.ruk_zvanie.setObjectName(u"ruk_zvanie")
        self.ruk_zvanie.setFont(font3)

        self.verticalLayout_8.addWidget(self.ruk_zvanie)


        self.verticalLayout_10.addLayout(self.verticalLayout_8)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_10 = QLabel(self.layoutWidget2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)

        self.verticalLayout_9.addWidget(self.label_10)

        self.ruk_stepen = QLineEdit(self.layoutWidget2)
        self.ruk_stepen.setObjectName(u"ruk_stepen")
        self.ruk_stepen.setFont(font3)

        self.verticalLayout_9.addWidget(self.ruk_stepen)


        self.verticalLayout_10.addLayout(self.verticalLayout_9)

        self.layoutWidget3 = QWidget(add_zapis_dialog)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(10, 350, 541, 112))
        self.verticalLayout_14 = QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_12 = QLabel(self.layoutWidget3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font2)

        self.verticalLayout_12.addWidget(self.label_12)

        self.vistavka = QLineEdit(self.layoutWidget3)
        self.vistavka.setObjectName(u"vistavka")
        self.vistavka.setFont(font3)

        self.verticalLayout_12.addWidget(self.vistavka)


        self.verticalLayout_14.addLayout(self.verticalLayout_12)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_13 = QLabel(self.layoutWidget3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font2)

        self.verticalLayout_13.addWidget(self.label_13)

        self.exponat_name = QLineEdit(self.layoutWidget3)
        self.exponat_name.setObjectName(u"exponat_name")
        self.exponat_name.setFont(font3)

        self.verticalLayout_13.addWidget(self.exponat_name)


        self.verticalLayout_14.addLayout(self.verticalLayout_13)

        self.layoutWidget4 = QWidget(add_zapis_dialog)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(10, 130, 411, 131))
        self.verticalLayout_15 = QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.layoutWidget4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)

        self.verticalLayout_3.addWidget(self.label_3)

        self.priznak = QComboBox(self.layoutWidget4)
        self.priznak.addItem("")
        self.priznak.addItem("")
        self.priznak.setObjectName(u"priznak")
        self.priznak.setFont(font3)

        self.verticalLayout_3.addWidget(self.priznak)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_11 = QLabel(self.layoutWidget4)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font2)

        self.verticalLayout_11.addWidget(self.label_11)

        self.exponat_est = QComboBox(self.layoutWidget4)
        self.exponat_est.addItem("")
        self.exponat_est.addItem("")
        self.exponat_est.addItem("")
        self.exponat_est.setObjectName(u"exponat_est")
        self.exponat_est.setFont(font3)

        self.verticalLayout_11.addWidget(self.exponat_est)


        self.horizontalLayout.addLayout(self.verticalLayout_11)


        self.verticalLayout_15.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_6 = QLabel(self.layoutWidget4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)

        self.verticalLayout_6.addWidget(self.label_6)

        self.grnti = QLineEdit(self.layoutWidget4)
        self.grnti.setObjectName(u"grnti")
        self.grnti.setFont(font3)

        self.verticalLayout_6.addWidget(self.grnti)


        self.horizontalLayout_2.addLayout(self.verticalLayout_6)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_5 = QLabel(self.layoutWidget4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)

        self.verticalLayout_5.addWidget(self.label_5)

        self.reg_number = QLineEdit(self.layoutWidget4)
        self.reg_number.setObjectName(u"reg_number")
        self.reg_number.setFont(font3)

        self.verticalLayout_5.addWidget(self.reg_number)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)


        self.verticalLayout_15.addLayout(self.horizontalLayout_2)

        self.layoutWidget5 = QWidget(add_zapis_dialog)
        self.layoutWidget5.setObjectName(u"layoutWidget5")
        self.layoutWidget5.setGeometry(QRect(430, 50, 81, 61))
        self.verticalLayout_16 = QVBoxLayout(self.layoutWidget5)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.layoutWidget5)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(123123, 123123))
        self.label_14.setFont(font2)

        self.verticalLayout_16.addWidget(self.label_14)

        self.codvuz = QComboBox(self.layoutWidget5)
        self.codvuz.setObjectName(u"codvuz")
        self.codvuz.setMaximumSize(QSize(123123, 123123))
        self.codvuz.setFont(font3)

        self.verticalLayout_16.addWidget(self.codvuz)

        self.bossname_error = QLabel(add_zapis_dialog)
        self.bossname_error.setObjectName(u"bossname_error")
        self.bossname_error.setGeometry(QRect(10, 600, 271, 20))
        self.layoutWidget6 = QWidget(add_zapis_dialog)
        self.layoutWidget6.setObjectName(u"layoutWidget6")
        self.layoutWidget6.setGeometry(QRect(10, 280, 539, 52))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.layoutWidget6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)

        self.verticalLayout_4.addWidget(self.label_4)

        self.nir_name = QLineEdit(self.layoutWidget6)
        self.nir_name.setObjectName(u"nir_name")
        self.nir_name.setFont(font3)

        self.verticalLayout_4.addWidget(self.nir_name)

        self.nir_error = QLabel(add_zapis_dialog)
        self.nir_error.setObjectName(u"nir_error")
        self.nir_error.setEnabled(True)
        self.nir_error.setGeometry(QRect(10, 330, 541, 16))
        self.grnti_error = QLabel(add_zapis_dialog)
        self.grnti_error.setObjectName(u"grnti_error")
        self.grnti_error.setGeometry(QRect(10, 260, 191, 16))
        self.reg_number_error = QLabel(add_zapis_dialog)
        self.reg_number_error.setObjectName(u"reg_number_error")
        self.reg_number_error.setGeometry(QRect(218, 260, 201, 16))
        self.vuz_error = QLabel(add_zapis_dialog)
        self.vuz_error.setObjectName(u"vuz_error")
        self.vuz_error.setGeometry(QRect(10, 110, 221, 16))
        self.code_vuz_error = QLabel(add_zapis_dialog)
        self.code_vuz_error.setObjectName(u"code_vuz_error")
        self.code_vuz_error.setGeometry(QRect(430, 110, 61, 16))

        self.retranslateUi(add_zapis_dialog)

        QMetaObject.connectSlotsByName(add_zapis_dialog)
    # setupUi

    def retranslateUi(self, add_zapis_dialog):
        add_zapis_dialog.setWindowTitle("")
        self.dialog_label.setText(QCoreApplication.translate("add_zapis_dialog", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0437\u0430\u043f\u0438\u0441\u0438 \u0432\u044b\u0441\u0442\u0430\u0432\u043a\u0438", None))
        self.save_btn.setText(QCoreApplication.translate("add_zapis_dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.label_2.setText(QCoreApplication.translate("add_zapis_dialog", u"\u0412\u0423\u0417 *", None))
        self.vuz.setPlaceholderText("")
        self.label_7.setText(QCoreApplication.translate("add_zapis_dialog", u"\u0420\u0443\u043a\u043e\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044c \u041d\u0418\u0420 *", None))
        self.nir_ruk.setText("")
        self.nir_ruk.setPlaceholderText(QCoreApplication.translate("add_zapis_dialog", u"\u041a\u043e\u0440\u043e\u043b\u0451\u0432 \u041f. \u041a.", None))
        self.label_8.setText(QCoreApplication.translate("add_zapis_dialog", u"\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c", None))
        self.ruk_doljnost.setText("")
        self.ruk_doljnost.setPlaceholderText(QCoreApplication.translate("add_zapis_dialog", u"\u0437\u0430\u0432.\u043a\u0430\u0444.", None))
        self.label_9.setText(QCoreApplication.translate("add_zapis_dialog", u"\u0423\u0447\u0435\u043d\u043e\u0435 \u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.ruk_zvanie.setText("")
        self.ruk_zvanie.setPlaceholderText(QCoreApplication.translate("add_zapis_dialog", u"\u0434\u043e\u0446.", None))
        self.label_10.setText(QCoreApplication.translate("add_zapis_dialog", u"\u0423\u0447\u0435\u043d\u0430\u044f \u0441\u0442\u0435\u043f\u0435\u043d\u044c", None))
        self.ruk_stepen.setText("")
        self.ruk_stepen.setPlaceholderText(QCoreApplication.translate("add_zapis_dialog", u"\u043a.\u0442.\u043d.", None))
        self.label_12.setText(QCoreApplication.translate("add_zapis_dialog", u"\u0412\u044b\u0441\u0442\u0430\u0432\u043a\u0430", None))
        self.vistavka.setText("")
        self.vistavka.setPlaceholderText(QCoreApplication.translate("add_zapis_dialog", u"\u041c\u0435\u0436\u0434\u0443\u043d\u0430\u0440\u043e\u0434\u043d\u0430\u044f \u0432\u044b\u0441\u0442\u0430\u0432\u043a\u0430 EXAMPLE \u0432 \u0433. \u041c\u043e\u0441\u043a\u0432\u0435", None))
        self.label_13.setText(QCoreApplication.translate("add_zapis_dialog", u"\u0412\u044b\u0441\u0442\u0430\u0432\u043e\u0447\u043d\u044b\u0439 \u044d\u043a\u0441\u043f\u043e\u043d\u0430\u0442", None))
        self.exponat_name.setText("")
        self.exponat_name.setPlaceholderText(QCoreApplication.translate("add_zapis_dialog", u"\u041a\u043e\u043c\u043f\u044c\u044e\u0442\u0435\u0440\u043d\u0430\u044f \u0440\u0430\u0434\u0438\u043e\u043b\u0430\u0431\u043e\u0440\u0430\u0442\u043e\u0440\u0438\u044f RADIOLAB", None))
        self.label_3.setText(QCoreApplication.translate("add_zapis_dialog", u"\u041f\u0440\u0438\u0437\u043d\u0430\u043a \u0444\u043e\u0440\u043c\u044b \u041d\u0418\u0420", None))
        self.priznak.setItemText(0, QCoreApplication.translate("add_zapis_dialog", u"\u0422\u0435\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u043f\u043b\u0430\u043d", None))
        self.priznak.setItemText(1, QCoreApplication.translate("add_zapis_dialog", u"\u041d\u0422\u041f", None))

        self.priznak.setPlaceholderText("")
        self.label_11.setText(QCoreApplication.translate("add_zapis_dialog", u"\u041d\u0430\u043b\u0438\u0447\u0438\u0435 \u044d\u043a\u0441\u043f\u043e\u043d\u0430\u0442\u0430", None))
        self.exponat_est.setItemText(0, QCoreApplication.translate("add_zapis_dialog", u"\u0415\u0441\u0442\u044c", None))
        self.exponat_est.setItemText(1, QCoreApplication.translate("add_zapis_dialog", u"\u041f\u043b\u0430\u043d\u0438\u0440\u0443\u0435\u0442\u0441\u044f", None))
        self.exponat_est.setItemText(2, QCoreApplication.translate("add_zapis_dialog", u"\u041d\u0435\u0442", None))

        self.exponat_est.setPlaceholderText("")
        self.label_6.setText(QCoreApplication.translate("add_zapis_dialog", u"\u041a\u043e\u0434 \u0413\u0420\u041d\u0422\u0418 *", None))
        self.grnti.setText("")
        self.grnti.setPlaceholderText(QCoreApplication.translate("add_zapis_dialog", u"29.34.12; 00.12", None))
        self.label_5.setText(QCoreApplication.translate("add_zapis_dialog", u"\u0420\u0435\u0433. \u043d\u043e\u043c\u0435\u0440 \u041d\u0418\u0420 *", None))
        self.reg_number.setText("")
        self.reg_number.setPlaceholderText(QCoreApplication.translate("add_zapis_dialog", u"183", None))
        self.label_14.setText(QCoreApplication.translate("add_zapis_dialog", u"\u041a\u043e\u0434 \u0412\u0423\u0417\u0430 *", None))
        self.bossname_error.setText("")
        self.label_4.setText(QCoreApplication.translate("add_zapis_dialog", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u041d\u0418\u0420 *", None))
        self.nir_name.setText("")
        self.nir_name.setPlaceholderText(QCoreApplication.translate("add_zapis_dialog", u"\u0422\u0435\u043f\u043b\u043e\u0444\u0438\u0437\u0438\u043a\u0430 \u0438 \u0442\u0435\u043f\u043b\u043e\u044d\u043d\u0435\u0440\u0433\u0435\u0442\u0438\u043a\u0430", None))
        self.nir_error.setText("")
        self.grnti_error.setText("")
        self.reg_number_error.setText("")
        self.vuz_error.setText("")
        self.code_vuz_error.setText("")
    # retranslateUi

