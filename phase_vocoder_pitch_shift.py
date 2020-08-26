from pyo import *
from pyo_osc_tools import OSCToSig

s = Server(audio="jack").boot()


osc = OSCToSig(idle_timer=False, port=8000)
fader1 = osc["/1/fader1"].sig
fader2 = osc["/1/fader2"].sig

audio_in = Input()

up = audio_in * fader1
down = audio_in * fader2

pva = PVAnal(up, size=2048)
pva2 = PVAnal(down, size=2048)

pvt = PVTranspose(pva, 0.5)
pvt2 = PVTranspose(pva2, 2)

pvs = PVSynth(PVMix(pvt, pvt2)).out()
audio_in*Sig(0.6).out()
s.start()
