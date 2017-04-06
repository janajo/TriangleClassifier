#Jana Jones April 2017



import tkinter as tk


class Geometry(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)


        self.output_var = tk.StringVar()

        self.label1 = tk.Label(self, text="side a length").grid(row=0)
        self.label2 = tk.Label(self, text="side b length").grid(row=1)
        self.label3 = tk.Label(self, text="side c length").grid(row=2)
        self.label4 = tk.Label(self, textvariable=self.output_var, width=40).grid(row=3, column=1)

        vcmd = (self.register(self.onValidate), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        self.e1 = tk.Entry(self, validate="key", validatecommand=vcmd)
        self.e2 = tk.Entry(self, validate="key", validatecommand=vcmd)
        self.e3 = tk.Entry(self, validate="key", validatecommand=vcmd)

        self.e1.insert(0, '0')
        self.e2.insert(0, '0')
        self.e3.insert(0, '0')

        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        self.e3.grid(row=2, column=1)


        self.bind('<Return>', self.func)



    def func(self, event):


        e1Input = float(self.e1.get())
        e2Input = float(self.e2.get())
        e3Input = float(self.e3.get())



        self.mathStuff(e1Input, e2Input, e3Input)


    def mathStuff(self, e1Input, e2Input, e3Input):




        longSide, medSide, shortSide = self.length_assignment(e1Input, e2Input, e3Input)




        self.label4 = tk.Label(self, textvariable=self.output_var, width=40)
        self.label4.grid(row=3, column=1)


        validTri = self.check_for_valid_tri(longSide, medSide, shortSide)

        self.type_of_tri(longSide, medSide, shortSide, validTri)

    def length_assignment(self, e1Input, e2Input, e3Input):
        longSide = max(e1Input, e2Input, e3Input)
        shortSide = min(e1Input, e2Input, e3Input)
        if (longSide != e1Input and shortSide != e1Input):
            medSide = e1Input
        elif (longSide != e2Input and shortSide != e2Input):
            medSide = e2Input
        elif (longSide != e3Input and shortSide != e3Input):
            medSide = e3Input
        else:  # accounts for sides of equal length
            if (e1Input == e2Input):
                medSide = e1Input
            else:
                medSide = e3Input
        return longSide, medSide, shortSide

    def type_of_tri(self, longSide, medSide, shortSide, validTri):
        if (validTri == True):
            if (pow(shortSide, 2) + pow(medSide, 2) == pow(longSide, 2)):
                self.output_var.set('These sides produce a valid \n right triangle')
            elif (longSide == shortSide == medSide):
                self.output_var.set('These sides produce a valid \n equilateral triangle')
            elif (longSide == shortSide or longSide == medSide or medSide == shortSide):
                self.output_var.set('These sides produces a valid \n isosceles triangle')
            else:
                self.output_var.set('These sides produce a \n valid triangle')

    def check_for_valid_tri(self, longSide, medSide, shortSide):
        validTri = True
        if (shortSide + medSide <= longSide or shortSide == 0 or medSide == 0 or longSide == 0):
            self.output_var.set('This is not a valid triangle. \n Please try again')
            self.bell()
            validTri = False
        else:
            self.output_var.set(' ')


        return validTri

    def onValidate(self, action, index, value_if_allowed,
    prior_value, text, validation_type, trigger_type, widget_name):
        if (action == '1'):
            if text in '0123456789.': # if text == r'[0-9]+'
                try:
                    float(value_if_allowed)
                    return True
                except ValueError:
                    self.output_var.set('Sorry! You can only input numbers.')
                    self.bell()
                    return False
            else:
                self.output_var.set('Sorry! You can only input numbers.')
                self.bell()
                return False
        else:
            return True




















app = Geometry()

app.mainloop()




