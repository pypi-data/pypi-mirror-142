import os
import subprocess

class JetsonUtils:
    def __init__(self):
        pass

    def get_serial_number(self) -> str:
        serial_no = subprocess.check_output("cat /proc/device-tree/serial-number")
        return str(serial_no)

    def get_serial_uuid(self):
        serial_uuid = subprocess.check_output("cat /proc/device-tree/chosen/uuid")
        return str(serial_uuid)

    def get_cpu_temperature(self) -> float:
        cpu_temp = subprocess.check_output("cat /sys/class/thermal/thermal_zone1/temp")
        return (float(cpu_temp) / 1000)

    def get_gpu_temperature(self) -> float:
        gpu_temp = subprocess.check_output("cat /sys/class/thermal/thermal_zone2/temp")
        return (float(gpu_temp) / 1000)

    def get_jetson_release(self) -> str:
        jetson_release = subprocess.check_output(
            "jetson_release -v", shell=True)
        jetson_release = jetson_release.decode()
        return jetson_release

    def get_jetson_env(self) -> dict:
        env_jetson = subprocess.check_output("env | grep JETSON", shell=True)
        foo = env_jetson.decode()
        env_list = foo.split("\n")
        env_dict = {}
        for i in env_list:
            if i:
                i_items = i.split("=")
                print(i_items)
                env_dict[i_items[0]] = i_items[1]
        return env_dict

    def get_hci_address(self)-> str:
        output = subprocess.check_output("hcitool dev | grep -o \"[[:xdigit:]:]\{11,17\}\"", shell=True)
        result = output.decode('utf-8')
        return str(result)
       
