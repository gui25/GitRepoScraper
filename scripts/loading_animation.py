import threading
import time
import sys

class LoadingSpinner:
    def __init__(self, message, duration=0.1):
        self.message = message
        self.duration = duration
        self.stop_event = threading.Event()
        self.spinner_thread = threading.Thread(target=self.spin)
        self.spinner_thread.daemon = True

    def spin(self):
        while not self.stop_event.is_set():
            for char in "|/-\\":
                sys.stdout.write(f"\r{self.message} {char}")
                sys.stdout.flush()
                time.sleep(self.duration)

    def start(self):
        self.spinner_thread.start()

    def stop(self):
        self.stop_event.set()
        self.spinner_thread.join()
        sys.stdout.write("\r" + " " * (len(self.message) + 2) + "\r")
        sys.stdout.flush()

def start_loading_animation(message, duration=0.1):
    spinner = LoadingSpinner(message, duration)
    spinner.start()
    return spinner
