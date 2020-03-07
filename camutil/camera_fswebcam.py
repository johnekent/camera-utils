import subprocess
import logging

"""this is the version for fswebcam
It just wraps the command.
"""

class Camera(object):

    def __init__(self):
        logging.info("Created")

    def _make_cmd(self, filename, device=None, resolution=None, brightness=None, contrast=None, zoom=None):

        cmd = ['fswebcam']

        # these would be nice for tests
        if device:
            cmd.append('-d')
            cmd.append(device)

        if resolution:
            cmd.append('-r')
            cmd.append(resolution)

        # controls
        if brightness:
            cmd.append('-s')
            cmd.append('brightness={}%'.format(brightness))

        if contrast:
            cmd.append('-s')
            cmd.append('contrast={}%'.format(contrast))

        if zoom:
            cmd.append('-s')
            cmd.append('zoom, absolute={}'.format(zoom))

        cmd.append('--jpeg')
        cmd.append('100')

        cmd.append(filename)

        return cmd

    def take_picture(self, filename, device=None, resolution=None, brightness=None, contrast=None, zoom=None):

        cmd = self._make_cmd(filename,
                             device=device,
                             resolution=resolution,
                             brightness=brightness,
                             contrast=contrast,
                             zoom=zoom)
        logging.info("cmd = {}".format(str(cmd)))
        status = subprocess.run(cmd)
