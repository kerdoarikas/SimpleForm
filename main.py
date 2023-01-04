from tkinter import *
from Circle import Circle


def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def calculate(event):
    #print('Button clicked')
    radius = user_input.get()

    if is_float(radius):
        radius = float(radius)
        circle = Circle(radius)
        txt_field.delete('1.0', END)
        txt_field.insert(END, 'Radius: ' + str(circle.radius) + '\n')
        txt_field.insert(END, 'Diameter: ' + str(circle.get_diameter()) + '\n')
        txt_field.insert(END, 'Perimeter: ' + str(circle.get_perimeter()) + '\n')
        txt_field.insert(END, 'Area: ' + str(circle.get_area()) + '\n')
        user_input.delete(0, END)

    #print(radius)


window = Tk()

window.geometry("400x400")  # Määrab algakna suuruse
window.title("Geometry - Circle")

frame_top = Frame(window, bg='#89CFF0', height=50)
frame_top.pack(fill='both')

frame_bottom = Frame(window, bg='#90EE90', height=50)
frame_bottom.pack(fill=BOTH)

lbl = Label(frame_top, text='Circle radius', bg='#89CFF0')
lbl.pack(side=LEFT)

user_input = Entry(frame_top)
user_input.pack(side=LEFT)

btn_calc = Button(frame_top, text='Calculate', command=lambda: calculate(0))
btn_calc.pack(side=LEFT, padx=4, pady=4)

txt_field = Text(frame_bottom)
txt_field.pack(side='left', padx=4, pady=4)

window.bind('<Return>', lambda event: calculate(event))

window.mainloop()