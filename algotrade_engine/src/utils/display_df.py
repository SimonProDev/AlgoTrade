import algotrade_engine.conf.settings as settings
import tkinter as tk
from pandastable import Table
from pandas import DataFrame


def display(df, name='dataframe', lines=1000):
    """
    Display a spark dataframe in a tkinter window
    Based on pandastable lib
    Best perf with PyArrow to optimize spark to pandas dataframe conversion

    `:param df:` a pandas dataframe
    `:param name:` name of the output window (default : 'dataframe')
    `:param lines:` number of lines to display (default = 1000)
    """

    # define the main gui window
    main_window = tk.Toplevel()
    main_window.title(name)

    frame = tk.Frame(main_window)
    frame.pack(fill='both', expand=True)
    pt = Table(frame, dataframe=df, showtoolbar=True, showstatusbar=True)

    # hide root window and show
    main_window.master.withdraw()
    pt.show()
