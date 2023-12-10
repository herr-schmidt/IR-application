import typing

from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import QUrl, QAbstractTableModel, QModelIndex
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QFileDialog

from const import IRConstants
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

    def __init__(self, controller):
        super().__init__()

        self.controller = controller

    def run(self):
        self.controller.compute_solution(self.planning_terminated)


class IRView(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.solver_options_popup = None
        self.controller = None
        self.planning_progress_popup = None
        self.planning_thread = None

        self.import_patients_list_button.clicked.connect(self.import_callback)
        self.solver_options_button.clicked.connect(self.open_solver_options_popup)
        self.launch_planning_button.clicked.connect(self.on_planning_start)


        # self.web_engine_view.load(QUrl.fromLocalFile("/ex.html"))

    def on_planning_start(self):
        self.planning_progress_popup = PlanningProgressPopup()
        self.planning_thread.start()

    def on_planning_end(self):
        self.planning_progress_popup.close()

        # update solution summary
        self.update_patients_summary()

        # update interactive planning tab with plotly graph
        self.web_engine_view.load(QUrl.fromLocalFile("/planning.html"))

    def update_patients_summary(self):
        solution_summary = self.controller.compute_solution_summary()

        total_patients = solution_summary[IRConstants.TOTAL_PATIENTS]
        anesthesia_patients = solution_summary[IRConstants.ANESTHESIA_PATIENTS]
        infectious_patients = solution_summary[IRConstants.INFECTIOUS_PATIENTS]
        selected_patients = solution_summary[IRConstants.SELECTED_PATIENTS]
        anesthesia_selected_patients = solution_summary[IRConstants.ANESTHESIA_SELECTED_PATIENTS]
        infectious_selected_patients = solution_summary[IRConstants.INFECTIOUS_SELECTED_PATIENTS]
        delayed_selected_patients = solution_summary[IRConstants.DELAYED_SELECTED_PATIENTS]
        average_OR1_OR2_utilization = solution_summary[IRConstants.AVERAGE_OR1_OR2_UTILIZATION]
        average_OR3_OR4_utilization = solution_summary[IRConstants.AVERAGE_OR3_OR4_UTILIZATION]
        specialty_1_selected_ratio = solution_summary[IRConstants.SPECIALTY_1_SELECTION_RATIO]
        specialty_2_selected_ratio = solution_summary[IRConstants.SPECIALTY_2_SELECTION_RATIO]

        self.total_patients_summary_entry.setText(str(total_patients))
        self.total_anesthesia_patients_summary_entry.setText(str(anesthesia_patients))
        self.total_infectious_patients_summary_entry.setText(str(infectious_patients))

        self.selected_patients_label.setText(selected_patients)
        self.anesthesia_selected_patients_label.setText(anesthesia_selected_patients)
        self.infectious_selected_patients_label.setText(infectious_selected_patients)
        self.delayed_selected_patients_label.setText(delayed_selected_patients)
        self.average_OR1_OR2_utilization_label.setText(average_OR1_OR2_utilization)
        self.average_OR3_OR4_utilization_label.setText(average_OR3_OR4_utilization)
        self.specialty_1_selected_ratio_label.setText(specialty_1_selected_ratio)
        self.specialty_2_selected_ratio_label.setText(specialty_2_selected_ratio)

    def import_callback(self):
        filepath, _ = QFileDialog.getOpenFileName(filter="File Excel (*.xlsx;*.xls)")
        self.controller.import_excel(filepath)

        self.update_patients_summary()

    def open_solver_options_popup(self):
        self.solver_options_popup = SolverOptionsPopup()

    def launch_planning(self):
        print("Launching planning!")

    def cancel(self):
        print('Cancel!')

    def bind_controller(self, controller):
        self.controller = controller

        self.planning_thread = PlanningThread(self.controller)
        self.planning_thread.planning_terminated.connect(self.on_planning_end)

    def initialize_input_table(self, patients_list_dataframe):
        table_model = TableModel(patients_list_dataframe)
        self.patients_list_table.setModel(table_model)
