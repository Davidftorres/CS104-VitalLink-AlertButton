import RPi.GPIO as GPIO
import requests
import time

TOKEN = "8731466568:AAEXoN3Gwp-7fFsiUW4HUgJ8F4iUOtgrJgE"
CHAT_ID = "8628434531"

URL = f"https://api.telegram.org/bot8731466568:AAEXoN3Gwp-7fFsiUW4HUgJ8F4iUOtgrJgE/sendMessage"

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    if GPIO.input(7) == GPIO.HIGH:
        print("Someone pressed the alert button!")

        data = {
            "chat_id": CHAT_ID,
            "text": "Someone pressed the alert button!"
        }

        requests.post(URL, data=data)
        time.sleep(1)
