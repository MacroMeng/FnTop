import os
import time
import pathlib as pl
from tkinter import *
from tkinter.ttk import *
from tkinter import font
from tkinter import filedialog

from pyglet import font as fnt


# 基本设置
root = Tk()
root.geometry("500x300")
root.iconbitmap(pl.Path.cwd() / "img" / "logo.ico")
root.title("FnTop")
root.resizable(False, False)


# 函数
def set_exec_path() -> None:
    path = filedialog.askopenfilename(
        title="选择程序", filetypes=[("可执行文件(Windows)", "*.exe"), ("自定义", "*.*")])
    if not path:
        return
    enter.delete(0, END)
    enter.insert(0, path)


def start_starting(path: str, delay: float) -> None:
    while True:
        os.system(path)
        time.sleep(delay)


def laucher() -> None:
    ""


# 字体设置
for path in (pl.Path.cwd() / "font").iterdir():
    fnt.add_file(str(path))
font_title = font.Font(family="MiSans Bold", size=20)
font_text = font.Font(family="MiSans", size=10)

# 控件
Label(root, text="FnTop 窗口管理工具", font=font_title).pack(
    padx=10, pady=10, anchor="n", side="top", fill="x")
chooser = Frame(root)
chooser.pack(padx=10, pady=10, anchor="n", fill="x", side="top")
Label(root, text="↑选择程序（若不知道可在任务管理器中查看）↑", font=font_text).pack(
    anchor="nw", side="top", fill="both", padx=10
)
enter = Entry(chooser, font=font_text, width=50)
enter.pack(anchor="nw", side="left", fill="both")
browse = Button(chooser, text="浏览...", command=set_exec_path)
browse.pack(anchor="ne", side="right", fill="both", ipady=5)
delay_enter = Entry(chooser, font=font_text, width=60)
delay_enter.pack(anchor="w", side="left", fill="both")

root.mainloop()
