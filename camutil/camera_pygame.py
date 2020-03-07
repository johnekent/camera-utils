import pygame
import pygame.camera
import time
import logging

"""This works nicely overall.
However, it gives an error about METH_OLDARGS when trying to tap into the controls such as brightness.
That seems to be a common problem with vresions of python and libraries backed by .so files.
That makes this challenging to use since adjusting brightness is quite important.
"""
class Camera:

    def __init__(self, max_num_cams = 1):
        pygame.camera.init()

        # try it a few times to make sure
        for i in [1,2,3]:
            working_cameras = self.get_working_cameras()
            time.sleep(1)

        self.all_working_cameras = working_cameras

        self._cam = None
        self._windows = None
        if working_cameras:

            self._cam = working_cameras[0]
        else:
            self.shutdown()
            raise Exception("No working cameras were found.")

        self.size = (640, 480)
        self._window = pygame.display.set_mode(self.size, pygame.RESIZABLE)

    def set_active_camera(self, index = 0):

        if index < 0:
            logging.warning("Please do not give a negative index")
            return

        max_index = len(self.all_working_cameras) - 1
        if max_index <= index:
            self._cam = self.all_working_cameras[index]
            logging.info("Changed camera index to {}".format(index))
        else:
            logging.info("Apologies, but the requested index {} is beyond the max index {} ".format(index, max_index))

    def shutdown(self):
        #TODO
        logging.info('Shutdown cameras')

    def get_working_cameras(self):

        # list of device names
        device_names = pygame.camera.list_cameras()
        working = []
        for device in device_names:
            camera = pygame.camera.Camera(device)
            img = self.take_picture(camera)
            if img:
                print("{} is working".format(device))
                working.append(camera)

        logging.info("There are %d working cameras", len(working))
        if len(working) > 0:
            return working
        else:
            return None

    def save_captured_image(self, window_image, file_name):
        pygame.image.save(window_image, file_name)

    def take_picture(self, cam=None):

        if not cam:
            cam = self._cam
        try:
            cam.start()
            image = cam.get_image()
            cam.stop()
        except Exception as err:
            logging.exception("Got an exception while taking picture: %s", str(err))
            return None
        return image

    def show_picture(self, image):

        self._window.blit(image, (0,0))
        pygame.display.update()