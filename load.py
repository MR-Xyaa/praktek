import itertools
import threading
import time
import sys

done = False

#animasi loading
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rSelesai Anjing!     ')

t = threading.Thread(target=animate)
t.start()

#proses lama disini

time.sleep(10)
done = True
