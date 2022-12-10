import tkinter as tk
window = tk.Tk()
window.title("Calculator_MMY")
window.geometry(f"260x280+100+200")  # изменение геометрии окна длина х высота + отступ вправо + отступ вниз
window.resizable(True,True) # True расфиксация/ false фиксация динамического изменеия размера окна по длине и высоте
window.minsize(220,300) # задём минимальные рамки для динам. изменения размера
window.maxsize(700,800) # задём максимальные рамки для динам. изменения размера
photo = tk.PhotoImage(file='logo.png') # загружаем иконку приложения в проект
window.iconphoto(False, photo) # прописываем иконку в шапку окна
window.config(bg = '#45D1CC') # расскрашиваем фон окна приложения под ргб код

# вводим функцию ввода ЦИФР в поле add_digit(i)

def add_digit(digit):
    value=calc.get()+str(digit) #добавление цифры справа
    if value[0]=='0':
        value=value[1:]
    calc.delete(0,tk.END) #очищение
    calc.insert(0,value) # добавление нового значения

# вводим функцию ввода ОПЕРАТОРОВ в поле add_digit(i)

def add_operation(operation):
    value=calc.get() #добавление операции
    if value[-1] in '-+/*':       # определение символа
        value=value[:-1]
    calc.delete(0,tk.END) #очищение старого значения
    calc.insert(0,value + operation) # добавление нового значения

# вводим функцию результата

def calcula():
    value=calc.get()
    if value[-1] in '-+/*':
        operation = value[-1]
        value = value + value[:-1]   # если провести операцию в стиле 5+= оно проведет операцию на само себя
    calc.delete(0,tk.END)
    calc.insert(0,eval(value))

# Очищаем область ввода

def clear():
    calc.delete(0,tk.END)
    calc.insert(0,0)


# размещение названия поля для ввода
calc=tk.Entry(window, justify=tk.RIGHT, font = ('Arial',15, 'bold'), width=15)  # и текст пишется в поле справа шрифтом ареал
calc.grid(row=0, column=0, columnspan=4, stick='we', padx=5)

# кнопки
btn0 = tk.Button(window, text="0",relief=tk.RAISED, bd=5, font=10, command=lambda : add_digit(0))
btn1 = tk.Button(window, text="1",relief=tk.RAISED, bd=5, font=10, command=lambda : add_digit(1))
btn2 = tk.Button(window, text="2",relief=tk.RAISED, bd=5, font=10, command=lambda : add_digit(2))
btn3 = tk.Button(window, text="3",relief=tk.RAISED, bd=5, font=10, command=lambda : add_digit(3))
btn4 = tk.Button(window, text="4",relief=tk.RAISED, bd=5, font=10, command=lambda : add_digit(4))
btn5 = tk.Button(window, text="5",relief=tk.RAISED, bd=5, font=10, command=lambda : add_digit(5))
btn6 = tk.Button(window, text="6",relief=tk.RAISED, bd=5, font=10, command=lambda : add_digit(6))
btn7 = tk.Button(window, text="7",relief=tk.RAISED, bd=5, font=10, command=lambda : add_digit(7))
btn8 = tk.Button(window, text="8",relief=tk.RAISED, bd=5, font=10, command=lambda : add_digit(8))
btn9 = tk.Button(window, text="9",relief=tk.RAISED, bd=5, font=10, command=lambda : add_digit(9))
btn10 = tk.Button(window, text="С",relief=tk.RAISED, bd=5, font=10, command=clear)
btn11 = tk.Button(window, text="=",relief=tk.RAISED, bd=5, font=10, command=calcula)
btn12 = tk.Button(window, text="+",relief=tk.RAISED, bd=5, font=10, command=lambda : add_operation('+'))
btn13 = tk.Button(window, text="-",relief=tk.RAISED, bd=5, font=10, command=lambda : add_operation('-'))
btn14 = tk.Button(window, text="*",relief=tk.RAISED, bd=5, font=10, command=lambda : add_operation('*'))
btn15 = tk.Button(window, text="/",relief=tk.RAISED, bd=5, font=10, command=lambda : add_operation('/'))


btn0.grid(row=4, column=0, stick='wens', padx=3, pady=3)
btn1.grid(row=3, column=0, stick='wens', padx=3, pady=3)
btn2.grid(row=3, column=1, stick='wens', padx=3, pady=3)
btn3.grid(row=3, column=2, stick='wens', padx=3, pady=3)
btn4.grid(row=2, column=0, stick='wens', padx=3, pady=3)
btn5.grid(row=2, column=1, stick='wens', padx=3, pady=3)
btn6.grid(row=2, column=2, stick='wens', padx=3, pady=3)
btn7.grid(row=1, column=0, stick='wens', padx=3, pady=3)
btn8.grid(row=1, column=1, stick='wens', padx=3, pady=3)
btn9.grid(row=1, column=2, stick='wens', padx=3, pady=3)
btn10.grid(row=4, column=1, stick='wens', padx=3, pady=3)
btn11.grid(row=4, column=3, stick='wens', padx=3, pady=3)
btn12.grid(row=3, column=3, stick='wens', padx=3, pady=3)
btn13.grid(row=2, column=3, stick='wens', padx=3, pady=3)
btn14.grid(row=1, column=3, stick='wens', padx=3, pady=3)
btn15.grid(row=4, column=2, stick='wens', padx=3, pady=3)


window.grid_columnconfigure(0,minsize=60)
window.grid_columnconfigure(1,minsize=60)
window.grid_columnconfigure(2,minsize=60)
window.grid_columnconfigure(3,minsize=60)

window.grid_rowconfigure(1,minsize=60)
window.grid_rowconfigure(2,minsize=60)
window.grid_rowconfigure(3,minsize=60)
window.grid_rowconfigure(4,minsize=60)
window.grid_rowconfigure(5,minsize=60)

window.mainloop()