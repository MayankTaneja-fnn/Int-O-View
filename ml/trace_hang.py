import traceback
import sys
import threading
import time
import os

def dump():
    time.sleep(5)
    print('Dumping trace...')
    for frameId, frame in sys._current_frames().items():
        if frameId == threading.main_thread().ident:
            traceback.print_stack(frame)
    os._exit(1)

threading.Thread(target=dump, daemon=True).start()
import index
