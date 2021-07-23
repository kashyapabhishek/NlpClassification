import datetime
import os


class Logger(object):

    def __init__(self, name):
        if not os.path.isdir(f"log/logs/{name}"):
            os.mkdir(f"log/logs/{name}")
        self.file_object = open(f"log/logs/{name}/log_{str(datetime.datetime.today())}.txt", "w+")

    def warning(self, message):
        self.file_object.write(f"[WARNING] {message}\n")

    def info(self, message):
        self.file_object.write(f"[INFO] {message}\n")

    def error(self, ex, message):
        self.file_object.write(f"[ERROR] {message} , {ex}\n")

    def close(self):
        self.file_object.close()