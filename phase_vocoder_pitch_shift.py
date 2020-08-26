from pyo import *
from pyo_osc_tools import OSCToSig

osc = OSCToSig(idle_timer=False, port=8000)
fader1 = osc["/1/fader1"].sig
fader2 = osc["/1/fader2"].sig

s = Server(audio="jack").boot()
audio_in = Input()

pva = PVAnal(audio_in, size=2048)

pvt = PVTranspose(pva, 0.5)
t2 = PVTranspose(pva, 2)

pvs = PVSynth([pvt,pvt2], [osc[f"/1/fader{i}"].sig for i in range(1,3)]).out()
audio_in*Sig(0.6).out()
s.start()
