import tkinter

import customtkinter


class MainWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x500")
        self.title("PyCalc_UI")

        # add widgets to app
        self.textbox = customtkinter.CTkTextbox(master=self, width=600, height=100, corner_radius=0)
        self.textbox.grid(row=0, column=0, sticky="nsew")

        self.button1 = customtkinter.CTkButton(self,
                                               width=100,
                                               height=50,
                                               border_width=0,
                                               corner_radius=8,
                                               text="1",
                                               command=self.button1_click)
        self.button1.place(relx=0.1,
                           rely=0.7,
                           anchor=tkinter.N)
        self.button2 = customtkinter.CTkButton(self,
                                               width=100,
                                               height=50,
                                               border_width=0,
                                               corner_radius=8,
                                               text="2",
                                               command=self.button2_click)
        self.button2.place(relx=0.3,
                           rely=0.7,
                           anchor=tkinter.N)
        self.button3 = customtkinter.CTkButton(self,
                                               width=100,
                                               height=50,
                                               border_width=0,
                                               corner_radius=8,
                                               text="3",
                                               command=self.button3_click)
        self.button3.place(relx=0.5,
                           rely=0.7,
                           anchor=tkinter.N)
        self.button4 = customtkinter.CTkButton(self,
                                               width=100,
                                               height=50,
                                               border_width=0,
                                               corner_radius=8,
                                               text="4",
                                               command=self.button4_click)
        self.button4.place(relx=0.1,
                           rely=0.55,
                           anchor=tkinter.N)
        self.button5 = customtkinter.CTkButton(self,
                                               width=100,
                                               height=50,
                                               border_width=0,
                                               corner_radius=8,
                                               text="5",
                                               command=self.button5_click)
        self.button5.place(relx=0.3,
                           rely=0.55,
                           anchor=tkinter.N)
        self.button6 = customtkinter.CTkButton(self,
                                               width=100,
                                               height=50,
                                               border_width=0,
                                               corner_radius=8,
                                               text="6",
                                               command=self.button6_click)
        self.button6.place(relx=0.5,
                           rely=0.55,
                           anchor=tkinter.N)
        self.button7 = customtkinter.CTkButton(self,
                                               width=100,
                                               height=50,
                                               border_width=0,
                                               corner_radius=8,
                                               text="7",
                                               command=self.button7_click)
        self.button7.place(relx=0.1,
                           rely=0.4,
                           anchor=tkinter.N)
        self.button8 = customtkinter.CTkButton(self,
                                               width=100,
                                               height=50,
                                               border_width=0,
                                               corner_radius=8,
                                               text="8",
                                               command=self.button8_click)
        self.button8.place(relx=0.3,
                           rely=0.4,
                           anchor=tkinter.N)
        self.button9 = customtkinter.CTkButton(self,
                                               width=100,
                                               height=50,
                                               border_width=0,
                                               corner_radius=8,
                                               text="9",
                                               command=self.button9_click)
        self.button9.place(relx=0.5,
                           rely=0.4,
                           anchor=tkinter.N)
        self.button0 = customtkinter.CTkButton(self,
                                               width=220,
                                               height=50,
                                               border_width=0,
                                               corner_radius=8,
                                               text="0",
                                               command=self.button0_click)
        self.button0.place(relx=0.2,
                           rely=0.9,
                           anchor=tkinter.CENTER)
        self.buttonPlus = customtkinter.CTkButton(self,
                                                  width=100,
                                                  height=50,
                                                  border_width=0,
                                                  corner_radius=8,
                                                  text="+",
                                                  command=self.button_plus_click)
        self.buttonPlus.place(relx=0.7,
                              rely=0.7,
                              anchor=tkinter.N)
        self.buttonMinus = customtkinter.CTkButton(self,
                                                   width=100,
                                                   height=50,
                                                   border_width=0,
                                                   corner_radius=8,
                                                   text="-",
                                                   command=self.button_minus_click)
        self.buttonMinus.place(relx=0.7,
                               rely=0.55,
                               anchor=tkinter.N)
        self.buttonDiv = customtkinter.CTkButton(self,
                                                 width=100,
                                                 height=50,
                                                 border_width=0,
                                                 corner_radius=8,
                                                 text="/",
                                                 command=self.button_div_click)
        self.buttonDiv.place(relx=0.7,
                             rely=0.25,
                             anchor=tkinter.N)
        self.buttonMult = customtkinter.CTkButton(self,
                                                  width=100,
                                                  height=50,
                                                  border_width=0,
                                                  corner_radius=8,
                                                  text="X",
                                                  command=self.button_mult_click)
        self.buttonMult.place(relx=0.7,
                              rely=0.4,
                              anchor=tkinter.N)
        self.buttonEqual = customtkinter.CTkButton(self,
                                                   width=100,
                                                   height=50,
                                                   border_width=0,
                                                   corner_radius=8,
                                                   text="=",
                                                   command=self.button_equal_click)
        self.buttonEqual.place(relx=0.7,
                               rely=0.9,
                               anchor=tkinter.CENTER)
        self.buttonTochka = customtkinter.CTkButton(self,
                                                    width=100,
                                                    height=50,
                                                    border_width=0,
                                                    corner_radius=8,
                                                    text=".",
                                                    command=self.button_point_click)
        self.buttonTochka.place(relx=0.5,
                                rely=0.9,
                                anchor=tkinter.CENTER)

    # add methods to app
    def button1_click(self):
        global number1
        if number1 == "":
            self.textbox.delete("0.0", "end")
            self.textbox.insert("end", "1")
            number1 = self.textbox.get("0.0", "end")
        else:
            self.textbox.insert("end", "1")

    def button2_click(self):
        global number1
        if number1 == "":
            self.textbox.delete("0.0", "end")
            self.textbox.insert("end", "2")
            number1 = self.textbox.get("0.0", "end")
        else:
            self.textbox.insert("end", "2")

    def button3_click(self):
        global number1
        if number1 == "":
            self.textbox.delete("0.0", "end")
            self.textbox.insert("end", "3")
            number1 = self.textbox.get("0.0", "end")
        else:
            self.textbox.insert("end", "3")

    def button4_click(self):
        global number1
        if number1 == "":
            self.textbox.delete("0.0", "end")
            self.textbox.insert("end", "4")
            number1 = self.textbox.get("0.0", "end")
        else:
            self.textbox.insert("end", "4")

    def button5_click(self):
        global number1
        if number1 == "":
            self.textbox.delete("0.0", "end")
            self.textbox.insert("end", "5")
            number1 = self.textbox.get("0.0", "end")
        else:
            self.textbox.insert("end", "5")

    def button6_click(self):
        global number1
        if number1 == "":
            self.textbox.delete("0.0", "end")
            self.textbox.insert("end", "6")
            number1 = self.textbox.get("0.0", "end")
        else:
            self.textbox.insert("end", "6")

    def button7_click(self):
        global number1
        if number1 == "":
            self.textbox.delete("0.0", "end")
            self.textbox.insert("end", "7")
            number1 = self.textbox.get("0.0", "end")
        else:
            self.textbox.insert("end", "7")

    def button8_click(self):
        global number1
        if number1 == "":
            self.textbox.delete("0.0", "end")
            self.textbox.insert("end", "8")
            number1 = self.textbox.get("0.0", "end")
        else:
            self.textbox.insert("end", "8")

    def button9_click(self):
        global number1
        if number1 == "":
            self.textbox.delete("0.0", "end")
            self.textbox.insert("end", "9")
            number1 = self.textbox.get("0.0", "end")
        else:
            self.textbox.insert("end", "9")

    def button0_click(self):
        global number1
        if number1 == "":
            self.textbox.delete("0.0", "end")
            self.textbox.insert("end", "0")
            number1 = self.textbox.get("0.0", "end")
        else:
            self.textbox.insert("end", "0")

    def button_point_click(self):
        global number1
        if number1 == "":
            self.textbox.insert("end", "0.")
            number1 = self.textbox.get("0.0", "end")
        else:
            self.textbox.insert("end", ".")

    def button_plus_click(self):
        global number1
        global command
        number1 = self.textbox.get("0.0", "end")
        command = "+"
        self.textbox.delete("0.0", "end")

    def button_minus_click(self):
        global number1
        global command
        number1 = self.textbox.get("0.0", "end")
        command = "-"
        self.textbox.delete("0.0", "end")

    def button_div_click(self):
        global number1
        global command
        number1 = self.textbox.get("0.0", "end")
        command = "/"
        self.textbox.delete("0.0", "end")

    def button_mult_click(self):
        global number1
        global command
        number1 = self.textbox.get("0.0", "end")
        command = "*"
        self.textbox.delete("0.0", "end")

    def button_equal_click(self):
        global number1
        global number2
        global command
        global recent_command
        global recent_number2
        global answer
        if command == "":
            if recent_command == "":
                answer = self.textbox.get("0.0", "end")
            elif recent_command == "+":
                answer = float(answer) + float(recent_number2)
            elif recent_command == "-":
                answer = float(answer) - float(recent_number2)
            elif recent_command == "/":
                answer = float(answer) / float(recent_number2)
            elif recent_command == "*":
                answer = float(answer) * float(recent_number2)
            self.textbox.delete("0.0", "end")
            if float(answer) % 1 != 0:
                self.textbox.insert("end", float(answer))
            else:
                self.textbox.insert("end", int(answer))

        else:
            number2 = self.textbox.get("0.0", "end")
            if command == "+":
                answer = float(number1) + float(number2)
            elif command == "-":
                answer = float(number1) - float(number2)
            elif command == "/":
                answer = float(number1) / float(number2)
            elif command == "*":
                answer = float(number1) * float(number2)
            self.textbox.delete("0.0", "end")
            if float(answer) % 1 != 0:
                self.textbox.insert("end", float(answer))
                number1 = ""
                recent_command = command
                recent_number2 = number2
                command = ""
            else:
                self.textbox.insert("end", int(answer))
                number1 = ""
                recent_command = command
                recent_number2 = number2
                command = ""

    def launch_cleaning(self):
        global number1
        global number2
        global command
        self.textbox.delete("0.0", "end")


answer = float()
number1 = ""
number2 = ""
command = ""
recent_command = ""
recent_number2 = ""
button = "button click"
app = MainWindow()
app.launch_cleaning()
app.mainloop()
