import os
import random
import threading
import requests
from pystyle import *
import time
import sys
import datetime
import hashlib
import platform
luc = "\033[1;32m"
trang = "\033[1;37m"
red = "\033[1;31m"
yellow = "\033[0;93m"
lightblue = "\033[1;35m"
xduong = "\033[1;34m"
xnhac = "\033[1;36m"
hong = "\033[1;95m"

def logo1():
    print(f'''
    {xduong} _______  __   __  __   __  _______    ___      _______ 
    {yellow}|       ||  | |  ||  | |  ||       |  |   |    |   _   |
    {xnhac}|    _  ||  |_|  ||  | |  ||       |  |   |    |  |_|  |
    {hong}|   |_| ||       ||  |_|  ||       |  |   |    |       |
    {luc}|    ___||       ||       ||      _|  |   |___ |       |
    {red}|   |    |   _   ||       ||     |_   |       ||   _   |
    {xduong}|___|    |__| |__||_______||_______|  |_______||__| |__|
    ''')

class MainSHare:
    def __init__(self):
        self.blue = Col.light_blue
        self.__success = 0
        self.__errors = 0
        self.lblue = Colors.StaticMIX((Col.light_blue, Col.white, Col.white))
        self.red = Colors.StaticMIX((Col.red, Col.white, Col.white))
        try:
            self.open_file = open('token.txt').read().split('\n')
            self.open_file.remove('')
            self.total = str(len(self.open_file))
        except:
            quit(self.format_print("$", 'No Such File "token.txt"'))
    def format_print(self, symbol, text):
        return f"""                      {Col.Symbol(symbol, self.lblue, self.blue)} {self.lblue}{text}{Col.reset}"""
    def format_input(self, symbol, text):
        return f"""                      {Col.Symbol(symbol, self.red, self.blue)} {self.red}{text}{Col.reset}"""
    def banner(self):
        os.system("cls" if os.name == "nt" else "clear")
        banner = logo1()
        print(Colorate.Vertical(Colors.DynamicMIX((Col.light_red, Col.light_blue)), Center.XCenter(banner)))
        if self.total == '0':
            quit(self.format_print("@", "Token Number Not Enough!"))
    def share(self, id_post, token):
        dt_now = datetime.datetime.now()
        response = requests.post(f'https://graph.facebook.com/me/feed?link=https://m.facebook.com/{id_post}&published=0&access_token={token}').json()
        if 'id' in response:
            print(self.format_print("*",f"{dt_now.strftime('%H:%M:%S')}: {response['id']}"))
            self.__success += 1
            if self.__success >= self.toltal:
                input(self.format_input("!",f"Done Share!"))
            os.system(f'title Post: {self.id_post} ^| Success: {self.__success} ^| Fail: {self.__errors} ^| Thread: {threading.active_count()}')
        else:
            self.__errors += 1
            os.system(f'title Post: {self.id_post} ^| Success: {self.__success} ^| Fail: {self.__errors} ^| Thread: {threading.active_count()}')
    def run_share(self):
        while True:
            main.banner()
            try: 
                self.id_post = input(self.format_input("!",f"NHẬP ID BÀI VIẾT: "))
                threa = int(input(self.format_input("!",f"SỐ LUỒNG: ")))
                self.toltal = int(input(self.format_input("!",f"SỐ SHARE MUỐN CHẠY: ")))
                if self.id_post != '' and threa > 0:
                    break
                else:
                    print(self.format_print("#", "Thread > 0!"))
                    time.sleep(3)
            except:
                print(self.format_print("#", "Thread INT!"))
                time.sleep(3)
        while True:
            for token in self.open_file:
                t = threading.Thread(target=self.share, args=(self.id_post, token))
                t.start()
                while threading.active_count() > threa:
                    t.join()
def gui():
    os.system("cls" if os.name == "nt" else "clear")
    banner = logo1()
    print(Colorate.Vertical(Colors.DynamicMIX((Col.light_red, Col.light_blue)), Center.XCenter(banner)))
if __name__ == "__main__":
    try:
        main = MainSHare()
        main.run_share()
    except KeyboardInterrupt:
        time.sleep(3)
        sys.exit('\n'+main.format_print('*', 'Good Bye:)'))