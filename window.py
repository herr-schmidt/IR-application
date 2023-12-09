# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QSizePolicy, QSlider,
    QWidget)

class Ui_SolverOptionsDialog(object):
    def setupUi(self, SolverOptionsDialog):
        if not SolverOptionsDialog.objectName():
            SolverOptionsDialog.setObjectName(u"SolverOptionsDialog")
        SolverOptionsDialog.setEnabled(True)
        SolverOptionsDialog.resize(260, 520)
        font = QFont()
        font.setFamilies([u"Source Sans Pro"])
        font.setPointSize(11)
        font.setUnderline(False)
        font.setKerning(False)
        SolverOptionsDialog.setFont(font)
        SolverOptionsDialog.setAutoFillBackground(False)
        SolverOptionsDialog.setStyleSheet(u"QMainWindow {\n"
"    background: white;\n"
"}")
        self.centralwidget = QWidget(SolverOptionsDialog)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 10, 241, 501))
        self.frame_2.setStyleSheet(u"QFrame{\n"
"    border: 1px solid \"#DFDFDF\";\n"
"    border-radius: 8px;\n"
"    padding: 2px;\n"
"background-color: white;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_9 = QFrame(self.frame_2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"QFrame{\n"
"	border-color: 0px;\n"
"    border-radius: 0px;\n"
"    padding: 2px;\n"
"}")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_9)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_11 = QLabel(self.frame_9)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(16777215, 20))
        font1 = QFont()
        font1.setFamilies([u"Source Sans Pro"])
        font1.setPointSize(11)
        font1.setUnderline(False)
        font1.setKerning(True)
        self.label_11.setFont(font1)

        self.gridLayout_8.addWidget(self.label_11, 0, 0, 1, 1)

        self.lineEdit_11 = QLineEdit(self.frame_9)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_11.sizePolicy().hasHeightForWidth())
        self.lineEdit_11.setSizePolicy(sizePolicy)
        self.lineEdit_11.setMaximumSize(QSize(30, 16777215))
        self.lineEdit_11.setStyleSheet(u"QLineEdit { border: white }")
        self.lineEdit_11.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.lineEdit_11, 1, 1, 1, 1)

        self.horizontalSlider_9 = QSlider(self.frame_9)
        self.horizontalSlider_9.setObjectName(u"horizontalSlider_9")
        self.horizontalSlider_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.horizontalSlider_9.setStyleSheet(u"QSlider::handle:horizontal {\n"
"    background: #287CFA;\n"
"    border: 1px solid #287CFA;\n"
"    width: 18px;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"    background: #1265EA;\n"
"    border: 1px solid #1265EA;\n"
"    width: 18px;\n"
"    border-radius: 3px;\n"
"}")
        self.horizontalSlider_9.setTracking(True)
        self.horizontalSlider_9.setOrientation(Qt.Horizontal)
        self.horizontalSlider_9.setInvertedAppearance(False)
        self.horizontalSlider_9.setInvertedControls(False)

        self.gridLayout_8.addWidget(self.horizontalSlider_9, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_9, 7, 0, 1, 1)

        self.line = QFrame(self.frame_2)
        self.line.setObjectName(u"line")
        self.line.setMaximumSize(QSize(16777215, 1))
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(1)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QFrame.HLine)

        self.gridLayout_2.addWidget(self.line, 6, 0, 1, 1)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"QFrame{\n"
"	border-color: 0px;\n"
"    border-radius: 0px;\n"
"    padding: 2px;\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.lineEdit_9 = QLineEdit(self.frame_5)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        sizePolicy.setHeightForWidth(self.lineEdit_9.sizePolicy().hasHeightForWidth())
        self.lineEdit_9.setSizePolicy(sizePolicy)
        self.lineEdit_9.setMaximumSize(QSize(30, 16777215))
        self.lineEdit_9.setStyleSheet(u"QLineEdit { border: white }")
        self.lineEdit_9.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.lineEdit_9, 2, 1, 1, 1)

        self.label_7 = QLabel(self.frame_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 20))
        self.label_7.setFont(font1)

        self.gridLayout_4.addWidget(self.label_7, 0, 0, 1, 1)

        self.horizontalSlider_14 = QSlider(self.frame_5)
        self.horizontalSlider_14.setObjectName(u"horizontalSlider_14")
        self.horizontalSlider_14.setCursor(QCursor(Qt.PointingHandCursor))
        self.horizontalSlider_14.setStyleSheet(u"QSlider::handle:horizontal {\n"
"    background: #287CFA;\n"
"    border: 1px solid #287CFA;\n"
"    width: 18px;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"    background: #1265EA;\n"
"    border: 1px solid #1265EA;\n"
"    width: 18px;\n"
"    border-radius: 3px;\n"
"}")
        self.horizontalSlider_14.setTracking(True)
        self.horizontalSlider_14.setOrientation(Qt.Horizontal)
        self.horizontalSlider_14.setInvertedAppearance(False)
        self.horizontalSlider_14.setInvertedControls(False)

        self.gridLayout_4.addWidget(self.horizontalSlider_14, 2, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_5, 2, 0, 1, 1)

        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 40))
        font2 = QFont()
        font2.setFamilies([u"Source Sans Pro"])
        font2.setPointSize(14)
        font2.setUnderline(False)
        font2.setKerning(True)
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"QLabel {\n"
"border: 0px;\n"
"}")

        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)

        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"QFrame{\n"
"	border-color: 0px;\n"
"    border-radius: 0px;\n"
"    padding: 2px;\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_6)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.lineEdit_7 = QLineEdit(self.frame_6)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        sizePolicy.setHeightForWidth(self.lineEdit_7.sizePolicy().hasHeightForWidth())
        self.lineEdit_7.setSizePolicy(sizePolicy)
        self.lineEdit_7.setMaximumSize(QSize(30, 16777215))
        self.lineEdit_7.setStyleSheet(u"QLineEdit { border: white }")
        self.lineEdit_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.lineEdit_7, 1, 1, 1, 1)

        self.label_8 = QLabel(self.frame_6)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 20))
        self.label_8.setFont(font1)

        self.gridLayout_5.addWidget(self.label_8, 0, 0, 1, 1)

        self.horizontalSlider_13 = QSlider(self.frame_6)
        self.horizontalSlider_13.setObjectName(u"horizontalSlider_13")
        self.horizontalSlider_13.setCursor(QCursor(Qt.PointingHandCursor))
        self.horizontalSlider_13.setStyleSheet(u"QSlider::handle:horizontal {\n"
"    background: #287CFA;\n"
"    border: 1px solid #287CFA;\n"
"    width: 18px;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"    background: #1265EA;\n"
"    border: 1px solid #1265EA;\n"
"    width: 18px;\n"
"    border-radius: 3px;\n"
"}")
        self.horizontalSlider_13.setTracking(True)
        self.horizontalSlider_13.setOrientation(Qt.Horizontal)
        self.horizontalSlider_13.setInvertedAppearance(False)
        self.horizontalSlider_13.setInvertedControls(False)

        self.gridLayout_5.addWidget(self.horizontalSlider_13, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_6, 3, 0, 1, 1)

        self.frame_8 = QFrame(self.frame_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"QFrame{\n"
"	border-color: 0px;\n"
"    border-radius: 0px;\n"
"    padding: 2px;\n"
"}")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_8)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_10 = QLabel(self.frame_8)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(16777215, 20))
        self.label_10.setFont(font1)

        self.gridLayout_7.addWidget(self.label_10, 0, 0, 1, 1)

        self.lineEdit_10 = QLineEdit(self.frame_8)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        sizePolicy.setHeightForWidth(self.lineEdit_10.sizePolicy().hasHeightForWidth())
        self.lineEdit_10.setSizePolicy(sizePolicy)
        self.lineEdit_10.setMaximumSize(QSize(30, 16777215))
        self.lineEdit_10.setStyleSheet(u"QLineEdit { border: white }")
        self.lineEdit_10.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.lineEdit_10, 1, 1, 1, 1)

        self.horizontalSlider_11 = QSlider(self.frame_8)
        self.horizontalSlider_11.setObjectName(u"horizontalSlider_11")
        self.horizontalSlider_11.setCursor(QCursor(Qt.PointingHandCursor))
        self.horizontalSlider_11.setStyleSheet(u"QSlider::handle:horizontal {\n"
"    background: #287CFA;\n"
"    border: 1px solid #287CFA;\n"
"    width: 18px;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"    background: #1265EA;\n"
"    border: 1px solid #1265EA;\n"
"    width: 18px;\n"
"    border-radius: 3px;\n"
"}")
        self.horizontalSlider_11.setTracking(True)
        self.horizontalSlider_11.setOrientation(Qt.Horizontal)
        self.horizontalSlider_11.setInvertedAppearance(False)
        self.horizontalSlider_11.setInvertedControls(False)

        self.gridLayout_7.addWidget(self.horizontalSlider_11, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_8, 5, 0, 1, 1)

        self.frame_7 = QFrame(self.frame_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"QFrame{\n"
"	border-color: 0px;\n"
"    border-radius: 0px;\n"
"    padding: 2px;\n"
"}")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_7)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_9 = QLabel(self.frame_7)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 20))
        self.label_9.setFont(font1)

        self.gridLayout_6.addWidget(self.label_9, 0, 0, 1, 1)

        self.lineEdit_8 = QLineEdit(self.frame_7)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        sizePolicy.setHeightForWidth(self.lineEdit_8.sizePolicy().hasHeightForWidth())
        self.lineEdit_8.setSizePolicy(sizePolicy)
        self.lineEdit_8.setMaximumSize(QSize(30, 16777215))
        self.lineEdit_8.setStyleSheet(u"QLineEdit { border: white }")
        self.lineEdit_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.lineEdit_8, 1, 1, 1, 1)

        self.horizontalSlider_12 = QSlider(self.frame_7)
        self.horizontalSlider_12.setObjectName(u"horizontalSlider_12")
        self.horizontalSlider_12.setCursor(QCursor(Qt.PointingHandCursor))
        self.horizontalSlider_12.setStyleSheet(u"QSlider::handle:horizontal {\n"
"    background: #287CFA;\n"
"    border: 1px solid #287CFA;\n"
"    width: 18px;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"    background: #1265EA;\n"
"    border: 1px solid #1265EA;\n"
"    width: 18px;\n"
"    border-radius: 3px;\n"
"}")
        self.horizontalSlider_12.setTracking(True)
        self.horizontalSlider_12.setOrientation(Qt.Horizontal)
        self.horizontalSlider_12.setInvertedAppearance(False)
        self.horizontalSlider_12.setInvertedControls(False)

        self.gridLayout_6.addWidget(self.horizontalSlider_12, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_7, 4, 0, 1, 1)

        self.frame_10 = QFrame(self.frame_2)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"QFrame{\n"
"	border-color: 0px;\n"
"    border-radius: 0px;\n"
"    padding: 2px;\n"
"}")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_10)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_12 = QLabel(self.frame_10)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(16777215, 20))
        self.label_12.setFont(font1)

        self.gridLayout_9.addWidget(self.label_12, 0, 0, 1, 1)

        self.lineEdit_12 = QLineEdit(self.frame_10)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        sizePolicy.setHeightForWidth(self.lineEdit_12.sizePolicy().hasHeightForWidth())
        self.lineEdit_12.setSizePolicy(sizePolicy)
        self.lineEdit_12.setMaximumSize(QSize(30, 16777215))
        self.lineEdit_12.setStyleSheet(u"QLineEdit { border: white }")
        self.lineEdit_12.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.lineEdit_12, 1, 1, 1, 1)

        self.horizontalSlider_10 = QSlider(self.frame_10)
        self.horizontalSlider_10.setObjectName(u"horizontalSlider_10")
        self.horizontalSlider_10.setCursor(QCursor(Qt.PointingHandCursor))
        self.horizontalSlider_10.setStyleSheet(u"QSlider::handle:horizontal {\n"
"    background: #287CFA;\n"
"    border: 1px solid #287CFA;\n"
"    width: 18px;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"    background: #1265EA;\n"
"    border: 1px solid #1265EA;\n"
"    width: 18px;\n"
"    border-radius: 3px;\n"
"}")
        self.horizontalSlider_10.setTracking(True)
        self.horizontalSlider_10.setOrientation(Qt.Horizontal)
        self.horizontalSlider_10.setInvertedAppearance(False)
        self.horizontalSlider_10.setInvertedControls(False)

        self.gridLayout_9.addWidget(self.horizontalSlider_10, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_10, 8, 0, 1, 1)

        SolverOptionsDialog.setCentralWidget(self.centralwidget)

        self.retranslateUi(SolverOptionsDialog)

        QMetaObject.connectSlotsByName(SolverOptionsDialog)
    # setupUi

    def retranslateUi(self, SolverOptionsDialog):
        SolverOptionsDialog.setWindowTitle(QCoreApplication.translate("SolverOptionsDialog", u"Impostazioni solver", None))
        self.label_11.setText(QCoreApplication.translate("SolverOptionsDialog", u"Gap relativo", None))
        self.lineEdit_11.setText(QCoreApplication.translate("SolverOptionsDialog", u"0.0", None))
        self.lineEdit_11.setPlaceholderText("")
        self.lineEdit_9.setText(QCoreApplication.translate("SolverOptionsDialog", u"0.0", None))
        self.lineEdit_9.setPlaceholderText("")
        self.label_7.setText(QCoreApplication.translate("SolverOptionsDialog", u"Robustezza", None))
        self.label_6.setText(QCoreApplication.translate("SolverOptionsDialog", u"Impostazioni solver", None))
        self.lineEdit_7.setText(QCoreApplication.translate("SolverOptionsDialog", u"0.0", None))
        self.lineEdit_7.setPlaceholderText("")
        self.label_8.setText(QCoreApplication.translate("SolverOptionsDialog", u"Giornata operatoria", None))
        self.label_10.setText(QCoreApplication.translate("SolverOptionsDialog", u"Disponibilit\u00e0 anestesisti", None))
        self.lineEdit_10.setText(QCoreApplication.translate("SolverOptionsDialog", u"0.0", None))
        self.lineEdit_10.setPlaceholderText("")
        self.label_9.setText(QCoreApplication.translate("SolverOptionsDialog", u"Anestesisti", None))
        self.lineEdit_8.setText(QCoreApplication.translate("SolverOptionsDialog", u"0.0", None))
        self.lineEdit_8.setPlaceholderText("")
        self.label_12.setText(QCoreApplication.translate("SolverOptionsDialog", u"Tempo limite", None))
        self.lineEdit_12.setText(QCoreApplication.translate("SolverOptionsDialog", u"0.0", None))
        self.lineEdit_12.setPlaceholderText("")
    # retranslateUi

