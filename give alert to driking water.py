import time

from plyer import notification

if __name__ == "__main__":
     while True:
        notification.notify(
          title= "**Please drink Water Now!**",
          message =" About 15.5 cups (3.7 liters) of fluids a day for men. About 11.5 cups (2.7 liters) of fluids a day for women.",
          app_icon ="F:\python projects\icon.ico",
          timeout=2
     )
     time.sleep(15)