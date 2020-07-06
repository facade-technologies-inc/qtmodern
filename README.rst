========
qtmodern
========

``qtmodern`` is a Python package aimed to make PyQt/PySide applications look
better and consistent on multiple platforms. The original repository can be 
found `here <https://github.com/gmarull/qtmodern>`_. 

In this fork, we've adapted it to have the following features:

* Improved titlebar functionality: more consistent windows-like behavior, such as dragging to top maximizing the window
* Tuned the theme colors, and added 4 other themes
* Introduced MessageBox, a QtModern implementation of QMessageBox
* Min/max/close button icons, from `here <https://www.deviantart.com/synetcon/art/OSX-Yosemite-window-buttons-459868391>`_, and the buttons are less buggy
* (WIP) Normal modal behavior (previously modality wasn't possible)

Installation
------------

Clone or download this repository, then place it in your project.

Usage
-----

In order to use ``qtmodern``, simply apply the style you want to your
application and then, create a ``ModernWindow`` enclosing the window you want to
*modernize*::

    from qtmodern.styles import Styles
    from qtmodern.windows import ModernWindow

    ...

    app = QApplication()
    win = YourWindow()

    Styles.dark(app)
    mw = ModernWindow(win)
    mw.show()

    ...

