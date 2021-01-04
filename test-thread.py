import threading
import time
threads = []

print ("hello")

class myThread(threading.Thread):
    def __init__(self, i):
        threading.Thread.__init__(self)
        self.i = i

    def run(self):
        print("i = ", self.i)
        for j in range(0, self.i):
            print("j = ",j)
            time.sleep(5)

for i in range(1,4):
    thread = myThread(i)
    thread.start()
