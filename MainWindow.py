import tkinter
from tkinter import filedialog
import Handler
import encoders
import Gate


class MainWindow:
    def __init__(self):
        # set window config
        self.first_col_width = 30
        self.second_col_width = 30
        self.window = tkinter.Tk()
        self.window.geometry('520x160')
        self.window.resizable(False, False)
        self.window.title('Encryptor 1.1')
        # set option menu
        self.encoder_var = tkinter.StringVar(self.window)
        self.encoder_var.trace('w', self.encoder_changed)
        self.encoder_var.set(list(encoders.encoders.keys())[0])
        self.encoder_menu = tkinter.OptionMenu(self.window, self.encoder_var, *encoders.encoders.keys())
        self.encoder_menu.config(width=self.second_col_width - 5)
        tkinter.Label(text='Choose encoder:', width=self.first_col_width).grid(row=0, column=0)
        self.encoder_menu.grid(row=0, column=1)
        # set input file button
        self.input_path_button = tkinter.Button(self.window, text='Choose input file path')
        self.input_path_button.config(width=self.first_col_width)
        self.input_path_button.bind("<Button-1>", self.choose_input_file_path)
        self.input_path_button.grid(row=1, column=0)
        # set input file entry
        self.input_path_entry = tkinter.Entry(self.window, width=self.second_col_width)
        self.input_path_entry.grid(row=1, column=1)
        # set output file button
        self.input_path_button = tkinter.Button(self.window, text='Choose output file path')
        self.input_path_button.config(width=self.first_col_width)
        self.input_path_button.bind("<Button-1>", self.choose_output_file_path)
        self.input_path_button.grid(row=2, column=0)
        # set output file entry
        self.output_path_entry = tkinter.Entry(self.window, width=self.second_col_width)
        self.output_path_entry.grid(row=2, column=1)
        # set key output file button
        self.key_path_button = tkinter.Button(self.window, text='Choose key file path')
        self.key_path_button.config(width=self.first_col_width)
        self.key_path_button.bind("<Button-1>", self.choose_key_file_path)
        self.key_path_button.grid(row=3, column=0)
        # set key output file entry
        self.key_path_entry = tkinter.Entry(self.window, width=self.second_col_width)
        self.key_path_entry.grid(row=3, column=1)
        # set decode button
        self.decode_button = tkinter.Button(self.window, text='Decode')
        self.decode_button.config(width=self.first_col_width)
        self.decode_button.bind("<Button-1>", self.decode_pressed)
        self.decode_button.grid(row=4, column=0)
        # set encode button
        self.encode_button = tkinter.Button(self.window, text='Encode')
        self.encode_button.config(width=self.first_col_width)
        self.encode_button.bind("<Button-1>", self.encode_pressed)
        self.encode_button.grid(row=4, column=1)
        # set Gate obj
        self.gate = Gate.Gate()
        self.handler = Handler.Handler(self.gate)

    def compose_message(self, mode):
        msg = Gate.Command(self.input_path_entry.get(), self.output_path_entry.get(),
                           self.encoder_var.get(), mode, self.key_path_entry.get())
        return msg

    def handle_message(self, msg):
        self.gate.__handle_command__(msg)
        self.handler.handle()

    def choose_input_file_path(self, event):
        filename = filedialog.askopenfilename()
        self.input_path_entry.insert(tkinter.END, filename)

    def choose_key_file_path(self, event):
        filename = filedialog.askopenfilename()
        self.key_path_entry.insert(tkinter.END, filename)

    def decode_pressed(self, event):
        msg = self.compose_message('decode')
        self.handle_message(msg)

    def encode_pressed(self, event):
        msg = self.compose_message('encode')
        self.handle_message(msg)

    def choose_output_file_path(self, event):
        filename = filedialog.askopenfilename()
        self.output_path_entry.insert(tkinter.END, filename)

    def encoder_changed(self, *args):
        print('changed')
        print(self.encoder_var.get())

    def start(self):
        self.window.mainloop()
