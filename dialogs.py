"""A collection of dialogs and message boxes.

This module contains the following functions
```
    standard:
        A unified tkinter filedialog that gracefully destroys itself when
        a selection is complete or the window is closed.

    message:
        A unified tkinter messagebox that gracefully destroys itself when the
        window is closed.
```
"""

from collections import defaultdict
from pathlib import Path
import tkinter as tk
import tkinter.filedialog as tkdialogs
import tkinter.messagebox as tkmsgbox
from typing import List, Optional, Tuple, Union


def root_deco(dialog):
    """Decorates a dialog with a toplevel that is destroyed on dialog exit."""

    def decorated(*args, **kwargs):
        #create root and withdraw from screen
        root = tk.Tk()
        root.withdraw()
        #open dialog returning result and destroy root
        result = dialog(*args, parent=root, **kwargs)
        root.destroy()
        return result
    return decorated


@root_deco
def standard(kind: str, **options: str) -> Union[Path, List[Path]]:
    """Opens a tkinter modal file dialog & returns a Path instance or list of
    Path instances.

    Args:
        kind:
            Name of a tkinter file dialog.
        options:
            - title (str):            title of the dialog window
            - initialdir (str):       dir dialog starts in
            - initialfile (str):      file selected on dialog open
            - filetypes (seq):        sequence of (label, pattern tuples) '*'
                                    with wildcard allowed
            - defaultextension (str): default ext to append during save dialogs
            - multiple (bool):        when True multiple selection enabled

    Returns:
        A Path instance or list of Path instances.
    """

    # disable parent placement since root_deco automates this
    options.pop('parent', None)
    paths = getattr(tkdialogs, kind)(**options)
    return Path(paths) if isinstance(paths, str) else [Path(p) for p in paths]


@root_deco
def message(kind: str, **options: str):
    """Opens a tkinter modal message box & returns a string response.

    Args:
        kind:
            Name of a tkinter messagebox (eg. 'askyesno')
        options:
            Any valid option for the message box except for 'parent'.

    Returns:
        A subset of (True, False, OK, None, Yes, No).
    """

    #disable parent placement since root_deco automates this
    options.pop('parent', None)
    return getattr(tkmsgbox, kind)(**options)
