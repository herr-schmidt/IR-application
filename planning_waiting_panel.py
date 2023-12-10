# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'planning_waiting_panel.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QProgressBar,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_PlanningProgressPopup(object):
    def setupUi(self, PlanningProgressPopup):
        if not PlanningProgressPopup.objectName():
            PlanningProgressPopup.setObjectName(u"PlanningProgressPopup")
        PlanningProgressPopup.resize(240, 120)
        PlanningProgressPopup.setMinimumSize(QSize(240, 120))
        PlanningProgressPopup.setMaximumSize(QSize(240, 120))
        PlanningProgressPopup.setStyleSheet(u"background: white;")
        self.verticalLayout = QVBoxLayout(PlanningProgressPopup)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label = QLabel(PlanningProgressPopup)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(180, 40))
        self.label.setMaximumSize(QSize(180, 40))
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignHCenter)

        self.planning_progress_bar = QProgressBar(PlanningProgressPopup)
        self.planning_progress_bar.setObjectName(u"planning_progress_bar")
        self.planning_progress_bar.setMinimumSize(QSize(180, 0))
        self.planning_progress_bar.setMaximumSize(QSize(180, 16777215))
        self.planning_progress_bar.setStyleSheet(u"QProgressBar\n"
"{\n"
"/*\n"
"background-color :white;\n"
"border: 1px solid black;\n"
"*/\n"
"height: 15px;\n"
"}")
        self.planning_progress_bar.setMaximum(0)
        self.planning_progress_bar.setValue(0)
        self.planning_progress_bar.setTextVisible(False)
        self.planning_progress_bar.setInvertedAppearance(False)

        self.verticalLayout.addWidget(self.planning_progress_bar, 0, Qt.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.retranslateUi(PlanningProgressPopup)

        QMetaObject.connectSlotsByName(PlanningProgressPopup)
    # setupUi

    def retranslateUi(self, PlanningProgressPopup):
        PlanningProgressPopup.setWindowTitle(QCoreApplication.translate("PlanningProgressPopup", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("PlanningProgressPopup", u"Calcolo pianificazione in corso...", None))
    # retranslateUi

