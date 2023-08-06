import os 
import subprocess


def getJetsonEnv():
    env_jetson = subprocess.check_output("env | grep JETSON", shell=True)
    # env_jetson = os.system("env | grep JETSON")

    print(env_jetson)
    foo = env_jetson.decode()
    print(foo)
    print(type(foo))

    print(foo.split("\n"))
    env_list = foo.split("\n")

    env_dict = {}

    for i in env_list:
        print(i, type(i))
        if i:
            i_items = i.split("=")
            print(i_items)
            env_dict[i_items[0]] = i_items[1]