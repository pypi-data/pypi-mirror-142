from tqdm import trange
from time import sleep

for i in trange(10, desc='1st loop', leave=True):
    for j in trange(100, desc='2nd loop', leave=False, position=1):
        sleep(0.01)
    for k in trange(100, desc='3nd loop', leave=False, position=2):
        sleep(0.01)
