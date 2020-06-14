import tkinter as tk
import serial
import serial.tools.list_ports


class form:
    def __init__(self, parent):
        self.parent = parent
        self.ser = serial.Serial()
        self.init_ui()
        self.init_commands()

    def init_ui(self):
        self.port_frame = tk.LabelFrame(self.parent, text='Port settings')
        self.port_frame.grid(row=1, column=1, padx=2, pady=2)

        self.port_label = tk.Label(self.port_frame, text='Port')
        self.port_label.grid(row=1, column=1)
        temp = ['None']
        if len(self.port_list()) != 0:
            temp.append(self.port_list())
        self.var_port = tk.StringVar(self.parent)
        self.var_port.set(temp[0])
        self.port_option = tk.OptionMenu(self.port_frame, self.var_port, *temp)
        self.port_option.grid(row=2, column=1)

        self.baud_label = tk.Label(self.port_frame, text='Baudrate')
        self.baud_label.grid(row=1, column=2)
        self.var_baud = tk.StringVar(self.parent)
        self.var_baud.set(self.baudrates[6])
        self.baud_option = tk.OptionMenu(self.port_frame, self.var_baud, *self.baudrates)
        self.baud_option.grid(row=2, column=2)

        self.databits_label = tk.Label(self.port_frame, text='Data bits')
        self.databits_label.grid(row=1, column=3)
        self.var_databits = tk.StringVar(self.parent)
        self.var_databits.set(self.bytesizes[3])
        self.databits_option = tk.OptionMenu(self.port_frame, self.var_databits, *self.bytesizes)
        self.databits_option.grid(row=2, column=3)

        self.parity_label = tk.Label(self.port_frame, text='Parity')
        self.parity_label.grid(row=1, column=4)
        self.var_parity = tk.StringVar(self.parent)
        self.var_parity.set(self.parities[0])
        self.parity_option = tk.OptionMenu(self.port_frame, self.var_parity, *self.parities)
        self.parity_option.grid(row=2, column=4)

        self.stop_label = tk.Label(self.port_frame, text='Stop bits')
        self.stop_label.grid(row=1, column=5)
        self.var_stop = tk.StringVar(self.parent)
        self.var_stop.set(self.stopbits[0])
        self.stop_option = tk.OptionMenu(self.port_frame, self.var_stop, *self.stopbits)
        self.stop_option.grid(row=2, column=5)

        self.timeout_label = tk.Label(self.port_frame, text='Timeout')
        self.timeout_label.grid(row=1, column=6)
        self.var_timeout = tk.BooleanVar(self.parent)
        self.var_timeout.set(1)
        self.timeout_none = tk.Label(self.port_frame, text='None')
        self.timeout_none.grid(row=2, column=6)
        self.timeout_check = tk.Checkbutton(self.port_frame, variable=self.var_timeout)
        self.timeout_check.grid(row=2, column=7)
        self.timeout_entry = tk.Entry(self.port_frame, width=6, bg='lightgrey')
        self.timeout_entry.grid(row=3, column=6)

        self.xonxoff_label = tk.Label(self.port_frame, text='xonxoff enable')
        self.xonxoff_label.grid(row=1, column=8)
        self.var_xonxoff = tk.BooleanVar(self.parent)
        self.var_xonxoff.set(0)
        self.xonxoff_check = tk.Checkbutton(self.port_frame, variable=self.var_xonxoff)
        self.xonxoff_check.grid(row=1, column=9)

        self.rtscts_label = tk.Label(self.port_frame, text='rtscts enable')
        self.rtscts_label.grid(row=2, column=8)
        self.var_rtscts = tk.BooleanVar(self.parent)
        self.var_rtscts.set(0)
        self.rtscts_check = tk.Checkbutton(self.port_frame, variable=self.var_rtscts)
        self.rtscts_check.grid(row=2, column=9)

        self.dsrdtr_label = tk.Label(self.port_frame, text='dsrdtr enable')
        self.dsrdtr_label.grid(row=3, column=8)
        self.var_dsrdtr = tk.BooleanVar(self.parent)
        self.var_dsrdtr.set(0)
        self.dsrdtr_check = tk.Checkbutton(self.port_frame, variable=self.var_dsrdtr)
        self.dsrdtr_check.grid(row=3, column=9)

        self.writetimeout_label = tk.Label(self.port_frame, text='Write \ntimeout')
        self.writetimeout_label.grid(row=1, column=10)
        self.var_writetimeout = tk.BooleanVar(self.parent)
        self.var_writetimeout.set(1)
        self.writetimeout_none = tk.Label(self.port_frame, text='None')
        self.writetimeout_none.grid(row=2, column=10)
        self.writetimeout_check = tk.Checkbutton(self.port_frame, variable=self.var_writetimeout)
        self.writetimeout_check.grid(row=2, column=11)
        self.writetimeout_entry = tk.Entry(self.port_frame, width=6, bg='lightgrey')
        self.writetimeout_entry.grid(row=3, column=10)

        self.interbytetimeout_label = tk.Label(self.port_frame, text='Write inter \n byte timeout')
        self.interbytetimeout_label.grid(row=1, column=12)
        self.var_interbytetimeout = tk.BooleanVar(self.parent)
        self.var_interbytetimeout.set(1)
        self.interbytetimeout_none = tk.Label(self.port_frame, text='None')
        self.interbytetimeout_none.grid(row=2, column=12)
        self.interbytetimeout_check = tk.Checkbutton(self.port_frame, variable=self.var_interbytetimeout)
        self.interbytetimeout_check.grid(row=2, column=13)
        self.interbytetimeout_entry = tk.Entry(self.port_frame, width=6, bg='lightgrey')
        self.interbytetimeout_entry.grid(row=3, column=12)

        self.connect_button = tk.Button(self.port_frame, text='Connect', width=15)
        self.connect_button.grid(row=1, column=14)
        self.disconnect_button = tk.Button(self.port_frame, text='Disconnect', width=15)
        self.disconnect_button.grid(row=2, column=14)
        self.connection_label = tk.Label(self.port_frame, text='Disconnected', fg='Red')
        self.connection_label.grid(row=4, column=14)

        self.command_frame = tk.LabelFrame(self.parent, text='Commands')
        self.command_frame.grid(row=4, column=1, sticky='w', padx=2, pady=2)

        self.command_label = tk.Label(self.command_frame, text='Command', width=30)
        self.command_label.grid(row=4, column=1)
        self.message_label = tk.Label(self.command_frame, text='Message', width=30)
        self.message_label.grid(row=4, column=2)

        self.command_listbox = tk.Listbox(self.command_frame, width=30, height=10, exportselection=0)
        self.read_commands()
        self.command_listbox.select_set(0)
        self.command_listbox.grid(row=5, column=1, padx=0, sticky='e', rowspan=8)

        self.message_listbox = tk.Listbox(self.command_frame, width=30, height=10, exportselection=0)
        self.read_messages()
        self.message_listbox.select_set(0)
        self.message_listbox.grid(row=5, column=2, sticky='w', padx=0, rowspan=8)

        self.send_button = tk.Button(self.command_frame, text='Send', width='20', command=self.send)
        self.send_button.grid(row=5, column=3)
        self.add_button = tk.Button(self.command_frame, text='Add', width='20', command=self.add)
        self.add_button.grid(row=6, column=3)
        self.del_button = tk.Button(self.command_frame, text='Delete', width=20, command=self.delete)
        self.del_button.grid(row=9, column=3)

        self.addcommand_label = tk.Label(self.command_frame, text='Command', width=20)
        self.addcommand_label.grid(row=7, column=3)
        self.addmessage_label = tk.Label(self.command_frame, text='Message', width=20)
        self.addmessage_label.grid(row=7, column=4)
        self.addcommand_entry = tk.Entry(self.command_frame, width=20)
        self.addcommand_entry.grid(row=8, column=3)
        self.addmessage_entry = tk.Entry(self.command_frame, width=20)
        self.addmessage_entry.grid(row=8, column=4)

    def read_commands(self):
        commands = [
            ['Send 1', '1'],
            ['Send H', 'H']
        ]
        for i in commands:
            self.command_listbox.insert('end', str(i[0]))

    def read_messages(self):
        commands = [
            ['Send 1', '1'],
            ['Send H', 'H']
        ]
        for i in commands:
            self.message_listbox.insert('end', str(i[1]))

    def init_commands(self):
        def click_timeout(event):
            self.disconnect()
            if self.var_timeout.get():
                self.timeout_entry.config(bg='white')
            else:
                self.timeout_entry.config(bg='lightgrey')

        self.timeout_check.bind('<Button-1>', click_timeout)

        def click_writetimeout(event):
            self.disconnect()
            if self.var_writetimeout.get():
                self.writetimeout_entry.config(bg='white')
            else:
                self.writetimeout_entry.config(bg='lightgrey')

        self.writetimeout_check.bind('<Button-1>', click_writetimeout)

        def click_interbytetimeout(event):
            self.disconnect()
            if self.var_interbytetimeout.get():
                self.interbytetimeout_entry.config(bg='white')
            else:
                self.interbytetimeout_entry.config(bg='lightgrey')

        self.interbytetimeout_check.bind('<Button-1>', click_interbytetimeout)

        def click_xonxoff(event):
            self.disconnect()

        self.xonxoff_check.bind('<Button-1>', click_xonxoff)

        def click_rtscts(event):
            self.disconnect()

        self.rtscts_check.bind('<Button-1>', click_rtscts)

        def click_dsrdtr(event):
            self.disconnect()

        self.dsrdtr_check.bind('<Button-1>', click_dsrdtr)

        def click_connect(event):
            self.connect()

        self.connect_button.bind('<Button-1>', click_connect)

        def click_disconnect(event):
            self.disconnect()

        self.disconnect_button.bind('<Button-1>', click_disconnect)

        def click_command(event):
            i = self.command_listbox.curselection()
            self.message_listbox.selection_clear(0, 'end')
            self.message_listbox.selection_set(i[0])

        self.command_listbox.bind('<Double-Button-1>', click_command)

        def click_message(event):
            i = self.message_listbox.curselection()
            self.command_listbox.selection_clear(0, 'end')
            self.command_listbox.selection_set(i[0])

        self.message_listbox.bind('<Double-Button-1>', click_message)

        def click_port(event):
            self.disconnect()

        self.port_option.bind('<Button-1>', click_port)

        def click_baud(event):
            self.disconnect()

        self.baud_option.bind('<Button-1>', click_baud)

        def click_databits(event):
            self.disconnect()

        self.databits_option.bind('<Button-1>', click_databits)

        def click_stopbits(event):
            self.disconnect()

        self.stop_option.bind('<Button-1>', click_stopbits)

        def click_parity(event):
            self.disconnect()

        self.parity_option.bind('<Button-1>', click_parity)

    def port_list(self):
        # s = ['COM1', 'COM2', 'COM3']
        s = serial.tools.list_ports.comports(include_links=False)
        return s

    def connect(self):
        if self.var_port.get() != 'None':
            if self.var_timeout.get() == 1:
                self.timeout = None
            else:
                self.timeout = float(self.timeout_entry.get())
            if self.var_writetimeout.get() == 1:
                self.writetimeout = None
            else:
                self.writetimeout = float(self.writetimeout_entry.get())
            if self.var_interbytetimeout.get() == 1:
                self.interbytetimeout = None
            else:
                self.interbytetimeout = float(self.interbytetimeout_entry.get())
            self.ser = serial.Serial(
                port=self.var_port.get(),
                baudrate=int(self.var_baud.get()),
                bytesize=int(self.var_databits.get()),
                parity=eval('serial.' + self.var_parity.get()),
                stopbits=int(self.var_stop.get()),
                timeout=self.timeout,
                xonxoff=self.xonxoff_check.get(),
                rtscts=self.rtscts_check.get(),
                dsrdtr=self.dsrdtr_check.get(),
                write_timeout=self.writetimeout,
                inter_byte_timeout=self.interbytetimeout
            )

            if self.ser.isOpen():
                self.connection_label.config(text='Connected', fg='Green')

    def disconnect(self):
        if self.ser in locals():
            if self.ser.isOpen():
                self.ser.close()
                self.connection_label.config(text='Disconnected', fg='Red')

    def send(self):
        if self.ser in locals():
            if self.ser.isOpen():
                s = self.message_listbox.curselection()
                s = self.message_listbox.get(s)
                self.ser.write(s)

    def add(self):
        s = self.addcommand_entry.get()
        self.command_listbox.insert('end', s)
        s = self.addmessage_entry.get()
        self.message_listbox.insert('end', s)

    def delete(self):
        s = self.message_listbox.curselection()
        self.message_listbox.delete(s)
        self.command_listbox.delete('active')

    baudrates = [
        '110   ',
        '300   ',
        '600   ',
        '1200  ',
        '2400  ',
        '4800  ',
        '9600  ',
        '19200 ',
        '38400 ',
        '57600 ',
        '115200',
        '128000',
        '256000',
    ]
    bytesizes = [
        '5',
        '6',
        '7',
        '8'
    ]
    parities = [
        'None ',
        'Even ',
        'Odd  ',
        'Mark ',
        'Space'
    ]
    stopbits = [
        '1  ',
        '1.5',
        '2  '
    ]
