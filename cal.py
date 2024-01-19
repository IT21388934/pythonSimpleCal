from tkinter import Tk, Entry, Button, StringVar


class Calculator:
    def __init__ (self,master):
        master.title("Calculator")
        master.geometry('357x420+0+0')
        master.configure(background='black')
        master.resizable(width=False, height=False)

        self.equation = StringVar()
        self.entry_value = ""
        Entry(width=17,bg="white",font=("arial",28,"bold"),textvariable=self.equation).place(x=0,y=0)

        Button(width=10,height=3,bg="white",text="(",relief='flat' ,command=lambda:self.show("(")).place(x=0,y=50)
        Button(width=10,height=3,bg="white",text=")",relief='flat' ,command=lambda:self.show(")")).place(x=90,y=50)
        Button(width=10,height=3,bg="white",text="%",relief='flat' ,command=lambda:self.show("%")).place(x=180,y=50)
        Button(width=10,height=3,bg="white",text="1",relief='flat' ,command=lambda:self.show(1)).place(x=0 , y=125)
        Button(width=10,height=3,bg="white",text="2",relief='flat' ,command=lambda:self.show(2)).place(x=90,y=125)
        Button(width=10,height=3,bg="white",text="3",relief='flat' ,command=lambda:self.show(3)).place(x=180,y=125)
        Button(width=10,height=3,bg="white",text="4",relief='flat' ,command=lambda:self.show(4)).place(x=0,y=200)
        Button(width=10,height=3,bg="white",text="5",relief='flat' ,command=lambda:self.show(5)).place(x=90,y=200)
        Button(width=10,height=3,bg="white",text="6",relief='flat' ,command=lambda:self.show(6)).place(x=180,y=200)
        Button(width=10,height=3,bg="white",text="7",relief='flat' ,command=lambda:self.show(7)).place(x=0,y=275)
        Button(width=10,height=3,bg="white",text="8",relief='flat' ,command=lambda:self.show(8)).place(x=90,y=275)
        Button(width=10,height=3,bg="white",text="9",relief='flat' ,command=lambda:self.show(9)).place(x=180,y=275)
        Button(width=10,height=3,bg="white",text="0",relief='flat' ,command=lambda:self.show(0)).place(x=90,y=350)
        Button(width=10,height=3,bg="white",text=".",relief='flat' ,command=lambda:self.show(".")).place(x=180,y=350)
        Button(width=10,height=3,bg="white",text="+",relief='flat' ,command=lambda:self.show("+")).place(x=270,y=275)
        Button(width=10,height=3,bg="white",text="-",relief='flat' ,command=lambda:self.show("-")).place(x=270,y=200)
        Button(width=10,height=3,bg="white",text="/",relief='flat' ,command=lambda:self.show("/")).place(x=270,y=50)
        Button(width=10,height=3,bg="white",text="*",relief='flat' ,command=lambda:self.show("*")).place(x=270,y=125)
        Button(width=10,height=3,bg="lightblue",text="=",relief='flat' ,command=self.solve).place(x=270,y=350)
        Button(width=10,height=3,bg="white",text="c",relief='flat' ,command=self.clear).place(x=0,y=350)




    def show(self,value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)


    def clear(self):
        self.entry_value = ""
        self.equation.set(self.entry_value)

    def solve(self):
        result = eval(self.entry_value)
        self.equation.set(result)


root = Tk()

cal = Calculator(root)
root.mainloop()
