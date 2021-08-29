from paho.mqtt import client as cli
import time
import subprocess
from plyer import notification
from plyer import battery

charger = cli.Client()
charger.connect("192.168.68.15", 1883)


while True:
    if "sandydunes" in subprocess.check_output(
        ["netsh", "WLAN", "show", "interfaces"]
    ).decode("utf-8"):
        charge = battery.status["percentage"]
        if charge < 45:
            charger.publish("cmnd/SanjitLaptop/POWER", "ON")
            notification.notify(
                title="Laptop Charger",
                message="turning the charger on that good?",
                timeout=3,
                app_icon=r"low.ico",
            )
        elif charge > 70:
            charger.publish("cmnd/SanjitLaptop/POWER", "OFF")
            notification.notify(
                title="Laptop Charger",
                message="OMG HIGH BATTERY I WILL STOP CHARGING IT?",
                timeout=3,
                app_icon=r"high.ico",
            )
    time.sleep(1800)
