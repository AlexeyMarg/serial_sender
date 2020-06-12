import tkinter as tk


class form:
    def __init__(self, parent):
        self.parent = parent
        self.init_ui()
        self.init_commands()

    def init_ui(self):
        self.port_label = tk.Label(self.parent, text='Port')
        self.port_label.grid(row=1, column=1)
        temp = self.port_list()
        self.var_port = tk.StringVar(self.parent)
        self.var_port.set(temp[0])
        self.port_option = tk.OptionMenu(self.parent, self.var_port, *temp)
        self.port_option.grid(row=2, column=1)

        self.baud_label = tk.Label(self.parent, text='Baudrate')
        self.baud_label.grid(row=1, column=2)
        self.var_baud = tk.StringVar(self.parent)
        self.var_baud.set(self.baudrates[6])
        self.baud_option = tk.OptionMenu(self.parent, self.var_baud, *self.baudrates)
        self.baud_option.grid(row=2, column=2)

        self.databits_label = tk.Label(self.parent, text='Data bits')
        self.databits_label.grid(row=1, column=3)
        self.var_databits = tk.StringVar(self.parent)
        self.var_databits.set(self.bytesizes[3])
        self.databits_option = tk.OptionMenu(self.parent, self.var_databits, *self.bytesizes)
        self.databits_option.grid(row=2, column=3)

        self.parity_label = tk.Label(self.parent, text='Parity')
        self.parity_label.grid(row=1, column=4)
        self.var_parity = tk.StringVar(self.parent)
        self.var_parity.set(self.parities[0])
        self.parity_option = tk.OptionMenu(self.parent, self.var_parity, *self.parities)
        self.parity_option.grid(row=2, column=4)

        self.stop_label = tk.Label(self.parent, text='Stop bits')
        self.stop_label.grid(row=1, column=5)
        self.var_stop = tk.StringVar(self.parent)
        self.var_stop.set(self.stopbits[0])
        self.stop_option = tk.OptionMenu(self.parent, self.var_stop, *self.stopbits)
        self.stop_option.grid(row=2, column=5)

        self.timeout_label = tk.Label(self.parent, text = 'Timeout')
        self.timeout_label.grid(row=1, column=6)
        self.var_timeout = tk.BooleanVar(self.parent)
        self.var_timeout.set(1)
        self.timeout_none = tk.Label(self.parent, text='None')
        self.timeout_none.grid(row=2, column=6)
        self.timeout_check = tk.Checkbutton(self.parent, variable=self.var_timeout)
        self.timeout_check.grid(row=2, column=7)
        self.timeout_entry = tk.Entry(self.parent, width=6, bg='lightgrey')
        self.timeout_entry.grid(row=3, column=6)

        self.xonxoff_label = tk.Label(self.parent, text='xonxoff enable')
        self.xonxoff_label.grid(row=1, column=8)
        self.var_xonxoff = tk.BooleanVar(self.parent)
        self.var_xonxoff.set(0)
        self.xonxoff_check = tk.Checkbutton(self.parent, variable=self.var_xonxoff)
        self.xonxoff_check.grid(row=1, column=9)

        self.rtscts_label = tk.Label(self.parent, text='rtscts enable')
        self.rtscts_label.grid(row=2, column=8)
        self.var_rtscts = tk.BooleanVar(self.parent)
        self.var_rtscts.set(0)
        self.rtscts_check = tk.Checkbutton(self.parent, variable=self.var_rtscts)
        self.rtscts_check.grid(row=2, column=9)

        self.dsrdtr_label = tk.Label(self.parent, text='dsrdtr enable')
        self.dsrdtr_label.grid(row=3, column=8)
        self.var_dsrdtr = tk.BooleanVar(self.parent)
        self.var_dsrdtr.set(0)
        self.dsrdtr_check = tk.Checkbutton(self.parent, variable=self.var_dsrdtr)
        self.dsrdtr_check.grid(row=3, column=9)

        self.writetimeout_label = tk.Label(self.parent, text = 'Write \ntimeout')
        self.writetimeout_label.grid(row=1, column=10)
        self.var_writetimeout = tk.BooleanVar(self.parent)
        self.var_writetimeout.set(1)
        self.writetimeout_none = tk.Label(self.parent, text='None')
        self.writetimeout_none.grid(row=2, column=10)
        self.writetimeout_check = tk.Checkbutton(self.parent, variable=self.var_writetimeout)
        self.writetimeout_check.grid(row=2, column=11)
        self.writetimeout_entry = tk.Entry(self.parent, width=6, bg='lightgrey')
        self.writetimeout_entry.grid(row=3, column=10)

        self.interbytetimeout_label = tk.Label(self.parent, text = 'Write inter \n byte timeout')
        self.interbytetimeout_label.grid(row=1, column=12)
        self.var_interbytetimeout = tk.BooleanVar(self.parent)
        self.var_interbytetimeout.set(1)
        self.interbytetimeout_none = tk.Label(self.parent, text='None')
        self.interbytetimeout_none.grid(row=2, column=12)
        self.interbytetimeout_check = tk.Checkbutton(self.parent, variable=self.var_interbytetimeout)
        self.interbytetimeout_check.grid(row=2, column=13)
        self.interbytetimeout_entry = tk.Entry(self.parent, width=6, bg='lightgrey')
        self.interbytetimeout_entry.grid(row=3, column=12)




    def init_commands(self):
        pass

    def port_list(self):
        s = [
            'COM1',
            'COM2',
            'COM3'
        ]
        return s

    baudrates = [
        '110',
        '300',
        '600',
        '1200',
        '2400',
        '4800',
        '9600',
        '19200',
        '38400',
        '57600',
        '115200',
        '128000',
        '256000',
    ]
    bytesizes=[
        '5',
        '6',
        '7',
        '8'
    ]
    parities = [
        'None',
        'Even',
        'Odd',
        'Mark',
        'Space'
    ]
    stopbits = [
        '1',
        '1.5',
        '2'
    ]
