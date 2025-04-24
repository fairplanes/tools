import string
import random
import time
keychars = string.ascii_letters+string.digits+string.punctuation
def reset():
        while True:
            time.sleep(60)
            keylist=list(keychars)
            random.shuffle(keylist)
            key="".join(keylist)
            print(key)
reset()
