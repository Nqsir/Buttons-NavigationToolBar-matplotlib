from PyQt5.QtWidgets import QDialog, QApplication, QVBoxLayout
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT
from shutil import copy2
import sys
import random
import os


class NavigationToolbar2QT(NavigationToolbar2QT):
    # Only display the buttons we need, comment buttons you don't want to display
    NavigationToolbar2QT.toolitems = (
        ('Home', 'Reset original view', 'home', 'home'),
        ('Back', 'Back to previous view', 'back', 'back'),
        ('Forward', 'Forward to next view', 'forward', 'forward'),
        (None, None, None, None),
        ('Pan', 'Pan axes with left mouse, zoom with right', 'move', 'pan'),
        ('Zoom', 'Zoom to rectangle', 'zoom_to_rect', 'zoom'),
        # ('Subplots', 'Configure subplots', 'subplots', 'configure_subplots'),
        (None, None, None, None),
        # ('Save', 'Save the figure', 'filesave', 'save_figure'),
        ('Quit', 'Close the window', 'exit', 'close_plot'),
    )

    def close_plot(self):
        print('close_plot called')
        pass


class Plot(QDialog):
    def __init__(self):
        super().__init__()
        # Define a window (QDialog)
        self.graph = QDialog()

        # Define the figure, which contains all the plot elements and that will be imported in the canvas
        self.graph.figure = plt.figure()

        # Define the Canvas that is the area onto which the figure is drawn
        self.graph.canvas = FigureCanvas(self.graph.figure)

        # Set the graph in the window (self.graph)
        self.graph.canvas.move(0, 0)

        # Define our ToolBar that is overrode above to display only 5 buttons
        self.graph.toolbar = NavigationToolbar2QT(self.graph.canvas, self)

        # Set a layout to our window
        layout = QVBoxLayout()
        layout.addWidget(self.graph.toolbar)
        layout.addWidget(self.graph.canvas)
        self.graph.setLayout(layout)

        # Call method plot() to define any plot you wish
        self.plot()

        # Show our window
        self.graph.show()

    def plot(self):
        """
        Plot your graph
        """

        # random data
        data = [random.random() for i in range(25)]

        # reverse random data
        rev_data = data.copy()
        rev_data.reverse()

        # clear all
        self.graph.figure.clf()

        # create an axis
        ax1 = self.graph.figure.add_subplot(111)
        ax1.set_xlabel('X1')
        ax1.set_ylabel('Y1')

        # create another axis
        ax2 = ax1.twinx()
        ax2.set_ylabel('Y2')

        # plot data
        ax1.plot(data, '-', color='k')
        ax2.plot(rev_data, '-.', color='c')

        self.graph.canvas.draw()


if __name__ == '__main__':
    mpl_path = os.path.join(sys.path[-1], os.path.join('matplotlib', os.path.join('mpl-data', 'images')))
    copy2('exit.png', mpl_path)
    copy2('exit_large.png', mpl_path)
    app = QApplication(sys.argv)
    p = Plot()
    sys.exit(app.exec_())

    
