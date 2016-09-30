import time
import io
import picamera
import threading


class Camera(object):
    thread = None  # background thread that reads frames from camera
    frame = None  # current frame is stored here by background thread
    last_access = 0  # time of last client access to the camera



    def initialize(self):
        if camera.thread is None:
        #start background frame thread
        Camera.thread = threading.Thread(target=self.thread)
        Camera.thread.start()

        #wait until frame turn to be available
        while self.frame is None:
            time.sleep(0)


    def get_frame(self):
        Camera.last_access = time.time()
        self.initialize()
        return self.frame




