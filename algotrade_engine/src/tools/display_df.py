import algotrade_engine.conf.settings as settings
import tkinter as tk
from pandastable import Table
from pandas import DataFrame


def display(df, name='dataframe', lines=1000):
    """
    Display a spark dataframe in a tkinter window
    Based on pandastable lib
    Best perf with PyArrow to optimize spark to pandas dataframe conversion

    `:param df:` a spark dataframe
    `:param name:` name of the output window (default : 'dataframe')
    `:param lines:` number of lines to display (default = 1000)
    """

    # moving spark dataframe to pandas
    # df_panda = df.limit(lines).toPandas()

    # define the main gui window
    main_window = tk.Toplevel()
    main_window.title(name)

    frame = tk.Frame(main_window)
    frame.pack(fill='both', expand=True)
    pt = Table(frame, dataframe=df, showtoolbar=True, showstatusbar=True)

    # hide root window and show
    main_window.master.withdraw()
    pt.show()


# settings.logger.info('Add display method to pandas Dataframe')
# DataFrame.display = display
