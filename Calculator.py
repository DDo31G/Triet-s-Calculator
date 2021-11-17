import math
import tkinter
import tkinter.messagebox
class GUI:
    def __init__(self):
        #Create the main window
        self.main_window=tkinter.Tk()

        self.main_window.title("My Calculator")
        self.top_frame = tkinter.Frame(self.main_window)
        self.top_frame.pack()

        #making basic operation
        #First input
        self.prompt_label=tkinter.Label(self.top_frame,
                                       text="Enter the first number here:")
        self.prompt_label.pack()
        self.firstNum_entry=tkinter.Entry(self.top_frame,
                                       width=10)
        self.firstNum_entry.pack()

        

        #Second input
        self.prompt2_label=tkinter.Label(self.top_frame,
                                       text="Enter the second number here:")
        self.prompt2_label.pack()
        self.secondNum_entry=tkinter.Entry(self.top_frame,
                                       width=10)
        self.secondNum_entry.pack()

        #Adding operation
        self.Addbutton=tkinter.Button(self.top_frame,
                                    text="+",
                                    command=self.Add_Button)
        self.Addbutton.pack()

        

        #Subtraction operation
        self.Subbutton=tkinter.Button(self.top_frame,
                                    text="-",
                                    command=self.Sub_Button)
        self.Subbutton.pack()

        #Multiple operation
        self.Mulbutton=tkinter.Button(self.top_frame,
                                    text="x",
                                    command=self.Mul_Button)
        self.Mulbutton.pack()

        #Division operation
        self.Divibutton=tkinter.Button(self.top_frame,
                                    text=":",
                                    command=self.Divi_Button)
        self.Divibutton.pack()
        

        #Squrt operation
        self.Squrtbutton=tkinter.Button(self.top_frame,
                                    text="sqrt",
                                    command=self.Sqrt_Button)
        self.Squrtbutton.pack()

        #Factorial operation
        self.Factbutton=tkinter.Button(self.top_frame,
                                    text="factorial",
                                    command=self.Fact_Button)
        self.Factbutton.pack()

        #Sin operation
        self.Sinbutton=tkinter.Button(self.top_frame,
                                    text="sin",
                                    command=self.Sin_Button)
        self.Sinbutton.pack()

        #Cos operation
        self.Cosbutton=tkinter.Button(self.top_frame,
                                    text="cos",
                                    command=self.Cos_Button)
        self.Cosbutton.pack()
        #Tan operation
        self.Tanbutton=tkinter.Button(self.top_frame,
                                    text="tan",
                                    command=self.Tan_Button)
        self.Tanbutton.pack()

        #Mem operation
        self.Membutton=tkinter.Button(self.top_frame,
                                    text="mem",
                                    command=self.Mem_Button)
        #explanation
        self.prompt_label=tkinter.Label(self.top_frame,
                                       text="Enter the degree and it will convert to radian auto")
        self.prompt_label.pack()
        self.Membutton.pack()
        tkinter.mainloop()



    def Add_Button(self):
        Addition1=float(self.firstNum_entry.get())
        Addition2=float(self.secondNum_entry.get())
        Addresult=Addition1+Addition2
        self.mem=Addresult
        tkinter.messagebox.showinfo(message=str(Addresult))

    def Sub_Button(self):
        Subtraction1=float(self.firstNum_entry.get())
        Subtraction2=float(self.secondNum_entry.get())
        Subresult=Subtraction1-Subtraction2
        self.mem=Subresult
        tkinter.messagebox.showinfo(message=str(Subresult))

    def Mul_Button(self):
        Mul1=float(self.firstNum_entry.get())
        Mul2=float(self.secondNum_entry.get())
        Mulresult=Mul1*Mul2
        self.mem=Mulresult
        tkinter.messagebox.showinfo(message=str(Mulresult))

    def Divi_Button(self):
        Divi1=float(self.firstNum_entry.get())
        Divi2=float(self.secondNum_entry.get())
        Diviresult=Divi1/Divi2
        self.mem=Diviresult
        tkinter.messagebox.showinfo(message=str(Diviresult))

    def Sqrt_Button(self):
        Sqrt1=float(self.firstNum_entry.get())
        Sqrtresult=math.sqrt(Sqrt)
        self.mem=Sqrtresult
        tkinter.messagebox.showinfo(message=str(Sqrtresult))

    def Fact_Button(self):
        Fact1=float(self.firstNum_entry.get())
        Factresult=math.factorial(Sqrt)
        self.mem=Factresult
        tkinter.messagebox.showinfo(message=str(Factresult))

    def Sin_Button(self):
        #Remember to make explaining button
        Sin1=float(self.firstNum_entry.get())
        Sinresult=math.sin(math.radians(Sin1))
        self.mem=Sinresult
        tkinter.messagebox.showinfo(message=str(Sinresult))

    def Cos_Button(self):
        #Remember to make explaining button
        Cos1=float(self.firstNum_entry.get())
        Cosresult=math.cos(math.radians(Cos1))
        self.mem=Cosresult
        tkinter.messagebox.showinfo(message=str(Cosresult))

    def Tan_Button(self):
        #Remember to make explaining button
        Tan1=float(self.firstNum_entry.get())
        Tanresult=math.cos(math.radians(Tan1))
        self.mem=Tanresult
        tkinter.messagebox.showinfo(message=str(Tanresult))

    def Mem_Button(self):
        #Remember to make explaining button
        Memresult=self.mem
        tkinter.messagebox.showinfo(message=str(Memresult))
    

if __name__=="__main__":
    myGui=GUI()
