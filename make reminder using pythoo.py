import time
from win10toast import ToastNotifier
import platform

def notify():
    toast = ToastNotifier()

    toast.show_toast(
        "Notification",
        "Drink water",
        duration = 20,
        icon_path = "1.ico",
    )

# os.system('uname')

operating = platform.uname()

# print(operating.system, type(str(operating)))
# print(type(time.strftime("%H")))

if str(operating.system) == "Windows":
    while True:
        a = time.strftime("%H")
        print(a)
        if int(a) > 6:
            time.sleep(10)
            print("Drink water")
            notify()

        else:
            print("testing")

if str(operating.system) == "Linux":
    print('Linux')

else:
    print(str(operating.system()))