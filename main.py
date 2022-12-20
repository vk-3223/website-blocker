import time
from datetime import datetime as dt
import os

host_temp = "hosts"
host = r"HERE_YOUR_HOST_FILE_PATH"
redirect = "127.0.0.1"

website_list = ["www.WBSITENAME.com","WEBSITENAME.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,23):
        print("working hour")
        with open(host_temp,"r+")as file:
            content = file.read()
            for websites in website_list:
                if content in websites:
                    pass
                else:
                    file.write(redirect + " " + websites + "\n")
    else:
        with open(host_temp,"r+")as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("fun hours")
    
    time.sleep(2)