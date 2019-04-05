# Buttons-NavigationToolBar-matplotlib
How to add / remove buttons from the NavigationToolBar using Matplotlib 3.x

Using PyQt5 and matplotlib version '3.0.2'

If you want to add some buttons just follow the doc given by the class NavigationToolbar2() that is initialised in NavigationToolbar2QT() wich is imported from matplotlib.backends.backend_qt5agg :

    # list of toolitems to add to the toolbar, format is:
    # (
    #   text, # the text of the button (often not visible to users)
    #   tooltip_text, # the tooltip shown on hover (where possible)
    #   image_file, # name of the image for the button (without the extension)
    #   name_of_method, # name of the method in NavigationToolbar2 to call
    # )

So you need to redefine your class as previously said (you can also see under, the pre-defined buttons available atm). In my case I wanted to remove 2 buttons ('Save' and 'Subplots' that I commented) so that gave me :

    class NavigationToolbar2QT(NavigationToolbar2QT):
        # only display the buttons we need
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
        )

And calling the NavigationToolbar (still in my case) :

    figure = plt.figure()
    canvas = FigureCanvas(figure)
    toolbar = NavigationToolbar(canvas, self)
