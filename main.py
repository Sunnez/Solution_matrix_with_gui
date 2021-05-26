import tkinter as tk
import random
import numpy as np


class SimpleTableInput(tk.Frame):  # Класс матрицы
    def __init__(self, parent, rows, columns, check, mass):  # Конструктор таблицы(матрицы)
        tk.Frame.__init__(self, parent)  # Внутринее окно
        self._entry = {}  # Поля значений таблицы
        self.rows = rows  # Поля размеров
        self.columns = columns
        vcmd = (self.register(self._validate), "%P")
        if check is False and mass is None:  # Конструктор значений матрицы 1 (рукописное)
            for row in range(self.rows):
                for column in range(self.columns):
                    index = (row, column)
                    e = tk.Entry(self, validate="key", validatecommand=vcmd)  # Создание ячейек
                    e.grid(row=row, column=column, stick="nsew")
                    self._entry[index] = e
        if check is True and mass is None:  # Конструктор значений матрицы 2 (рандом)
            for row in range(self.rows):
                for column in range(self.columns):
                    index = (row, column)
                    e = tk.Entry(self, validate="key", validatecommand=vcmd)  # Создание ячейек
                    e.grid(row=row, column=column, stick="nsew")
                    e.insert(0, random.randint(1, 20))  # Запись значений
                    self._entry[index] = e
        if mass is not None:  # Конструктор значений матрицы 3 (перезапись)
            for row in range(self.rows):
                for column in range(self.columns):
                    index = (row, column)
                    e = tk.Entry(self, validate="key", validatecommand=vcmd)  # Создание ячейек
                    e.grid(row=row, column=column, stick="nsew")
                    e.insert(0, float('{:.3f}'.format(mass[row][column])))  # Запись значений
                    self._entry[index] = e
        for column in range(self.columns):
            self.grid_columnconfigure(column, weight=1)
        self.grid_rowconfigure(rows, weight=1)

    def get(self):  # Метод класса для получения значений из матрицы
        result = []
        for row in range(self.rows):
            current_row = []
            for column in range(self.columns):
                index = (row, column)
                current_row.append(float(self._entry[index].get()))
            result.append(current_row)
        return result  # массив значений таблицы

    def _validate(self, P):  # Метод проверки коректности значений
        if P.strip() == "":
            return True

        try:  # Обработчики исключения, условия создания массива
            f = float(P)
        except ValueError:
            self.bell()
            return False
        return True


class Example(tk.Frame):  # Главный класс получения окна
    def __init__(self, parent):  # Конструктор общего окна и кнопок
        tk.Frame.__init__(self, parent, bg="teal")  # Поля создание объектов на окне(кнопки, надписи, и т.д.)
        self.lbl4 = tk.Label(self, text="A:", bg="aqua")
        self.lbl4.pack(side="top")

        self.table = SimpleTableInput(self, 2, 2, False, None)
        self.table.pack(side="top", fill='x', expand=False, padx=10, pady=10)

        self.lbl5 = tk.Label(self, text="B:", bg="aqua")
        self.lbl5.pack(side="top")

        self.table1 = SimpleTableInput(self, 2, 2, False, None)
        self.table1.pack(side="top", fill='x', expand=False, padx=10, pady=10)

        self.lbl3 = tk.Label(self, text="Result A*B:", bg="aqua")
        self.lbl3.pack(side="top")

        self.table2 = SimpleTableInput(self, 2, 2, False, None)
        self.table2.pack(side="top", fill='x', expand=False, padx=10, pady=10)

        self.lbl = tk.Label(self, text="Size of matrix", bg="aqua")
        self.lbl.pack(side="left", )
        self.info = tk.Entry(self, width=4, bg="aqua")
        self.info.pack(side="left")
        self.info.insert(0, "2, 2")
        self.btn = tk.Button(self, text="Generate matrix", command=self.on_clicked, bg="aqua")
        self.btn.pack(side="left")
        self.btn = tk.Button(self, text="Randomize", command=self.random, bg="aqua")
        self.btn.pack(side="left")

        self.lbl1 = tk.Label(self, text="Size of matrix", padx=10, bg="aqua")
        self.lbl1.pack(side="left")
        self.info1 = tk.Entry(self, width=4, bg="aqua")
        self.info1.pack(side="left")
        self.info1.insert(0, "2, 2")
        self.btn1 = tk.Button(self, text="Generate matrix", command=self.on_clicked1, bg="aqua")
        self.btn1.pack(side="left")
        self.btn1 = tk.Button(self, text="Randomize", command=self.random1, bg="aqua")
        self.btn1.pack(side="left")

        self.submit = tk.Button(self, text="Multiply", command=self.alg, bg="aqua")
        self.submit.pack(side="left", padx=20)

    def on_clicked(self):  # Команда кнопки генерации матрицы заданого размера
        self.table.destroy()  # Резапись таблицы
        try:
            temp = str(self.info.get()).split(',')
            self.table = SimpleTableInput(self, int(temp[0]), int(temp[1]), False, None)
            self.table.pack(side="top", fill="both", expand=False, padx=10, pady=10, after=self.lbl4)
        except ValueError:
            print("Invalid input")

    def random(self):  # Команда кнопки получения рандоммных значений матрицы
        self.table.destroy()  # Резапись таблицы
        try:
            temp = str(self.info.get()).split(',')
            self.table = SimpleTableInput(self, int(temp[0]), int(temp[1]), True, None)
            self.table.pack(side="top", fill="both", expand=False, padx=10, pady=10, after=self.lbl4)
        except ValueError:
            print("Invalid input")

    def on_clicked1(self):  # Команда кнопки генерации матрицы заданого размера
        self.table1.destroy()  # Резапись таблицы
        try:
            temp = str(self.info1.get()).split(',')
            self.table1 = SimpleTableInput(self, int(temp[0]), int(temp[1]), False, None)
            self.table1.pack(side="top", fill="both", expand=False, padx=10, pady=10, after=self.lbl5)
        except ValueError:
            print("Invalid input")

    def random1(self):  # Команда кнопки получения рандоммных значений матрицы
        self.table1.destroy()  # Резапись таблицы
        try:
            temp = str(self.info1.get()).split(',')
            self.table1 = SimpleTableInput(self, int(temp[0]), int(temp[1]), True, None)
            self.table1.pack(side="top", fill="both", expand=False, padx=10, pady=10, after=self.lbl5)
        except ValueError:
            print("Invalid input")

    def alg(self):  # Команда кнопки получения решения окаймелння
        try:
            A = np.array(self.table.get())
            B = np.array(self.table1.get())
            c = A.dot(B)
            temp = A.dot(B).shape
            self.table2.destroy()  # резапись таблицы и запись полученных значений
            self.table2 = SimpleTableInput(self, int(temp[0]), int(temp[1]), False, c)
            self.table2.pack(side="top", fill="both", expand=False, after=self.lbl3)
        except ValueError:
            print("Invalid input")
        except IndexError:
            print("Index out")
        except Exception:
            print("Error got")


# Запуск окон
root = tk.Tk()
Example(root).pack(side="top", fill="both", expand=True)
root.geometry('650x400+500+200')
root.title("Matrix calculation")
root["bg"] = "black"
root.config(bg="green")
root.mainloop()
