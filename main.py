import sounddevice
import soundfile
import time
import threading

def play(files,de):
    array, smp_rt = soundfile.read(files, dtype = 'float32') 
    sounddevice.play(array,smp_rt,device=de)
    sounddevice.wait()

def seeforclass(start,end,eye):
    while True:
        if time.strftime('%H:%M:%S',time.localtime(time.time())) in start:
            play('data/start.wav','CABLE Input (VB-Audio Virtual C, MME')
        if time.strftime('%H:%M:%S',time.localtime(time.time())) in end:
            play('data/end.wav','CABLE Input (VB-Audio Virtual C, MME')
        if time.strftime('%H:%M:%S',time.localtime(time.time())) in eye:
            play('data/eye.wav','CABLE Input (VB-Audio Virtual C, MME')

def seeforme(start,end,eye):
    while True:
        if time.strftime('%H:%M:%S',time.localtime(time.time())) in start:
            play('data/start.wav','LG IPS FULLHD (NVIDIA High Defi, MME')
        if time.strftime('%H:%M:%S',time.localtime(time.time())) in end:
            play('data/end.wav','LG IPS FULLHD (NVIDIA High Defi, MME')
        if time.strftime('%H:%M:%S',time.localtime(time.time())) in eye:
            play('data/eye.wav','LG IPS FULLHD (NVIDIA High Defi, MME')



if __name__ =='__main__':
    start = ['07:59:03','08:59:03','10:19:03',"12:59:03","13:59:03","14:59:03","15:59:03"]
    end = ['08:45:00',"11:05:00","13:45:00","15:45:00","16:45:00"]
    eye = ["09:45:00",'14:45:00']
    thread1 = threading.Thread(name='t1',target=seeforclass,args=[start,end,eye])
    thread2 = threading.Thread(name='t2',target=seeforme,args=[start,end,eye])
    thread1.start()
    thread2.start()