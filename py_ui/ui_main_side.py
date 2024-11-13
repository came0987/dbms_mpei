# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStackedWidget, QTabWidget, QTableView, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1200, 751)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(200, 100))
        MainWindow.setMaximumSize(QSize(1920, 1080))
        MainWindow.setTabShape(QTabWidget.TabShape.Rounded)
        self.vistavki_action = QAction(MainWindow)
        self.vistavki_action.setObjectName(u"vistavki_action")
        self.grnti_action = QAction(MainWindow)
        self.grnti_action.setObjectName(u"grnti_action")
        self.vuz_action = QAction(MainWindow)
        self.vuz_action.setObjectName(u"vuz_action")
        self.svod_action = QAction(MainWindow)
        self.svod_action.setObjectName(u"svod_action")
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pages_ = QStackedWidget(self.centralwidget)
        self.pages_.setObjectName(u"pages_")
        self.menu_tables_page = QWidget()
        self.menu_tables_page.setObjectName(u"menu_tables_page")
        self.layoutWidget = QWidget(self.menu_tables_page)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(180, 670, 801, 41))
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

        self.db_tables = QStackedWidget(self.menu_tables_page)
        self.db_tables.setObjectName(u"db_tables")
        self.db_tables.setGeometry(QRect(0, 100, 1181, 581))
        self.svod = QWidget()
        self.svod.setObjectName(u"svod")
        self.gridLayout = QGridLayout(self.svod)
        self.gridLayout.setObjectName(u"gridLayout")
        self.svod_table = QTableView(self.svod)
        self.svod_table.setObjectName(u"svod_table")

        self.gridLayout.addWidget(self.svod_table, 0, 0, 1, 1)

        self.db_tables.addWidget(self.svod)
        self.vyst_mo = QWidget()
        self.vyst_mo.setObjectName(u"vyst_mo")
        self.gridLayout_6 = QGridLayout(self.vyst_mo)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.vyst_mo_table = QTableView(self.vyst_mo)
        self.vyst_mo_table.setObjectName(u"vyst_mo_table")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.vyst_mo_table.sizePolicy().hasHeightForWidth())
        self.vyst_mo_table.setSizePolicy(sizePolicy1)

        self.gridLayout_6.addWidget(self.vyst_mo_table, 0, 0, 1, 1)

        self.db_tables.addWidget(self.vyst_mo)
        self.vuz = QWidget()
        self.vuz.setObjectName(u"vuz")
        self.gridLayout_5 = QGridLayout(self.vuz)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.vuz_table = QTableView(self.vuz)
        self.vuz_table.setObjectName(u"vuz_table")

        self.gridLayout_5.addWidget(self.vuz_table, 0, 0, 1, 1)

        self.db_tables.addWidget(self.vuz)
        self.grntirub = QWidget()
        self.grntirub.setObjectName(u"grntirub")
        self.gridLayout_3 = QGridLayout(self.grntirub)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.grntirub_table = QTableView(self.grntirub)
        self.grntirub_table.setObjectName(u"grntirub_table")

        self.gridLayout_3.addWidget(self.grntirub_table, 0, 0, 1, 1)

        self.db_tables.addWidget(self.grntirub)
        self.layoutWidget1 = QWidget(self.menu_tables_page)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(11, 36, 1081, 63))
        self.toplevel_layout = QHBoxLayout(self.layoutWidget1)
        self.toplevel_layout.setObjectName(u"toplevel_layout")
        self.toplevel_layout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.add_filters_cb = QComboBox(self.layoutWidget1)
        self.add_filters_cb.setObjectName(u"add_filters_cb")
        self.add_filters_cb.setMinimumSize(QSize(180, 0))
        self.add_filters_cb.setMaximumSize(QSize(180, 16777215))
        font = QFont()
        font.setPointSize(11)
        self.add_filters_cb.setFont(font)
        self.add_filters_cb.setEditable(False)
        self.add_filters_cb.setMinimumContentsLength(2)

        self.verticalLayout.addWidget(self.add_filters_cb, 0, Qt.AlignmentFlag.AlignVCenter)

        self.delete_all_filters = QPushButton(self.layoutWidget1)
        self.delete_all_filters.setObjectName(u"delete_all_filters")
        self.delete_all_filters.setEnabled(True)
        self.delete_all_filters.setMinimumSize(QSize(180, 0))
        self.delete_all_filters.setMaximumSize(QSize(180, 16777215))
        self.delete_all_filters.setFont(font)

        self.verticalLayout.addWidget(self.delete_all_filters, 0, Qt.AlignmentFlag.AlignLeft)


        self.toplevel_layout.addLayout(self.verticalLayout)

        self.current_table_label = QLabel(self.menu_tables_page)
        self.current_table_label.setObjectName(u"current_table_label")
        self.current_table_label.setGeometry(QRect(10, 0, 331, 21))
        font1 = QFont()
        font1.setPointSize(14)
        self.current_table_label.setFont(font1)
        self.pages_.addWidget(self.menu_tables_page)
        self.menu_groups_page = QWidget()
        self.menu_groups_page.setObjectName(u"menu_groups_page")
        self.stackedWidget = QStackedWidget(self.menu_groups_page)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 1181, 701))
        self.group_list_page = QWidget()
        self.group_list_page.setObjectName(u"group_list_page")
        self.layoutWidget2 = QWidget(self.group_list_page)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 30, 301, 51))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.create_group_btn = QPushButton(self.layoutWidget2)
        self.create_group_btn.setObjectName(u"create_group_btn")
        font2 = QFont()
        font2.setPointSize(12)
        self.create_group_btn.setFont(font2)

        self.horizontalLayout.addWidget(self.create_group_btn)

        self.delete_group_btn = QPushButton(self.layoutWidget2)
        self.delete_group_btn.setObjectName(u"delete_group_btn")
        self.delete_group_btn.setFont(font2)

        self.horizontalLayout.addWidget(self.delete_group_btn)

        self.group_list_table = QTableView(self.group_list_page)
        self.group_list_table.setObjectName(u"group_list_table")
        self.group_list_table.setGeometry(QRect(10, 91, 1161, 611))
        self.label_2 = QLabel(self.group_list_page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 0, 141, 21))
        self.label_2.setFont(font1)
        self.stackedWidget.addWidget(self.group_list_page)
        self.group_view_page = QWidget()
        self.group_view_page.setObjectName(u"group_view_page")
        self.group_view_table = QTableView(self.group_view_page)
        self.group_view_table.setObjectName(u"group_view_table")
        self.group_view_table.setGeometry(QRect(10, 91, 1161, 611))
        self.export_btn = QPushButton(self.group_view_page)
        self.export_btn.setObjectName(u"export_btn")
        self.export_btn.setGeometry(QRect(1070, 40, 91, 30))
        self.export_btn.setFont(font2)
        self.layoutWidget3 = QWidget(self.group_view_page)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(10, 30, 431, 51))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.add_record_btn = QPushButton(self.layoutWidget3)
        self.add_record_btn.setObjectName(u"add_record_btn")
        self.add_record_btn.setFont(font2)

        self.horizontalLayout_2.addWidget(self.add_record_btn)

        self.delete_record_btn_2 = QPushButton(self.layoutWidget3)
        self.delete_record_btn_2.setObjectName(u"delete_record_btn_2")
        self.delete_record_btn_2.setFont(font2)

        self.horizontalLayout_2.addWidget(self.delete_record_btn_2)

        self.delete_group_btn_2 = QPushButton(self.layoutWidget3)
        self.delete_group_btn_2.setObjectName(u"delete_group_btn_2")
        self.delete_group_btn_2.setFont(font2)

        self.horizontalLayout_2.addWidget(self.delete_group_btn_2)

        self.label = QLabel(self.group_view_page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 0, 201, 31))
        self.label.setFont(font1)
        self.stackedWidget.addWidget(self.group_view_page)
        self.pages_.addWidget(self.menu_groups_page)

        self.gridLayout_2.addWidget(self.pages_, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1200, 22))
        self.tables_menu = QMenu(self.menuBar)
        self.tables_menu.setObjectName(u"tables_menu")
        self.groups = QMenu(self.menuBar)
        self.groups.setObjectName(u"groups")
        self.groups.setGeometry(QRect(195, 125, 182, 72))
        self.help = QMenu(self.menuBar)
        self.help.setObjectName(u"help")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.tables_menu.menuAction())
        self.menuBar.addAction(self.groups.menuAction())
        self.menuBar.addAction(self.help.menuAction())
        self.tables_menu.addAction(self.svod_action)
        self.tables_menu.addAction(self.vistavki_action)
        self.tables_menu.addAction(self.grnti_action)
        self.tables_menu.addAction(self.vuz_action)
        self.groups.addAction(self.action)

        self.retranslateUi(MainWindow)

        self.pages_.setCurrentIndex(0)
        self.db_tables.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0430 \u0434\u0430\u043d\u043d\u044b\u0445 \u043e \u0432\u044b\u0441\u0442\u0430\u0432\u043e\u0447\u043d\u044b\u0445 \u044d\u043a\u0441\u043f\u043e\u043d\u0430\u0442\u0430\u0445", None))
        self.vistavki_action.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0441\u0442\u0430\u0432\u043a\u0438", None))
        self.grnti_action.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0420\u041d\u0422\u0418", None))
        self.vuz_action.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0423\u0417\u044b", None))
        self.svod_action.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0432\u043e\u0434\u043d\u0430\u044f \u0442\u0430\u0431\u043b\u0438\u0446\u0430", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0433\u0440\u0443\u043f\u043f", None))
        self.create_btn.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.update_btn.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"+ \u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043d\u043e\u0432\u0443\u044e \u0433\u0440\u0443\u043f\u043f\u0443", None))

        self.comboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c \u0432 \u0433\u0440\u0443\u043f\u043f\u0443", None))
        self.delete_btn.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.add_filters_cb.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0444\u0438\u043b\u044c\u0442\u0440", None))
        self.delete_all_filters.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c \u0432\u0441\u0435 \u0444\u0438\u043b\u044c\u0442\u0440\u044b", None))
        self.current_table_label.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0431\u043b\u0438\u0446\u0430 <\u0438\u043c\u044f \u0442\u0430\u0431\u043b\u0438\u0446\u044b>", None))
        self.create_group_btn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0433\u0440\u0443\u043f\u043f\u0443", None))
        self.delete_group_btn.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0433\u0440\u0443\u043f\u043f\u0443", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0433\u0440\u0443\u043f\u043f", None))
        self.export_btn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0447\u0430\u0442\u044c", None))
        self.add_record_btn.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.delete_record_btn_2.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.delete_group_btn_2.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0433\u0440\u0443\u043f\u043f\u0443", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0443\u043f\u043f\u0430 <\u0438\u043c\u044f \u0433\u0440\u0443\u043f\u043f\u044b>", None))
        self.tables_menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0431\u043b\u0438\u0446\u044b", None))
        self.groups.setTitle(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0443\u043f\u043f\u044b", None))
        self.help.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043c\u043e\u0449\u044c", None))
    # retranslateUi

