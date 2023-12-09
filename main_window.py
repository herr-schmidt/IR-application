# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QTableView, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1199, 659)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setMaximumSize(QSize(200, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.patients_list_tab = QWidget()
        self.patients_list_tab.setObjectName(u"patients_list_tab")
        self.verticalLayout_2 = QVBoxLayout(self.patients_list_tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.patients_list_table = QTableView(self.patients_list_tab)
        self.patients_list_table.setObjectName(u"patients_list_table")
        self.patients_list_table.setFrameShadow(QFrame.Plain)
        self.patients_list_table.setSortingEnabled(True)

        self.verticalLayout_2.addWidget(self.patients_list_table)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.lineEdit = QLineEdit(self.patients_list_tab)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_3.addWidget(self.lineEdit)

        self.pushButton_7 = QPushButton(self.patients_list_tab)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMaximumSize(QSize(25, 16777215))

        self.horizontalLayout_3.addWidget(self.pushButton_7)

        self.prev_button = QPushButton(self.patients_list_tab)
        self.prev_button.setObjectName(u"prev_button")
        self.prev_button.setMaximumSize(QSize(25, 16777215))
        icon = QIcon()
        icon.addFile(u"../progetti/interventional-radiology-application/resources/prev_b.png", QSize(), QIcon.Normal, QIcon.Off)
        self.prev_button.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.prev_button)

        self.pushButton_5 = QPushButton(self.patients_list_tab)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMaximumSize(QSize(25, 16777215))

        self.horizontalLayout_3.addWidget(self.pushButton_5)

        self.pushButton_4 = QPushButton(self.patients_list_tab)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMaximumSize(QSize(25, 16777215))

        self.horizontalLayout_3.addWidget(self.pushButton_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.tabWidget.addTab(self.patients_list_tab, "")
        self.planning_tab = QWidget()
        self.planning_tab.setObjectName(u"planning_tab")
        self.verticalLayout_3 = QVBoxLayout(self.planning_tab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tableWidget_2 = QTableWidget(self.planning_tab)
        if (self.tableWidget_2.columnCount() < 8):
            self.tableWidget_2.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.tableWidget_2.setObjectName(u"tableWidget_2")

        self.verticalLayout_3.addWidget(self.tableWidget_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.lineEdit_2 = QLineEdit(self.planning_tab)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_4.addWidget(self.lineEdit_2)

        self.pushButton_8 = QPushButton(self.planning_tab)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMaximumSize(QSize(25, 16777215))

        self.horizontalLayout_4.addWidget(self.pushButton_8)

        self.pushButton_9 = QPushButton(self.planning_tab)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMaximumSize(QSize(25, 16777215))

        self.horizontalLayout_4.addWidget(self.pushButton_9)

        self.pushButton_10 = QPushButton(self.planning_tab)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMaximumSize(QSize(25, 16777215))

        self.horizontalLayout_4.addWidget(self.pushButton_10)

        self.pushButton_11 = QPushButton(self.planning_tab)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMaximumSize(QSize(25, 16777215))

        self.horizontalLayout_4.addWidget(self.pushButton_11)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.tabWidget.addTab(self.planning_tab, "")
        self.interactive_planning_tab = QWidget()
        self.interactive_planning_tab.setObjectName(u"interactive_planning_tab")
        self.verticalLayout_4 = QVBoxLayout(self.interactive_planning_tab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.web_engine_view = QWebEngineView(self.interactive_planning_tab)
        self.web_engine_view.setObjectName(u"web_engine_view")
        self.web_engine_view.setUrl(QUrl(u"about:blank"))

        self.verticalLayout_4.addWidget(self.web_engine_view)

        self.tabWidget.addTab(self.interactive_planning_tab, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.import_patients_list_button = QPushButton(self.centralwidget)
        self.import_patients_list_button.setObjectName(u"import_patients_list_button")

        self.horizontalLayout.addWidget(self.import_patients_list_button)

        self.solver_options_button = QPushButton(self.centralwidget)
        self.solver_options_button.setObjectName(u"solver_options_button")

        self.horizontalLayout.addWidget(self.solver_options_button)

        self.launch_planning_button = QPushButton(self.centralwidget)
        self.launch_planning_button.setObjectName(u"launch_planning_button")

        self.horizontalLayout.addWidget(self.launch_planning_button)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.import_patients_list_button, self.launch_planning_button)
        QWidget.setTabOrder(self.launch_planning_button, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.solver_options_button)
        QWidget.setTabOrder(self.solver_options_button, self.pushButton_4)
        QWidget.setTabOrder(self.pushButton_4, self.pushButton_5)
        QWidget.setTabOrder(self.pushButton_5, self.prev_button)
        QWidget.setTabOrder(self.prev_button, self.pushButton_7)
        QWidget.setTabOrder(self.pushButton_7, self.lineEdit)
        QWidget.setTabOrder(self.lineEdit, self.tableWidget_2)
        QWidget.setTabOrder(self.tableWidget_2, self.lineEdit_2)
        QWidget.setTabOrder(self.lineEdit_2, self.pushButton_8)
        QWidget.setTabOrder(self.pushButton_8, self.pushButton_9)
        QWidget.setTabOrder(self.pushButton_9, self.pushButton_10)
        QWidget.setTabOrder(self.pushButton_10, self.pushButton_11)
        QWidget.setTabOrder(self.pushButton_11, self.lineEdit_2)
        QWidget.setTabOrder(self.lineEdit_2, self.pushButton_8)
        QWidget.setTabOrder(self.pushButton_8, self.pushButton_9)
        QWidget.setTabOrder(self.pushButton_9, self.pushButton_10)
        QWidget.setTabOrder(self.pushButton_10, self.pushButton_11)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.prev_button.setText("")
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.patients_list_tab), QCoreApplication.translate("MainWindow", u"Lista pazienti", None))
        ___qtablewidgetitem = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem1 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Cognome", None));
        ___qtablewidgetitem2 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Sala", None));
        ___qtablewidgetitem3 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Data operazione", None));
        ___qtablewidgetitem4 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Orario inizio operazione", None));
        ___qtablewidgetitem5 = self.tableWidget_2.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Ritardo", None));
        ___qtablewidgetitem6 = self.tableWidget_2.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Anestesista", None));
        ___qtablewidgetitem7 = self.tableWidget_2.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Infezioni in atto", None));
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.planning_tab), QCoreApplication.translate("MainWindow", u"Pianificazione", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.interactive_planning_tab), QCoreApplication.translate("MainWindow", u"Pianificazione interattiva", None))
        self.import_patients_list_button.setText(QCoreApplication.translate("MainWindow", u"Importa lista pazienti...", None))
        self.solver_options_button.setText(QCoreApplication.translate("MainWindow", u"Impostazioni solver", None))
        self.launch_planning_button.setText(QCoreApplication.translate("MainWindow", u"Avvia pianificazione", None))
    # retranslateUi

