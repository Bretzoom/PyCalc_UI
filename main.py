# Imports
import tkinter
import customtkinter


class MainWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x500")
        self.title("PyCalc_UI")

        # Textbox
        self.textbox = customtkinter.CTkTextbox(master=self, width=600, height=100, corner_radius=0)
        self.textbox.grid(row=0, column=0, sticky="nsew")

        # Buttons set and place
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
        self.buttonPoint = customtkinter.CTkButton(self,
                                                   width=100,
                                                   height=50,
                                                   border_width=0,
                                                   corner_radius=8,
                                                   text=".",
                                                   command=self.button_point_click)
        self.buttonPoint.place(relx=0.5,
                               rely=0.9,
                               anchor=tkinter.CENTER)
        self.buttonC = customtkinter.CTkButton(self,
                                               width=100,
                                               height=50,
                                               border_width=0,
                                               corner_radius=8,
                                               text="C",
                                               command=self.cleaning_soft)
        self.buttonC.place(relx=0.3,
                           rely=0.25,
                           anchor=tkinter.N)
        self.buttonAC = customtkinter.CTkButton(self,
                                                width=100,
                                                height=50,
                                                border_width=0,
                                                corner_radius=8,
                                                text="AC",
                                                command=self.cleaning_hard)
        self.buttonAC.place(relx=0.1,
                            rely=0.25,
                            anchor=tkinter.N)
        self.buttonBackspace = customtkinter.CTkButton(self,
                                                       width=100,
                                                       height=50,
                                                       border_width=0,
                                                       corner_radius=8,
                                                       text="Backspace",
                                                       command=self.cleaning_backspace)
        self.buttonBackspace.place(relx=0.5,
                                   rely=0.25,
                                   anchor=tkinter.N)

        # Buttons functions

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
        global pressed_button
        if pressed_button == "":
            number1 = self.textbox.get("0.0", "end")
            pressed_button = self.buttonPlus
            pressed_button.configure(text_color="red")
            self.textbox.delete("0.0", "end")
        else:
            pressed_button.configure(text_color="white")
            pressed_button = self.buttonPlus
            pressed_button.configure(text_color="red")
            self.textbox.delete("0.0", "end")

    def button_minus_click(self):
        global number1
        global command
        global pressed_button
        if pressed_button == "":
            number1 = self.textbox.get("0.0", "end")
            pressed_button = self.buttonMinus
            pressed_button.configure(text_color="red")
            self.textbox.delete("0.0", "end")
        else:
            pressed_button.configure(text_color="white")
            pressed_button = self.buttonMinus
            pressed_button.configure(text_color="red")
            self.textbox.delete("0.0", "end")

    def button_div_click(self):
        global number1
        global command
        global pressed_button
        if pressed_button == "":
            number1 = self.textbox.get("0.0", "end")
            pressed_button = self.buttonDiv
            pressed_button.configure(text_color="red")
            self.textbox.delete("0.0", "end")
        else:
            pressed_button.configure(text_color="white")
            pressed_button = self.buttonDiv
            pressed_button.configure(text_color="red")
            self.textbox.delete("0.0", "end")

    def button_mult_click(self):
        global number1
        global command
        global pressed_button
        if pressed_button == "":
            number1 = self.textbox.get("0.0", "end")
            pressed_button = self.buttonMult
            pressed_button.configure(text_color="red")
            self.textbox.delete("0.0", "end")
        else:
            pressed_button.configure(text_color="white")
            pressed_button = self.buttonMult
            pressed_button.configure(text_color="red")
            self.textbox.delete("0.0", "end")

    def button_equal_click(self):
        global number1
        global number2
        global command
        global recent_command
        global recent_number2
        global answer
        global pressed_button
        if pressed_button == "":
            if recent_command == "":
                answer = self.textbox.get("0.0", "end")
            elif recent_command == self.buttonPlus:
                answer = float(answer) + float(recent_number2)
            elif recent_command == self.buttonMinus:
                answer = float(answer) - float(recent_number2)
            elif recent_command == self.buttonDiv:
                answer = float(answer) / float(recent_number2)
            elif recent_command == self.buttonMult:
                answer = float(answer) * float(recent_number2)
            self.textbox.delete("0.0", "end")
            if float(answer) % 1 != 0:
                self.textbox.insert("end", float(answer))
            else:
                self.textbox.insert("end", int(answer))
        else:
            pressed_button.configure(text_color="white")
            number2 = self.textbox.get("0.0", "end")
            if number2 != r"\s{*}":
                number1 = float(number1)
                number2 = float(number2)
                if pressed_button == self.buttonPlus:
                    answer = float(number1) + float(number2)
                elif pressed_button == self.buttonMinus:
                    answer = float(number1) - float(number2)
                elif pressed_button == self.buttonDiv:
                    answer = float(number1) / float(number2)
                elif pressed_button == self.buttonMult:
                    answer = float(number1) * float(number2)
                self.textbox.delete("0.0", "end")
                if float(answer) % 1 != 0:
                    self.textbox.insert("end", float(answer))
                    recent_command = pressed_button
                    recent_number2 = number2
                    number1 = ""
                    number2 = ""
                    pressed_button = ""
                else:
                    self.textbox.insert("end", int(answer))
                    recent_command = pressed_button
                    recent_number2 = number2
                    number1 = ""
                    number2 = ""
                    pressed_button = ""
            else:
                if float(number1) % 1 != 0:
                    self.textbox.insert("end", float(number1))
                    recent_command = pressed_button
                    recent_number2 = number2
                    number1 = ""
                    number2 = ""
                    pressed_button = ""
                else:
                    self.textbox.insert("end", int(number1))
                    recent_command = pressed_button
                    recent_number2 = number2
                    number1 = ""
                    number2 = ""
                    pressed_button = ""

    def cleaning_hard(self):
        global number1
        global number2
        global pressed_button
        global recent_number2
        global recent_command
        self.textbox.delete("0.0", "end")
        number1 = ""
        number2 = ""
        pressed_button = ""
        recent_command = ""
        recent_number2 = ""

    def cleaning_soft(self):
        self.textbox.delete("0.0", "end")

    def cleaning_backspace(self):
        index = len(self.textbox.get("0.0", "end"))
        self.textbox.delete(f"1.{str(index - 2)}")


answer = float()
number1 = ""
number2 = ""
command = ""
recent_command = str()
recent_number2 = ""
button = "button click"
pressed_button = str()
app = MainWindow()
app.cleaning_hard()
app.mainloop()
