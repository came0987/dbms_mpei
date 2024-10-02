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
    QMainWindow, QMenu, QMenuBar, QPlainTextEdit,
    QPushButton, QSizePolicy, QStackedWidget, QTabWidget,
    QTableView, QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1200, 700)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1200, 700))
        MainWindow.setMaximumSize(QSize(1200, 700))
        MainWindow.setTabShape(QTabWidget.TabShape.Rounded)
        self.vistavki = QAction(MainWindow)
        self.vistavki.setObjectName(u"vistavki")
        self.grnti = QAction(MainWindow)
        self.grnti.setObjectName(u"grnti")
        self.vuz_2 = QAction(MainWindow)
        self.vuz_2.setObjectName(u"vuz_2")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pages_ = QStackedWidget(self.centralwidget)
        self.pages_.setObjectName(u"pages_")
        self.pages_.setGeometry(QRect(0, 0, 1200, 678))
        self.menu_tables_page = QWidget()
        self.menu_tables_page.setObjectName(u"menu_tables_page")
        self.add_filters_cb = QComboBox(self.menu_tables_page)
        self.add_filters_cb.setObjectName(u"add_filters_cb")
        self.add_filters_cb.setGeometry(QRect(220, 20, 141, 31))
        self.search_field = QPlainTextEdit(self.menu_tables_page)
        self.search_field.setObjectName(u"search_field")
        self.search_field.setGeometry(QRect(40, 20, 161, 31))
        self.modify_table_cb = QComboBox(self.menu_tables_page)
        self.modify_table_cb.setObjectName(u"modify_table_cb")
        self.modify_table_cb.setGeometry(QRect(1050, 20, 131, 31))
        self.tables_area = QStackedWidget(self.menu_tables_page)
        self.tables_area.setObjectName(u"tables_area")
        self.tables_area.setGeometry(QRect(20, 80, 1160, 530))
        self.tables_page = QWidget()
        self.tables_page.setObjectName(u"tables_page")
        self.db_tables = QStackedWidget(self.tables_page)
        self.db_tables.setObjectName(u"db_tables")
        self.db_tables.setGeometry(QRect(0, 0, 1160, 530))
        self.vyst_mo = QWidget()
        self.vyst_mo.setObjectName(u"vyst_mo")
        self.vyst_mo_table = QTableView(self.vyst_mo)
        self.vyst_mo_table.setObjectName(u"vyst_mo_table")
        self.vyst_mo_table.setGeometry(QRect(0, 0, 1160, 530))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.vyst_mo_table.sizePolicy().hasHeightForWidth())
        self.vyst_mo_table.setSizePolicy(sizePolicy1)
        self.db_tables.addWidget(self.vyst_mo)
        self.vuz = QWidget()
        self.vuz.setObjectName(u"vuz")
        self.vuz_table = QTableView(self.vuz)
        self.vuz_table.setObjectName(u"vuz_table")
        self.vuz_table.setGeometry(QRect(0, 0, 1160, 530))
        self.db_tables.addWidget(self.vuz)
        self.grntirub = QWidget()
        self.grntirub.setObjectName(u"grntirub")
        self.grntirub_table = QTableView(self.grntirub)
        self.grntirub_table.setObjectName(u"grntirub_table")
        self.grntirub_table.setGeometry(QRect(0, 0, 1160, 530))
        self.db_tables.addWidget(self.grntirub)
        self.tables_area.addWidget(self.tables_page)
        self.group_page = QWidget()
        self.group_page.setObjectName(u"group_page")
        self.group_table = QTableWidget(self.group_page)
        self.group_table.setObjectName(u"group_table")
        self.group_table.setGeometry(QRect(0, 0, 1160, 530))
        self.tables_area.addWidget(self.group_page)
        self.layoutWidget = QWidget(self.menu_tables_page)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(190, 620, 801, 41))
        self.crud_menu = QHBoxLayout(self.layoutWidget)
        self.crud_menu.setObjectName(u"crud_menu")
        self.crud_menu.setContentsMargins(0, 0, 0, 0)
        self.create_btn = QPushButton(self.layoutWidget)
        self.create_btn.setObjectName(u"create_btn")

        self.crud_menu.addWidget(self.create_btn)

        self.update_btn = QPushButton(self.layoutWidget)
        self.update_btn.setObjectName(u"update_btn")

        self.crud_menu.addWidget(self.update_btn)

        self.comboBox = QComboBox(self.layoutWidget)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.crud_menu.addWidget(self.comboBox)

        self.delete_btn = QPushButton(self.layoutWidget)
        self.delete_btn.setObjectName(u"delete_btn")

        self.crud_menu.addWidget(self.delete_btn)

        self.filter_container = QWidget(self.menu_tables_page)
        self.filter_container.setObjectName(u"filter_container")
        self.filter_container.setGeometry(QRect(380, 10, 661, 61))
        self.pages_.addWidget(self.menu_tables_page)
        self.menu_groups_page = QWidget()
        self.menu_groups_page.setObjectName(u"menu_groups_page")
        self.groups_pages = QStackedWidget(self.menu_groups_page)
        self.groups_pages.setObjectName(u"groups_pages")
        self.groups_pages.setGeometry(QRect(20, 80, 1160, 530))
        self.group_1 = QWidget()
        self.group_1.setObjectName(u"group_1")
        self.tableView = QTableView(self.group_1)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(0, 0, 1160, 530))
        self.groups_pages.addWidget(self.group_1)
        self.group_2 = QWidget()
        self.group_2.setObjectName(u"group_2")
        self.groups_pages.addWidget(self.group_2)
        self.pushButton_2 = QPushButton(self.menu_groups_page)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(1070, 30, 111, 31))
        font = QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.widget = QWidget(self.menu_groups_page)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 30, 421, 41))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.comboBox_2 = QComboBox(self.widget)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setFont(font)

        self.horizontalLayout.addWidget(self.comboBox_2)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font)

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font)

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pages_.addWidget(self.menu_groups_page)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1200, 22))
        self.tables = QMenu(self.menuBar)
        self.tables.setObjectName(u"tables")
        self.groups = QMenu(self.menuBar)
        self.groups.setObjectName(u"groups")
        self.groups.setGeometry(QRect(345, 125, 182, 50))
        self.help = QMenu(self.menuBar)
        self.help.setObjectName(u"help")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.tables.menuAction())
        self.menuBar.addAction(self.groups.menuAction())
        self.menuBar.addAction(self.help.menuAction())
        self.tables.addAction(self.vistavki)
        self.tables.addAction(self.grnti)
        self.tables.addAction(self.vuz_2)

        self.retranslateUi(MainWindow)

        self.pages_.setCurrentIndex(0)
        self.tables_area.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0430 \u0434\u0430\u043d\u043d\u044b\u0445 \u043e \u0432\u044b\u0441\u0442\u0430\u0432\u043e\u0447\u043d\u044b\u0445 \u044d\u043a\u0441\u043f\u043e\u043d\u0430\u0442\u0430\u0445", None))
        self.vistavki.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0441\u0442\u0430\u0432\u043a\u0438", None))
        self.grnti.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0420\u041d\u0422\u0418", None))
        self.vuz_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0423\u0417\u044b", None))
        self.create_btn.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.update_btn.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"+ \u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043d\u043e\u0432\u0443\u044e \u0433\u0440\u0443\u043f\u043f\u0443", None))

        self.comboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c \u0432 \u0433\u0440\u0443\u043f\u043f\u0443", None))
        self.delete_btn.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442", None))
        self.comboBox_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0433\u0440\u0443\u043f\u043f\u0443", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0433\u0440\u0443\u043f\u043f\u0443", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0433\u0440\u0443\u043f\u043f\u0443", None))
        self.tables.setTitle(QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0431\u043b\u0438\u0446\u044b", None))
        self.groups.setTitle(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0443\u043f\u043f\u044b", None))
        self.help.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043c\u043e\u0449\u044c", None))
    # retranslateUi

