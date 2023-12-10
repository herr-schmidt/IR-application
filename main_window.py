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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QTableView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(980, 540)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.summary_frame = QFrame(self.centralwidget)
        self.summary_frame.setObjectName(u"summary_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.summary_frame.sizePolicy().hasHeightForWidth())
        self.summary_frame.setSizePolicy(sizePolicy1)
        self.summary_frame.setMaximumSize(QSize(250, 16777215))
        self.summary_frame.setStyleSheet(u"QFrame{\n"
"	border: 1px solid \"#DFDFDF\";\n"
"   /*\n"
"	border-radius: 8px;\n"
"	*/\n"
"    padding: 2px;\n"
"	background-color: white;\n"
"}")
        self.summary_frame.setFrameShape(QFrame.StyledPanel)
        self.summary_frame.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.summary_frame)
        self.formLayout.setObjectName(u"formLayout")
        self.label_3 = QLabel(self.summary_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"border: 0px;\n"
"padding: 0px 0px 0px 10px;")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.lineEdit = QLineEdit(self.summary_frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"border: 0px;")
        self.lineEdit.setReadOnly(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit)

        self.label_2 = QLabel(self.summary_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"border: 0px;\n"
"padding: 0px 0px 0px 10px;")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.lineEdit_2 = QLineEdit(self.summary_frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"border: 0px;")
        self.lineEdit_2.setReadOnly(True)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_2)

        self.label_4 = QLabel(self.summary_frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"border: 0px;\n"
"padding: 0px 0px 0px 10px;")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.lineEdit_3 = QLineEdit(self.summary_frame)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setStyleSheet(u"border: 0px;")
        self.lineEdit_3.setReadOnly(True)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lineEdit_3)

        self.label_5 = QLabel(self.summary_frame)
        self.label_5.setObjectName(u"label_5")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"border: 0px;")

        self.formLayout.setWidget(4, QFormLayout.SpanningRole, self.label_5)

        self.label_6 = QLabel(self.summary_frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"border: 0px;\n"
"padding: 0px 0px 0px 10px;")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_6)

        self.lineEdit_4 = QLineEdit(self.summary_frame)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setStyleSheet(u"border: 0px;")
        self.lineEdit_4.setReadOnly(True)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.lineEdit_4)

        self.label_7 = QLabel(self.summary_frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"border: 0px;\n"
"padding: 0px 0px 0px 10px;")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_7)

        self.lineEdit_5 = QLineEdit(self.summary_frame)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setStyleSheet(u"border: 0px;")
        self.lineEdit_5.setReadOnly(True)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.lineEdit_5)

        self.label_8 = QLabel(self.summary_frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"border: 0px;\n"
"padding: 0px 0px 0px 10px;")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_8)

        self.lineEdit_6 = QLineEdit(self.summary_frame)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setStyleSheet(u"border: 0px;")
        self.lineEdit_6.setReadOnly(True)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.lineEdit_6)

        self.label_9 = QLabel(self.summary_frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"border: 0px;\n"
"padding: 0px 0px 0px 10px;")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_9)

        self.lineEdit_7 = QLineEdit(self.summary_frame)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setStyleSheet(u"border: 0px;")
        self.lineEdit_7.setReadOnly(True)

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.lineEdit_7)

        self.label_10 = QLabel(self.summary_frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"border: 0px;\n"
"padding: 0px 0px 0px 10px;")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.label_10)

        self.lineEdit_8 = QLineEdit(self.summary_frame)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setStyleSheet(u"border: 0px;")
        self.lineEdit_8.setReadOnly(True)

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.lineEdit_8)

        self.label_11 = QLabel(self.summary_frame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"border: 0px;\n"
"padding: 0px 0px 0px 10px;")

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.label_11)

        self.lineEdit_9 = QLineEdit(self.summary_frame)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setStyleSheet(u"border: 0px;")
        self.lineEdit_9.setReadOnly(True)

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.lineEdit_9)

        self.label_13 = QLabel(self.summary_frame)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"border: 0px;\n"
"padding: 0px 0px 0px 10px;")

        self.formLayout.setWidget(12, QFormLayout.LabelRole, self.label_13)

        self.label_14 = QLabel(self.summary_frame)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"border: 0px;\n"
"padding: 0px 0px 0px 10px;")

        self.formLayout.setWidget(13, QFormLayout.LabelRole, self.label_14)

        self.label_15 = QLabel(self.summary_frame)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"border: 0px;\n"
"padding: 0px 0px 0px 10px;")

        self.formLayout.setWidget(14, QFormLayout.LabelRole, self.label_15)

        self.label_16 = QLabel(self.summary_frame)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"border: 0px;\n"
"padding: 0px 0px 0px 10px;")

        self.formLayout.setWidget(15, QFormLayout.LabelRole, self.label_16)

        self.label_17 = QLabel(self.summary_frame)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"border: 0px;\n"
"padding: 0px 0px 0px 10px;")

        self.formLayout.setWidget(16, QFormLayout.LabelRole, self.label_17)

        self.label_18 = QLabel(self.summary_frame)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"border: 0px;\n"
"padding: 0px 0px 0px 10px;")

        self.formLayout.setWidget(17, QFormLayout.LabelRole, self.label_18)

        self.label_19 = QLabel(self.summary_frame)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setStyleSheet(u"border: 0px;\n"
"padding: 0px 0px 0px 10px;")

        self.formLayout.setWidget(18, QFormLayout.LabelRole, self.label_19)

        self.label_20 = QLabel(self.summary_frame)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setStyleSheet(u"border: 0px;\n"
"padding: 0px 0px 0px 10px;")

        self.formLayout.setWidget(19, QFormLayout.LabelRole, self.label_20)

        self.label_12 = QLabel(self.summary_frame)
        self.label_12.setObjectName(u"label_12")
        sizePolicy2.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy2)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet(u"border: 0px;")

        self.formLayout.setWidget(11, QFormLayout.SpanningRole, self.label_12)

        self.lineEdit_10 = QLineEdit(self.summary_frame)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setStyleSheet(u"border: 0px;")
        self.lineEdit_10.setReadOnly(True)

        self.formLayout.setWidget(12, QFormLayout.FieldRole, self.lineEdit_10)

        self.lineEdit_11 = QLineEdit(self.summary_frame)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setStyleSheet(u"border: 0px;")
        self.lineEdit_11.setReadOnly(True)

        self.formLayout.setWidget(13, QFormLayout.FieldRole, self.lineEdit_11)

        self.lineEdit_12 = QLineEdit(self.summary_frame)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setStyleSheet(u"border: 0px;")
        self.lineEdit_12.setReadOnly(True)

        self.formLayout.setWidget(14, QFormLayout.FieldRole, self.lineEdit_12)

        self.lineEdit_13 = QLineEdit(self.summary_frame)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setStyleSheet(u"border: 0px;")
        self.lineEdit_13.setReadOnly(True)

        self.formLayout.setWidget(15, QFormLayout.FieldRole, self.lineEdit_13)

        self.lineEdit_14 = QLineEdit(self.summary_frame)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setStyleSheet(u"border: 0px;")
        self.lineEdit_14.setReadOnly(True)

        self.formLayout.setWidget(16, QFormLayout.FieldRole, self.lineEdit_14)

        self.lineEdit_15 = QLineEdit(self.summary_frame)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        self.lineEdit_15.setStyleSheet(u"border: 0px;")
        self.lineEdit_15.setReadOnly(True)

        self.formLayout.setWidget(17, QFormLayout.FieldRole, self.lineEdit_15)

        self.lineEdit_16 = QLineEdit(self.summary_frame)
        self.lineEdit_16.setObjectName(u"lineEdit_16")
        self.lineEdit_16.setStyleSheet(u"border: 0px;")
        self.lineEdit_16.setReadOnly(True)

        self.formLayout.setWidget(18, QFormLayout.FieldRole, self.lineEdit_16)

        self.lineEdit_17 = QLineEdit(self.summary_frame)
        self.lineEdit_17.setObjectName(u"lineEdit_17")
        self.lineEdit_17.setStyleSheet(u"border: 0px;")
        self.lineEdit_17.setReadOnly(True)

        self.formLayout.setWidget(19, QFormLayout.FieldRole, self.lineEdit_17)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(20, QFormLayout.LabelRole, self.verticalSpacer)

        self.label = QLabel(self.summary_frame)
        self.label.setObjectName(u"label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)
        self.label.setFont(font)
        self.label.setStyleSheet(u"border: 0px;")

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.label)


        self.horizontalLayout_2.addWidget(self.summary_frame)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.tabWidget.setTabBarAutoHide(False)
        self.patients_list_tab = QWidget()
        self.patients_list_tab.setObjectName(u"patients_list_tab")
        self.verticalLayout_2 = QVBoxLayout(self.patients_list_tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.patients_list_table = QTableView(self.patients_list_tab)
        self.patients_list_table.setObjectName(u"patients_list_table")
        sizePolicy1.setHeightForWidth(self.patients_list_table.sizePolicy().hasHeightForWidth())
        self.patients_list_table.setSizePolicy(sizePolicy1)
        self.patients_list_table.setStyleSheet(u"")
        self.patients_list_table.setFrameShadow(QFrame.Raised)
        self.patients_list_table.setSortingEnabled(True)
        self.patients_list_table.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_2.addWidget(self.patients_list_table)

        self.tabWidget.addTab(self.patients_list_tab, "")
        self.planning_tab = QWidget()
        self.planning_tab.setObjectName(u"planning_tab")
        self.verticalLayout_3 = QVBoxLayout(self.planning_tab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tableView_2 = QTableView(self.planning_tab)
        self.tableView_2.setObjectName(u"tableView_2")
        self.tableView_2.setStyleSheet(u"")
        self.tableView_2.setFrameShadow(QFrame.Raised)
        self.tableView_2.horizontalHeader().setStretchLastSection(True)
        self.tableView_2.verticalHeader().setCascadingSectionResizes(True)

        self.verticalLayout_3.addWidget(self.tableView_2)

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
        QWidget.setTabOrder(self.solver_options_button, self.tableView_2)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Pazienti totali:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Anestesie:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Infezioni in atto:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Impostazioni solver", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Robustezza (pz/sala):", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Giornata operatoria (min):", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Anestesisti per giorno:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Disponibilit\u00e0 anestesisti (min/gg):", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Gap relativo (%):", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Tempo limite (s):", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Pazienti selezionati:", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Anestesie:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Infezioni in atto:", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Ritardi:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Utilizzo medio R.I. vascolare:", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Utilizzo medio radiodiagnostica:", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Pazienti R.I. vascolare:", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Pazienti radiodiagnostica:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Soluzione", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Pazienti", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.patients_list_tab), QCoreApplication.translate("MainWindow", u"Lista pazienti", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.planning_tab), QCoreApplication.translate("MainWindow", u"Pianificazione", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.interactive_planning_tab), QCoreApplication.translate("MainWindow", u"Pianificazione interattiva", None))
        self.import_patients_list_button.setText(QCoreApplication.translate("MainWindow", u"Importa lista pazienti...", None))
        self.solver_options_button.setText(QCoreApplication.translate("MainWindow", u"Impostazioni solver", None))
        self.launch_planning_button.setText(QCoreApplication.translate("MainWindow", u"Avvia pianificazione", None))
    # retranslateUi

