import time
import RPi.GPIO as GPIO

# GPIO.BCMを指定するとGPIO番号モードで指定
GPIO.setmode(GPIO.BCM)

# GPIO14を出力に設定
GPIO.setup(14, GPIO.OUT)

try:
    while True:
        # GPIO14にHighを出力（LED点灯）
        GPIO.output(14, GPIO.HIGH)
        time.sleep(1)  # 1秒待つ

        # GPIO14にLowを出力（LED消灯）
        GPIO.output(14, GPIO.LOW)
        time.sleep(1)  # 1秒待つ

except KeyboardInterrupt:
    pass

GPIO.cleanup()