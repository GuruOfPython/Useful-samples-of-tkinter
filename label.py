from __future__ import absolute_import, division, print_function, unicode_literals

try:
    import tkinter as tk
except:
    import Tkinter as tk
import ttk
from tkinter import Button, filedialog, messagebox
from tkinter import *

status_var = StringVar()
status = Label(textvariable=status_var, text="Status |", bd=1, relief=GROOVE, anchor=W, width=86, bg="white",
               fg="blue")
status.place(x=40, y=380)