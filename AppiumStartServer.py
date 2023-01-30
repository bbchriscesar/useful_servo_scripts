import os
from time import sleep

# os.system("start /B start cmd.exe @cmd /k appium")
os.system("start /B start cmd.exe @cmd /k appium -a 127.0.0.1 -p 4728")

sleep(8)
os.system("taskkill /F /IM node.exe")
os.system("taskkill /F /IM cmd.exe")