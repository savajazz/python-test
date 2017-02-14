import numpy
from matplotlib.pyplot import *
# from mwavepy import *
import mwavepy as mv
import pylab

import file ms_functions

if len(sys.argv) == 2:
    inFileName = sys.argv[1]
else:
    inFileName = "HMC8500LP5DE_Sparameters.s2p"
    
network = mv.Network(inFileName)

network.plot_s_db()
pylab.show()

network.plot_s_db(m=0, n=0)
pylab.show()
