from PySide2.QtWidgets import QApplication
import numpy as np
import visoptslider

if __name__ == "__main__":
    app = QApplication()

    # Define the target function and bound
    num_dimensions = 3

    def target_function(x):
        # Rosenbrock function
        value = 0.0
        for i in range(x.shape[0] - 1):
            value += 100.0 * (x[i + 1] - x[i] * x[i]) * (x[i + 1] - x[i] * x[i]) + (1.0 - x[i]) * (1.0 - x[i])
        return value

    upper_bound = np.array([+2.0, +2.0, +2.0])
    lower_bound = np.array([-2.0, -2.0, -2.0])
    maximum_value = 200.0
    minimum_value = 0.0

    # Optional settings
    labels = ["x1", "x2", "x3"]
    show_values = True
    resolution = 200

    # Instantiate and initialize the widget
    sliders_widget = visoptslider.SlidersWidget()
    sliders_widget.initialize(num_dimensions=num_dimensions,
                              target_function=target_function,
                              upper_bound=upper_bound,
                              lower_bound=lower_bound,
                              maximum_value=maximum_value,
                              minimum_value=minimum_value,
                              labels=labels,
                              show_values=show_values,
                              resolution=resolution)

    # Set a callback function
    sliders_widget.callback = lambda: print(sliders_widget.argument)

    # Show the widget
    sliders_widget.show()
    app.exec_()
