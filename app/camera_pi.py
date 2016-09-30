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

    @classmethod
    def _thread(cls):
        with picamera.PiCamera() as camera:
            #camera setup
            camera.resolution = (320,240)
            camera.hflip = True
            camera.vflip = True

            #the camera is warming up
            camera.start_preview()
            time.sleep(2)

            stream= io.BytesIO()
            for foo in camera.capture_continuous(stream, 'jpeg', use_video_port=True)

                #store frame
                stream.seek(0)
                cls.frame = stream.read()


                #reseting stream fr the next frame
                stream.seek(0)
                stream.truncate()




