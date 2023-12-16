# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'solver_options_panel.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSlider, QSpacerItem, QWidget)

class Ui_SolverOptionsPopup(object):
    def setupUi(self, SolverOptionsPopup):
        if not SolverOptionsPopup.objectName():
            SolverOptionsPopup.setObjectName(u"SolverOptionsPopup")
        SolverOptionsPopup.resize(280, 550)
        SolverOptionsPopup.setMinimumSize(QSize(280, 550))
        SolverOptionsPopup.setMaximumSize(QSize(280, 550))
        SolverOptionsPopup.setStyleSheet(u"/*\n"
"background: white;\n"
"*/")
        self.frame_2 = QFrame(SolverOptionsPopup)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 10, 260, 500))
        self.frame_2.setStyleSheet(u"QFrame{\n"
"	border: 1px solid \"#DFDFDF\";\n"
"   /*\n"
"	border-radius: 8px;\n"
"	*/\n"
"    padding: 2px;\n"
"	background-color: white;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
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
        self.operating_day_slider_entry = QLineEdit(self.frame_6)
        self.operating_day_slider_entry.setObjectName(u"operating_day_slider_entry")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.operating_day_slider_entry.sizePolicy().hasHeightForWidth())
        self.operating_day_slider_entry.setSizePolicy(sizePolicy)
        self.operating_day_slider_entry.setMaximumSize(QSize(30, 16777215))
        font = QFont()
        font.setFamilies([u"Source Sans Pro"])
        font.setPointSize(10)
        self.operating_day_slider_entry.setFont(font)
        self.operating_day_slider_entry.setStyleSheet(u"QLineEdit { border: white }")
        self.operating_day_slider_entry.setAlignment(Qt.AlignCenter)
        self.operating_day_slider_entry.setReadOnly(True)

        self.gridLayout_5.addWidget(self.operating_day_slider_entry, 1, 1, 1, 1)

        self.operating_day_slider = QSlider(self.frame_6)
        self.operating_day_slider.setObjectName(u"operating_day_slider")
        self.operating_day_slider.setCursor(QCursor(Qt.PointingHandCursor))
        self.operating_day_slider.setStyleSheet(u"QSlider::handle:horizontal {\n"
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
        self.operating_day_slider.setMaximum(480)
        self.operating_day_slider.setPageStep(1)
        self.operating_day_slider.setValue(270)
        self.operating_day_slider.setTracking(True)
        self.operating_day_slider.setOrientation(Qt.Horizontal)
        self.operating_day_slider.setInvertedAppearance(False)
        self.operating_day_slider.setInvertedControls(False)

        self.gridLayout_5.addWidget(self.operating_day_slider, 1, 0, 1, 1)

        self.label_8 = QLabel(self.frame_6)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 20))
        font1 = QFont()
        font1.setFamilies([u"Source Sans Pro"])
        font1.setPointSize(10)
        font1.setUnderline(False)
        font1.setKerning(True)
        self.label_8.setFont(font1)

        self.gridLayout_5.addWidget(self.label_8, 0, 0, 1, 2)


        self.gridLayout_2.addWidget(self.frame_6, 2, 0, 1, 1)

        self.line = QFrame(self.frame_2)
        self.line.setObjectName(u"line")
        self.line.setMaximumSize(QSize(16777215, 1))
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(1)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QFrame.HLine)

        self.gridLayout_2.addWidget(self.line, 5, 0, 1, 1)

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
        self.anesthetists_slider_entry = QLineEdit(self.frame_7)
        self.anesthetists_slider_entry.setObjectName(u"anesthetists_slider_entry")
        sizePolicy.setHeightForWidth(self.anesthetists_slider_entry.sizePolicy().hasHeightForWidth())
        self.anesthetists_slider_entry.setSizePolicy(sizePolicy)
        self.anesthetists_slider_entry.setMaximumSize(QSize(30, 16777215))
        self.anesthetists_slider_entry.setFont(font)
        self.anesthetists_slider_entry.setStyleSheet(u"QLineEdit { border: white }")
        self.anesthetists_slider_entry.setAlignment(Qt.AlignCenter)
        self.anesthetists_slider_entry.setReadOnly(True)

        self.gridLayout_6.addWidget(self.anesthetists_slider_entry, 1, 1, 1, 1)

        self.anesthetists_slider = QSlider(self.frame_7)
        self.anesthetists_slider.setObjectName(u"anesthetists_slider")
        self.anesthetists_slider.setCursor(QCursor(Qt.PointingHandCursor))
        self.anesthetists_slider.setStyleSheet(u"QSlider::handle:horizontal {\n"
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
        self.anesthetists_slider.setMaximum(5)
        self.anesthetists_slider.setPageStep(1)
        self.anesthetists_slider.setValue(1)
        self.anesthetists_slider.setTracking(True)
        self.anesthetists_slider.setOrientation(Qt.Horizontal)
        self.anesthetists_slider.setInvertedAppearance(False)
        self.anesthetists_slider.setInvertedControls(False)

        self.gridLayout_6.addWidget(self.anesthetists_slider, 1, 0, 1, 1)

        self.label_9 = QLabel(self.frame_7)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 20))
        self.label_9.setFont(font1)

        self.gridLayout_6.addWidget(self.label_9, 0, 0, 1, 2)


        self.gridLayout_2.addWidget(self.frame_7, 3, 0, 1, 1)

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
        self.robustness_slider_entry = QLineEdit(self.frame_5)
        self.robustness_slider_entry.setObjectName(u"robustness_slider_entry")
        sizePolicy.setHeightForWidth(self.robustness_slider_entry.sizePolicy().hasHeightForWidth())
        self.robustness_slider_entry.setSizePolicy(sizePolicy)
        self.robustness_slider_entry.setMaximumSize(QSize(30, 16777215))
        self.robustness_slider_entry.setFont(font)
        self.robustness_slider_entry.setStyleSheet(u"QLineEdit { border: white }")
        self.robustness_slider_entry.setAlignment(Qt.AlignCenter)
        self.robustness_slider_entry.setReadOnly(True)

        self.gridLayout_4.addWidget(self.robustness_slider_entry, 2, 1, 1, 1)

        self.robustness_slider = QSlider(self.frame_5)
        self.robustness_slider.setObjectName(u"robustness_slider")
        self.robustness_slider.setCursor(QCursor(Qt.PointingHandCursor))
        self.robustness_slider.setStyleSheet(u"QSlider::handle:horizontal {\n"
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
        self.robustness_slider.setMaximum(5)
        self.robustness_slider.setPageStep(1)
        self.robustness_slider.setTracking(True)
        self.robustness_slider.setOrientation(Qt.Horizontal)
        self.robustness_slider.setInvertedAppearance(False)
        self.robustness_slider.setInvertedControls(False)

        self.gridLayout_4.addWidget(self.robustness_slider, 2, 0, 1, 1)

        self.label_7 = QLabel(self.frame_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 20))
        self.label_7.setFont(font1)

        self.gridLayout_4.addWidget(self.label_7, 0, 0, 1, 2)


        self.gridLayout_2.addWidget(self.frame_5, 1, 0, 1, 1)

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
        self.relative_gap_slider_entry = QLineEdit(self.frame_9)
        self.relative_gap_slider_entry.setObjectName(u"relative_gap_slider_entry")
        sizePolicy.setHeightForWidth(self.relative_gap_slider_entry.sizePolicy().hasHeightForWidth())
        self.relative_gap_slider_entry.setSizePolicy(sizePolicy)
        self.relative_gap_slider_entry.setMaximumSize(QSize(30, 16777215))
        self.relative_gap_slider_entry.setFont(font)
        self.relative_gap_slider_entry.setStyleSheet(u"QLineEdit { border: white }")
        self.relative_gap_slider_entry.setAlignment(Qt.AlignCenter)
        self.relative_gap_slider_entry.setReadOnly(True)

        self.gridLayout_8.addWidget(self.relative_gap_slider_entry, 1, 1, 1, 1)

        self.relative_gap_slider = QSlider(self.frame_9)
        self.relative_gap_slider.setObjectName(u"relative_gap_slider")
        self.relative_gap_slider.setCursor(QCursor(Qt.PointingHandCursor))
        self.relative_gap_slider.setStyleSheet(u"QSlider::handle:horizontal {\n"
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
        self.relative_gap_slider.setMaximum(50)
        self.relative_gap_slider.setSingleStep(1)
        self.relative_gap_slider.setPageStep(1)
        self.relative_gap_slider.setTracking(True)
        self.relative_gap_slider.setOrientation(Qt.Horizontal)
        self.relative_gap_slider.setInvertedAppearance(False)
        self.relative_gap_slider.setInvertedControls(False)

        self.gridLayout_8.addWidget(self.relative_gap_slider, 1, 0, 1, 1)

        self.label_11 = QLabel(self.frame_9)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(16777215, 20))
        self.label_11.setFont(font1)

        self.gridLayout_8.addWidget(self.label_11, 0, 0, 1, 2)


        self.gridLayout_2.addWidget(self.frame_9, 6, 0, 1, 1)

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
        self.timelimit_slider_entry = QLineEdit(self.frame_10)
        self.timelimit_slider_entry.setObjectName(u"timelimit_slider_entry")
        sizePolicy.setHeightForWidth(self.timelimit_slider_entry.sizePolicy().hasHeightForWidth())
        self.timelimit_slider_entry.setSizePolicy(sizePolicy)
        self.timelimit_slider_entry.setMaximumSize(QSize(30, 16777215))
        self.timelimit_slider_entry.setFont(font)
        self.timelimit_slider_entry.setStyleSheet(u"QLineEdit { border: white }")
        self.timelimit_slider_entry.setAlignment(Qt.AlignCenter)
        self.timelimit_slider_entry.setReadOnly(True)

        self.gridLayout_9.addWidget(self.timelimit_slider_entry, 1, 1, 1, 1)

        self.timelimit_slider = QSlider(self.frame_10)
        self.timelimit_slider.setObjectName(u"timelimit_slider")
        self.timelimit_slider.setCursor(QCursor(Qt.PointingHandCursor))
        self.timelimit_slider.setStyleSheet(u"QSlider::handle:horizontal {\n"
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
        self.timelimit_slider.setMaximum(3600)
        self.timelimit_slider.setPageStep(1)
        self.timelimit_slider.setValue(600)
        self.timelimit_slider.setTracking(True)
        self.timelimit_slider.setOrientation(Qt.Horizontal)
        self.timelimit_slider.setInvertedAppearance(False)
        self.timelimit_slider.setInvertedControls(False)

        self.gridLayout_9.addWidget(self.timelimit_slider, 1, 0, 1, 1)

        self.label_12 = QLabel(self.frame_10)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(16777215, 20))
        self.label_12.setFont(font1)

        self.gridLayout_9.addWidget(self.label_12, 0, 0, 1, 2)


        self.gridLayout_2.addWidget(self.frame_10, 7, 0, 1, 1)

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
        self.anesthetists_availability_slider_entry = QLineEdit(self.frame_8)
        self.anesthetists_availability_slider_entry.setObjectName(u"anesthetists_availability_slider_entry")
        sizePolicy.setHeightForWidth(self.anesthetists_availability_slider_entry.sizePolicy().hasHeightForWidth())
        self.anesthetists_availability_slider_entry.setSizePolicy(sizePolicy)
        self.anesthetists_availability_slider_entry.setMaximumSize(QSize(30, 16777215))
        self.anesthetists_availability_slider_entry.setFont(font)
        self.anesthetists_availability_slider_entry.setStyleSheet(u"QLineEdit { border: white }")
        self.anesthetists_availability_slider_entry.setAlignment(Qt.AlignCenter)
        self.anesthetists_availability_slider_entry.setReadOnly(True)

        self.gridLayout_7.addWidget(self.anesthetists_availability_slider_entry, 1, 1, 1, 1)

        self.anesthetists_availability_slider = QSlider(self.frame_8)
        self.anesthetists_availability_slider.setObjectName(u"anesthetists_availability_slider")
        self.anesthetists_availability_slider.setCursor(QCursor(Qt.PointingHandCursor))
        self.anesthetists_availability_slider.setStyleSheet(u"QSlider::handle:horizontal {\n"
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
        self.anesthetists_availability_slider.setMaximum(480)
        self.anesthetists_availability_slider.setPageStep(1)
        self.anesthetists_availability_slider.setValue(270)
        self.anesthetists_availability_slider.setTracking(True)
        self.anesthetists_availability_slider.setOrientation(Qt.Horizontal)
        self.anesthetists_availability_slider.setInvertedAppearance(False)
        self.anesthetists_availability_slider.setInvertedControls(False)

        self.gridLayout_7.addWidget(self.anesthetists_availability_slider, 1, 0, 1, 1)

        self.label_10 = QLabel(self.frame_8)
        self.label_10.setObjectName(u"label_10")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy1)
        self.label_10.setMaximumSize(QSize(16777215, 20))
        self.label_10.setFont(font1)

        self.gridLayout_7.addWidget(self.label_10, 0, 0, 1, 2)


        self.gridLayout_2.addWidget(self.frame_8, 4, 0, 1, 1)

        self.horizontalLayoutWidget = QWidget(SolverOptionsPopup)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 510, 261, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.solver_options_reset_button = QPushButton(self.horizontalLayoutWidget)
        self.solver_options_reset_button.setObjectName(u"solver_options_reset_button")

        self.horizontalLayout.addWidget(self.solver_options_reset_button)

        self.solver_options_confirm_button = QPushButton(self.horizontalLayoutWidget)
        self.solver_options_confirm_button.setObjectName(u"solver_options_confirm_button")

        self.horizontalLayout.addWidget(self.solver_options_confirm_button)


        self.retranslateUi(SolverOptionsPopup)

        QMetaObject.connectSlotsByName(SolverOptionsPopup)
    # setupUi

    def retranslateUi(self, SolverOptionsPopup):
        SolverOptionsPopup.setWindowTitle(QCoreApplication.translate("SolverOptionsPopup", u"Form", None))
        self.operating_day_slider_entry.setText(QCoreApplication.translate("SolverOptionsPopup", u"270", None))
        self.operating_day_slider_entry.setPlaceholderText("")
        self.label_8.setText(QCoreApplication.translate("SolverOptionsPopup", u"Giornata operatoria (min)", None))
        self.anesthetists_slider_entry.setText(QCoreApplication.translate("SolverOptionsPopup", u"1", None))
        self.anesthetists_slider_entry.setPlaceholderText("")
        self.label_9.setText(QCoreApplication.translate("SolverOptionsPopup", u"Anestesisti per giorno", None))
        self.robustness_slider_entry.setText(QCoreApplication.translate("SolverOptionsPopup", u"0", None))
        self.robustness_slider_entry.setPlaceholderText("")
        self.label_7.setText(QCoreApplication.translate("SolverOptionsPopup", u"Robustezza (pz/sala)", None))
        self.relative_gap_slider_entry.setText(QCoreApplication.translate("SolverOptionsPopup", u"0.0", None))
        self.relative_gap_slider_entry.setPlaceholderText("")
        self.label_11.setText(QCoreApplication.translate("SolverOptionsPopup", u"Gap relativo (%)", None))
        self.timelimit_slider_entry.setText(QCoreApplication.translate("SolverOptionsPopup", u"600", None))
        self.timelimit_slider_entry.setPlaceholderText("")
        self.label_12.setText(QCoreApplication.translate("SolverOptionsPopup", u"Tempo limite (s)", None))
        self.anesthetists_availability_slider_entry.setText(QCoreApplication.translate("SolverOptionsPopup", u"270", None))
        self.anesthetists_availability_slider_entry.setPlaceholderText("")
        self.label_10.setText(QCoreApplication.translate("SolverOptionsPopup", u"Disponibilit\u00e0 anestesisti (min/gg)", None))
        self.solver_options_reset_button.setText(QCoreApplication.translate("SolverOptionsPopup", u"Reset", None))
        self.solver_options_confirm_button.setText(QCoreApplication.translate("SolverOptionsPopup", u"Conferma", None))
    # retranslateUi

