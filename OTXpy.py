from OTXv2 import OTXv2
from OTXv2 import IndicatorTypes
import numpy as np



otx = OTXv2("API_Key")
with open('pulses.txt', 'r') as f:
    x = f.read().splitlines()
    for row in x:
        indicators = otx.get_pulse_indicators(row)
        a = np.asarray(indicators)
        for i in a:
            print i.get("indicator")


