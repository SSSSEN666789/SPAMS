import tkinter as tk
import tkinter.filedialog as fd

def py_sel():
    root = tk.Tk()
    root.geometry('320x240')
    root.title('Choose Python File')
 
    frame = tk.Frame(root)
    frame.pack()
 
    path1 = fd.askopenfilename(initialdir='/',title="select a file",
                          filetypes =(("Python files","*.py"),
                                      ("txt files","*.txt"),("all files","*.*")))
    print(path1)

    root.mainloop()

    return path1


"""
file1 = fd.askopenfile(initialdir='/',title="select a file",
                          filetypes =(("Python files","*.py"),
                                      ("txt files","*.txt"),("all files","*.*")))
 
print(file1.readline())
"""
