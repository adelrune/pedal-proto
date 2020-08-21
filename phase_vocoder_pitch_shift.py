from pyo import *
s = Server(audio="jack").boot()
audio_in = Input()
pva = PVAnal(audio_in, size=2048)
pvt = PVTranspose(pva, 0.5)
pvs = PVSynth(pvt).out()

s.start()
