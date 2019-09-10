import time
from datetime import datetime as dt

website_list = ["www.facebook.com", "facebook.com"]
redirects = "127.0.0.1"
host_path = "C:\Windows\System32\drivers\etc\hosts"
host_temp = "hosts"

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 9) <= dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 19):
        with open(host_path, "r+") as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirects + " " + website+"\n")
        print("Working hours")
    else:
        with open(host_path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for lines in content:
                if not any(website in lines for website in website_list):
                    file.write(lines)
            file.truncate()
        print("Chill mode On")
    time.sleep(5)