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
        add_zapis_dialog.resize(561, 664)
        self.label = QLabel(add_zapis_dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 10, 381, 31))
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.save_btn = QPushButton(add_zapis_dialog)
        self.save_btn.setObjectName(u"save_btn")
        self.save_btn.setGeometry(QRect(10, 620, 121, 31))
        font1 = QFont()
        font1.setPointSize(11)
        self.save_btn.setFont(font1)
        self.layoutWidget = QWidget(add_zapis_dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 50, 541, 53))
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

        self.widget = QWidget(add_zapis_dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 470, 271, 61))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 16777215))
        self.label_7.setFont(font2)

        self.verticalLayout.addWidget(self.label_7)

        self.nir_ruk = QLineEdit(self.widget)
        self.nir_ruk.setObjectName(u"nir_ruk")
        self.nir_ruk.setFont(font3)

        self.verticalLayout.addWidget(self.nir_ruk)

        self.widget1 = QWidget(add_zapis_dialog)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(290, 410, 261, 170))
        self.verticalLayout_10 = QVBoxLayout(self.widget1)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_8 = QLabel(self.widget1)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)

        self.verticalLayout_7.addWidget(self.label_8)

        self.ruk_doljnost = QLineEdit(self.widget1)
        self.ruk_doljnost.setObjectName(u"ruk_doljnost")
        self.ruk_doljnost.setFont(font3)

        self.verticalLayout_7.addWidget(self.ruk_doljnost)


        self.verticalLayout_10.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_9 = QLabel(self.widget1)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font2)

        self.verticalLayout_8.addWidget(self.label_9)

        self.ruk_zvanie = QLineEdit(self.widget1)
        self.ruk_zvanie.setObjectName(u"ruk_zvanie")
        self.ruk_zvanie.setFont(font3)

        self.verticalLayout_8.addWidget(self.ruk_zvanie)


        self.verticalLayout_10.addLayout(self.verticalLayout_8)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_10 = QLabel(self.widget1)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)

        self.verticalLayout_9.addWidget(self.label_10)

        self.ruk_stepen = QLineEdit(self.widget1)
        self.ruk_stepen.setObjectName(u"ruk_stepen")
        self.ruk_stepen.setFont(font3)

        self.verticalLayout_9.addWidget(self.ruk_stepen)


        self.verticalLayout_10.addLayout(self.verticalLayout_9)

        self.widget2 = QWidget(add_zapis_dialog)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(10, 230, 541, 170))
        self.verticalLayout_14 = QVBoxLayout(self.widget2)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(self.widget2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)

        self.verticalLayout_4.addWidget(self.label_4)

        self.nir_name = QLineEdit(self.widget2)
        self.nir_name.setObjectName(u"nir_name")
        self.nir_name.setFont(font3)

        self.verticalLayout_4.addWidget(self.nir_name)


        self.verticalLayout_14.addLayout(self.verticalLayout_4)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_12 = QLabel(self.widget2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font2)

        self.verticalLayout_12.addWidget(self.label_12)

        self.vistavka = QLineEdit(self.widget2)
        self.vistavka.setObjectName(u"vistavka")
        self.vistavka.setFont(font3)

        self.verticalLayout_12.addWidget(self.vistavka)


        self.verticalLayout_14.addLayout(self.verticalLayout_12)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_13 = QLabel(self.widget2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font2)

        self.verticalLayout_13.addWidget(self.label_13)

        self.exponat_name = QLineEdit(self.widget2)
        self.exponat_name.setObjectName(u"exponat_name")
        self.exponat_name.setFont(font3)

        self.verticalLayout_13.addWidget(self.exponat_name)


        self.verticalLayout_14.addLayout(self.verticalLayout_13)

        self.widget3 = QWidget(add_zapis_dialog)
        self.widget3.setObjectName(u"widget3")
        self.widget3.setGeometry(QRect(10, 110, 401, 117))
        self.verticalLayout_15 = QVBoxLayout(self.widget3)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.widget3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)

        self.verticalLayout_3.addWidget(self.label_3)

        self.priznak = QComboBox(self.widget3)
        self.priznak.addItem("")
        self.priznak.addItem("")
        self.priznak.setObjectName(u"priznak")
        self.priznak.setFont(font3)

        self.verticalLayout_3.addWidget(self.priznak)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_11 = QLabel(self.widget3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font2)

        self.verticalLayout_11.addWidget(self.label_11)

        self.exponat_est = QComboBox(self.widget3)
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
        self.label_6 = QLabel(self.widget3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)

        self.verticalLayout_6.addWidget(self.label_6)

        self.grnti = QLineEdit(self.widget3)
        self.grnti.setObjectName(u"grnti")
        self.grnti.setFont(font3)

        self.verticalLayout_6.addWidget(self.grnti)


        self.horizontalLayout_2.addLayout(self.verticalLayout_6)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_5 = QLabel(self.widget3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)

        self.verticalLayout_5.addWidget(self.label_5)

        self.reg_number = QLineEdit(self.widget3)
        self.reg_number.setObjectName(u"reg_number")
        self.reg_number.setFont(font3)

        self.verticalLayout_5.addWidget(self.reg_number)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)


        self.verticalLayout_15.addLayout(self.horizontalLayout_2)


        self.retranslateUi(add_zapis_dialog)

        QMetaObject.connectSlotsByName(add_zapis_dialog)
    # setupUi

    def retranslateUi(self, add_zapis_dialog):
        add_zapis_dialog.setWindowTitle("")
        self.label.setText(QCoreApplication.translate("add_zapis_dialog", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0437\u0430\u043f\u0438\u0441\u0438", None))
        self.save_btn.setText(QCoreApplication.translate("add_zapis_dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.label_2.setText(QCoreApplication.translate("add_zapis_dialog", u"\u0412\u0423\u0417", None))
        self.vuz.setPlaceholderText("")
        self.label_7.setText(QCoreApplication.translate("add_zapis_dialog", u"\u0420\u0443\u043a\u043e\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044c \u041d\u0418\u0420", None))
        self.nir_ruk.setText("")
        self.nir_ruk.setPlaceholderText(QCoreApplication.translate("add_zapis_dialog", u"\u0421\u0435\u0440\u0433\u0435\u0439 \u041f\u0430\u0432\u043b\u043e\u0432\u0438\u0447 \u041a\u043e\u0440\u043e\u043b\u0451\u0432", None))
        self.label_8.setText(QCoreApplication.translate("add_zapis_dialog", u"\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c", None))
        self.ruk_doljnost.setText("")
        self.ruk_doljnost.setPlaceholderText(QCoreApplication.translate("add_zapis_dialog", u"\u0440\u0443\u043a.\u043e\u0442\u0434., \u0437\u0430\u0432.\u043a\u0430\u0444., \u0437\u0430\u0432.\u043b\u0430\u0431., \u043d\u0430\u0447.\u043e\u0442\u0434", None))
        self.label_9.setText(QCoreApplication.translate("add_zapis_dialog", u"\u0423\u0447\u0435\u043d\u043e\u0435 \u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.ruk_zvanie.setText("")
        self.ruk_zvanie.setPlaceholderText(QCoreApplication.translate("add_zapis_dialog", u"\u0434\u043e\u0446., \u043f\u0440\u043e\u0444., \u0447\u043b.-\u043a\u043e\u0440\u0440, \u0430\u043a\u0430\u0434. ", None))
        self.label_10.setText(QCoreApplication.translate("add_zapis_dialog", u"\u0423\u0447\u0435\u043d\u0430\u044f \u0441\u0442\u0435\u043f\u0435\u043d\u044c", None))
        self.ruk_stepen.setText("")
        self.ruk_stepen.setPlaceholderText(QCoreApplication.translate("add_zapis_dialog", u"\u043a.\u0442.\u043d., \u0434.\u0442.\u043d., \u043a.\u0431.\u043d., \u0434.\u0444.-\u043c.\u043d.", None))
        self.label_4.setText(QCoreApplication.translate("add_zapis_dialog", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u041d\u0418\u0420", None))
        self.nir_name.setText("")
        self.nir_name.setPlaceholderText(QCoreApplication.translate("add_zapis_dialog", u"\u0422\u0435\u043f\u043b\u043e\u0444\u0438\u0437\u0438\u043a\u0430 \u0438 \u0442\u0435\u043f\u043b\u043e\u044d\u043d\u0435\u0440\u0433\u0435\u0442\u0438\u043a\u0430", None))
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
        self.label_6.setText(QCoreApplication.translate("add_zapis_dialog", u"\u041a\u043e\u0434 \u0413\u0420\u041d\u0422\u0418", None))
        self.grnti.setText("")
        self.grnti.setPlaceholderText(QCoreApplication.translate("add_zapis_dialog", u"29.34.12; 02.12.32; 03.43", None))
        self.label_5.setText(QCoreApplication.translate("add_zapis_dialog", u"\u0420\u0435\u0433. \u043d\u043e\u043c\u0435\u0440 \u041d\u0418\u0420", None))
        self.reg_number.setText("")
        self.reg_number.setPlaceholderText(QCoreApplication.translate("add_zapis_dialog", u"183", None))
    # retranslateUi

