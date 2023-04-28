# Imports
import tkinter
import customtkinter as ctk
from PIL import Image, ImageTk


class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x500")
        self.title("PyCalc_UI")

        # Textbox
        self.textbox = ctk.CTkTextbox(master=self, width=600, height=100, corner_radius=0, font=("Comic Sans MS", 32))
        self.textbox.grid(row=0, column=0, sticky="nsew")

        # Button images
        self.image_1 = ctk.CTkImage(Image.open('resourses/button_1.png'), size=(30, 30))
        self.image_2 = ctk.CTkImage(Image.open('resourses/button_2.png'), size=(30, 30))
        self.image_3 = ctk.CTkImage(Image.open('resourses/button_3.png'), size=(30, 30))
        self.image_4 = ctk.CTkImage(Image.open('resourses/button_4.png'), size=(30, 30))
        self.image_5 = ctk.CTkImage(Image.open('resourses/button_5.png'), size=(30, 30))
        self.image_6 = ctk.CTkImage(Image.open('resourses/button_6.png'), size=(30, 30))
        self.image_7 = ctk.CTkImage(Image.open('resourses/button_7.png'), size=(30, 30))
        self.image_8 = ctk.CTkImage(Image.open('resourses/button_8.png'), size=(30, 30))
        self.image_9 = ctk.CTkImage(Image.open('resourses/button_9.png'), size=(30, 30))
        self.image_0 = ctk.CTkImage(Image.open('resourses/button_0.png'), size=(30, 30))
        self.image_Plus = ctk.CTkImage(Image.open('resourses/button_Plus.png'), size=(30, 30))
        self.image_Plus_pressed = ctk.CTkImage(Image.open('resourses/button_Plus_pressed.png'), size=(30, 30))
        self.image_Minus = ctk.CTkImage(Image.open('resourses/button_Minus.png'), size=(30, 30))
        self.image_Minus_pressed = ctk.CTkImage(Image.open('resourses/button_Minus_pressed.png'), size=(30, 30))
        self.image_Div = ctk.CTkImage(Image.open('resourses/button_Div.png'), size=(30, 30))
        self.image_Div_pressed = ctk.CTkImage(Image.open('resourses/button_Div_pressed.png'), size=(30, 30))
        self.image_Mult = ctk.CTkImage(Image.open('resourses/button_Mult.png'), size=(30, 30))
        self.image_Mult_pressed = ctk.CTkImage(Image.open('resourses/button_Mult_pressed.png'), size=(30, 30))
        self.image_Point = ctk.CTkImage(Image.open('resourses/button_Point.png'), size=(30, 30))
        self.image_Backspace = ctk.CTkImage(Image.open('resourses/button_Backspace.png'), size=(30, 30))
        self.image_Equal = ctk.CTkImage(Image.open('resourses/button_Equal.png'), size=(30, 30))
        self.image_C = ctk.CTkImage(Image.open('resourses/button_C.png'), size=(30, 30))
        self.image_AC = ctk.CTkImage(Image.open('resourses/button_AC.png'), size=(35, 35))

        # Buttons set and place
        self.button1 = ctk.CTkButton(self,
                                     width=100,
                                     height=50,
                                     border_width=0,
                                     corner_radius=8,
                                     fg_color="#87A3DB",
                                     text="",
                                     image=self.image_1,
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
                                     text="",
                                     image=self.image_2,
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
                                     text="",
                                     image=self.image_3,
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
                                     text="",
                                     image=self.image_4,
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
                                     text="",
                                     image=self.image_5,
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
                                     text="",
                                     image=self.image_6,
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
                                     text="",
                                     image=self.image_7,
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
                                     text="",
                                     image=self.image_8,
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
                                     text="",
                                     image=self.image_9,
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
                                     text="",
                                     image=self.image_0,
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
                                        text="",
                                        image=self.image_Plus,
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
                                         text="",
                                         image=self.image_Minus,
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
                                       text="",
                                       image=self.image_Div,
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
                                        text="",
                                        image=self.image_Mult,
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
                                         text="",
                                         image=self.image_Equal,
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
                                         text="",
                                         image=self.image_Point,
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
                                     text="",
                                     image=self.image_C,
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
                                      text="",
                                      image=self.image_AC,
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
                                             text="",
                                             image=self.image_Backspace,
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
        global answer
        if number1 == "":
            self.textbox.delete("0.0", "end")
            self.textbox.insert("end", "0.")
            number1 = self.textbox.get("0.0", "end")
        else:
            self.textbox.insert("end", ".")

    def button_plus_click(self):
        global number1
        global command
        global pressed_button
        global pressed_button_image
        if pressed_button == "":
            number1 = self.textbox.get("0.0", "end")
            pressed_button = self.buttonPlus
            pressed_button.configure(image=self.image_Plus_pressed,
                                     fg_color="#aabbdc",
                                     border_width=2,
                                     border_color="#87A3DB")
            pressed_button_image = self.image_Plus
            self.textbox.delete("0.0", "end")
        else:
            pressed_button.configure(image=pressed_button_image,
                                     fg_color="#87A3DB",
                                     border_width=0)
            pressed_button = self.buttonPlus
            pressed_button.configure(image=self.image_Plus_pressed,
                                     fg_color="#aabbdc",
                                     border_width=2,
                                     border_color="#87A3DB")
            pressed_button_image = self.image_Plus
            self.textbox.delete("0.0", "end")

    def button_minus_click(self):
        global number1
        global command
        global pressed_button
        global pressed_button_image
        if pressed_button == "":
            number1 = self.textbox.get("0.0", "end")
            pressed_button = self.buttonMinus
            pressed_button.configure(image=self.image_Minus_pressed,
                                     fg_color="#aabbdc",
                                     border_width=2,
                                     border_color="#87A3DB")
            pressed_button_image = self.image_Minus
            self.textbox.delete("0.0", "end")
        else:
            pressed_button.configure(image=pressed_button_image,
                                     fg_color="#87A3DB",
                                     border_width=0)
            pressed_button = self.buttonMinus
            pressed_button.configure(image=self.image_Minus_pressed,
                                     fg_color="#aabbdc",
                                     border_width=2,
                                     border_color="#87A3DB")
            pressed_button_image = self.image_Minus
            self.textbox.delete("0.0", "end")

    def button_div_click(self):
        global number1
        global command
        global pressed_button
        global pressed_button_image
        if pressed_button == "":
            number1 = self.textbox.get("0.0", "end")
            pressed_button = self.buttonDiv
            pressed_button.configure(image=self.image_Div_pressed,
                                     fg_color="#aabbdc",
                                     border_width=2,
                                     border_color="#87A3DB")
            pressed_button_image = self.image_Div
            self.textbox.delete("0.0", "end")
        else:
            pressed_button.configure(image=pressed_button_image,
                                     fg_color="#87A3DB",
                                     border_width=0)
            pressed_button = self.buttonDiv
            pressed_button.configure(image=self.image_Div_pressed,
                                     fg_color="#aabbdc",
                                     border_width=2,
                                     border_color="#87A3DB")
            pressed_button_image = self.image_Div
            self.textbox.delete("0.0", "end")

    def button_mult_click(self):
        global number1
        global command
        global pressed_button
        global pressed_button_image
        if pressed_button == "":
            number1 = self.textbox.get("0.0", "end")
            pressed_button = self.buttonMult
            pressed_button.configure(image=self.image_Mult_pressed,
                                     fg_color="#aabbdc",
                                     border_width=2,
                                     border_color="#87A3DB")
            pressed_button_image = self.image_Mult
            self.textbox.delete("0.0", "end")
        else:
            pressed_button.configure(image=pressed_button_image,
                                     fg_color="#87A3DB",
                                     border_width=0)
            pressed_button = self.buttonMult
            pressed_button.configure(image=self.image_Mult_pressed,
                                     fg_color="#aabbdc",
                                     border_width=2,
                                     border_color="#87A3DB")
            pressed_button_image = self.image_Mult
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
            pressed_button.configure(image=pressed_button_image,
                                     fg_color="#87A3DB",
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

    def cleaning_dbz(self):
        global number1
        global number2
        global pressed_button
        global recent_number2
        global recent_command
        number1 = ""
        number2 = ""
        pressed_button = ""
        recent_command = ""
        recent_number2 = ""

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
number1 = str()
number2 = str()
command = str()
recent_command = str()
recent_number2 = str()
pressed_button = str()
pressed_button_image = str()
app = MainWindow()
app.cleaning_hard()
app.mainloop()
