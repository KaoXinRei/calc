import tkinter as tk
import tkinter.ttk as ttk
import sys
from math import *


def cot(x):
    return 1 / tan(x)


class Window(ttk.Frame):

    def __init__(self, master):
        super().__init__(master, padding=2)
        self.create_variables()
        self.create_widgets()
        self.create_layout()
        self.bind_buttons()
        self.bind_keys()


    def create_variables(self):
        self.input_var = tk.StringVar()
        self.ans = tk.StringVar()
        self.flag = True
        self.error = False
        self.accuracy = tk.IntVar()
        self.accuracy.set(16)

    def create_widgets(self):
        self.input = tk.Entry(self, justify='right', textvariable=self.input_var, state='readonly')
        self.output = tk.Entry(self, justify='right', textvariable=self.ans, state='readonly')
        self.answer = tk.Label(self, text='Answer:')
        self.history_text = tk.Label(self, text='History:', width=10)
        self.box_history = tk.Listbox(self, width=30)
        self.Scrollbar_horizontal = tk.Scrollbar(self.box_history, orient='horizontal', command=self.box_history.xview)
        self.Scrollbar_vertical = tk.Scrollbar(self.box_history, orient='vertical', command=self.box_history.yview)
        self.box_history.config(xscrollcommand=self.Scrollbar_horizontal.set,
                                yscrollcommand=self.Scrollbar_vertical.set)
        self.Button_1 = tk.Button(self, text='1', width=7, height=2)
        self.Button_2 = tk.Button(self, text='2', width=7)
        self.Button_3 = tk.Button(self, text='3', width=7)
        self.Button_4 = tk.Button(self, text='4', height=2)
        self.Button_5 = tk.Button(self, text='5')
        self.Button_6 = tk.Button(self, text='6')
        self.Button_7 = tk.Button(self, text='7', height=2)
        self.Button_8 = tk.Button(self, text='8')
        self.Button_9 = tk.Button(self, text='9')
        self.Button_0 = tk.Button(self, text='0', height=2)
        self.Button_c = tk.Button(self, text='c', height=2)
        self.Button_plus = tk.Button(self, text='+', width=7)
        self.Button_minus = tk.Button(self, text='-')
        self.Button_equals = tk.Button(self, text='=')
        self.Button_multiply = tk.Button(self, text='*')
        self.Button_divide = tk.Button(self, text='/')
        self.Button_bracket1 = tk.Button(self, text='(')
        self.Button_bracket2 = tk.Button(self, text=')')
        self.Button_point = tk.Button(self, text='.')
        self.Button_backspace = tk.Button(self, text='⌫', width=10)
        self.Button_clear_history = tk.Button(self, text='Clear', width=10)
        self.Button_power = tk.Button(self, text='**')
        self.Button_div = tk.Button(self, text='//', width=7)
        self.Button_mod = tk.Button(self, text='%', width=7)
        self.Button_sin = tk.Button(self, text='sin')
        self.Button_cos = tk.Button(self, text='cos')
        self.Button_tan = tk.Button(self, text='tan')
        self.Button_cot = tk.Button(self, text='cot')
        self.Button_log = tk.Button(self, text='log')
        self.Button_log2 = tk.Button(self, text='log2')
        self.Button_log10 = tk.Button(self, text='log10')
        self.accuracy_lable = ttk.Label(self, text='Accuracy:')
        self.Scale = tk.Scale(self, from_=0, to=16, variable=self.accuracy, orient='horizontal', length=200)

    def create_layout(self):
        pad = dict(sticky=(tk.W, tk.E, tk.S, tk.N), padx=1.5, pady=1.5)
        self.history_text.grid(row=0, column=6 + 2, **pad)
        self.input.grid(row=0, column=0, columnspan=6, **pad)
        self.answer.grid(row=1, column=0, **pad)
        self.output.grid(row=1, column=1, columnspan=5, **pad)
        self.box_history.grid(row=1, column=5 + 2, rowspan=5, columnspan=3, **pad)
        self.Button_1.grid(row=5, column=0 + 2, **pad)
        self.Button_2.grid(row=5, column=1 + 2, **pad)
        self.Button_3.grid(row=5, column=2 + 2, **pad)
        self.Button_4.grid(row=4, column=0 + 2, **pad)
        self.Button_5.grid(row=4, column=1 + 2, **pad)
        self.Button_6.grid(row=4, column=2 + 2, **pad)
        self.Button_7.grid(row=3, column=0 + 2, **pad)
        self.Button_8.grid(row=3, column=1 + 2, **pad)
        self.Button_9.grid(row=3, column=2 + 2, **pad)
        self.Button_0.grid(row=6, column=0 + 2, columnspan=2, **pad)
        self.Button_c.grid(row=2, column=0 + 2, **pad)
        self.Button_plus.grid(row=5, column=3 + 2, **pad)
        self.Button_minus.grid(row=4, column=3 + 2, **pad)
        self.Button_equals.grid(row=6, column=3 + 2, **pad)
        self.Button_multiply.grid(row=3, column=3 + 2, **pad)
        self.Button_divide.grid(row=2, column=3 + 2, **pad)
        self.Button_bracket1.grid(row=2, column=1 + 2, **pad)
        self.Button_bracket2.grid(row=2, column=2 + 2, **pad)
        self.Button_point.grid(row=6, column=2 + 2, **pad)
        self.Button_power.grid(row=6, column=1, **pad)
        self.Button_div.grid(row=2, column=0, **pad)
        self.Button_mod.grid(row=2, column=1, **pad)
        self.Button_sin.grid(row=3, column=0, **pad)
        self.Button_cos.grid(row=3, column=1, **pad)
        self.Button_tan.grid(row=4, column=0, **pad)
        self.Button_cot.grid(row=4, column=1, **pad)
        self.Button_log.grid(row=5, column=0, **pad)
        self.Button_log2.grid(row=5, column=1, **pad)
        self.Button_log10.grid(row=6, column=0, **pad)
        self.Button_backspace.grid(row=0, column=5 + 2, **pad)
        self.Button_clear_history.grid(row=0, column=7 + 2, **pad)
        self.Scrollbar_horizontal.pack(side='bottom', fill='x')
        self.Scrollbar_vertical.pack(side='right', fill='y')
        self.accuracy_lable.grid(row=6, column=7, **pad)
        self.Scale.grid(row=6, column=8,columnspan=2)
        self.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.E, tk.W))

    def click_1(self, event=None):
        if self.flag:
            self.input_var.set(self.input_var.get() + '1')
        else:
            self.input_var.set('')
            self.flag = True
            self.error = False
            self.ans.set('')
            self.click_1(self)

    def click_2(self, event=None):
        if self.flag:
            self.input_var.set(self.input_var.get() + '2')
        else:
            self.input_var.set('')
            self.flag = True
            self.error = False
            self.ans.set('')
            self.click_2(self)

    def click_3(self, event=None):
        if self.flag:
            self.input_var.set(self.input_var.get() + '3')
        else:
            self.input_var.set('')
            self.flag = True
            self.error = False
            self.ans.set('')
            self.click_3(self)

    def click_4(self, event=None):
        if self.flag:
            self.input_var.set(self.input_var.get() + '4')
        else:
            self.input_var.set('')
            self.flag = True
            self.error = False
            self.ans.set('')
            self.click_4(self)

    def click_5(self, event=None):
        if self.flag:
            self.input_var.set(self.input_var.get() + '5')
        else:
            self.input_var.set('')
            self.flag = True
            self.error = False
            self.ans.set('')
            self.click_5(self)

    def click_6(self, event=None):
        if self.flag:
            self.input_var.set(self.input_var.get() + '6')
        else:
            self.input_var.set('')
            self.flag = True
            self.error = False
            self.ans.set('')
            self.click_6(self)

    def click_7(self, event=None):
        if self.flag:
            self.input_var.set(self.input_var.get() + '7')
        else:
            self.input_var.set('')
            self.flag = True
            self.error = False
            self.ans.set('')
            self.click_7(self)

    def click_8(self, event=None):
        if self.flag:
            self.input_var.set(self.input_var.get() + '8')
        else:
            self.input_var.set('')
            self.flag = True
            self.error = False
            self.ans.set('')
            self.click_8(self)

    def click_9(self, event=None):
        if self.flag:
            self.input_var.set(self.input_var.get() + '9')
        else:
            self.input_var.set('')
            self.flag = True
            self.error = False
            self.ans.set('')
            self.click_9(self)

    def click_0(self, event=None):
        if self.flag:
            self.input_var.set(self.input_var.get() + '0')
        else:
            self.input_var.set('')
            self.flag = True
            self.error = False
            self.ans.set('')
            self.click_0(self)

    def click_c(self, event):
        self.input_var.set('')
        self.ans.set('')
        self.flag = True
        self.error = False

    def click_plus(self, event):
        if self.flag:
            self.input_var.set(self.input_var.get() + '+')
        elif not self.error:
            self.input_var.set(self.ans.get())
            self.flag = True
            self.error = False
            self.ans.set('')
            self.click_plus(self)

    def click_minus(self, event):
        if self.flag:
            self.input_var.set(self.input_var.get() + '-')
        elif not self.error:
            self.input_var.set(self.ans.get())
            self.flag = True
            self.error = False
            self.ans.set('')
            self.click_minus(self)

    def click_multiply(self, event):
        if self.flag:
            self.input_var.set(self.input_var.get() + '*')
        elif not self.error:
            self.input_var.set(self.ans.get())
            self.flag = True
            self.error = False
            self.ans.set('')
            self.click_multiply(self)

    def click_divide(self, event):
        if self.flag:
            self.input_var.set(self.input_var.get() + '/')
        elif not self.error:
            self.input_var.set(self.ans.get())
            self.flag = True
            self.error = False
            self.ans.set('')
            self.click_divide(self)

    def reformation_of_input(self, var):
        var = var.get()
        i = 0
        while i < len(var):
            if not (var[i].isnumeric()) and not var[i] == '.':
                if var[i] == '-':
                    if i == 0:
                        pass
                    elif var[i - 1] == ' ':
                        pass
                    else:
                        var = var[:i] + ' ' + var[i] + ' ' + (var[-1:i:-1])[::-1]
                        i += 2
                else:
                    var = var[:i] + ' ' + var[i] + ' ' + (var[-1:i:-1])[::-1]
                    i += 2
            i += 1
        return var.split()

    def click_equals(self, event):
        if not self.error:
            try:
                self.flag = False
                op = ['-', '*', '**', '+', '/', '//', '%']
                ans = self.reformation_of_input(self.input)
                if ans[-1] in op:
                    a = str(eval(''.join(ans[:-1])))
                    x = round(eval(a + ans[-1] + a), self.accuracy.get())
                    self.input_var.set(a + ans[-1] + a)
                else:
                    x = round(eval(self.input_var.get()), self.accuracy.get())
                x = float(x)
                if x.is_integer():
                    x = int(x)
                self.ans.set(x)
                self.box_history.insert(0, self.input_var.get() + '=' + self.ans.get())
            except ZeroDivisionError:
                self.ans.set('Division by zero')
                self.error = True
            except OverflowError:
                self.ans.set('Answer is too big')
                self.error = True
            except:
                self.ans.set('Incorrect input')
                self.error = True

    def click_bracket1(self, event):
        if self.flag:
            self.input_var.set(self.input_var.get() + '(')
        else:
            self.input_var.set('')
            self.flag = True
            self.error = False
            self.ans.set('')
            self.click_bracket1(self)

    def click_bracket2(self, event):
        if self.flag:
            self.input_var.set(self.input_var.get() + ')')

    def click_point(self, event):
        if self.flag:
            self.input_var.set(self.input_var.get() + '.')

    def click_backspace(self, event):
        if self.flag:
            self.input_var.set(self.input_var.get()[0:-1])
        else:
            self.flag = False
            self.input_var.set('')
            self.ans.set('')

    def click_clear_history(self, event):
        self.box_history.delete(0, 'end')

    def click_power(self, event):
        if self.flag:
            self.input_var.set(self.input_var.get() + '**')
        elif not self.error:
            self.input_var.set(self.ans.get())
            self.flag = True
            self.error = False
            self.ans.set('')
            self.click_power(self)

    def choose_history(self, event):
        if self.flag:
            if self.box_history.get(0) != '':
                x = self.box_history.get(self.box_history.curselection())
                self.input_var.set(self.input_var.get() + x[x.index('=') + 1:])
        elif not self.error:
            self.input_var.set('')
            self.flag = True
            self.error = False
            self.ans.set('')
            self.choose_history(self)

    def click_div(self, event):
        if self.flag:
            self.input_var.set(self.input_var.get() + '//')
        elif not self.error:
            self.input_var.set(self.ans.get())
            self.flag = True
            self.error = False
            self.ans.set('')
            self.click_div(self)

    def click_mod(self, event):
        if self.flag:
            self.input_var.set(self.input_var.get() + '%')
        elif not self.error:
            self.input_var.set(self.ans.get())
            self.flag = True
            self.error = False
            self.ans.set('')
            self.click_mod(self)

    def click_sin(self, event):
        if self.flag:
            self.input_var.set(self.input_var.get() + 'sin(')
        else:
            self.input_var.set('')
            self.flag = True
            self.error = False
            self.ans.set('')
            self.click_sin(self)

    def click_cos(self, event):
        if self.flag:
            self.input_var.set(self.input_var.get() + 'cos(')
        else:
            self.input_var.set('')
            self.flag = True
            self.error = False
            self.ans.set('')
            self.click_cos(self)

    def click_cot(self, event):
        if self.flag:
            self.input_var.set(self.input_var.get() + 'cot(')
        else:
            self.input_var.set('')
            self.flag = True
            self.error = False
            self.ans.set('')
            self.click_cot(self)

    def click_tan(self, event):
        if self.flag:
            self.input_var.set(self.input_var.get() + 'tan(')
        else:
            self.input_var.set('')
            self.flag = True
            self.error = False
            self.ans.set('')
            self.click_tan(self)

    def click_log(self, event):
        if self.flag:
            self.input_var.set(self.input_var.get() + 'log(')
        else:
            self.input_var.set('')
            self.flag = True
            self.error = False
            self.ans.set('')
            self.click_log(self)

    def click_log2(self, event):
        if self.flag:
            self.input_var.set(self.input_var.get() + 'log2(')
        else:
            self.input_var.set('')
            self.flag = True
            self.error = False
            self.ans.set('')
            self.log2(self)

    def click_log10(self, event):
        if self.flag:
            self.input_var.set(self.input_var.get() + 'log10(')
        else:
            self.input_var.set('')
            self.flag = True
            self.error = False
            self.ans.set('')
            self.click_log10(self)

    def bind_buttons(self):
        self.Button_1.bind('<Button-1>', self.click_1)
        self.Button_2.bind('<Button-1>', self.click_2)
        self.Button_3.bind('<Button-1>', self.click_3)
        self.Button_4.bind('<Button-1>', self.click_4)
        self.Button_5.bind('<Button-1>', self.click_5)
        self.Button_6.bind('<Button-1>', self.click_6)
        self.Button_7.bind('<Button-1>', self.click_7)
        self.Button_8.bind('<Button-1>', self.click_8)
        self.Button_9.bind('<Button-1>', self.click_9)
        self.Button_0.bind('<Button-1>', self.click_0)
        self.Button_c.bind('<Button-1>', self.click_c)
        self.Button_plus.bind('<Button-1>', self.click_plus)
        self.Button_minus.bind('<Button-1>', self.click_minus)
        self.Button_multiply.bind('<Button-1>', self.click_multiply)
        self.Button_divide.bind('<Button-1>', self.click_divide)
        self.Button_equals.bind('<Button-1>', self.click_equals)
        self.Button_bracket1.bind('<Button-1>', self.click_bracket1)
        self.Button_bracket2.bind('<Button-1>', self.click_bracket2)
        self.Button_point.bind('<Button-1>', self.click_point)
        self.Button_backspace.bind('<Button-1>', self.click_backspace)
        self.Button_clear_history.bind('<Button-1>', self.click_clear_history)
        self.Button_power.bind('<Button-1>', self.click_power)
        self.box_history.bind('<Double-Button-1>', self.choose_history)
        self.Button_div.bind('<Button-1>', self.click_div)
        self.Button_mod.bind('<Button-1>', self.click_mod)
        self.Button_sin.bind('<Button-1>', self.click_sin)
        self.Button_cos.bind('<Button-1>', self.click_cos)
        self.Button_tan.bind('<Button-1>', self.click_tan)
        self.Button_cot.bind('<Button-1>', self.click_cot)
        self.Button_log.bind('<Button-1>', self.click_log)
        self.Button_log2.bind('<Button-1>', self.click_log2)
        self.Button_log10.bind('<Button-1>', self.click_log10)

    def bind_keys(self):
        self.master.bind('1', self.click_1)
        self.master.bind('2', self.click_2)
        self.master.bind('3', self.click_3)
        self.master.bind('4', self.click_4)
        self.master.bind('5', self.click_5)
        self.master.bind('6', self.click_6)
        self.master.bind('7', self.click_7)
        self.master.bind('8', self.click_8)
        self.master.bind('9', self.click_9)
        self.master.bind('0', self.click_0)
        self.master.bind('+', self.click_plus)
        self.master.bind('-', self.click_minus)
        self.master.bind('=', self.click_equals)
        self.master.bind('<Return>', self.click_equals)
        self.master.bind('*', self.click_multiply)
        self.master.bind('(', self.click_bracket1)
        self.master.bind(')', self.click_bracket2)
        self.master.bind('/', self.click_divide)
        self.master.bind('.', self.click_point)
        self.master.bind('<BackSpace>', self.click_backspace)
        self.master.bind('^', self.click_power)


if __name__ == "__main__":
    if sys.stdout.isatty():
        application = tk.Tk()
        application.title("Window")
        Window(application)
        application.mainloop()
    else:
        print("Loaded OK")
