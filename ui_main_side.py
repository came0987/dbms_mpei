# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStackedWidget, QStatusBar, QTableView,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(838, 597)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 50, 553, 61))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.tables_combobox = QComboBox(self.layoutWidget)
        self.tables_combobox.addItem("")
        self.tables_combobox.addItem("")
        self.tables_combobox.addItem("")
        self.tables_combobox.addItem("")
        self.tables_combobox.setObjectName(u"tables_combobox")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(20)
        self.tables_combobox.setFont(font)
        self.tables_combobox.setEditable(False)
        self.tables_combobox.setFrame(True)

        self.horizontalLayout.addWidget(self.tables_combobox)

        self.group_button = QPushButton(self.layoutWidget)
        self.group_button.setObjectName(u"group_button")
        self.group_button.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.group_button.setStyleSheet(u"font-size: 20pt;\n"
"")
        self.group_button.setCheckable(False)

        self.horizontalLayout.addWidget(self.group_button)

        self.pushButton_3 = QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"font-size: 20pt;\n"
"")

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.layoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"font-size: 20pt;\n"
"")

        self.horizontalLayout.addWidget(self.pushButton_4)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(20, 130, 801, 381))
        self.tables_page = QWidget()
        self.tables_page.setObjectName(u"tables_page")
        self.db_tables = QStackedWidget(self.tables_page)
        self.db_tables.setObjectName(u"db_tables")
        self.db_tables.setGeometry(QRect(0, 0, 801, 381))
        self.vyst_mo = QWidget()
        self.vyst_mo.setObjectName(u"vyst_mo")
        self.vyst_mo_table = QTableView(self.vyst_mo)
        self.vyst_mo_table.setObjectName(u"vyst_mo_table")
        self.vyst_mo_table.setGeometry(QRect(0, 0, 801, 381))
        self.db_tables.addWidget(self.vyst_mo)
        self.vuz = QWidget()
        self.vuz.setObjectName(u"vuz")
        self.vuz_table = QTableWidget(self.vuz)
        self.vuz_table.setObjectName(u"vuz_table")
        self.vuz_table.setGeometry(QRect(0, 0, 801, 381))
        self.db_tables.addWidget(self.vuz)
        self.grntirub = QWidget()
        self.grntirub.setObjectName(u"grntirub")
        self.grntirub_table = QTableWidget(self.grntirub)
        self.grntirub_table.setObjectName(u"grntirub_table")
        self.grntirub_table.setGeometry(QRect(0, 0, 801, 381))
        self.db_tables.addWidget(self.grntirub)
        self.stackedWidget.addWidget(self.tables_page)
        self.group_page = QWidget()
        self.group_page.setObjectName(u"group_page")
        self.group_table = QTableWidget(self.group_page)
        self.group_table.setObjectName(u"group_table")
        self.group_table.setGeometry(QRect(5, 11, 801, 381))
        self.stackedWidget.addWidget(self.group_page)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QRect(600, 40, 119, 44))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setStyleSheet(u"font-size: 20pt;\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setEnabled(True)
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 838, 48))
        font1 = QFont()
        font1.setPointSize(23)
        self.menuBar.setFont(font1)
        self.menu = QMenu(self.menuBar)
        self.menu.setObjectName(u"menu")
        font2 = QFont()
        font2.setPointSize(17)
        self.menu.setFont(font2)
        self.menu_2 = QMenu(self.menuBar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_3 = QMenu(self.menuBar)
        self.menu_3.setObjectName(u"menu_3")
        self.menu_4 = QMenu(self.menuBar)
        self.menu_4.setObjectName(u"menu_4")
        self.menu_4.setTearOffEnabled(False)
        self.menu_4.setSeparatorsCollapsible(False)
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menu_2.menuAction())
        self.menuBar.addAction(self.menu_3.menuAction())
        self.menuBar.addAction(self.menu_4.menuAction())

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0430 \u0434\u0430\u043d\u043d\u044b\u0445 \u043e \u0432\u044b\u0441\u0442\u0430\u0432\u043e\u0447\u043d\u044b\u0445 \u044d\u043a\u0441\u043f\u043e\u043d\u0430\u0442\u0430\u0445.", None))
        self.tables_combobox.setItemText(0, QCoreApplication.translate("MainWindow", u"123", None))
        self.tables_combobox.setItemText(1, QCoreApplication.translate("MainWindow", u"12332", None))
        self.tables_combobox.setItemText(2, QCoreApplication.translate("MainWindow", u"123213", None))
        self.tables_combobox.setItemText(3, QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None))

        self.tables_combobox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0431\u043b\u0438\u0446\u044b", None))
        self.group_button.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0443\u043f\u043f\u0430", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043c\u043e\u0449\u044c", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0431\u043b\u0438\u0446\u0430", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0442\u0430\u0431\u043b\u0438\u0446\u0430", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u0433\u0440\u0443\u043f\u043f\u0430", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u044d\u043a\u0441\u043f\u043e\u0440\u0442", None))
        self.menu_4.setTitle(QCoreApplication.translate("MainWindow", u"\u043f\u043e\u043c\u043e\u0449\u044c\u044c", None))
    # retranslateUi

