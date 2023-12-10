import sys
import typing

from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import QUrl, QAbstractTableModel, QModelIndex
from PySide6.QtGui import Qt
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QFileDialog

from main_window import Ui_MainWindow
from solver_options_panel import Ui_SolverOptionsPopup
from planning_waiting_panel import Ui_PlanningProgressPopup


class TableModel(QAbstractTableModel):

    def __init__(self, table_data):
        super().__init__()
        self.table_data = table_data

    def rowCount(self, parent: QModelIndex = ...) -> int:
        return self.table_data.shape[0]

    def columnCount(self, parent: QModelIndex = ...) -> int:
        return self.table_data.shape[1]

    def data(self, index: QModelIndex, role: int = ...) -> typing.Any:
        if role == Qt.DisplayRole:
            return str(self.table_data.loc[index.row()][index.column()])

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...) -> typing.Any:
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return str(self.table_data.columns[section])

    def sort(self, column: int, order: Qt.SortOrder = ...) -> None:
        self.layoutAboutToBeChanged.emit()
        ascending_order = order == Qt.AscendingOrder
        self.table_data.sort_values(by=self.table_data.columns[column], ascending=ascending_order, inplace=True)
        self.table_data.reset_index(inplace=True, drop=True)
        self.layoutChanged.emit()

    def setColumn(self, col, array_items):
        self.table_data[col] = array_items
        self.dataChanged.emit(QModelIndex(), QModelIndex())

    def getColumn(self, col):
        return self.table_data[col]


class SolverOptionsPopup(QtWidgets.QWidget, Ui_SolverOptionsPopup):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.show()

class PlanningProgressPopup(QtWidgets.QWidget, Ui_PlanningProgressPopup):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.show()


class PlanningThread(QtCore.QThread):
    planning_terminated = QtCore.Signal()

    def run(self):
        for i in range(500000):
            print(i)
        self.planning_terminated.emit()


class IRView(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.solver_options_popup = None
        self.controller = None
        self.planning_progress_popup = None

        self.import_patients_list_button.clicked.connect(self.import_callback)
        self.solver_options_button.clicked.connect(self.open_solver_options_popup)
        self.launch_planning_button.clicked.connect(self.on_planning_start)

        self.planning_thread = PlanningThread()
        self.planning_thread.planning_terminated.connect(self.on_planning_end)

        # self.web_engine_view.load(QUrl.fromLocalFile("/ex.html"))

    def on_planning_start(self):
        self.planning_progress_popup = PlanningProgressPopup()
        # self.planning_progress_popup.setupUi()
        # self.planning_progress_popup.show()

        self.planning_thread.start()

    def on_planning_end(self):
        self.planning_progress_popup.close()

    def import_callback(self):
        filepath, _ = QFileDialog.getOpenFileName(filter="File Excel (*.xlsx;*.xls)")
        self.controller.import_excel(filepath)

    def open_solver_options_popup(self):
        self.solver_options_popup = SolverOptionsPopup()

    def launch_planning(self):
        print("Launching planning!")

    def cancel(self):
        print('Cancel!')

    def bind_controller(self, controller):
        self.controller = controller

    def initialize_input_table(self, patients_list_dataframe):
        table_model = TableModel(patients_list_dataframe)
        self.patients_list_table.setModel(table_model)
