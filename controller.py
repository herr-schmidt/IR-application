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

    def create_empty_planning(self):
        tab_name = self.get_new_tab_name()

        empty_dataframe = self.model.create_empty_dataframe(tab_name)
        self.view.initialize_input_table(tab_name=tab_name,
                                         data_frame=empty_dataframe)

    def get_new_tab_name(self):
        return self.model.get_new_tab_name()

    def compute_solution(self, tab_name, optimization_completed_event):
        self.model.compute_solution(tab_name)
        optimization_completed_event.set()

    def compute_solution_summary(self, tab_name):
        return self.model.compute_solution_summary(tab_name)

    def get_patients_dataframe(self, tab_name):
        return self.model.get_patients_dataframe(tab_name)

    def get_planning_dataframe(self, tab_name):
        return self.model.get_planning_dataframe(tab_name)

    def update_solver_parameters(self, new_solver_parameters):
        self.model.update_solver_parameters(new_solver_parameters)

    def get_solver_parameters(self):
        return self.model.get_solver_parameters()
