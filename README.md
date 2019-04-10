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
        )

# Add_images_to_matplotlib_NavigationToolBar2QT

In my case the purpose was to add new images to the image pool and the matplotlib, in order to be able to use images I wanted in my 
NavigationToolBar and my new button.

In that repo this is a simple override, **_BUT_** the NavigationToolBar started to be very complicated to be overriden (multiple inialisation, methods and instances...).

So to add my images to the buttons I simply decided to copy my icons directly in the matplotlib directory. I would not recommend it, but here's a solution and I would still invite you to use a venv.

Here's the points you need to pay attention to before :
- I am using Win10 so that may be not that portable,
- You need 2 icons formated that way :
  - name.png => 24x24 pixels
  - name_large.png => 48x48 pixels

```
import sys
import os
from shutil import copy2


if __name__ == '__main__':
    mpl_path = os.path.join(sys.path[-1], os.path.join('matplotlib', os.path.join('mpl-data', 'images')))
    copy2('name.png', mpl_path)
    copy2('name_large.png', mpl_path)

```
