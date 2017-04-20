#!/usr/bin python3
# -*- coding: utf-8 -*-
from slacker import Slacker
import subprocess
from datetime import datetime

class Slack(object):
    __slacker = None

    def __init__(self, token):
        self.__slacker = Slacker(token)

    def file_upload(self, path, file_title):
        self.__slacker.files.upload(path, channels="#general", title=file_title)
        
if __name__ == "__main__":

    time = datetime.now().strftime("%Y%m%d-%H%M%S")
    path = "/tmp/" + time + ".jpg"
    subprocess.run(["fswebcam", "-d", "/dev/video0", path])
    slack = Slack("token")
    slack.file_upload(path, time)
