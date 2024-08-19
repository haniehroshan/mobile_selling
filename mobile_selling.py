import tkinter
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from tkinter import END

# Showing error when the user doesn't enter anything and saves:
# def save_click():
#     if brand.get() and model.get() and color.get():
#         mobile = {
#             "brand": brand.get(),
#             "model": model.get(),
#             "color": color.get(),
#             "options": {
#                 "glass": glass.get(),
#                 "memory": memory.get()
#             }
#         }
#         mobile_list.append(mobile)
#         msg.showinfo('Save', f'Mobile {mobile["brand"]} {mobile["model"]} is saved!')
#     else:
#         msg.showerror('error', 'Please select a mobile first!')
#     reset_form()

# def reset_form():
#     brand.set("")
#     model.set("")
#     color.set("")
#     glass.set(False)
#     memory.set(False)

mobile_list = []


def save_click():
    mobile = (brand.get(), model.get(), color.get(), glass.get(), memory.get())
    mobile_list.append(mobile)
    msg.showinfo('Save', f"mobile {mobile} saved")
    refresh_table()
    brand.set("")
    model.set("")
    color.set("")
    glass.set(False)
    memory.set(False)


def refresh_table():
    # clear table
    for item in table.get_children():
        table.delete(item)
    # show mobile list on table
    for mobile in mobile_list:
        table.insert("", END, values=mobile)

    # for mobile in mobile_list:
    #     table.insert("", END, values=mobile, tags=(mobile[3], mobile[4]))


win = tkinter.Tk()
win.title('Mobile Selling')
win.geometry('800x600')

# creating a table
table = ttk.Treeview(win, columns=(1, 2, 3), show='headings')
table.heading(1, text='Brand')
table.heading(2, text='Model')
table.heading(3, text='Color')
# table.heading(4, text='Options')
table.column(1, width=100)
table.column(2, width=100)
table.column(3, width=100)
# table.column(4, width=100)
table.place(x=350, y=60)

# brand combobox
tkinter.Label(win, text='Brand').place(x=30, y=60)
brand = tkinter.StringVar()
ttk.Combobox(win, textvariable=brand,
             values=["Apple", "Samsung", "Nokia"],
             state="readonly").place(x=100, y=60)

# model Entry
tkinter.Label(win, text='Model').place(x=30, y=120)
model = tkinter.StringVar()
tkinter.Entry(win, textvariable=model, width=22).place(x=100, y=120)

# Color combobox
tkinter.Label(win, text='Color').place(x=30, y=180)
color = tkinter.StringVar()
ttk.Combobox(win, textvariable=color,
             values=["White", "Black", "Red", "Blue"]).place(x=100, y=180)

# Checkbutton for glass and memory
tkinter.Label(win, text='Options').place(x=30, y=240)

glass = tkinter.BooleanVar()
tkinter.Checkbutton(win, text='gLass', variable=glass).place(x=100, y=240)

memory = tkinter.BooleanVar()
tkinter.Checkbutton(win, text='memory', variable=memory).place(x=100, y=270)

# tag (with glass: blue, with memory: pink)
# table.tag_configure("gLass", background="lightblue")
# table.tag_configure("memory", background="pink")

# save Button with sell text
tkinter.Button(win, text='Sell', command=save_click, width=10).place(x=150, y=380)

win.mainloop()
print(mobile_list)
