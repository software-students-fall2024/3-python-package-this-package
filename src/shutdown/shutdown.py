import os
import sys
import time
import platform
import subprocess
from timer.timer import timer

def shutdown_system():
    system_os = platform.system()
    print("Computer will shutdown in 20 seconds, please save your important files ASAP!")
    timer(20)
    if system_os == "Windows":
        os.system("shutdown /s /t 1")
    elif system_os == "Linux":
        subprocess.call(['osascript', '-e','tell app "System Events" to shut down'])
    else:  
        os.system("sudo shutdown -h now")