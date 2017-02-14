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

S11 = network.s_db[:,1,1]
freqs = network.frequency.f_scaled

freqs_array = numpy.array(freqs)
S11_array = numpy.array(S11)

plot(freqs_array/1e9, S11_array, marker='o')
xlabel('f [GHz]')
ylabel('S11 [dB]')
xlim(numpy.min(freqs_array)/1e9, numpy.max(freqs_array)/1e9)
show()

# This is just a test comment to see how GitHub desktop works

# And this is just another comment
