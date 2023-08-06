import os
import subprocess


class JetsonUtils:
    def __init__(self):
        pass

    def getCpuTemperature(self) -> float:
        cpu_temp = os.system("cat /sys/class/thermal/thermal_zone1/temp")
        return float(cpu_temp) / 1000

    def getGpuTemperature(self) -> float:
        gpu_temp = os.system("cat /sys/class/thermal/thermal_zone2/temp")
        return float(gpu_temp) / 1000

    def getJetsonRelease(self) -> str:
        jetson_release = subprocess.check_output(
            "jetson_release -v", shell=True)
        jetson_release = jetson_release.decode()
        return jetson_release

    def getJetsonEnv(self) -> dict:
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
