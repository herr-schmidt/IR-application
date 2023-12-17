import copy

from const import IRConstants


class Controller():

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_dataframe(tab_name):
        pass

    def export_sheet(self, tab_name, file_name):
        self.model.export_to_excel(tab_name, file_name)

    def import_excel(self, selected_file):
        self.model.import_from_excel(selected_file)
        self.view.initialize_input_table(patients_list_dataframe=self.model.patients_dataframes[0])

        self.view.update_summary(self.model.summary)

    def edit_solver_options(self):
        self.view.open_solver_options_popup(self.model.solver_parameters)

    def confirm_solver_options(self):
        self.model.solver_parameters = self.view.solver_options_popup.solver_options
        self.model.compute_summary()
        self.view.close_solver_options_popup()
        self.view.update_summary(self.model.summary)

    def reset_solver_options(self):
        self.model.solver_parameters = copy.deepcopy(self.model.default_solver_parameters)
        self.model.compute_summary()
        self.view.solver_options_popup.solver_options = self.model.solver_parameters
        self.view.solver_options_popup.initialize_sliders()

    def get_new_tab_name(self):
        return self.model.get_new_tab_name()

    def compute_solution(self, planning_terminated):
        self.model.compute_solution()
        planning_terminated.emit()

        self.view.update_summary(self.model.summary)
        self.view.initialize_output_table(selected_patients_dataframe=self.model.patients_dataframes[1])

    def get_patients_dataframe(self, tab_name):
        return self.model.get_patients_dataframe(tab_name)

    def get_planning_dataframe(self, tab_name):
        return self.model.get_planning_dataframe(tab_name)

    def update_solver_parameters(self, new_solver_parameters):
        self.model.update_solver_parameters(new_solver_parameters)

    def get_solver_parameters(self):
        return self.model.get_solver_parameters()
