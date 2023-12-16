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
    def __init__(self, controller, solver_options):
        super().__init__()
        self.setupUi(self)

        self.solver_options = solver_options

        self.initialize_sliders()
        self.bind_sliders_to_entries()

        self.solver_options_confirm_button.clicked.connect(controller.confirm_solver_options)
        self.solver_options_reset_button.clicked.connect(controller.reset_solver_options)

        self.show()

    def bind_sliders_to_entries(self):
        self.robustness_slider.valueChanged.connect(lambda slider=self.robustness_slider,
                                                           entry=self.robustness_slider_entry,
                                                           parameter=IRConstants.SOLVER_ROBUSTNESS_PARAM: self.update_slider(slider, entry,
                                                                                                                             parameter))
        self.operating_day_slider.valueChanged.connect(lambda slider=self.operating_day_slider,
                                                              entry=self.operating_day_slider_entry,
                                                              parameter=IRConstants.SOLVER_OPERATING_ROOM_TIME: self.update_slider(slider, entry,
                                                                                                                                   parameter))
        self.anesthetists_slider.valueChanged.connect(lambda slider=self.robustness_slider,
                                                             entry=self.anesthetists_slider_entry,
                                                             parameter=IRConstants.SOLVER_ANESTHETISTS: self.update_slider(slider, entry, parameter))
        self.anesthetists_availability_slider.valueChanged.connect(lambda slider=self.robustness_slider,
                                                                          entry=self.anesthetists_availability_slider_entry,
                                                                          parameter=IRConstants.SOLVER_ANESTHETISTS_TIME: self.update_slider(slider,
                                                                                                                                             entry,
                                                                                                                                             parameter))
        self.relative_gap_slider.valueChanged.connect(lambda slider=self.robustness_slider,
                                                             entry=self.relative_gap_slider_entry,
                                                             parameter=IRConstants.SOLVER_GAP: self.update_slider(slider, entry, parameter,
                                                                                                                  divider=2,
                                                                                                                  round_at=1))
        self.timelimit_slider.valueChanged.connect(lambda slider=self.robustness_slider,
                                                          entry=self.timelimit_slider_entry,
                                                          parameter=IRConstants.SOLVER_TIME_LIMIT: self.update_slider(slider, entry, parameter))

    def initialize_sliders(self):
        self.robustness_slider.setValue(self.solver_options[IRConstants.SOLVER_ROBUSTNESS_PARAM])
        self.robustness_slider_entry.setText(str(self.solver_options[IRConstants.SOLVER_ROBUSTNESS_PARAM]))
        self.operating_day_slider.setValue(self.solver_options[IRConstants.SOLVER_OPERATING_ROOM_TIME])
        self.operating_day_slider_entry.setText(str(self.solver_options[IRConstants.SOLVER_OPERATING_ROOM_TIME]))
        self.anesthetists_slider.setValue(self.solver_options[IRConstants.SOLVER_ANESTHETISTS])
        self.anesthetists_slider_entry.setText(str(self.solver_options[IRConstants.SOLVER_ANESTHETISTS]))
        self.anesthetists_availability_slider.setValue(self.solver_options[IRConstants.SOLVER_ANESTHETISTS_TIME])
        self.anesthetists_availability_slider_entry.setText(str(self.solver_options[IRConstants.SOLVER_ANESTHETISTS_TIME]))
        self.relative_gap_slider.setValue(self.solver_options[IRConstants.SOLVER_GAP])
        self.relative_gap_slider_entry.setText(str(self.solver_options[IRConstants.SOLVER_GAP]))
        self.timelimit_slider.setValue(self.solver_options[IRConstants.SOLVER_TIME_LIMIT])
        self.timelimit_slider_entry.setText(str(self.solver_options[IRConstants.SOLVER_TIME_LIMIT]))

    def update_slider(self, slider, entry, parameter, divider=1, round_at=None):
        new_value = round(slider / divider, round_at)
        entry.setText(str(new_value))
        self.solver_options[parameter] = new_value


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
        self.launch_planning_button.clicked.connect(self.on_planning_start)

    def on_planning_start(self):
        self.planning_progress_popup = PlanningProgressPopup()
        self.planning_thread.start()

    def on_planning_end(self):
        self.planning_progress_popup.close()

        # update interactive planning tab with plotly graph
        self.web_engine_view.load(QUrl.fromLocalFile("/planning.html"))

    def update_summary(self, summary):
        total_patients = summary[IRConstants.TOTAL_PATIENTS]
        anesthesia_patients = summary[IRConstants.ANESTHESIA_PATIENTS]
        infectious_patients = summary[IRConstants.INFECTIOUS_PATIENTS]

        robustness = summary[IRConstants.SOLVER_ROBUSTNESS_PARAM]
        operating_day = summary[IRConstants.SOLVER_OPERATING_ROOM_TIME]
        anesthetists = summary[IRConstants.SOLVER_ANESTHETISTS]
        anesthetists_availability = summary[IRConstants.SOLVER_ANESTHETISTS_TIME]
        relative_gap = summary[IRConstants.SOLVER_GAP]
        time_limit = summary[IRConstants.SOLVER_TIME_LIMIT]

        selected_patients = summary[IRConstants.SELECTED_PATIENTS]
        anesthesia_selected_patients = summary[IRConstants.ANESTHESIA_SELECTED_PATIENTS]
        infectious_selected_patients = summary[IRConstants.INFECTIOUS_SELECTED_PATIENTS]
        delayed_selected_patients = summary[IRConstants.DELAYED_SELECTED_PATIENTS]
        average_OR1_OR2_utilization = summary[IRConstants.AVERAGE_OR1_OR2_UTILIZATION]
        average_OR3_OR4_utilization = summary[IRConstants.AVERAGE_OR3_OR4_UTILIZATION]
        specialty_1_selected_ratio = summary[IRConstants.SPECIALTY_1_SELECTION_RATIO]
        specialty_2_selected_ratio = summary[IRConstants.SPECIALTY_2_SELECTION_RATIO]

        self.total_patients_summary_entry.setText(str(total_patients))
        self.total_anesthesia_patients_summary_entry.setText(str(anesthesia_patients))
        self.total_infectious_patients_summary_entry.setText(str(infectious_patients))

        self.robustness_entry.setText(str(robustness))
        self.operating_day_entry.setText(str(operating_day))
        self.anesthetists_entry.setText(str(anesthetists))
        self.anesthetists_availability_entry.setText(str(anesthetists_availability))
        self.relative_gap_entry.setText(str(relative_gap))
        self.time_limit_entry.setText(str(time_limit))

        self.selected_patients_entry.setText(selected_patients)
        self.anesthesia_selected_patients_entry.setText(anesthesia_selected_patients)
        self.infectious_selected_patients_entry.setText(infectious_selected_patients)
        self.delayed_selected_patients_entry.setText(delayed_selected_patients)
        self.average_OR1_OR2_utilization_entry.setText(average_OR1_OR2_utilization)
        self.average_OR3_OR4_utilization_entry.setText(average_OR3_OR4_utilization)
        self.specialty_1_selected_ratio_entry.setText(specialty_1_selected_ratio)
        self.specialty_2_selected_ratio_entry.setText(specialty_2_selected_ratio)

    def import_callback(self):
        filepath, _ = QFileDialog.getOpenFileName(filter="File Excel (*.xlsx;*.xls)")
        self.controller.import_excel(filepath)

    def open_solver_options_popup(self, solver_options):
        self.solver_options_popup = SolverOptionsPopup(self.controller, solver_options)

    def close_solver_options_popup(self):
        self.solver_options_popup.destroy()

    def launch_planning(self):
        print("Launching planning!")

    def cancel(self):
        print('Cancel!')

    def bind_controller(self, controller):
        self.controller = controller

        self.planning_thread = PlanningThread(self.controller)
        self.planning_thread.planning_terminated.connect(self.on_planning_end)

        self.solver_options_button.clicked.connect(self.controller.edit_solver_options)

    def initialize_input_table(self, patients_list_dataframe):
        table_model = TableModel(patients_list_dataframe)
        self.patients_list_table.setModel(table_model)
