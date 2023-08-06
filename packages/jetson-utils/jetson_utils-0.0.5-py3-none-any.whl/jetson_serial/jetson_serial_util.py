import os

def get_serial_no(self):
    serial_no = os.system("cat /proc/device-tree/serial-number")
    return str(serial_no)
