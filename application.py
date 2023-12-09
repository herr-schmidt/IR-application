from PySide6 import QtWidgets
import sys

from view import IRView
from model import InterventionalRadiologyModel
from controller import Controller

model = InterventionalRadiologyModel()

app = QtWidgets.QApplication(sys.argv)
view = IRView()

controller = Controller(model=model, view=view)
view.bind_controller(controller=controller)

view.show()
app.exec()
