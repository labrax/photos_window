

import time
import subprocess

FOLDER = "/home/pi/photos_window/data/"
DELAY_PHOTOS = 60 * 2 # 2 minutes

def run():
    start_time = time.time()
    file = time.strftime("%Y%m%d_%H%M.image.jpg")
    command = "raspistill -ex auto -fli auto -awb auto -q 25 -o {}{}".format(FOLDER, file)
    subprocess.run(command, shell=True, check=False)
    end_time = time.time()
    time.sleep(DELAY_PHOTOS - (end_time - start_time))


if __name__ == '__main__':
    while True:
        try:
            run()
        except Exception as e:
            print(e)
        time.sleep(5)

