import tkinter as tk
window = tk.Tk()
window.title("Calculator_MMY")
window.geometry("500x600+100+100")  # изменение геометрии окна длина х высота + отступ вправо + отступ вниз
window.resizable(True,True) # расфиксация/фиксация динамического изменеия размера окна по длине и высоте
window.minsize(300,400) # задём минимальные рамки для динам. изменения размера
window.maxsize(700,800) # задём максимальные рамки для динам. изменения размера
photo = tk.PhotoImage(file='logo.png') # загружаем иконку приложения в проект
window.iconphoto(False, photo) # прописываем иконку в шапку окна
window.config(bg = '#45D1CC') # расскрашиваем фон окна приложения под ргб код

def get_entry():
    value = name.get()
    if value:
        print(value)
    else:
        print('Empty Entry')

def delete_entry():
    name.delete(1,'end')


# знакомство с виджетами

# label_1 = tk.Label(window, text='''Ohayo
# Samurai-Neko!''',
#                    bg='#5189D2',
#                    fg='white',  # bg - фон  fg - цвет шрифта
#                    font = ('Arial',10, 'bold'),  # свойства шрифта
#                    padx=20,
#                    pady=40,  #размер области под лейбл/заголовок
#                    width=20,
#                    height=10, # отступы по длине и высоте
#                    anchor='ne',  # выравнивание по краю n- север/вверх s - юг/низ w- запад e-восток можно nw ne sw se
#                    relief=tk.RAISED, # назначение рельефа на лейбл
#                    bd=10,  # ширина тени
#                    justify=tk.RIGHT
#
#                    )
# label_1.pack()  # Размещаем заголовок в основном поле окна - Лейбл / метолд pack


# создаём кнопку

# def click():   #функция пишущая в консоль 1 при нажатии кнопки
#     print(1)
# def add_label():  # функция добавления лейбла в окне
#     label = tk.Label(window, text='Ohayo!',
#                      font = ('Arial',10, 'bold'),
#                      padx=10,
#                      pady=10,
#                      relief=tk.RAISED, # назначение рельефа на лейбл
#                      bd=10,  # ширина тени
#                      justify=tk.RIGHT
#                      )
#     label.pack()
# def counter(): # функция счетчика
#     global count
#     count+=1
#     btn4['text']=f'Счетчик: {count}'
# count=0
#
# btn1 = tk.Button(window, text="push me", command=click)
# btn2 = tk.Button(window, text="Add label", command=add_label)
# btn3 = tk.Button(window, text="dobavka",
#                  command=lambda:tk.Label(window,text='new lambda').pack()
#                  )
# btn4 = tk.Button(window, text=f'Счетчик: {count}',
#                  command=counter,
#                  activebackground="blue", # кнопка изменения цвета при нажатии
#                  bg='light pink',
#                  fg="red")         # после каждого нажатия розовой кнопки счетчик увеличивается +1
#
# btn1.pack()
# btn2.pack()
# btn3.pack()
# btn4.pack()

#  Размещение виджетов при помощи метода grid()

btn1 = tk.Button(window, text="1",padx=10, pady=10,relief=tk.RAISED)
btn2 = tk.Button(window, text="2",padx=10, pady=10,relief=tk.RAISED)
btn3 = tk.Button(window, text="3",padx=10, pady=10,relief=tk.RAISED)
btn4 = tk.Button(window, text=" Ohayo!!!",padx=10, pady=10,relief=tk.RAISED)
btn5 = tk.Button(window, text="5",padx=10, pady=10,relief=tk.RAISED)
btn6 = tk.Button(window, text="6",padx=10, pady=10,relief=tk.RAISED)
btn7 = tk.Button(window, text="7",padx=10, pady=10,relief=tk.RAISED)
btn8 = tk.Button(window, text="8",padx=10, pady=10,relief=tk.RAISED)


btn1.grid(row=0, column=0)  # метод расположения виджетов в виде таблицы
btn2.grid(row=0, column=1, stick='we')
btn3.grid(row=1, column=0)
btn4.grid(row=1, column=1)
btn5.grid(row=2, column=0)
btn6.grid(row=2, column=1, stick='we')
btn7.grid(row=3, column=0, columnspan=2, stick='we') # columnspan - Объединение колонок,
                                                    #   stick - растяжка обЪедин.ячейки по сторонам света
btn8.grid(row=0, column=2, rowspan=3, stick='ns')
window.grid_columnconfigure(0,minsize=100) # изменение параметров (размер) колонки в окне
window.grid_columnconfigure(1,minsize=100)

# виджет ввода entry

tk.Label(window, text='ввод').grid(row=3, column=0, stick='w') # размещение названия поля для ввода
name=tk.Entry(window)
name.grid(row=3, column=1)

tk.Button(window, text='get', command=get_entry).grid(row=4, column=0) # получение содержимого окна ввода
tk.Button(window, text='delete', command=delete_entry).grid(row=4, column=1)
window.mainloop()