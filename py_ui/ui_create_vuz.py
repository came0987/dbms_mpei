# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_vuz.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_create_vuz_dialog(object):
    def setupUi(self, create_vuz_dialog):
        if not create_vuz_dialog.objectName():
            create_vuz_dialog.setObjectName(u"create_vuz_dialog")
        create_vuz_dialog.resize(468, 550)
        self.dialog_label = QLabel(create_vuz_dialog)
        self.dialog_label.setObjectName(u"dialog_label")
        self.dialog_label.setGeometry(QRect(120, 0, 241, 41))
        font = QFont()
        font.setPointSize(14)
        self.dialog_label.setFont(font)
        self.save_btn = QPushButton(create_vuz_dialog)
        self.save_btn.setObjectName(u"save_btn")
        self.save_btn.setGeometry(QRect(20, 510, 91, 31))
        font1 = QFont()
        font1.setPointSize(12)
        self.save_btn.setFont(font1)
        self.layoutWidget = QWidget(create_vuz_dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 120, 431, 53))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        font2 = QFont()
        font2.setPointSize(11)
        self.label_3.setFont(font2)

        self.verticalLayout.addWidget(self.label_3)

        self.vuz_name = QLineEdit(self.layoutWidget)
        self.vuz_name.setObjectName(u"vuz_name")
        self.vuz_name.setFont(font2)

        self.verticalLayout.addWidget(self.vuz_name)

        self.layoutWidget1 = QWidget(create_vuz_dialog)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 200, 431, 53))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.layoutWidget1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)

        self.verticalLayout_2.addWidget(self.label_4)

        self.vuz_full_name = QLineEdit(self.layoutWidget1)
        self.vuz_full_name.setObjectName(u"vuz_full_name")
        self.vuz_full_name.setFont(font2)

        self.verticalLayout_2.addWidget(self.vuz_full_name)

        self.layoutWidget2 = QWidget(create_vuz_dialog)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(20, 50, 211, 53))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)

        self.verticalLayout_3.addWidget(self.label_5)

        self.vuz_short_name = QLineEdit(self.layoutWidget2)
        self.vuz_short_name.setObjectName(u"vuz_short_name")
        self.vuz_short_name.setFont(font2)

        self.verticalLayout_3.addWidget(self.vuz_short_name)

        self.layoutWidget3 = QWidget(create_vuz_dialog)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(240, 50, 75, 53))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)

        self.verticalLayout_4.addWidget(self.label_2)

        self.vuz_code = QLineEdit(self.layoutWidget3)
        self.vuz_code.setObjectName(u"vuz_code")
        self.vuz_code.setFont(font2)

        self.verticalLayout_4.addWidget(self.vuz_code)

        self.layoutWidget4 = QWidget(create_vuz_dialog)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(20, 280, 181, 53))
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.layoutWidget4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)

        self.verticalLayout_5.addWidget(self.label_6)

        self.federal_region_cb = QComboBox(self.layoutWidget4)
        self.federal_region_cb.setObjectName(u"federal_region_cb")
        self.federal_region_cb.setFont(font2)

        self.verticalLayout_5.addWidget(self.federal_region_cb)

        self.layoutWidget5 = QWidget(create_vuz_dialog)
        self.layoutWidget5.setObjectName(u"layoutWidget5")
        self.layoutWidget5.setGeometry(QRect(220, 280, 231, 53))
        self.verticalLayout_6 = QVBoxLayout(self.layoutWidget5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.layoutWidget5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)

        self.verticalLayout_6.addWidget(self.label_7)

        self.city = QLineEdit(self.layoutWidget5)
        self.city.setObjectName(u"city")
        self.city.setFont(font2)

        self.verticalLayout_6.addWidget(self.city)

        self.layoutWidget6 = QWidget(create_vuz_dialog)
        self.layoutWidget6.setObjectName(u"layoutWidget6")
        self.layoutWidget6.setGeometry(QRect(20, 420, 151, 53))
        self.verticalLayout_7 = QVBoxLayout(self.layoutWidget6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.layoutWidget6)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)

        self.verticalLayout_7.addWidget(self.label_8)

        self.vuz_status = QLineEdit(self.layoutWidget6)
        self.vuz_status.setObjectName(u"vuz_status")
        self.vuz_status.setFont(font2)

        self.verticalLayout_7.addWidget(self.vuz_status)

        self.layoutWidget7 = QWidget(create_vuz_dialog)
        self.layoutWidget7.setObjectName(u"layoutWidget7")
        self.layoutWidget7.setGeometry(QRect(20, 350, 281, 53))
        self.verticalLayout_8 = QVBoxLayout(self.layoutWidget7)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.layoutWidget7)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font2)

        self.verticalLayout_8.addWidget(self.label_9)

        self.federal_subject_cb = QComboBox(self.layoutWidget7)
        self.federal_subject_cb.setObjectName(u"federal_subject_cb")
        self.federal_subject_cb.setFont(font2)

        self.verticalLayout_8.addWidget(self.federal_subject_cb)

        self.layoutWidget8 = QWidget(create_vuz_dialog)
        self.layoutWidget8.setObjectName(u"layoutWidget8")
        self.layoutWidget8.setGeometry(QRect(190, 420, 81, 53))
        self.verticalLayout_9 = QVBoxLayout(self.layoutWidget8)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.layoutWidget8)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)

        self.verticalLayout_9.addWidget(self.label_10)

        self.vuz_category = QLineEdit(self.layoutWidget8)
        self.vuz_category.setObjectName(u"vuz_category")
        self.vuz_category.setFont(font2)

        self.verticalLayout_9.addWidget(self.vuz_category)

        self.layoutWidget9 = QWidget(create_vuz_dialog)
        self.layoutWidget9.setObjectName(u"layoutWidget9")
        self.layoutWidget9.setGeometry(QRect(290, 420, 71, 53))
        self.verticalLayout_10 = QVBoxLayout(self.layoutWidget9)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.layoutWidget9)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font2)

        self.verticalLayout_10.addWidget(self.label_11)

        self.vuz_profile = QLineEdit(self.layoutWidget9)
        self.vuz_profile.setObjectName(u"vuz_profile")
        self.vuz_profile.setFont(font2)

        self.verticalLayout_10.addWidget(self.vuz_profile)

        self.layoutWidget10 = QWidget(create_vuz_dialog)
        self.layoutWidget10.setObjectName(u"layoutWidget10")
        self.layoutWidget10.setGeometry(QRect(320, 350, 127, 53))
        self.verticalLayout_11 = QVBoxLayout(self.layoutWidget10)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.layoutWidget10)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font2)

        self.verticalLayout_11.addWidget(self.label_12)

        self.federal_subject_code_cb = QComboBox(self.layoutWidget10)
        self.federal_subject_code_cb.setObjectName(u"federal_subject_code_cb")
        self.federal_subject_code_cb.setFont(font2)

        self.verticalLayout_11.addWidget(self.federal_subject_code_cb)

        self.vuz_short_name_err = QLabel(create_vuz_dialog)
        self.vuz_short_name_err.setObjectName(u"vuz_short_name_err")
        self.vuz_short_name_err.setGeometry(QRect(20, 100, 211, 16))
        self.label_14 = QLabel(create_vuz_dialog)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(240, 100, 71, 16))
        self.vuz_name_err = QLabel(create_vuz_dialog)
        self.vuz_name_err.setObjectName(u"vuz_name_err")
        self.vuz_name_err.setGeometry(QRect(20, 170, 281, 16))
        self.vuz_full_name_err = QLabel(create_vuz_dialog)
        self.vuz_full_name_err.setObjectName(u"vuz_full_name_err")
        self.vuz_full_name_err.setGeometry(QRect(20, 250, 311, 16))
        self.federal_region_err = QLabel(create_vuz_dialog)
        self.federal_region_err.setObjectName(u"federal_region_err")
        self.federal_region_err.setGeometry(QRect(20, 330, 181, 16))
        self.city_err = QLabel(create_vuz_dialog)
        self.city_err.setObjectName(u"city_err")
        self.city_err.setGeometry(QRect(220, 330, 221, 16))
        self.federal_subject_err = QLabel(create_vuz_dialog)
        self.federal_subject_err.setObjectName(u"federal_subject_err")
        self.federal_subject_err.setGeometry(QRect(20, 400, 271, 16))
        self.federal_subject_code_err = QLabel(create_vuz_dialog)
        self.federal_subject_code_err.setObjectName(u"federal_subject_code_err")
        self.federal_subject_code_err.setGeometry(QRect(320, 400, 111, 16))
        self.vuz_status_err = QLabel(create_vuz_dialog)
        self.vuz_status_err.setObjectName(u"vuz_status_err")
        self.vuz_status_err.setGeometry(QRect(20, 470, 151, 16))
        self.label_22 = QLabel(create_vuz_dialog)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(190, 470, 81, 16))
        self.label_23 = QLabel(create_vuz_dialog)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(290, 470, 49, 16))

        self.retranslateUi(create_vuz_dialog)

        QMetaObject.connectSlotsByName(create_vuz_dialog)
    # setupUi

    def retranslateUi(self, create_vuz_dialog):
        create_vuz_dialog.setWindowTitle(QCoreApplication.translate("create_vuz_dialog", u"Dialog", None))
        self.dialog_label.setText(QCoreApplication.translate("create_vuz_dialog", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043d\u043e\u0432\u043e\u0433\u043e \u0412\u0423\u0417\u0430", None))
        self.save_btn.setText(QCoreApplication.translate("create_vuz_dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.label_3.setText(QCoreApplication.translate("create_vuz_dialog", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0412\u0423\u0417\u0430 *", None))
        self.label_4.setText(QCoreApplication.translate("create_vuz_dialog", u"\u041f\u043e\u043b\u043d\u043e\u0435 \u043d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0412\u0423\u0417\u0430 *", None))
        self.label_5.setText(QCoreApplication.translate("create_vuz_dialog", u"\u041a\u0440\u0430\u0442\u043a\u043e\u0435 \u043d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0412\u0423\u0417\u0430 *", None))
        self.vuz_short_name.setPlaceholderText(QCoreApplication.translate("create_vuz_dialog", u"\u0410\u043b\u0442\u0413\u0422\u0423", None))
        self.label_2.setText(QCoreApplication.translate("create_vuz_dialog", u"\u041a\u043e\u0434 \u0412\u0423\u0417\u0430 *", None))
        self.vuz_code.setPlaceholderText(QCoreApplication.translate("create_vuz_dialog", u"1", None))
        self.label_6.setText(QCoreApplication.translate("create_vuz_dialog", u"\u0424\u0435\u0434\u0435\u0440\u0430\u043b\u044c\u043d\u044b\u0439 \u043e\u043a\u0440\u0443\u0433 *", None))
        self.label_7.setText(QCoreApplication.translate("create_vuz_dialog", u"\u0413\u043e\u0440\u043e\u0434 *", None))
        self.city.setText("")
        self.city.setPlaceholderText(QCoreApplication.translate("create_vuz_dialog", u"\u0411\u0430\u0440\u043d\u0430\u0443\u043b", None))
        self.label_8.setText(QCoreApplication.translate("create_vuz_dialog", u"\u0421\u0442\u0430\u0442\u0443\u0441 *", None))
        self.vuz_status.setPlaceholderText(QCoreApplication.translate("create_vuz_dialog", u"\u0423\u043d\u0438\u0432\u0435\u0440\u0441\u0438\u0442\u0435\u0442", None))
        self.label_9.setText(QCoreApplication.translate("create_vuz_dialog", u"\u0421\u0443\u0431\u044a\u0435\u043a\u0442 \u0420\u0424 *", None))
        self.label_10.setText(QCoreApplication.translate("create_vuz_dialog", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f", None))
        self.vuz_category.setText("")
        self.vuz_category.setPlaceholderText(QCoreApplication.translate("create_vuz_dialog", u"\u041f\u0421\u0420", None))
        self.label_11.setText(QCoreApplication.translate("create_vuz_dialog", u"\u041f\u0440\u043e\u0444\u0438\u043b\u044c", None))
        self.vuz_profile.setText("")
        self.vuz_profile.setPlaceholderText(QCoreApplication.translate("create_vuz_dialog", u"\u0418\u0422", None))
        self.label_12.setText(QCoreApplication.translate("create_vuz_dialog", u"\u041a\u043e\u0434 \u0441\u0443\u0431\u044a\u0435\u043a\u0442\u0430 \u0420\u0424 *", None))
        self.vuz_short_name_err.setText("")
        self.label_14.setText("")
        self.vuz_name_err.setText("")
        self.vuz_full_name_err.setText("")
        self.federal_region_err.setText("")
        self.city_err.setText("")
        self.federal_subject_err.setText("")
        self.federal_subject_code_err.setText("")
        self.vuz_status_err.setText("")
        self.label_22.setText("")
        self.label_23.setText("")
    # retranslateUi

