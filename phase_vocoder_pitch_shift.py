from pyo import *
s = Server(audio="jack").boot()
audio_in = Input()
pva = PVAnal(audio_in, size=2048)
pvt = PVTranspose(pva, 0.5)
pvt2 = PVTranspose(pva, 2)
pvs = PVSynth(PVMix(pvt,pvt2),mul=0.6).out()
audio_in*Sig(0.6).out()
s.start()
