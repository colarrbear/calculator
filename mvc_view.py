# """Display the calculator user interface."""
# from cal_ui import CalculatorUI
#
# if __name__ == '__main__':
#     # create the UI.  There is no controller (yet), so nothing to inject.
#     ui = CalculatorUI()
#     ui.run()

from cal_ui import CalculatorUI
from mvc_controller import CalculatorController
from mvc_model import CalculatorModel

if __name__ == '__main__':
    model = CalculatorModel()
    view = CalculatorUI()
    controller = CalculatorController(model, view)
    view.run()
