from mvc_view import CalculatorView
from mvc_controller import CalculatorController
from mvc_model import CalculatorModel

if __name__ == '__main__':
    # model = CalculatorModel()
    # view = CalculatorView()
    # controller = CalculatorController(model, view)
    controller = CalculatorController()
    controller.run()
