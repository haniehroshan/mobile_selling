import tkinter
import tkinter.ttk as ttk
import tkinter.messagebox as msg

mobile_list = []


# def save_click():
#     mobile = {
#         "brand": brand.get(),
#         "model": model.get(),
#         "color": color.get(),
#         "options": {
#             "glass": glass.get(),
#             "memory": memory.get()
#         }
#     }
def save_click():
    brand_value = brand.get()
    model_value = model.get()
    color_value = color.get()
    glass_value = glass.get()
    memory_value = memory.get()

    if not brand_value or not model_value or not color_value:
        msg.showerror('Error', 'All fields must be filled out!')
        return

    mobile = {
        "brand": brand_value,
        "model": model_value,
        "color": color_value,
        "options": {
            "glass": glass_value,
            "memory": memory_value
        }
    }
    mobile_list.append(mobile)
    # msg.showinfo('Save', f'Mobile {mobile["brand"]} {mobile["model"]} is saved!')
    msg.showinfo('Save', f'Mobile{mobile} is saved!')
    reset_form()


def reset_form():
    brand.set("")
    model.set("")
    color.set("")
    glass.set(False)
    memory.set(False)


win = tkinter.Tk()
win.title('Mobile Selling')
win.geometry('420x500')

tkinter.Label(win, text='Brand').place(x=30, y=60)
brand = tkinter.StringVar()
ttk.Combobox(win, textvariable=brand,
             values=["Apple", "Samsung", "Nokia"],
             state="readonly").place(x=100, y=60)

tkinter.Label(win, text='Model').place(x=30, y=120)
model = tkinter.StringVar()
tkinter.Entry(win, textvariable=model, width=22).place(x=100, y=120)

tkinter.Label(win, text='Color').place(x=30, y=180)
color = tkinter.StringVar()
ttk.Combobox(win, textvariable=color,
             values=["White", "Black", "Red", "Blue"]).place(x=100, y=180)

tkinter.Label(win, text='Options').place(x=30, y=240)

glass = tkinter.BooleanVar()
tkinter.Checkbutton(win, text='gLass', variable=glass).place(x=100, y=240)

memory = tkinter.BooleanVar()
tkinter.Checkbutton(win, text='memory', variable=memory).place(x=100, y=270)

tkinter.Button(win, text='Sell', command=save_click, width=10).place(x=150, y=380)

win.mainloop()
print(mobile_list)
