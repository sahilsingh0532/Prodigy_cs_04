from pynput.mouse import Listener
def writetofile(x,y):
    print('postion of current mouse (0)'.format((x,y)))

with Listener(onmove=writetofile) as l:
    l.join()