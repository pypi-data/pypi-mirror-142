import slippi
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import os
import io
import imageio as iio
from .slippire import getstage
from multiprocessing import Pool

starttime = time.time()

thisgame = slippi.game.Game("games/Game_20210917T135508.slp")
gframes = thisgame.frames
totframes = len(gframes) - 1
imgpath = './game.gif'
stage = getstage(thisgame)
inc = 4
poolsize = 4

def frame(itr):
    plt.scatter(float(gframes[itr].ports[0].leader.pre.position.x), float(gframes[itr].ports[0].leader.pre.position.y), c="#2980B9")
    plt.scatter(float(gframes[itr].ports[1].leader.pre.position.x), float(gframes[itr].ports[1].leader.pre.position.y), c="#E74C3C")
    plt.grid()
    plt.axis([-100, 100, -100, 100])
    buf = io.BytesIO()
    plt.savefig(buf, format='jpg')
    plt.close()

    return iio.imread(buf) 

if __name__ == '__main__':
    with Pool(poolsize) as p:
        iio.mimwrite(imgpath, p.map(frame, range(1, totframes, inc)), format='.gif', fps=15)

    print(time.time() - starttime)
    
