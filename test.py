from camutil import Camera_PG
from camutil import Camera_FS
import sys
import time



"""
Helpful commands:
  connected videos   --  ls -ltrh /dev/video*
  USB devices        --  lsusb
  supported controls -- fswebcam -d '/dev/video2' --list-controls
"""
def run_PG():
    cam = Camera_PG()
    cam.set_active_camera(1)
    #cam.set_brightness(50)


    while True:
        try:
            print("Taking a new picture")

            image = cam.take_picture()
            cam.show_picture(image)
            time.sleep(5)

        except KeyboardInterrupt:
            cam.shutdown()
            sys.exit(0)


def run_FS():
    cam = Camera_FS()

    index = 1
    while index <= 10:
        try:
            print("Taking a new picture")
            brightness = index * 10
            zoom = index * 50

            # fswebcam -d '/dev/video2' --list-controls
            #   e.g. fswebcam -d '/dev/video2' -s 'exposure (absolute)'=2000
            #        fswebcam -d '/dev/video2' -s "zoom, absolute"=500 outzoom.jpg
            filename = 'out-b{}-z{}.jpg'.format(brightness, zoom)

            image = cam.take_picture(filename=filename, device='/dev/video2', brightness=brightness, zoom=zoom)
            time.sleep(5)
            index = index + 1

        except KeyboardInterrupt:
            sys.exit(0)

def simple():
    cam = Camera_FS()
    cam.take_picture(filename='out.jpg', resolution='1920x1080', device='/dev/video2', brightness=100, zoom=125)

if __name__ == '__main__':
    #run_PG()
    #run_FS()

    simple()