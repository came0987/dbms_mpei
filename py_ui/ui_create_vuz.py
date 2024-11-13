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
    QLineEdit, QPushButton, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(468, 573)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 0, 241, 41))
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 530, 91, 31))
        font1 = QFont()
        font1.setPointSize(12)
        self.pushButton.setFont(font1)
        self.layoutWidget = QWidget(Dialog)
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

        self.lineEdit = QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setFont(font2)

        self.verticalLayout.addWidget(self.lineEdit)

        self.layoutWidget1 = QWidget(Dialog)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 190, 431, 101))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.layoutWidget1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)

        self.verticalLayout_2.addWidget(self.label_4)

        self.textEdit = QTextEdit(self.layoutWidget1)
        self.textEdit.setObjectName(u"textEdit")
        font3 = QFont()
        font3.setPointSize(10)
        self.textEdit.setFont(font3)

        self.verticalLayout_2.addWidget(self.textEdit)

        self.layoutWidget2 = QWidget(Dialog)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(20, 50, 211, 53))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)

        self.verticalLayout_3.addWidget(self.label_5)

        self.lineEdit_3 = QLineEdit(self.layoutWidget2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setFont(font2)

        self.verticalLayout_3.addWidget(self.lineEdit_3)

        self.layoutWidget3 = QWidget(Dialog)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(240, 50, 75, 53))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)

        self.verticalLayout_4.addWidget(self.label_2)

        self.lineEdit_4 = QLineEdit(self.layoutWidget3)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setFont(font2)

        self.verticalLayout_4.addWidget(self.lineEdit_4)

        self.layoutWidget4 = QWidget(Dialog)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(20, 310, 181, 53))
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.layoutWidget4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)

        self.verticalLayout_5.addWidget(self.label_6)

        self.comboBox = QComboBox(self.layoutWidget4)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font2)

        self.verticalLayout_5.addWidget(self.comboBox)

        self.layoutWidget5 = QWidget(Dialog)
        self.layoutWidget5.setObjectName(u"layoutWidget5")
        self.layoutWidget5.setGeometry(QRect(220, 310, 231, 53))
        self.verticalLayout_6 = QVBoxLayout(self.layoutWidget5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.layoutWidget5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)

        self.verticalLayout_6.addWidget(self.label_7)

        self.lineEdit_5 = QLineEdit(self.layoutWidget5)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setFont(font2)

        self.verticalLayout_6.addWidget(self.lineEdit_5)

        self.layoutWidget6 = QWidget(Dialog)
        self.layoutWidget6.setObjectName(u"layoutWidget6")
        self.layoutWidget6.setGeometry(QRect(20, 450, 151, 53))
        self.verticalLayout_7 = QVBoxLayout(self.layoutWidget6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.layoutWidget6)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)

        self.verticalLayout_7.addWidget(self.label_8)

        self.lineEdit_6 = QLineEdit(self.layoutWidget6)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setFont(font2)

        self.verticalLayout_7.addWidget(self.lineEdit_6)

        self.layoutWidget7 = QWidget(Dialog)
        self.layoutWidget7.setObjectName(u"layoutWidget7")
        self.layoutWidget7.setGeometry(QRect(20, 380, 281, 53))
        self.verticalLayout_8 = QVBoxLayout(self.layoutWidget7)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.layoutWidget7)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font2)

        self.verticalLayout_8.addWidget(self.label_9)

        self.comboBox_2 = QComboBox(self.layoutWidget7)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setFont(font2)

        self.verticalLayout_8.addWidget(self.comboBox_2)

        self.layoutWidget8 = QWidget(Dialog)
        self.layoutWidget8.setObjectName(u"layoutWidget8")
        self.layoutWidget8.setGeometry(QRect(190, 450, 81, 53))
        self.verticalLayout_9 = QVBoxLayout(self.layoutWidget8)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.layoutWidget8)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)

        self.verticalLayout_9.addWidget(self.label_10)

        self.lineEdit_8 = QLineEdit(self.layoutWidget8)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setFont(font2)

        self.verticalLayout_9.addWidget(self.lineEdit_8)

        self.layoutWidget9 = QWidget(Dialog)
        self.layoutWidget9.setObjectName(u"layoutWidget9")
        self.layoutWidget9.setGeometry(QRect(290, 450, 71, 53))
        self.verticalLayout_10 = QVBoxLayout(self.layoutWidget9)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.layoutWidget9)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font2)

        self.verticalLayout_10.addWidget(self.label_11)

        self.lineEdit_9 = QLineEdit(self.layoutWidget9)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setFont(font2)

        self.verticalLayout_10.addWidget(self.lineEdit_9)

        self.layoutWidget10 = QWidget(Dialog)
        self.layoutWidget10.setObjectName(u"layoutWidget10")
        self.layoutWidget10.setGeometry(QRect(320, 380, 127, 53))
        self.verticalLayout_11 = QVBoxLayout(self.layoutWidget10)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.layoutWidget10)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font2)

        self.verticalLayout_11.addWidget(self.label_12)

        self.comboBox_3 = QComboBox(self.layoutWidget10)
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setFont(font2)

        self.verticalLayout_11.addWidget(self.comboBox_3)

        self.label_13 = QLabel(Dialog)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(20, 100, 49, 16))
        self.label_14 = QLabel(Dialog)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(240, 100, 49, 16))
        self.label_15 = QLabel(Dialog)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(20, 170, 49, 16))
        self.label_16 = QLabel(Dialog)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(20, 290, 49, 16))
        self.label_17 = QLabel(Dialog)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(20, 360, 49, 16))
        self.label_18 = QLabel(Dialog)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(220, 360, 49, 16))
        self.label_19 = QLabel(Dialog)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(20, 430, 49, 16))
        self.label_20 = QLabel(Dialog)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(320, 430, 49, 16))
        self.label_21 = QLabel(Dialog)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(20, 500, 49, 16))
        self.label_22 = QLabel(Dialog)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(190, 500, 49, 16))
        self.label_23 = QLabel(Dialog)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(290, 500, 49, 16))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043d\u043e\u0432\u043e\u0433\u043e \u0412\u0423\u0417\u0430", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0412\u0423\u0417\u0430 *", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u043b\u043d\u043e\u0435 \u043d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0412\u0423\u0417\u0430 *", None))
        self.textEdit.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p></body></html>", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0424\u0435\u0434\u0435\u0440\u0430\u043b\u044c\u043d\u043e\u0435 \u0433\u043e\u0441\u0443\u0434\u0430\u0440\u0441\u0442\u0432\u0435\u043d\u043d\u043e\u0435 \u0431\u044e\u0434\u0436\u0435\u0442\u043d\u043e\u0435 \u043e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c\u043d\u043e\u0435 \u0443\u0447\u0440\u0435\u0436\u0434\u0435\u043d\u0438\u0435 \u0432\u044b\u0441\u0448\u0435\u0433\u043e \u043f\u0440\u043e\u0444\u0435\u0441\u0441\u0438\u043e\u043d\u0430\u043b\u044c\u043d\u043e\u0433\u043e \u043e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u043d\u0438\u044f \"\u0410\u043b\u0442\u0430\u0439\u0441\u043a\u0438\u0439 \u0433\u043e\u0441\u0443\u0434\u0430\u0440\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0439 \u0442\u0435\u0445\u043d\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0443\u043d\u0438\u0432\u0435\u0440\u0441\u0438\u0442\u0435\u0442 \u0438\u043c. \u0418.\u0418. \u041f\u043e\u043b\u0437\u0443\u043d\u043e\u0432\u0430\"", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u041a\u0440\u0430\u0442\u043a\u043e\u0435 \u043d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0412\u0423\u0417\u0430 *", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0410\u043b\u0442\u0413\u0422\u0423", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u0434 \u0412\u0423\u0417\u0430 *", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("Dialog", u"1", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u0424\u0435\u0434\u0435\u0440\u0430\u043b\u044c\u043d\u044b\u0439 \u043e\u043a\u0440\u0443\u0433 *", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"\u0413\u043e\u0440\u043e\u0434 *", None))
        self.lineEdit_5.setText("")
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0411\u0430\u0440\u043d\u0430\u0443\u043b", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"\u0421\u0442\u0430\u0442\u0443\u0441 *", None))
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0423\u043d\u0438\u0432\u0435\u0440\u0441\u0438\u0442\u0435\u0442", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"\u0421\u0443\u0431\u044a\u0435\u043a\u0442 \u0420\u0424 *", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f", None))
        self.lineEdit_8.setText("")
        self.lineEdit_8.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041f\u0421\u0420", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u043e\u0444\u0438\u043b\u044c", None))
        self.lineEdit_9.setText("")
        self.lineEdit_9.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0418\u0422", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u0434 \u0441\u0443\u0431\u044a\u0435\u043a\u0442\u0430 \u0420\u0424 *", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label_15.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label_16.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label_17.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label_18.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label_19.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label_20.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label_21.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label_22.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label_23.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
    # retranslateUi

