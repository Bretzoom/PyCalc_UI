# Imports
import tkinter
import customtkinter as ctk
import re


class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x500")
        self.title("PyCalc_UI")

        # Textbox
        self.textbox = ctk.CTkTextbox(master=self, width=600, height=100, corner_radius=0, font=("Comic Sans MS", 32),
                                      state="disabled")
        self.textbox.grid(row=0, column=0, sticky="nsew")

        # Buttons appearance

        # Buttons set and place
        self.button1 = ctk.CTkButton(self,
                                     width=100,
                                     height=50,
                                     border_width=0,
                                     corner_radius=8,
                                     fg_color="#87A3DB",
                                     text="1",
                                     text_color="white",
                                     anchor="E",
                                     font=("Comic Sans MS", 32),
                                     command=self.button1_click)
        self.button1.place(relx=0.1,
                           rely=0.7,
                           anchor=tkinter.N)
        self.button2 = ctk.CTkButton(self,
                                     width=100,
                                     height=50,
                                     border_width=0,
                                     corner_radius=8,
                                     fg_color="#87A3DB",
                                     text="2",
                                     text_color="white",
                                     anchor="E",
                                     font=("Comic Sans MS", 32),
                                     command=self.button2_click)
        self.button2.place(relx=0.3,
                           rely=0.7,
                           anchor=tkinter.N)
        self.button3 = ctk.CTkButton(self,
                                     width=100,
                                     height=50,
                                     border_width=0,
                                     corner_radius=8,
                                     fg_color="#87A3DB",
                                     text="3",
                                     text_color="white",
                                     anchor="E",
                                     font=("Comic Sans MS", 32),
                                     command=self.button3_click)
        self.button3.place(relx=0.5,
                           rely=0.7,
                           anchor=tkinter.N)
        self.button4 = ctk.CTkButton(self,
                                     width=100,
                                     height=50,
                                     border_width=0,
                                     corner_radius=8,
                                     fg_color="#87A3DB",
                                     text="4",
                                     text_color="white",
                                     anchor="E",
                                     font=("Comic Sans MS", 32),
                                     command=self.button4_click)
        self.button4.place(relx=0.1,
                           rely=0.55,
                           anchor=tkinter.N)
        self.button5 = ctk.CTkButton(self,
                                     width=100,
                                     height=50,
                                     border_width=0,
                                     corner_radius=8,
                                     fg_color="#87A3DB",
                                     text="5",
                                     text_color="white",
                                     anchor="E",
                                     font=("Comic Sans MS", 32),
                                     command=self.button5_click)
        self.button5.place(relx=0.3,
                           rely=0.55,
                           anchor=tkinter.N)
        self.button6 = ctk.CTkButton(self,
                                     width=100,
                                     height=50,
                                     border_width=0,
                                     corner_radius=8,
                                     fg_color="#87A3DB",
                                     text="6",
                                     text_color="white",
                                     anchor="E",
                                     font=("Comic Sans MS", 32),
                                     command=self.button6_click)
        self.button6.place(relx=0.5,
                           rely=0.55,
                           anchor=tkinter.N)
        self.button7 = ctk.CTkButton(self,
                                     width=100,
                                     height=50,
                                     border_width=0,
                                     corner_radius=8,
                                     fg_color="#87A3DB",
                                     text="7",
                                     text_color="white",
                                     anchor="E",
                                     font=("Comic Sans MS", 32),
                                     command=self.button7_click)
        self.button7.place(relx=0.1,
                           rely=0.4,
                           anchor=tkinter.N)
        self.button8 = ctk.CTkButton(self,
                                     width=100,
                                     height=50,
                                     border_width=0,
                                     corner_radius=8,
                                     fg_color="#87A3DB",
                                     text="8",
                                     text_color="white",
                                     anchor="E",
                                     font=("Comic Sans MS", 32),
                                     command=self.button8_click)
        self.button8.place(relx=0.3,
                           rely=0.4,
                           anchor=tkinter.N)
        self.button9 = ctk.CTkButton(self,
                                     width=100,
                                     height=50,
                                     border_width=0,
                                     corner_radius=8,
                                     fg_color="#87A3DB",
                                     text="9",
                                     text_color="white",
                                     anchor="E",
                                     font=("Comic Sans MS", 32),
                                     command=self.button9_click)
        self.button9.place(relx=0.5,
                           rely=0.4,
                           anchor=tkinter.N)
        self.button0 = ctk.CTkButton(self,
                                     width=220,
                                     height=50,
                                     border_width=0,
                                     corner_radius=8,
                                     fg_color="#87A3DB",
                                     text="0",
                                     text_color="white",
                                     anchor="E",
                                     font=("Comic Sans MS", 32),
                                     command=self.button0_click)
        self.button0.place(relx=0.2,
                           rely=0.9,
                           anchor=tkinter.CENTER)
        self.buttonPlus = ctk.CTkButton(self,
                                        width=100,
                                        height=50,
                                        border_width=0,
                                        corner_radius=8,
                                        fg_color="#87A3DB",
                                        text="+",
                                        text_color="white",
                                        anchor="E",
                                        font=("Comic Sans MS", 32),
                                        command=self.button_plus_click)
        self.buttonPlus.place(relx=0.7,
                              rely=0.7,
                              anchor=tkinter.N)
        self.buttonMinus = ctk.CTkButton(self,
                                         width=100,
                                         height=50,
                                         border_width=0,
                                         corner_radius=8,
                                         fg_color="#87A3DB",
                                         text="-",
                                         text_color="white",
                                         anchor="E",
                                         font=("Comic Sans MS", 32),
                                         command=self.button_minus_click)
        self.buttonMinus.place(relx=0.7,
                               rely=0.55,
                               anchor=tkinter.N)
        self.buttonDiv = ctk.CTkButton(self,
                                       width=100,
                                       height=50,
                                       border_width=0,
                                       corner_radius=8,
                                       fg_color="#87A3DB",
                                       text="÷",
                                       text_color="white",
                                       anchor="E",
                                       font=("Comic Sans MS", 32),
                                       command=self.button_div_click)
        self.buttonDiv.place(relx=0.7,
                             rely=0.25,
                             anchor=tkinter.N)
        self.buttonMult = ctk.CTkButton(self,
                                        width=100,
                                        height=50,
                                        border_width=0,
                                        corner_radius=8,
                                        fg_color="#87A3DB",
                                        text="×",
                                        text_color="white",
                                        anchor="E",
                                        font=("Comic Sans MS", 32),
                                        command=self.button_mult_click)
        self.buttonMult.place(relx=0.7,
                              rely=0.4,
                              anchor=tkinter.N)
        self.buttonEqual = ctk.CTkButton(self,
                                         width=100,
                                         height=50,
                                         border_width=0,
                                         corner_radius=8,
                                         fg_color="#87A3DB",
                                         text="=",
                                         text_color="white",
                                         anchor="E",
                                         font=("Comic Sans MS", 32),
                                         command=self.button_equal_click)
        self.buttonEqual.place(relx=0.7,
                               rely=0.9,
                               anchor=tkinter.CENTER)
        self.buttonPoint = ctk.CTkButton(self,
                                         width=100,
                                         height=50,
                                         border_width=0,
                                         corner_radius=8,
                                         fg_color="#87A3DB",
                                         text=".",
                                         text_color="white",
                                         anchor="E",
                                         font=("Comic Sans MS", 32),
                                         command=self.button_point_click)
        self.buttonPoint.place(relx=0.5,
                               rely=0.9,
                               anchor=tkinter.CENTER)
        self.buttonC = ctk.CTkButton(self,
                                     width=100,
                                     height=50,
                                     border_width=0,
                                     corner_radius=8,
                                     fg_color="#87A3DB",
                                     text="C",
                                     text_color="white",
                                     anchor="E",
                                     font=("Comic Sans MS", 32),
                                     command=self.cleaning_soft)
        self.buttonC.place(relx=0.3,
                           rely=0.25,
                           anchor=tkinter.N)
        self.buttonAC = ctk.CTkButton(self,
                                      width=100,
                                      height=50,
                                      border_width=0,
                                      corner_radius=8,
                                      fg_color="#87A3DB",
                                      text="AC",
                                      text_color="white",
                                      anchor="E",
                                      font=("Comic Sans MS", 32),
                                      command=self.cleaning_hard)
        self.buttonAC.place(relx=0.1,
                            rely=0.25,
                            anchor=tkinter.N)
        self.buttonBackspace = ctk.CTkButton(self,
                                             width=100,
                                             height=50,
                                             border_width=0,
                                             corner_radius=8,
                                             fg_color="#87A3DB",
                                             text="←",
                                             text_color="white",
                                             anchor="N",
                                             font=("Comic Sans MS", 32),
                                             command=self.cleaning_backspace)
        self.buttonBackspace.place(relx=0.5,
                                   rely=0.25,
                                   anchor=tkinter.N)
        self.buttonChange = ctk.CTkButton(self,
                                          width=100,
                                          height=50,
                                          border_width=0,
                                          corner_radius=8,
                                          fg_color="#87A3DB",
                                          text="±",
                                          text_color="white",
                                          anchor="N",
                                          font=("Comic Sans MS", 32),
                                          command=self.button_change_click)
        self.buttonChange.place(relx=0.9,
                                rely=0.25,
                                anchor=tkinter.N)

        # Buttons functions

    def button1_click(self):
        global number1
        self.textbox.configure(state="normal")
        if number1 == "":
            self.textbox.delete("0.0", "end")
            self.textbox.insert("end", "1")
            number1 = self.textbox.get("0.0", "end")
        else:
            self.textbox.insert("end", "1")
        self.textbox.configure(state="disabled")

    def button2_click(self):
        global number1
        self.textbox.configure(state="normal")
        if number1 == "":
            self.textbox.delete("0.0", "end")
            self.textbox.insert("end", "2")
            number1 = self.textbox.get("0.0", "end")
        else:
            self.textbox.insert("end", "2")
        self.textbox.configure(state="disabled")

    def button3_click(self):
        global number1
        self.textbox.configure(state="normal")
        if number1 == "":
            self.textbox.delete("0.0", "end")
            self.textbox.insert("end", "3")
            number1 = self.textbox.get("0.0", "end")
        else:
            self.textbox.insert("end", "3")
        self.textbox.configure(state="disabled")

    def button4_click(self):
        global number1
        self.textbox.configure(state="normal")
        if number1 == "":
            self.textbox.delete("0.0", "end")
            self.textbox.insert("end", "4")
            number1 = self.textbox.get("0.0", "end")
        else:
            self.textbox.insert("end", "4")
        self.textbox.configure(state="disabled")

    def button5_click(self):
        global number1
        self.textbox.configure(state="normal")
        if number1 == "":
            self.textbox.delete("0.0", "end")
            self.textbox.insert("end", "5")
            number1 = self.textbox.get("0.0", "end")
        else:
            self.textbox.insert("end", "5")
        self.textbox.configure(state="disabled")

    def button6_click(self):
        global number1
        self.textbox.configure(state="normal")
        if number1 == "":
            self.textbox.delete("0.0", "end")
            self.textbox.insert("end", "6")
            number1 = self.textbox.get("0.0", "end")
        else:
            self.textbox.insert("end", "6")
        self.textbox.configure(state="disabled")

    def button7_click(self):
        global number1
        self.textbox.configure(state="normal")
        if number1 == "":
            self.textbox.delete("0.0", "end")
            self.textbox.insert("end", "7")
            number1 = self.textbox.get("0.0", "end")
        else:
            self.textbox.insert("end", "7")
        self.textbox.configure(state="disabled")

    def button8_click(self):
        global number1
        self.textbox.configure(state="normal")
        if number1 == "":
            self.textbox.delete("0.0", "end")
            self.textbox.insert("end", "8")
            number1 = self.textbox.get("0.0", "end")
        else:
            self.textbox.insert("end", "8")
        self.textbox.configure(state="disabled")

    def button9_click(self):
        global number1
        self.textbox.configure(state="normal")
        if number1 == "":
            self.textbox.delete("0.0", "end")
            self.textbox.insert("end", "9")
            number1 = self.textbox.get("0.0", "end")
        else:
            self.textbox.insert("end", "9")
        self.textbox.configure(state="disabled")

    def button0_click(self):
        global number1
        self.textbox.configure(state="normal")
        if number1 == "":
            self.textbox.delete("0.0", "end")
            self.textbox.insert("end", "0")
            number1 = self.textbox.get("0.0", "end")
        else:
            self.textbox.insert("end", "0")
        self.textbox.configure(state="disabled")

    def button_point_click(self):
        global number1
        global answer
        self.textbox.configure(state="normal")
        if number1 == "":
            self.textbox.delete("0.0", "end")
            self.textbox.insert("end", "0.")
            number1 = self.textbox.get("0.0", "end")
        else:
            self.textbox.insert("end", ".")
        self.textbox.configure(state="disabled")

    def button_plus_click(self):
        global number1
        global command
        global pressed_button
        self.textbox.configure(state="normal")
        if pressed_button == "":
            number1 = self.textbox.get("0.0", "end")
            pressed_button = self.buttonPlus
            pressed_button.configure(fg_color="#aabbdc",
                                     border_width=2,
                                     border_color="#87A3DB")
            self.textbox.delete("0.0", "end")
        else:
            pressed_button.configure(fg_color="#87A3DB",
                                     border_width=0)
            pressed_button = self.buttonPlus
            pressed_button.configure(fg_color="#aabbdc",
                                     border_width=2,
                                     border_color="#87A3DB")
            self.textbox.delete("0.0", "end")
        self.textbox.configure(state="disabled")

    def button_minus_click(self):
        global number1
        global command
        global pressed_button
        self.textbox.configure(state="normal")
        if pressed_button == "":
            number1 = self.textbox.get("0.0", "end")
            pressed_button = self.buttonMinus
            pressed_button.configure(fg_color="#aabbdc",
                                     border_width=2,
                                     border_color="#87A3DB")
            self.textbox.delete("0.0", "end")
        else:
            pressed_button.configure(fg_color="#87A3DB",
                                     border_width=0)
            pressed_button = self.buttonMinus
            pressed_button.configure(fg_color="#aabbdc",
                                     border_width=2,
                                     border_color="#87A3DB")
            self.textbox.delete("0.0", "end")
        self.textbox.configure(state="disabled")

    def button_div_click(self):
        global number1
        global command
        global pressed_button
        self.textbox.configure(state="normal")
        if pressed_button == "":
            number1 = self.textbox.get("0.0", "end")
            pressed_button = self.buttonDiv
            pressed_button.configure(fg_color="#aabbdc",
                                     border_width=2,
                                     border_color="#87A3DB")
            self.textbox.delete("0.0", "end")
        else:
            pressed_button.configure(fg_color="#87A3DB",
                                     border_width=0)
            pressed_button = self.buttonDiv
            pressed_button.configure(fg_color="#aabbdc",
                                     border_width=2,
                                     border_color="#87A3DB")
            self.textbox.delete("0.0", "end")
        self.textbox.configure(state="disabled")

    def button_mult_click(self):
        global number1
        global command
        global pressed_button
        self.textbox.configure(state="normal")
        if pressed_button == "":
            number1 = self.textbox.get("0.0", "end")
            pressed_button = self.buttonMult
            pressed_button.configure(fg_color="#aabbdc",
                                     border_width=2,
                                     border_color="#87A3DB")
            self.textbox.delete("0.0", "end")
        else:
            pressed_button.configure(fg_color="#87A3DB",
                                     border_width=0)
            pressed_button = self.buttonMult
            pressed_button.configure(fg_color="#aabbdc",
                                     border_width=2,
                                     border_color="#87A3DB")
            self.textbox.delete("0.0", "end")
        self.textbox.configure(state="disabled")

    def button_change_click(self):
        self.textbox.configure(state="normal")
        if re.search("-", self.textbox.get("0.0", "end")) is not None:
            self.textbox.delete("0.0", "1.1")
        else:
            self.textbox.insert("0.0", "-")
        self.textbox.configure(state="disabled")

    def button_equal_click(self):
        global number1
        global number2
        global command
        global recent_command
        global recent_number2
        global answer
        global pressed_button
        self.textbox.configure(state="normal")
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
            pressed_button.configure(fg_color="#87A3DB",
                                     border_width=0)
            number2 = self.textbox.get("0.0", "end")
            if number2 != r"\s{*}":
                number1 = float(number1)
                number2 = float(number2)
                if pressed_button == self.buttonPlus:
                    answer = float(number1) + float(number2)
                elif pressed_button == self.buttonMinus:
                    answer = float(number1) - float(number2)
                elif pressed_button == self.buttonDiv:
                    if number2 != 0:
                        answer = float(number1) / float(number2)
                elif pressed_button == self.buttonMult:
                    answer = float(number1) * float(number2)
                self.textbox.delete("0.0", "end")
                if number2 == 0 and pressed_button == self.buttonDiv:
                    self.textbox.insert("end", "Division by zero")
                    self.cleaning_dbz()
                else:
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
        self.textbox.configure(state="disabled")

    def cleaning_dbz(self):
        global number1
        global number2
        global pressed_button
        global recent_number2
        global recent_command
        self.textbox.configure(state="normal")
        number1 = ""
        number2 = ""
        pressed_button = ""
        recent_command = ""
        recent_number2 = ""
        self.textbox.configure(state="disabled")

    def cleaning_hard(self):
        global number1
        global number2
        global pressed_button
        global recent_number2
        global recent_command
        self.textbox.configure(state="normal")
        self.textbox.delete("0.0", "end")
        number1 = ""
        number2 = ""
        pressed_button = ""
        recent_command = ""
        recent_number2 = ""
        self.textbox.configure(state="disabled")

    def cleaning_soft(self):
        self.textbox.configure(state="normal")
        self.textbox.delete("0.0", "end")
        self.textbox.configure(state="disabled")

    def cleaning_backspace(self):
        self.textbox.configure(state="normal")
        index = len(self.textbox.get("0.0", "end"))
        self.textbox.delete(f"1.{str(index - 2)}")
        self.textbox.configure(state="disabled")

    def first_zero(self):
        self.textbox.configure(state="normal")
        self.textbox.insert("0.0", "0")
        self.textbox.configure(state="disabled")


answer = float()
number1 = str()
number2 = str()
command = str()
recent_command = str()
recent_number2 = str()
pressed_button = str()
app = MainWindow()
app.cleaning_hard()
app.first_zero()
app.mainloop()
