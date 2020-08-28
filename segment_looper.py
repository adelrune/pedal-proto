from pyo import *
from pyo_osc_tools import OSCToSig

s = Server(audio="jack").boot()
osc = OSCToSig(idle_timer=False, port=8000, ramp=0, sig_size=1)

recorder = None
audio_in = Input()
loops = []
audio_outs = []
recording = False

def push_recording():

    global recorder
    global recording

    if not recording:
        temp_table = NewTable(120)
        recorder = TableRec(audio_in, temp_table)
        recorder.play()
        loops.append(temp_table)
        recording = True
        return

    recorder.stop()
    table = loops.pop()
    table_with_the_right_lenght = DataTable(size=int(recorder["time"].get()))
    table_with_the_right_lenght.copyData(table)
    loops.append(table_with_the_right_lenght)
    tr = TableRead(table_with_the_right_lenght, table_with_the_right_lenght.getRate(), loop=True)
    audio_outs.append(tr)
    tr.out()
    recording = False

push_sig = osc[1]["push1"].sig
push_trig = Thresh(push_sig, threshold=0.9999, dir=0)
push_tf = TrigFunc(push_trig, push_recording)

s.start()
