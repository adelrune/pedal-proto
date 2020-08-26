from pyo import *
from pyo_osc_tools import OSCToSig

s = Server(audio="jack").boot()


osc = OSCToSig(idle_timer=False, port=8000)
fader1 = osc["/1/fader1"].sig
fader2 = osc["/1/fader2"].sig

audio_in = Input()
dist = Disto(audio_in, drive=fader1, slope=fader2).out()
s.start()
